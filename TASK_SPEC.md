# TASK_SPEC: 修复 github_trending.py 抓取超时导致任务失败

## 缺陷 (已由 CTO 现场诊断确认)

2026-10-24 16:01 HKT 运行 `python3 scripts/github_trending.py daily` 失败:

```
  raw attempt 1/6 failed on 20.205.243.166: The read operation timed out
  HTTP attempt 2/6 failed on 20.205.243.166: <urlopen error timed out>
  HTTP attempt 3/6 failed on 20.205.243.166: <urlopen error timed out>
  HTTP attempt 4/6 failed on 20.205.243.166: <urlopen error timed out>
  raw attempt 5/6 failed on 20.27.177.113: The read operation timed out
  HTTP attempt 6/6 failed on 20.27.177.113: <urlopen error timed out>
Error fetching https://github.com/trending?since=daily: <urlopen error timed out>
⚠️ Trending 页面仅返回 0 个项目, 回退 Search API...
❌ 无法获取数据
```

### 根因

`_http_get()` 中 `max_attempts=6` 是**全局共享预算**, 而 `_candidate_ips()` 返回的
IP 顺序是:

```
['20.205.243.166', '20.27.177.113', '140.82.112.3', '140.82.113.3', '140.82.114.3', '140.82.116.3']
```

前两个 IP (本机 DNS 黑洞地址 + 陈旧备用地址) 的**正文读取会挂死**,
每个消耗 1 次 raw + 3 次 urllib 重试 = 4 次预算。
两个死 IP 合计吃掉 **8 次预算 > 6 次上限**, 于是 `_http_get()` 在**还没轮到
4 个健康边缘 IP 之前就耗尽预算并退出**。

### CTO 已实测验证的关键事实

1. 4 个健康边缘 IP **完全可用**:
   ```
   140.82.112.3  http=200 size=45537
   140.82.113.3  http=200 size=45534
   140.82.114.3  http=200 size=45535
   140.82.116.3  http=200 size=45549
   ```
2. 用**现有 `_raw_http_get()` 直连 140.82.113.3** 实测成功:
   ```
   len= 550862  has_html_close= True  articles= 8
   ```
   => **解析逻辑与 socket 路径都没问题, 纯粹是候选 IP 排序 + 预算分配问题。**
3. TLS 握手对全部 6 个 IP 均能成功 (0.2~1.0s), 但**正文读取**对前两个 IP 会挂死。
   => 不能用 TLS 探测来区分死活, 必须靠"读正文"来判断。
4. GitHub Search API (`api.github.com` / 20.205.243.168) **是通的** (http=200),
   但它是降级源, 质量低且易混入 SEO 垃圾仓库, 不能作为主路径。

## 修改要求 (scripts/github_trending.py)

### 修复 1 (核心): 健康 IP 优先 + 每 IP 独立预算

在 `_http_get()` 中:
- 把 `max_attempts` 从"全局总预算"改为**每个 IP 独立的尝试预算**, 并把整体
  上限提到足以覆盖全部 6 个候选 IP (例如每 IP 3 次尝试, 总上限 18)。
- **候选 IP 排序必须把已验证可达的边缘 IP 放在最前面**, 把本机 DNS 解析出的
  地址放到最后 (本机 DNS 是黑洞源)。建议维护一个"优先边缘 IP"元组, 或直接
  调整 `_candidate_ips()` 的返回顺序: `_FALLBACK_IPS` 优先, DNS 结果垫后。
- **新增"熔断"**: 某个 IP 若已失败(超时), 后续不再重复重试它, 直接跳到下一个 IP。
  避免在单个黑洞 IP 上浪费 90s。

### 修复 2: 单次请求超时收紧 + 快速失败

- `_http_get` 的 `timeout` 默认值 30s 偏大。黑洞 IP 单次挂死 30s, 6 个 IP 最坏
  要 3 分钟。改为**更短的超时** (建议 12~15s), 配合熔断后总耗时可控。
- 给 `_raw_http_get` 增加 `socket.settimeout` 在读取阶段的独立保护 (若已存在则保留)。

### 修复 3: 死 IP 黑名单 (自愈)

- 在模块级维护一个 `_DEAD_IPS` 集合 (host -> set(ip))。
- 某 IP 连续失败 >= 2 次后加入黑名单, 本进程后续请求直接跳过。
- 对 `github.com` 硬编码**已验证可达**的边缘 IP 白名单优先使用:
  `140.82.112.3, 140.82.113.3, 140.82.114.3, 140.82.116.3`
  (这 4 个 CTO 已实测 HTTP 200)。

### 修复 4: 降级路径也必须能自愈

当前 Trending 页面失败后回退 `fetch_trending_repos()` (Search API), 但该 API
用的是 `_urlopen_with_retry` + `HEADERS`, **没有走 `_http_get` 的 IP 容错逻辑**。
需确认 Search API 路径在 `api.github.com` 不可达时也能给出清晰错误, 且**不得**
让降级数据覆盖已有的官方榜单内容 (现有 `save_article()` 已有该保护, 不要破坏)。

## 约束

- **不改动** `fetch_trending_from_page()` 的 HTML 解析正则 (已验证 8 个 article 解析正确)。
- **不改动** `fetch_trending_repos()` / `generate_article()` / `save_article()` 的业务逻辑。
- **不改动** markdown 模板与文章输出格式。
- **不改动** `main()` 的数据源优先级 (Trending 页面为权威源, Search API 降级) —— 已修复过, 勿回退。
- 保持中文注释风格。
- 单文件改动, 不引入新依赖 (仅用标准库 `socket`/`ssl`/`time`)。
- **不得**为了"通过测试"而放宽 `len(repos) < 5` 的发布质量闸。

## 验收标准

1. `python3 -c "import ast; ast.parse(open('scripts/github_trending.py').read())"` 通过。
2. 实跑 `python3 scripts/github_trending.py daily`:
   - 退出码 0
   - 输出 `✅ 获取到 N 个项目`, N >= 5
   - 输出前 5 个项目为**真实知名开源项目** (非 SEO 垃圾仓库)
   - 抓取耗时 < 90 秒
3. 生成的 Markdown 文件 frontmatter 合法, 中文内容无乱码, 项目名/star 数/描述非空。
4. 连续跑 2 次不报错 (验证熔断/黑名单不会误伤健康 IP)。

## 备份

原文件已备份至 `/tmp/github_trending.py.bak_20261024_160745`。
