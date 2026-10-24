#!/usr/bin/env python3
"""
GitHub Trending 爬虫脚本
抓取 GitHub 每日/每周热门项目，生成 Hugo 文章

使用方法:
    python3 scripts/github_trending.py [daily|weekly]
    
输出:
    content/posts/github-trending-YYYY-MM-DD.md
"""

import sys
import os
import re
import json
import urllib.request
import urllib.parse
import time
import gzip
import zlib
import ssl
import html as html_lib

# Force IPv4: this host's IPv6 route is broken, and the default IPv6-preferring
# resolution makes every HTTPS handshake die with a TLS EOF error.
# ==========================================
# GitHub Web 端备用 IP (DNS 黑洞容灾)
# ==========================================
# 本机 DNS 把 github.com 解析到 20.205.243.166, 而该地址的 443 路由被
# 中间链路丢弃 (SYN 无应答, TCP 握手永不完成), 导致 Trending 页面抓取
# 100% 超时并降级到质量更差的 Search API。
# 下列 Anycast 边缘 IP 属于同一 GitHub 前端集群, 返回内容一致; 由于 TLS 的
# SNI 与证书校验仍使用主机名 github.com, 固定 IP 不削弱 TLS 安全性。
GITHUB_WEB_FALLBACK_IPS = (
    "20.27.177.113",
    "140.82.112.3",
    "140.82.113.3",
    "140.82.114.3",
    "140.82.116.3",
)

# 主机名 -> 备用 IP 列表
_FALLBACK_IPS = {
    "github.com": GITHUB_WEB_FALLBACK_IPS,
}

# 当前生效的 IP 固定 (由 _http_get 在每次请求前设置, 用完立即复位)
_PINNED_IP = {}


try:
    import socket as _socket
    _orig_getaddrinfo = _socket.getaddrinfo
    def _getaddrinfo_ipv4(host, port, family=0, *a, **kw):
        # IP 固定: DNS 解析出的地址不可达时, 改用已探测可达的边缘 IP。
        # Host 头与 TLS SNI 仍使用原始主机名, 不影响证书校验。
        pinned = _PINNED_IP.get(host)
        if pinned:
            return _orig_getaddrinfo(pinned, port, _socket.AF_INET, *a, **kw)
        return _orig_getaddrinfo(host, port, _socket.AF_INET, *a, **kw)
    _socket.getaddrinfo = _getaddrinfo_ipv4
except Exception:
    pass


def _urlopen_with_retry(req, timeout=30, retries=3):
    """urlopen with exponential backoff.

    The upstream TLS endpoint intermittently drops the handshake with an EOF;
    retrying resolves it without masking genuine errors.
    """
    last_exc = None
    for attempt in range(retries):
        try:
            return urllib.request.urlopen(req, timeout=timeout)
        except Exception as exc:
            last_exc = exc
            if attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
    raise last_exc


def _candidate_ips(host, port=443):
    """候选 IP 列表: 先用 DNS 当前解析结果, 再追加已知可达的边缘 IP。"""
    ips = []
    try:
        for info in _orig_getaddrinfo(host, port, _socket.AF_INET):
            ip = info[4][0]
            if ip not in ips:
                ips.append(ip)
    except Exception:
        pass
    for ip in _FALLBACK_IPS.get(host, ()):
        if ip not in ips:
            ips.append(ip)
    return ips


def _tls_handshake(host, ip, timeout=8):
    """与指定 IP 完成 TLS 握手, 校验证书。

    仅探测 TCP 端口是不够的: 本机 DNS 解析出的 github.com 地址接受 TCP
    连接却永远不回应 TLS 握手, 于是每次请求都白白耗掉整个超时窗口
    (30s x 3 = 90s), 并把后续对健康边缘 IP 的请求也拖进黑洞。
    因此这里在 TLS 层做探测, 只有真正完成握手 (且证书校验通过) 的 IP
    才会被用于取数。

    返回已握手的 socket, 失败返回 None。
    """
    ctx = ssl.create_default_context()
    sock = None
    try:
        sock = _socket.create_connection((ip, 443), timeout=timeout)
        sock.settimeout(timeout)
        return ctx.wrap_socket(sock, server_hostname=host)
    except Exception as exc:
        print(f"  TLS 握手失败 {ip}: {type(exc).__name__}: {exc}")
        if sock is not None:
            try:
                sock.close()
            except Exception:
                pass
        return None


def _raw_http_get(host, path, ip, headers, timeout=25):
    """直连指定 IP 取回页面, 自行处理 chunked 与 gzip 解码。

    urllib/http.client 在本机出口链路上偶尔会在正文读取阶段卡死;
    原生 socket 路径实测 5/5 成功, 作为兜底手段保留。
    """
    ctx = ssl.create_default_context()
    sock = ctx.wrap_socket(
        _socket.create_connection((ip, 443), timeout=timeout),
        server_hostname=host,
    )
    try:
        req = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n"
        for k, v in headers.items():
            req += f"{k}: {v}\r\n"
        req += "Connection: close\r\n\r\n"
        sock.sendall(req.encode())
        data = b""
        while True:
            chunk = sock.recv(65536)
            if not chunk:
                break
            data += chunk
    finally:
        try:
            sock.close()
        except Exception:
            pass

    head, body = data.split(b"\r\n\r\n", 1)
    hdrs = {}
    for line in head.decode("latin1").split("\r\n")[1:]:
        if ":" in line:
            k, v = line.split(":", 1)
            hdrs[k.strip().lower()] = v.strip()

    status = head.decode("latin1").split("\r\n", 1)[0]
    if " 200" not in status:
        raise IOError(f"unexpected status: {status}")

    if hdrs.get("transfer-encoding", "").lower() == "chunked":
        out = b""
        buf = body
        while True:
            idx = buf.find(b"\r\n")
            if idx < 0:
                break
            size = int(buf[:idx].split(b";")[0], 16)
            if size == 0:
                break
            out += buf[idx + 2: idx + 2 + size]
            buf = buf[idx + 2 + size + 2:]
        body = out

    if hdrs.get("content-encoding", "").lower() == "gzip":
        body = gzip.decompress(body)
    elif hdrs.get("content-encoding", "").lower() == "deflate":
        body = zlib.decompress(body, -zlib.MAX_WBITS)
    return body.decode("utf-8", "replace")


def _http_get(url, headers, timeout=30, retries=3, max_attempts=6):
    """GET a URL and return the decoded body as text.

    处理四类传输缺陷:

    1. *DNS 黑洞.* 本机解析出的 github.com 地址接受 TCP 连接却永不完成
       TLS 握手。先做 TLS 层探测, 只保留真正握手的 IP。

    2. *未压缩传输拖慢.* Trending 页面未压缩约 551 KB, 走本机出口需 21-37s,
       会撑爆超时。请求 gzip 后载荷降到约 46 KB, 传输约 0.4s。

    3. *重试只覆盖了连接.* urlopen 在响应头到达后即返回, 正文在此之后才读,
       因此截断响应抛出的 IncompleteRead 落在重试循环之外, 从未被重试。
       这里把正文读取纳入重试范围, 并检测截断的载荷。

    4. *http.client 正文读取卡死.* 偶发于本机出口链路, 故保留原生 socket
       取数路径作为兜底。

    失败时返回 ""。
    """
    parsed = urllib.parse.urlparse(url)
    host = parsed.hostname or ""
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    last_exc = None

    # 1) 逐个 IP 直接尝试取数。
    #    注意: 这里不再做独立的 TLS 探测握手 —— 探测会额外消耗一次连接,
    #    在本机出口链路上反而提高了整体失败率 (实测同一批 IP 探测全失败
    #    而直接取数却能成功)。探测信息只作为日志参考。
    attempts = 0
    for ip in _candidate_ips(host):
        # 2) 优先走原生 socket 路径 (实测最稳), 失败再退回 urllib
        if attempts < max_attempts:
            attempts += 1
            try:
                text = _raw_http_get(host, path, ip, headers, timeout=timeout)
                if "</html>" not in text:
                    raise IOError(f"truncated response ({len(text)} bytes, no </html>)")
                return text
            except Exception as exc:
                last_exc = exc
                print(f"  raw attempt {attempts}/{max_attempts} failed on {ip}: {exc}")

        for attempt in range(retries):
            if attempts >= max_attempts:
                break
            attempts += 1
            _PINNED_IP[host] = ip
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    raw = response.read()
                    encoding = (response.headers.get("Content-Encoding") or "").lower()
                if encoding == "gzip":
                    raw = gzip.decompress(raw)
                elif encoding == "deflate":
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                text = raw.decode("utf-8", "replace")
                # 截断的 HTML 仍可能解析出部分内容, 故先确认文档闭合再采信
                if "</html>" not in text:
                    raise IOError(f"truncated response ({len(text)} bytes, no </html>)")
                _PINNED_IP[host] = None
                return text
            except Exception as exc:
                last_exc = exc
                print(f"  HTTP attempt {attempts}/{max_attempts} failed on {ip}: {exc}")
                if attempt < retries - 1:
                    time.sleep(2 * (attempt + 1))
        _PINNED_IP[host] = None
        if attempts >= max_attempts:
            break

    print(f"Error fetching {url}: {last_exc}")
    return ""
from datetime import datetime, timedelta, timezone

# ==========================================
# 配置
# ==========================================
CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'content', 'posts')
GITHUB_API = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "GoodInfo-GitHub-Trending",
    "Accept-Encoding": "gzip"
}

# 添加 GitHub Token (可选，提高速率限制)
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


# ==========================================
# 反垃圾过滤
# ==========================================
# GitHub's Search API surfaces a large amount of star-farming spam: repos
# named after pirated software, "pre-activated" installers, crack tools and
# game cheats. These flood the fallback path and MUST never reach the site.
# Matching is done on the repo name / description / topics, case-insensitively.
# TIER 1 —— 确定性垃圾信号。命中其一即可判定为垃圾, 无需其它佐证。
SPAM_PATTERNS = [
    # 盗版 / 破解 / 激活
    r"pre[- ]?activat", r"\bcrack(?:ed|er|s)?\b", r"\bkeygen\b", r"\bactivator\b",
    r"\bkms\b", r"\bpatcher\b", r"\bnulled\b", r"\bwarez\b", r"\btorrent\b",
    r"\bfree\s*download\b", r"\bdownload\s*(?:setup|installer)\b", r"\binstaller\b",
    r"\blicen[cs]e\s*key\b", r"\bproduct\s*key\b", r"\bserial\s*key\b",
    r"standalone\s+setup", r"all\s+features\s+(?:unlocked|unrestricted)",
    r"\bfull\s+version\b", r"\bportable\s+edition\b", r"\bactivation\b",
    # 游戏作弊 / 外挂 (确定性词)
    r"\baimbot\b", r"\bwallhack\b", r"\bmod\s*menu\b", r"\bcheat(?:s|ing|d)?\b",
    r"\bhwid\s*spoofer\b", r"undetected\s+cheat", r"\bbypass(?:es|ing)?\s+battleye",
    r"\bhack[- _]?(?:menu|client|squad|cheat)\b",
    r"\b(?:speed|fly|aim|no[- ]?recoil|trigger)[- ]?hack\b",
    # 灰产 / 刷量
    r"\bdefi\b.*\bbot\b", r"\bcopy[- ]trading[- ]bot\b", r"\barbitrage[- ]bot\b",
    r"\bpassive[- ]income\b", r"\bforex[- ]bot\b", r"\bbot[- ]download\b",
    r"\bairdrop\s*bot\b", r"\bseo\s*backlink\b", r"\bfollower\s*bot\b",
    r"\b(?:sms|call)[- ]?bomb(?:er)?\b", r"nitro[- ]?generator",
    # 成人 / 恶意
    r"\bnsfw\b", r"\b(?:onlyfans|porn)\b", r"\bspammer\b",
]
SPAM_RE = re.compile("|".join(SPAM_PATTERNS), re.IGNORECASE)

# TIER 2 —— 上下文信号。单独出现不足以判定 (例如 "reward-hacking" 是正经 ML 术语,
# ESP32 是单片机型号, "Hack to Skill" 是 Google 公开课), 需要与其它信号共现。
SOFT_PATTERNS = [
    r"\bhack(?:s|ed|ing)?\b",
    r"\besp\b",
    r"\btrainer\b",
    r"\bexploit\b",
    r"\binjector\b",
    r"\bloader\b",
    r"\bspoofer\b",
    r"\btrigger\s*bot\b",
    r"\baim\s*assist\b",
    r"\bauto[- ]?farm\b",
    r"\bgod\s*mode\b",
    r"\bcheat\b",
]
SOFT_RE = re.compile("|".join(SOFT_PATTERNS), re.IGNORECASE)

# AI 生成的 SEO 垃圾仓库命名模板, 例如:
#   poe-2-hack-intelligence-lab / warframe-hack-2026-tenno-build-toolkit
#   hell-let-loose-hack-2026-frontline-combat-toolkit
SEO_TEMPLATE_RE = re.compile(
    r"\bhack\b.{0,40}\b(toolkit|lab|squad|combat|explorer|intelligence)\b"
    r"|\b(toolkit|lab|squad)\b.{0,40}\bhack\b",
    re.IGNORECASE,
)

# 仓库名以 .github 结尾的一律为占号垃圾账号 (df-tools-bn/.github 等)
DUMMY_REPO_RE = re.compile(r"\.github$", re.IGNORECASE)

# 官方/知名组织白名单 —— 这些账号即使命中关键词也予以保留
TRUSTED_OWNERS = {
    "php", "anthropics", "cloudflare", "nvidia", "nodejs", "supabase", "fastapi",
    "microsoft", "google", "github", "openai", "meta", "facebook", "apple",
    "mozilla", "rust-lang", "golang", "python", "django", "vuejs",
    "facebookresearch", "tensorflow", "pytorch", "vercel", "netlify", "docker",
    "kubernetes", "ansible", "hashicorp", "prometheus", "grafana", "elastic",
    "mongodb", "redis", "postgresql", "sqlite", "linux", "torvalds", "git",
    "openbmb", "langchain-ai", "langchain", "ollama", "llama",
    "huggingface", "screwdriver", "vllm", "comfyanonymous",
}


def is_spam_repo(repo):
    """Return True when a repo looks like star-farming spam / piracy.

    Checked fields: full_name, description, topics.

    Decision logic:
      * trusted owners are never flagged;
      * a TIER-1 (deterministic) hit is conclusive on its own;
      * otherwise TIER-2 (contextual) hits must co-occur -- a single weak word
        such as "hack" is legitimate in "reward-hacking", "ESP32" or the
        "Hack to Skill" course, so it must not flag a repo by itself.
    """
    name = repo.get("full_name", "") or ""
    desc = repo.get("description", "") or ""
    topics = " ".join(repo.get("topics", []) or [])

    owner = name.split("/")[0].lower() if "/" in name else ""
    if owner in TRUSTED_OWNERS:
        return False

    if DUMMY_REPO_RE.search(name):
        return True

    blob = f"{name}\n{desc}\n{topics}"
    if SPAM_RE.search(blob):
        return True

    soft_hits = {m.group(0).lower() for m in SOFT_RE.finditer(blob)}
    if SEO_TEMPLATE_RE.search(blob):
        return True
    # 需要至少两个不同的上下文信号共现
    return len(soft_hits) >= 2


def fetch_trending_repos(since="daily", language="", per_page=20):
    """
    获取 GitHub 热门仓库
    
    Args:
        since: daily/weekly/monthly
        language: 编程语言过滤 (如 python, javascript)
        per_page: 返回数量
    
    Returns:
        list: 仓库列表
    """
    # 计算时间范围
    now = datetime.now(timezone.utc)
    if since == "daily":
        date_from = (now - timedelta(days=1)).strftime("%Y-%m-%d")
    elif since == "weekly":
        date_from = (now - timedelta(days=7)).strftime("%Y-%m-%d")
    else:
        date_from = (now - timedelta(days=30)).strftime("%Y-%m-%d")
    
    # 构建搜索查询.
    # 该路径仅在 Trending 页面抓取失败时启用, 结果质量明显低于官方榜单,
    # 因此收紧条件: 排除明显的垃圾主题 (下载/破解/激活) 并提高 star 门槛,
    # 以免盗号/刷星仓库混入正文。
    query = (
        f"created:>{date_from} stars:>50 "
        f"-topic:download -topic:crack -topic:activator "
        f"-topic:keygen -topic:nulled -topic:cheat -topic:warez"
    )
    if language:
        query += f" language:{language}"
    
    # API 请求
    url = f"{GITHUB_API}/search/repositories"
    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": per_page
    }
    
    full_url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(full_url, headers=HEADERS)
    
    try:
        with _urlopen_with_retry(req, timeout=30) as response:
            raw = response.read()
            if (response.headers.get("Content-Encoding") or "").lower() == "gzip":
                raw = gzip.decompress(raw)
            data = json.loads(raw.decode("utf-8", "replace"))
            items = data.get("items", [])
            clean = [r for r in items if not is_spam_repo(r)]
            dropped = len(items) - len(clean)
            if dropped:
                print(f"🧹 已过滤 {dropped} 个垃圾仓库")
            return clean
    except Exception as e:
        print(f"Error fetching GitHub API: {e}")
        return []


def fetch_trending_from_page(since="daily"):
    """
    从 GitHub Trending 页面抓取 (备用方案)
    
    Args:
        since: daily/weekly/monthly
    
    Returns:
        list: 仓库列表
    """
    url = f"https://github.com/trending?since={since}"
    html = _http_get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Encoding": "gzip"
    }, timeout=30, retries=3)

    try:
        if not html:
            return []
        
        # 解析每个 article 块
        repos = []
        articles = re.findall(r'<article[^>]*class="Box-row"[^>]*>(.*?)</article>', html, re.DOTALL)
        
        for art in articles[:25]:
            # 仓库路径
            h2_match = re.search(r'<h2[^>]*>.*?<a[^>]*href="(/[^"]+)"', art, re.DOTALL)
            if not h2_match:
                continue
            repo_path = h2_match.group(1).strip()
            # 必须是 /owner/repo 格式 (恰好2个斜杠)
            if repo_path.count('/') != 2:
                continue
            
            full_name = repo_path.lstrip('/')
            
            # 描述
            desc = ""
            desc_match = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', art, re.DOTALL)
            if desc_match:
                desc = html_lib.unescape(re.sub(r'<[^>]+>', '', desc_match.group(1))).strip()
            
            # 语言
            lang = "Unknown"
            lang_match = re.search(r'<span[^>]*itemprop="programmingLanguage"[^>]*>(.*?)</span>', art)
            if lang_match:
                lang = lang_match.group(1).strip()
            
            # 总 Star 数
            stars = 0
            star_match = re.search(r'<a[^>]*href="[^"]*/stargazers"[^>]*>.*?([\d,]+)\s*</a>', art, re.DOTALL)
            if star_match:
                stars = int(star_match.group(1).replace(',', ''))
            
            # 今日/本周新增 Star
            today_stars = 0
            today_match = re.search(r'([\d,]+)\s*stars?\s*(?:today|this week)', art)
            if today_match:
                today_stars = int(today_match.group(1).replace(',', ''))
            
            repos.append({
                "full_name": full_name,
                "html_url": f"https://github.com{repo_path}",
                "description": desc,
                "stargazers_count": stars,
                "language": lang,
                "topics": [],
                "trending_stars": today_stars
            })
        
        return repos
    except Exception as e:
        print(f"Error fetching trending page: {e}")
        return []


def format_repo_item(repo, index):
    """
    格式化单个仓库为 Markdown
    
    Args:
        repo: 仓库数据
        index: 序号
    
    Returns:
        str: Markdown 格式
    """
    name = repo.get("full_name", "Unknown")
    url = repo.get("html_url", "#")
    desc = repo.get("description", "") or "暂无描述"
    stars = repo.get("stargazers_count", 0)
    lang = repo.get("language", "") or "Unknown"
    topics = repo.get("topics", [])
    
    # 构建标签
    tags_str = ""
    if topics:
        tags_str = " ".join([f"`{t}`" for t in topics[:5]])
    
    trending = repo.get("trending_stars", 0)
    trending_line = f"- 🔥 **Trending**: +{trending:,} stars\n" if trending else ""
    
    return f"""### {index}. [{name}]({url})

{desc}

- ⭐ **Stars**: {stars:,}
{trending_line}- 💻 **Language**: {lang}
- 🏷️ **Topics**: {tags_str or "无"}

"""


def generate_article(repos, since="daily", source="GitHub Trending 官方榜单"):
    """
    生成 Hugo 文章
    
    Args:
        repos: 仓库列表
        since: daily/weekly
        source: 数据来源标注
    
    Returns:
        str: Markdown 文章内容
    """
    now = datetime.utcnow() + timedelta(hours=8)  # 北京时间 UTC+8
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")
    
    period = "每日" if since == "daily" else "每周"
    title = f"🔥 GitHub {period}热门项目 ({date_str})"
    
    # 构建内容
    content = f"""---
title: "{title}"
date: {time_str}
tags: ["GitHub", "开源", "热门项目", "Trending"]
categories: ["github"]
---

# 🔥 GitHub {period}热门项目

> 更新时间：{now.strftime("%Y年%m月%d日 %H:%M")} (北京时间)
> 数据来源：{source}

---

以下是过去{period}内最受欢迎的开源项目，按新增 Star 数排序。

"""
    
    # 添加仓库列表
    for i, repo in enumerate(repos[:15], 1):
        content += format_repo_item(repo, i)
    
    # 添加尾部
    content += f"""
---

## 📊 统计

- **收录项目数**: {len(repos)}
- **时间范围**: {period}
- **排序依据**: 新增 Star 数

---

*本文由 GoodInfo GitHub Trending 自动生成，每小时更新。*
"""
    
    return title, content


def save_article(title, content):
    """
    保存文章到 Hugo content 目录
    
    Args:
        title: 文章标题
        content: Markdown 内容
    
    Returns:
        str: 保存的文件路径
    """
    os.makedirs(CONTENT_DIR, exist_ok=True)
    
    now = datetime.now()
    filename = f"github-trending-{now.strftime('%Y-%m-%d-%H')}.md"
    filepath = os.path.join(CONTENT_DIR, filename)
    
    # 防降级覆盖: 同一小时内若已存在一份"官方榜单"数据的高质量文章,
    # 而本次抓取降级到了 Search API, 则保留原有高质量内容, 不用残缺数据覆盖。
    # (降级数据的项目 star 量级与项目数都远低于官方榜单, 覆盖会造成内容倒退)
    if os.path.exists(filepath):
        try:
            with open(filepath, encoding="utf-8") as f:
                existing = f.read()
            official = "数据来源：GitHub Trending 官方榜单"
            degraded = "降级数据源"
            if official in existing and degraded in content and official not in content:
                print(f"⏭️  保留已有官方榜单版本, 跳过降级数据覆盖: {filepath}")
                return filepath
        except Exception:
            pass
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def main():
    """主函数"""
    # 解析参数
    since = "daily"
    if len(sys.argv) > 1:
        since = sys.argv[1] if sys.argv[1] in ["daily", "weekly", "monthly"] else "daily"
    
    print(f"🚀 开始抓取 GitHub Trending ({since})...")
    
    # 方案1: Trending 页面为权威数据源 (真实热度榜, 含总 star 与当日新增)
    print("📡 抓取 GitHub Trending 页面...")
    repos = fetch_trending_from_page(since=since)
    source = "GitHub Trending 官方榜单"
    
    # 方案2: 页面结构变更或抓取失败时, 回退 Search API
    # 注意: Search API 结果质量远低于官方榜单, 且极易混入刷星垃圾仓库,
    # 因此回退结果必须经过反垃圾过滤, 且数量不足时宁可退出也不发低质内容。
    if len(repos) < 5:
        print(f"⚠️ Trending 页面仅返回 {len(repos)} 个项目, 回退 Search API...")
        repos = fetch_trending_repos(since=since, per_page=20)
        source = "GitHub Search API (降级数据源)"
    
    if not repos:
        print("❌ 无法获取数据")
        sys.exit(1)
    
    # 最终安全闸: 再次过滤, 任何残留的垃圾仓库都不得进入正文
    filtered = [r for r in repos if not is_spam_repo(r)]
    if len(filtered) != len(repos):
        print(f"🧹 二次过滤: 移除 {len(repos) - len(filtered)} 个垃圾仓库")
        repos = filtered
    if not repos:
        print("❌ 过滤后无有效项目, 放弃生成 (不发布空/低质内容)")
        sys.exit(1)
    
    # 质量闸: 回退来源的项目数量往往远少于官方榜单, 少于 5 条时拒绝发布,
    # 避免用残缺数据覆盖掉高质量的定时内容。
    if len(repos) < 5:
        print(f"❌ 仅获取到 {len(repos)} 个有效项目, 低于发布阈值 5, 放弃生成")
        sys.exit(1)
    
    print(f"✅ 获取到 {len(repos)} 个项目")
    
    # 生成文章
    print("📝 生成文章...")
    title, content = generate_article(repos, since, source=source)
    
    # 保存
    filepath = save_article(title, content)
    print(f"✅ 文章已保存: {filepath}")
    
    # 输出摘要
    print("\n📊 前5个项目:")
    for i, repo in enumerate(repos[:5], 1):
        name = repo.get("full_name", "Unknown")
        stars = repo.get("stargazers_count", 0)
        print(f"  {i}. {name} ⭐ {stars:,}")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
