---
title: "Antigravity-Manager ：为 Antigravity 提供一键无缝账号切换功能"
date: 2026-01-03T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Antigravity-Manager 是一个集 AI 账号管理、协议中转、智能调度于一体的“本地 AI 控制中心”。   它能帮你： ✅ 一键切换多个 AI 账号 ✅ 稳定调用 Claude / GPT / Gemini ✅ 自动修复限流错误 ✅ 节省 Token 与时间   帮你统一管理和中转多"
source_url: "https://www.xiaohu.ai/p/antigravity-manager-antigravity/28229121"
xiahuid: "28229121"
---

## 📰 正文

Antigravity-Manager 是一个集 AI 账号管理、协议中转、智能调度于一体的“本地 AI 控制中心”。


它能帮你：
✅ 一键切换多个 AI 账号
✅ 稳定调用 Claude / GPT / Gemini
✅ 自动修复限流错误
✅ 节省 Token 与时间


帮你统一管理和中转多家 AI 服务的账号（如 OpenAI、Claude、Gemini 等），并将不同厂商的接口协议转换成统一的 API 标准。

![image]()

> 

换句话说：
它让你在一个应用里就能 一键切换账号 + 调用不同模型 + 自动中转请求，
不再需要记 token、改 API URL、手动登录登出。


- 

✅ 一键切换账号（不用反复登录/登出）

- 

✅ 自动检测失效账号

- 

✅ 兼容多个 AI 协议（OpenAI / Claude / Gemini）

- 

✅ 智能分流和修复请求

- 

✅ 本地运行，无隐私风险

- 

✅ 图形界面 + 命令行都支持



核心功能


![image]()


① 智能仪表盘（Smart Dashboard）



💡 一眼看清所有 AI 账号的状态。

- 

实时显示：各账号的剩余额度、状态（健康/封禁/限流）

- 

自动推荐最优账号：系统根据配额、延迟、速率，动态推荐最合适的账号调用

- 

快照记录：每个账号的更新时间和使用率

![image]()



🧠 举例：
你有 3 个 Claude 账号、2 个 Gemini 账号，它会告诉你哪个快用完了，哪个最空闲，并自动优先使用最稳定的那个。


---



② 强大的账号管家（Account Manager）



💡 让账号管理彻底自动化。

- 

支持 OAuth 2.0 登录（自动生成授权链接）

- 

支持 批量导入 JSON 配置（一次添加几十个账号）

- 

自动识别 403 封禁 / 401 失效

- 

可视化管理界面 + 拖拽排序

- 

一键禁用 / 启用账号



🧩 小功能亮点：

- 

拖拽调整账号顺序，常用账号置顶

- 

自动保存排序偏好，下次启动直接生效



---



③ 协议转换（API Proxy）



💡 把不同厂商的接口统一成标准格式。

![image]()


🔄 自动修复：

- 

当遇到限流（429）或 Token 过期时，系统会自动切换账号继续请求

- 

完全无感知，调用不中断

![image]()



📈 应用场景：

> 

你可以把它当作「本地中转服务器」，
让任何 AI 客户端（Cursor、Claude CLI、Cherry Studio）
都统一走一个 Base URL。



---



④ 模型智能路由（Model Router）



💡 把复杂的模型体系自动分层调度。

- 

自动分类模型家族（如 GPT-4 → gemini-3-pro-high）

- 

按账号类型（Ultra / Pro / Free）自动优先级排序

- 

高级模型优先供前台对话，后台任务自动降级（省 Token）

- 

支持正则匹配自定义映射

![image]()



🧠 举例：
当你跑 Claude CLI 时，它能自动识别“后台摘要任务” → 降级到 Flash 模型；
而主要对话仍用高级模型（Sonnet / Gemini 3 Pro）。


---



⑤ 多模态与图像生成功能（Imagen 3 支持）


- 

支持图片生成与识别（4K 高清）

- 

支持多种分辨率：1024×1024、16:9、21:9、2K

- 

支持自动参数映射：size=1024x1024 → 匹配合适的 Imagen 3 模型



🧩 适用范围：

- 

文本转图像

- 

图片理解（OCR / 视觉输入）

- 

UI 原型生成



---



⑥ 智能错误恢复（Self-Healing System）



遇到错误时自动修复，不需要你手动干预。

![image]()


🧠 意思是：

> 

你的请求基本不会失败。系统会自己“想办法重试”，直到成功。



---



⑦ 高级调度系统（Scheduling Engine）


- 

账号池支持三种模式：
1️⃣ Exclusive 专属模式：单账号独享
2️⃣ Pooled 池化模式：多个账号轮流使用
3️⃣ Fallback 模式：备用账号自动顶替

- 

内置 3 层限流保护机制

- 

全局 Session 粘性（同一会话始终用同一账号）

![image]()



---



⑧ 日志系统与可视化监控


- 

实时显示请求、响应、耗时、Token 使用量

- 

日志等级（INFO / DEBUG / TRACE）分层

- 

可搜索、过滤、导出

- 

请求完成时自动标记 Token 消耗与账号来源



安装与使用



---



🖥️ 方式一：macOS（推荐）



```None
brew tap lbjlaq/antigravity-manager https://github.com/lbjlaq/Antigravity-Manager
brew install --cask --no-quarantine antigravity-tools

```



---



🪟 方式二：Windows


- 

直接下载 .msi 安装包

- 

或下载 portable 便携版（可放 U 盘运行）



---



🐧 方式三：Linux



下载 .AppImage 或 .deb，命令行执行：


```None
chmod +x AntigravityTools.AppImage
./AntigravityTools.AppImage

```



---



🧠 五、接入示例（Claude / Gemini / Python）



Claude CLI:



```None
export ANTHROPIC_API_KEY="sk-antigravity"
export ANTHROPIC_BASE_URL="http://127.0.0.1:8045"
claude

```



Python SDK:



```None
import openai
client = openai.OpenAI(
    api_key="sk-antigravity",
    base_url="http://127.0.0.1:8045/v1"
)
response = client.chat.completions.create(
    model="gemini-3-flash",
    messages=[{"role": "user", "content": "写一个Python快速排序"}]
)
print(response.choices[0].message.content)
```



项目信息


- 

🌍 GitHub： https://github.com/lbjlaq/Antigravity-Manager

---

*来源：[Antigravity-Manager ：为 Antigravity 提供一键无缝账号切换功能](https://www.xiaohu.ai/p/antigravity-manager-antigravity/28229121)*
