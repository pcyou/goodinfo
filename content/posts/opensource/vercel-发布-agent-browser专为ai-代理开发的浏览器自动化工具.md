---
title: "Vercel  发布 “Agent Browser”：专为AI 代理开发的浏览器自动化工具"
date: 2026-01-13T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Vercel 实验室（Vercel Labs）发布全新开源项目 Agent Browser 。该工具是一个为人工智能代理（AI Agents）设计的浏览器自动化命令行工具（CLI），旨在让 AI 模型不仅能理解网页信息，还能直接在网页上执行操作。   Vercel 表示，Agent Browser"
source_url: "https://www.xiaohu.ai/p/vercel-agent-browser-ai/28558819"
xiahuid: "28558819"
---

## 📰 正文

Vercel 实验室（Vercel Labs）发布全新开源项目 Agent Browser 。该工具是一个为人工智能代理（AI Agents）设计的浏览器自动化命令行工具（CLI），旨在让 AI 模型不仅能理解网页信息，还能直接在网页上执行操作。


Vercel 表示，Agent Browser 的出现，为 AI 代理与真实互联网交互提供了底层执行能力，标志着从“对话式智能”向“行动式智能”迈出了关键一步。

![image]()

- 

零配置（Zero config）：安装即可用，无需手动设置浏览器或依赖。

- 

高性能（Fast Rust CLI）：底层用 Rust 实现，运行速度远高于传统 Node/Python 工具。

- 

支持两种模式（Headed / Headless）：既可打开可视化浏览器调试，也能在后台静默执行任务。

- 

轻量高效（93% 减少上下文）：相比 Playwright MCP，Agent Browser 为 AI 提供更紧凑的数据结构，使交互更高效。

- 

广泛兼容（Compatible with major AI agents）：支持 Codex、Claude Code、Gemini、Cursor、Copilot、opencode 等主流 AI 工具，以及任何能运行 Bash 命令的系统。



Agent Browser 是一个为「AI 代理（AI Agents）」设计的浏览器自动化命令行工具。


它的目标是让 AI 能够像人类一样操作网页，而不仅仅是读取网页内容。


它不是给人用的「浏览器」，而是一种让 AI 在网页环境中执行操作的底层接口。


可以理解为：“让 ChatGPT 或 Claude 这样的模型有一双能使用浏览器的手。”


核心能力概览



Agent Browser 是一个命令行工具（CLI）。


它通过简洁的命令让 AI 或脚本直接控制浏览器的行为。


主要功能包括：

![image]()


AI 专用特性



1. Snapshot + Ref 模式



Agent Browser 的设计重点在于让 AI 能稳定、可控地操作浏览器。
项目引入了独特的 Snapshot + Ref 机制：

- 

AI 先执行 snapshot 命令，获取网页的结构化快照（包含所有交互元素）；

- 

每个元素拥有唯一引用（例如 @e1, @e2）；



如：


```None
@e1 = 登录按钮  
@e2 = 邮箱输入框  
@e3 = 密码输入框
```


- 

随后，AI 可通过这些引用精确执行操作：


```None
agent-browser click @e1
agent-browser fill @e2 "user@test.com"
```




这种方式既避免了传统CSS/XPath选择器的不稳定问题，也更符合AI的“符号化”思维逻辑。
所有结果均可返回为 JSON 格式，方便AI解析和决策，实现“感知—推理—执行”的闭环。


这种方式具有三个特点：

- 

确定性强：不会因页面结构变化出错；

- 

执行快速：无需重新查找DOM；

- 

AI可理解：输出为JSON，方便模型解析。



---



2. JSON 输出模式



所有命令都可以返回结构化数据：


```None
agent-browser get text @e1 --json
```



输出：


```None
{"success": true, "data": "Submit"}
```



AI 可以直接读取和解析结果，形成“观察—决策—执行”的闭环。


---



3. Claude / GPT 集成能力



Vercel 提供了 .claude/skills/agent-browser 模板。
这意味着 Claude Code 或 CoWork 可以自动识别并使用 Agent Browser。
开发者无需额外适配，AI 便能执行网页操作。


开发者可直接在 .claude/skills/ 目录中加载该工具，使 Claude 自动具备网页操作能力。


同时，其标准化 CLI 接口和 JSON 输出格式，也便于与 OpenAI、LangChain、LlamaIndex 等生态工具集成。


Vercel Labs 表示，Agent Browser 将成为构建**具备实际执行力的AI工作流（Agent Workflows）**的重要基础设施。


技术架构



Agent Browser 采用双层架构，兼顾性能与可移植性：


```None
┌─────────────────────────────┐
│ Rust CLI 层                 │ ← 解析命令，快速响应
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│ Node.js 守护进程（Daemon）   │ ← 管理 Playwright 浏览实例
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│ 浏览器引擎（Chromium / WebKit）│ ← 执行网页操作
└─────────────────────────────┘

```



运行逻辑：

- 

用户或AI输入命令；

- 

Rust CLI 解析并传递给 Node.js 守护进程；

- 

守护进程驱动 Playwright 与浏览器交互；

- 

命令执行结果返回给调用者（人或AI）。



优势：

- 

Rust 层高性能（接近原生二进制速度）；

- 

Node 层高兼容性（易部署在各种系统）；

- 

守护进程常驻（减少浏览器重启开销）。



可以通过以下方式安装：


```None
npm install -g agent-browser
agent-browser install
```


![image]()


也支持嵌入式部署，例如在云端函数中：


```None
import { BrowserManager } from "agent-browser";
const browser = new BrowserManager();
await browser.launch({ headless: true });
```



典型应用场景


- 

AI 办公自动化：AI 自动登录企业系统、下载报表、汇总数据；

- 

网页测试与质量验证：快速替代 Selenium/Playwright 测试脚本；

- 

信息采集与监控：智能识别网页结构，自动提取与比对内容；

- 

多Agent协作：多实例并行操作，实现跨系统任务执行；

- 

安全分析与验证：在隔离环境中模拟用户行为，测试安全风险。



GitHub：

---

*来源：[Vercel  发布 “Agent Browser”：专为AI 代理开发的浏览器自动化工具](https://www.xiaohu.ai/p/vercel-agent-browser-ai/28558819)*
