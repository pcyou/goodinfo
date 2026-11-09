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
# 本机 DNS (10.0.0.1) 把 github.com 解析到 20.205.243.166, 而该地址的
# 443 路由被中间链路丢弃 (SYN 无应答, TCP 握手永不完成), 导致 Trending
# 页面抓取 100% 超时并降级到质量更差的 Search API。
# 下列 Anycast 边缘 IP 属于同一 GitHub 前端集群, 返回内容一致; 由于 TLS 的
# SNI 与证书校验仍使用主机名 github.com, 固定 IP 不削弱 TLS 安全性。
#
# 2026-11-09 复盘 (16:00 事故): 上一版白名单里的 9 个地址 (140.82.11x.3/4
# 与 20.27.177.113) **全部实测失效** —— 要么连不上, 要么 HTTP 504, 18 次
# 尝试全灭, 脚本最终按质量闸 (len(repos) < 5) 正确地拒绝发布。教训依旧是:
# 固定 IP 白名单会随 GitHub 边缘调度漂移而必然复发, 必须靠定期实测刷新。
#
# 2026-11-09 复盘 (核心修复): 真正的解药不是继续猜 IP, 而是**换一条解析
# 路径** —— 本机 DNS 是黑洞, 但两家独立的 DoH (dns.google 与 cloudflare-dns)
# 给出一致的权威答案 172.182.252.133; 实测该地址 HTTP 200、页面含 9 个
# Box-row、连续 8 次请求全部成功, 且抓到的 9 个项目与当天 08:00 已发布
# 文章完全一致 (顺序/数量/star 数均吻合) → 证明是真实榜单数据。
# 因此这里的硬编码白名单只保留"实测最稳"的少数地址, 并新增 DoH 动态解析
# (见 _doh_resolve_ips) 作为白名单之后的第二梯队, 不再依赖单一猜测。
#
# 2026-11-09 复盘 (假阳性陷阱): 20.27.177.121 等地址会返回 **HTTP 200
# 但 body 只有 4 字节 "OK"** —— 那是 GitHub 边缘节点的健康检查端点, 不是
# Trending 页面。只看状态码会把它误判为成功, 从而生成 0 个项目的空文章。
# 因此 _http_get 对 github.com 的 HTML 页面额外校验: 长度 > 10000 且含
# "Box-row" 且以 "</html>" 闭合, 任一不满足即视为无效响应并换下一个 IP。
# 同样地, 504 错误页 (仅 92 字节) 也会被这道校验挡下。
# 20.27.177.121 是已知的假阳性端点, **禁止**加入任何白名单或候选列表。
#
# 教训: 固定 IP 白名单会随 GitHub 边缘调度漂移而失效, 必须靠定期实测刷新,
# 不能假设"上次能用这次也能用"; 动态解析 (DoH) 只是补充, 不能替代实测。
GITHUB_WEB_FALLBACK_IPS = (
    "172.182.252.133",
    "172.182.252.137",
)

# 同段邻近地址, 作为白名单与 DoH 之后的兜底
GITHUB_WEB_SECONDARY_IPS = (
    "172.182.252.134",
    "172.182.252.135",
    "172.182.252.136",
)

# 末位兜底: 本机 DNS 当前解析值, 可能随时恢复; 放在最后, 不占用优先额度
GITHUB_WEB_LAST_RESORT_IPS = (
    "20.205.243.166",
)

# 主机名 -> 硬编码白名单 (仅第一梯队; 其余梯队由 _candidate_ips 按时序组装)
_FALLBACK_IPS = {
    "github.com": GITHUB_WEB_FALLBACK_IPS,
}

# 死 IP 黑名单 (自愈): 主机名 -> {已连续失败 >= 2 次的 IP}
# 某个 IP 一旦进入黑名单, 本进程后续请求直接跳过它, 不再浪费超时窗口。
_DEAD_IPS = {}

# 判定为"死 IP"所需的连续失败次数
_DEAD_IP_THRESHOLD = 2

# 每个 IP 的首次尝试超时 (秒)。
# 健康边缘 IP 实测 0.4-3s 返回, 用短超时可以快速识别黑洞地址;
# 超时后该 IP 才被熔断并让位给下一个候选。
#
# 2026-11-09 复盘: 该阈值原为 6s, 但 172.182.252.133 在**冷连接**下
# 首包偶尔要 6.3s 左右 (热连接 1.2-1.9s), 于是健康 IP 会被误判成黑洞
# 并打印"⏱️ 判定为黑洞", 造成不必要的熔断。这里放宽到 12s:
# 真正的黑洞 IP 是"SYN 无应答 / 读取永远不返回", 等满 12s 才暴露,
# 代价可以接受; 而健康边缘 IP 不再被误杀。整体请求预算 (timeout=15)
# 仍作为上限, 因此单次抓取的耗时不会明显变长。
_FIRST_ATTEMPT_TIMEOUT = 12

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


# ==========================================
# DoH (DNS over HTTPS) 动态解析
# ==========================================
# 本机 DNS 会把 github.com 解析到黑洞地址, 但 DoH 服务 (dns.google /
# cloudflare-dns) 会给出完全不同的边缘 IP。硬编码白名单会随 GitHub 边缘
# 调度漂移而必然失效, 动态解析是对"硬编码必然过期"这一根因的补充。
#
# 设计约束:
#   * 仅用标准库 (urllib.request + json), 不引入第三方依赖;
#   * 模块级缓存, TTL 600 秒, 避免每次请求都打 DoH;
#   * 超时与异常一律静默降级 —— DoH 不可达时只影响候选来源, 绝不能
#     让整体抓取失败。
DOH_ENDPOINTS = (
    # (URL, 额外请求头) —— 两者取并集
    ("https://dns.google/resolve?name={host}&type=A", {}),
    (
        "https://cloudflare-dns.com/dns-query?name={host}&type=A",
        {"Accept": "application/dns-json"},
    ),
)

# DoH 解析结果的本地缓存: 主机名 -> (时间戳, [IP, ...])
_DOH_CACHE = {}

# DoH 缓存有效期 (秒)
_DOH_CACHE_TTL = 600

# 单个 DoH 端点的超时 (秒) —— 不可达时快速放弃, 不拖慢整体抓取
_DOH_TIMEOUT = 5


def _doh_fetch_json(url, extra_headers):
    """请求 DoH 端点并解析 JSON, 失败返回 None。"""
    headers = {
        "User-Agent": "GoodInfo-GitHub-Trending",
        "Accept": "application/dns-json",
    }
    headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=_DOH_TIMEOUT) as response:
            raw = response.read()
            encoding = (response.headers.get("Content-Encoding") or "").lower()
        if encoding == "gzip":
            raw = gzip.decompress(raw)
        elif encoding == "deflate":
            raw = zlib.decompress(raw, -zlib.MAX_WBITS)
        return json.loads(raw.decode("utf-8", "replace"))
    except Exception as exc:
        print(f"  DoH 请求失败 {url}: {type(exc).__name__}: {exc}")
        return None


def _doh_resolve_ips(host):
    """通过 DoH 解析主机名的 A 记录, 返回 IP 列表 (按 DoH 返回顺序去重)。

    两个独立 DoH 服务的结果取并集 —— 两者给出一致答案时可信度更高,
    只有一个可用时也仍有价值。异常一律吞掉并返回空列表: DoH 是**可选**
    增强, 它的故障绝不能导致整体抓取失败。
    """
    cached = _DOH_CACHE.get(host)
    now = time.time()
    if cached and now - cached[0] < _DOH_CACHE_TTL:
        return cached[1]

    ips = []
    for template, extra_headers in DOH_ENDPOINTS:
        url = template.format(host=urllib.parse.quote(host))
        data = _doh_fetch_json(url, extra_headers)
        if not data:
            continue
        if str(data.get("Status", 0)) != "0":
            continue
        for answer in data.get("Answer") or []:
            if int(answer.get("type", 0) or 0) != 1:
                continue
            ip = (answer.get("data") or "").strip()
            # DoH 回答里偶尔混进 CNAME 等其它类型, 这里只收 IPv4 字面量
            if not re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", ip):
                continue
            if ip not in ips:
                ips.append(ip)

    if ips:
        print(f"  DoH 解析 {host} -> {ips}")
    else:
        print(f"  ⚠️ DoH 未解析到 {host} 的 A 记录, 静默降级 (仅用本地候选)")
    # 失败结果同样写入缓存, 避免 DoH 故障时反复超时拖慢抓取
    _DOH_CACHE[host] = (now, ips)
    return ips


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
    # 梯队顺序 (规范要求, 不可调换):
    #   1) 硬编码实测白名单 -> 2) DoH 动态地址 -> 3) secondary -> 4) 本机 DNS
    # 每一梯队内部去重, 但不跨梯队去重: 同一个 IP 若同时出现在白名单与
    # DoH 结果里, 保留它在更高优先级的位置即可 (下面的 ip not in ips 会
    # 跳过重复项, 因此顺序仍然稳定)。

    # 1) 首选: 硬编码的已实测可达边缘 IP (CTO 2026-11-09 实测白名单)
    for ip in _FALLBACK_IPS.get(host, ()):
        if ip not in ips:
            ips.append(ip)
    # 2) 次选: DoH 动态解析出的边缘 IP (本次修复的核心 —— 本机 DNS 是黑洞,
    #    但 dns.google / cloudflare-dns 会给出真正可达的边缘地址;
    #    DoH 不可达时静默降级为空列表, 不影响其余候选)
    for ip in _doh_resolve_ips(host):
        if ip not in ips:
            ips.append(ip)
    # 3) 再次: secondary 兜底地址 (同段邻近边缘 IP)
    for ip in GITHUB_WEB_SECONDARY_IPS:
        if ip not in ips:
            ips.append(ip)
    # 4) 末位兜底: 保留的旧地址 (本机 DNS 当前解析值, 可能随时恢复)
    for ip in GITHUB_WEB_LAST_RESORT_IPS:
        if ip not in ips:
            ips.append(ip)
    # 5) 垫底: 本机 DNS 当前解析结果 (可能是黑洞源, 仅作兜底)
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


def _is_invalid_response(exc):
    """判断异常是否为"IP 可达但返回无效内容"。

    2026-11-09 复盘: 这类失败 (200 + "OK" 假阳性、504 短响应、截断页面)
    与超时一样说明该 IP 不能提供有效数据, 应计入 ip_failures 并在达到
    阈值后拉黑, 否则脚本会在同一个坏 IP 上反复浪费预算。
    """
    text = str(exc).lower()
    return "invalid response" in text or "truncated response" in text


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


# github.com 的 Trending HTML 页面最小合理长度。
# 健康页面实测约 520 KB (gzip 解压后), 远大于该阈值;
# 而假阳性端点只回 4 字节 "OK", 504 错误页只有 92 字节。
_MIN_TRENDING_HTML_BYTES = 10000


def _validate_html_body(text):
    """校验 HTML 响应体确实是 GitHub 的 Trending 页面, 而不是假阳性。

    2026-11-09 复盘: 某些边缘地址 (如 20.27.177.121) 会返回 **HTTP 200
    但 body 只有 4 字节 "OK"** —— 那是边缘节点的健康检查端点, 不是 Trending
    页面。若只看状态码就会把它误判为成功, 从而生成 0 个项目的空文章。
    504 错误页 (92 字节) 同样会被这道校验挡下。

    校验三要素: 长度 > 10000、含 "Box-row"、以 "</html>" 闭合。
    任一不满足 → 抛异常, 由调用方走"换下一个 IP"的快速失败路径。
    """
    size = len(text)
    if size <= _MIN_TRENDING_HTML_BYTES:
        raise IOError(
            f"invalid response: body too small ({size} bytes, "
            f"expected > {_MIN_TRENDING_HTML_BYTES})"
        )
    if "Box-row" not in text:
        raise IOError(
            f"invalid response: no Box-row marker ({size} bytes, "
            f"likely a health-check endpoint)"
        )
    stripped = text.rstrip()
    if not stripped.endswith("</html>"):
        raise IOError(
            f"invalid response: not closed by </html> ({size} bytes, truncated)"
        )
    return text


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
                # 假阳性端点会返回 200 + "OK", 必须校验正文才是真正的 Trending 页面
                if expect_html:
                    _validate_html_body(text)
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
                # 无效响应 (200 + "OK" 假阳性 / 504 短响应 / 截断页):
                # IP 可达但拿不到有效数据, 同样计一次失败, 达到阈值后拉黑。
                if _is_invalid_response(exc):
                    print(f"  🚫 {ip} 返回无效响应, 计一次失败并换下一个 IP")

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
                # 截断的 HTML 仍可能解析出部分内容, 且 200 + "OK" 的假阳性
                # 端点也会蒙混过关, 故对 HTML 页面做完整有效性校验;
                # JSON 接口 (Search API) 不含 Box-row/</html>, 由 expect_html
                # 关闭该校验。
                if expect_html:
                    _validate_html_body(text)
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
                # 无效响应重试也没有意义 (同一 IP 返回同样的垃圾内容),
                # 直接换下一个候选 IP, 但仍计入 ip_failures 以便阈值拉黑。
                if _is_invalid_response(exc):
                    print(f"  🚫 {ip} 返回无效响应, 计一次失败并换下一个 IP")
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

# 正文最多展示的项目数上限。
# 实测 Trending 榜单条目数区间为 14~24, 取 25 足以覆盖正常情况;
# 仅在异常超额时才发生截断, 截断时必须在统计区块显式标注, 不得静默丢弃信息。
# 统计区块的"收录项目数"必须与正文实际渲染条目数严格一致 (恒等约束)。
DISPLAY_LIMIT = 25

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
    # 正文实际渲染的条目集合 —— 统计区块必须以它为准, 保证"正文条目数 == 收录项目数"恒成立
    displayed = repos[:DISPLAY_LIMIT]
    for i, repo in enumerate(displayed, 1):
        content += format_repo_item(repo, i)

    # 截断时显式标注被省略的项目数, 避免静默丢弃信息
    # (未发生截断时绝不出现该行, 保持与既有文章风格一致)
    note_line = ""
    if len(repos) > len(displayed):
        note_line = f"- **备注**: 榜单共 {len(repos)} 个项目，此处展示前 {len(displayed)} 个\n"

    # 添加尾部
    content += f"""
---

## 📊 统计

- **收录项目数**: {len(displayed)}
- **时间范围**: {period}
- **排序依据**: 新增 Star 数
{note_line}

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
