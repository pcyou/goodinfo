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
#
# 2026-10-24 复盘: 黑洞 IP 不只是本机 DNS 那一个 —— 20.27.177.113 这一
# 陈旧备用地址同样会在"正文读取"阶段挂死 (TLS 握手能成功, 但读 body
# 永远收不到数据)。因此这里把**已实测 HTTP 200** 的 4 个边缘 IP 单独
# 提为白名单并放在最前面, DNS 解析结果一律垫后。
#
# 2026-10-26 复盘: 上一版白名单里的 "140.82.11x.3" 四个地址已全部黑洞化
# (TLS 握手成功但 body 永远不返回), 同时 "140.82.116.3" 退化为间歇性可用。
# 实测同一 GitHub 前端集群的 "140.82.11x.4" 四地址稳定返回 HTTP 200 且
# /trending 页面结构完整 (11 个 Box-row), 因此把 .4 系列提到白名单最前面,
# .3 系列降级为次选, 陈旧的 "20.27.177.113" 移入末位。
#
# 教训: 固定 IP 白名单会随 GitHub 边缘调度漂移而失效, 必须靠定期实测刷新,
# 不能假设"上次能用这次也能用"。
GITHUB_WEB_FALLBACK_IPS = (
    "140.82.112.4",
    "140.82.116.4",
    "140.82.113.4",
    "140.82.114.4",
    "140.82.116.3",
)

# 已实测可达但可能随时间失效的备用地址, 排在白名单之后尝试
GITHUB_WEB_SECONDARY_IPS = (
    "140.82.112.3",
    "140.82.113.3",
    "140.82.114.3",
    "20.27.177.113",
)

# 主机名 -> 备用 IP 列表 (顺序即优先级)
_FALLBACK_IPS = {
    "github.com": GITHUB_WEB_FALLBACK_IPS + GITHUB_WEB_SECONDARY_IPS,
}

# 死 IP 黑名单 (自愈): 主机名 -> {已连续失败 >= 2 次的 IP}
# 某个 IP 一旦进入黑名单, 本进程后续请求直接跳过它, 不再浪费超时窗口。
_DEAD_IPS = {}

# 判定为"死 IP"所需的连续失败次数
_DEAD_IP_THRESHOLD = 2

# 每个 IP 的首次尝试超时 (秒)。
# 健康边缘 IP 实测 0.4-3s 返回, 用短超时可以快速识别黑洞地址;
# 超时后该 IP 才被熔断并让位给下一个候选。
_FIRST_ATTEMPT_TIMEOUT = 6

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


def _urlopen_with_retry(req, timeout=15, retries=3):
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
    """候选 IP 列表: **已验证可达的边缘 IP 在前, DNS 解析结果垫后**。

    2026-10-24 复盘: 本机 DNS 把 github.com 解析到一个正文读取会挂死的
    黑洞地址, 而旧的实现把 DNS 结果排在最前, 于是每次请求都要先在黑洞
    地址上耗尽整个超时窗口, 健康边缘 IP 根本轮不到。
    黑名单中的 IP 直接剔除 (自愈: 已被证实读不出正文的地址不再重试)。
    """
    ips = []
    # 1) 首选: 硬编码的已验证可达边缘 IP
    for ip in _FALLBACK_IPS.get(host, ()):
        if ip not in ips:
            ips.append(ip)
    # 2) 垫底: 本机 DNS 当前解析结果 (可能是黑洞源, 仅作兜底)
    try:
        for info in _orig_getaddrinfo(host, port, _socket.AF_INET):
            ip = info[4][0]
            if ip not in ips:
                ips.append(ip)
    except Exception:
        pass
    # 3) 剔除已被判定为死的 IP
    dead = _DEAD_IPS.get(host) or set()
    alive = [ip for ip in ips if ip not in dead]
    if dead:
        print(f"  跳过 {len(ips) - len(alive)} 个已知死 IP: {sorted(dead)}")
    if not alive and ips:
        # 全部候选都被拉黑时, 宁可重试一次也不要直接放弃
        print("  ⚠️ 全部候选 IP 均被拉黑, 放开一次重试")
        return ips
    return alive


def _is_timeout(exc):
    """判断异常是否为超时类 (黑洞 IP 的确定性信号)。"""
    if isinstance(exc, TimeoutError):
        return True
    reason = getattr(exc, "reason", None)
    if isinstance(reason, TimeoutError):
        return True
    text = str(exc).lower()
    return "timed out" in text or "timeout" in text


def _mark_ip_dead(host, ip, failures):
    """累计单个 IP 的失败次数, 达到阈值后加入黑名单。"""
    if failures < _DEAD_IP_THRESHOLD:
        return
    dead = _DEAD_IPS.setdefault(host, set())
    if ip not in dead:
        dead.add(ip)
        print(f"  🚫 熔断 {ip} (连续失败 {failures} 次), 本进程后续跳过该 IP")


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


def _raw_http_get(host, path, ip, headers, timeout=15):
    """直连指定 IP 取回页面, 自行处理 chunked 与 gzip 解码。

    urllib/http.client 在本机出口链路上偶尔会在正文读取阶段卡死;
    原生 socket 路径实测 5/5 成功, 作为兜底手段保留。

    2026-10-24 复盘: 黑洞 IP 的典型表现是"TCP + TLS 都成功, 但 recv
    永远不返回"。因此这里在握手完成后显式调用 settimeout, 给**读取阶段**
    单独加上保护, 避免一次挂死拖垮整个抓取流程。
    """
    ctx = ssl.create_default_context()
    sock = ctx.wrap_socket(
        _socket.create_connection((ip, 443), timeout=timeout),
        server_hostname=host,
    )
    try:
        # 读取阶段的独立超时保护 (握手后的 socket 需要显式设置)
        sock.settimeout(timeout)
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


def _http_get(url, headers, timeout=12, retries=2, max_attempts=18, expect_html=True):
    """GET a URL and return the decoded body as text.

    处理五类传输缺陷:

    1. *DNS 黑洞.* 本机解析出的 github.com 地址能完成 TLS 握手, 但正文
       读取会永远挂死。故候选 IP 里已验证可达的边缘 IP 排在最前, DNS
       结果垫后 (见 _candidate_ips)。

    2. *全局预算被黑洞 IP 吃光.* 旧的 max_attempts 是所有候选 IP 共享的
       总预算: 每个坏 IP 要消耗 1 次 raw + 3 次 urllib 重试 = 4 次, 两个
       坏 IP 就是 8 次 > 6 次上限, 于是还没轮到健康 IP 就已退出。现在改为
       **每个 IP 独立预算** (默认 3 次), 整体上限 18 次可覆盖全部候选。

    3. *未压缩传输拖慢.* Trending 页面未压缩约 551 KB, 走本机出口需 21-37s,
       会撑爆超时。请求 gzip 后载荷降到约 46 KB, 传输约 0.4s。

    4. *重试只覆盖了连接.* urlopen 在响应头到达后即返回, 正文在此之后才读,
       因此截断响应抛出的 IncompleteRead 落在重试循环之外, 从未被重试。
       这里把正文读取纳入重试范围, 并检测截断的载荷。

    5. *http.client 正文读取卡死.* 偶发于本机出口链路, 故保留原生 socket
       取数路径作为兜底。

    expect_html=True 时会校验响应体是否以 </html> 闭合 (用于识别被截断的
    HTML 页面); 取 JSON 接口 (如 GitHub Search API) 时须传 expect_html=False,
    否则 JSON 响应会因不含 </html> 被误判为截断。

    失败时返回 ""。
    """
    parsed = urllib.parse.urlparse(url)
    host = parsed.hostname or ""
    path = parsed.path or "/"
    if parsed.query:
        path += "?" + parsed.query
    last_exc = None

    # 每个 IP 的独立尝试预算: raw 一次 + urllib 重试若干次。
    # total_budget 是所有候选 IP 共享的硬上限 (兜底), 保证整体耗时可控。
    per_ip_budget = 1 + max(0, retries)
    total_budget = max_attempts
    attempts = 0

    # 逐个 IP 尝试。候选顺序已把已验证可达的边缘 IP 放在最前。
    for ip in _candidate_ips(host):
        if attempts >= total_budget:
            break

        # 单个 IP 连续失败次数 (用于熔断 / 黑名单)
        ip_failures = 0

        # 首次尝试用较短的超时: 健康 IP 0.4-3s 就能返回, 用不着一口气等满;
        # 黑洞 IP 则在几秒内就暴露, 快速失败并交给下一个 IP。
        # 只有在"看起来有希望"的 IP 上才启用完整超时。
        first_timeout = min(timeout, _FIRST_ATTEMPT_TIMEOUT)

        # 优先走原生 socket 路径 (实测最稳), 失败再退回 urllib
        if attempts < total_budget:
            attempts += 1
            try:
                text = _raw_http_get(host, path, ip, headers, timeout=first_timeout)
                if expect_html and "</html>" not in text:
                    raise IOError(f"truncated response ({len(text)} bytes, no </html>)")
                return text
            except Exception as exc:
                last_exc = exc
                ip_failures += 1
                print(f"  raw attempt {attempts}/{total_budget} failed on {ip}: {exc}")
                # 首次尝试就超时的 IP 直接判死: 该路径已证明读不出正文,
                # 再花一次 urllib 重试纯属浪费超时窗口, 立刻让位给下一个 IP。
                # 首次超时已经是"黑洞"的确定性证据, 故按阈值计满并立即拉黑。
                if _is_timeout(exc):
                    print(f"  ⏱️ {ip} 首次即超时, 判定为黑洞并跳过")
                    _mark_ip_dead(host, ip, _DEAD_IP_THRESHOLD)
                    continue

        for attempt in range(retries):
            if attempts >= total_budget or ip_failures >= per_ip_budget:
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
                # 截断的 HTML 仍可能解析出部分内容, 故先确认文档闭合再采信;
                # JSON 接口 (Search API) 不含 </html>, 故由 expect_html 关闭该校验。
                if expect_html and "</html>" not in text:
                    raise IOError(f"truncated response ({len(text)} bytes, no </html>)")
                _PINNED_IP[host] = None
                return text
            except Exception as exc:
                last_exc = exc
                ip_failures += 1
                print(f"  HTTP attempt {attempts}/{total_budget} failed on {ip}: {exc}")
                # 超时是"黑洞"的确定性信号: 该 IP 读不出正文, 再重试也是
                # 白白等满整个超时窗口, 故立刻熔断并让位给下一个候选 IP。
                if _is_timeout(exc):
                    print(f"  ⏱️ {ip} 超时, 直接判定为黑洞并跳过")
                    break
                if attempt < retries - 1:
                    time.sleep(2 * (attempt + 1))
        _PINNED_IP[host] = None

        # 熔断: 该 IP 已连续失败达阈值则拉黑, 直接跳到下一个 IP,
        # 不再在同一个黑洞地址上白白耗掉几十秒。
        _mark_ip_dead(host, ip, ip_failures)

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

    # 降级路径同样要能自愈: Search API 走的是 api.github.com, 若该主机在本
    # 出口链路上不可达, 必须给出清晰错误并返回空列表, 而不是抛出未捕获
    # 异常或挂死。这里先试带 IP 容错的 _http_get (它会按候选 IP 依次尝试),
    # 失败后再退回常规 urlopen。
    raw_text = _http_get(full_url, headers=HEADERS, timeout=15, retries=2,
                         expect_html=False)
    if raw_text:
        try:
            data = json.loads(raw_text)
            items = data.get("items", [])
            clean = [r for r in items if not is_spam_repo(r)]
            dropped = len(items) - len(clean)
            if dropped:
                print(f"🧹 已过滤 {dropped} 个垃圾仓库")
            return clean
        except Exception as e:
            print(f"Error parsing GitHub API response: {e}")
            return []

    print("⚠️ api.github.com 经 IP 容错仍不可达, 回退常规 urlopen 重试一次...")
    req = urllib.request.Request(full_url, headers=HEADERS)

    try:
        with _urlopen_with_retry(req, timeout=15) as response:
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
    }, timeout=15, retries=3)

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
