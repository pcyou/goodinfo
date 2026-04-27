---
title: "Google 发布官方命令行工具 一个 CLI 搞定所有 Google 办公全家桶"
date: 2026-03-05T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google 官方发布的一个命令行工具，叫做 gws，专门用来操控整个 Google Workspace 生态。   你平时用 Google Drive 存文件、用 Gmail 发邮件、用 Google Calendar 约会议，这些操作都要打开浏览器手动点。   这个工具让你在命令行里直接干这些事"
source_url: "https://www.xiaohu.ai/p/google-cli-google/30326175"
xiahuid: "30326175"
---

## 📰 正文

Google 官方发布的一个命令行工具，叫做 gws，专门用来操控整个 Google Workspace 生态。


你平时用 Google Drive 存文件、用 Gmail 发邮件、用 Google Calendar 约会议，这些操作都要打开浏览器手动点。


这个工具让你在命令行里直接干这些事，比如：


```None
gws drive files list        # 列出你的 Drive 文件
gws gmail users messages list  # 看邮件
```



更重要的是，它专门为 AI Agent 设计，所有结果都输出 JSON，AI 能直接读懂并操作。


所以你可以告诉 Claude/Gemini："帮我把今天收到的所有邮件整理成摘要"，AI 就能通过这个工具真的去读你的邮件、处理、甚至回复，全自动，不用你动手。


还支持作为 MCP Server 接入 Claude Desktop，等于给 Claude 开通了操作你整个 Google 工作区的权限。

![image]()


核心特点：


一个 CLI 搞定所有 Google Workspace，包括 Drive、Gmail、Calendar、Sheets、Docs、Chat、Admin 等，所有命令从 Google Discovery Service 动态生成，并内置了 AI agent skills。


几个亮点：
1. 

动态命令生成，它不是预先写死一堆命令，而是运行时读取 Google 的 Discovery Service 动态构建所有命令，Google Workspace 新增 API 后，gws 自动支持。

2. 

专为 AI Agent 设计，所有输出都是结构化 JSON，配合内置的 40+ agent skills，LLM 可以直接用它管理 Google Workspace，无需自己写工具。

3. 

内置 MCP Server，gws mcp 可以启动一个 MCP 服务，把 Google Workspace API 暴露成结构化工具，供 Claude Desktop、Gemini CLI、VS Code 等 MCP 客户端直接调用。

4. 

100+ Agent Skills，仓库里附带了 100 多个 SKILL.md 格式的 Agent Skills，覆盖 Gmail、Drive、Docs、Calendar、Sheets 的常用工作流，可以直接安装到 AI agent 框架里用。



简单来说，这个工具是 Google Workspace 版的"Claude Code"，让 AI Agent 能直接通过命令行操作你的 Google 全家桶，对做 AI 自动化工作流的开发者很有价值，值得关注。用 Rust 写的


GitHub：https://github.com/googleworkspace/cli

---

*来源：[Google 发布官方命令行工具 一个 CLI 搞定所有 Google 办公全家桶 ](https://www.xiaohu.ai/p/google-cli-google/30326175)*
