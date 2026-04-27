---
title: "Claude Code Workflow Studio： Claude Code 可视化工作流编辑器"
date: 2025-12-30T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Claude Code Workflow Studio 是为 Anthropic Claude Code CLI 打造的 可视化工作流编辑器，支持拖拽式 AI 工作流设计，无需编程即可创建和导出自动化流程。   它让用户能 用图形界面创建、修改、运行 Claude code 的自动化流程。   比如"
source_url: "https://www.xiaohu.ai/p/claude-code-workflow-studio-claude-code/28120737"
xiahuid: "28120737"
---

## 📰 正文

Claude Code Workflow Studio 是为 Anthropic Claude Code CLI 打造的 可视化工作流编辑器，支持拖拽式 AI 工作流设计，无需编程即可创建和导出自动化流程。


它让用户能 用图形界面创建、修改、运行 Claude code 的自动化流程。


比如：

- 

你可以设计一个自动“文档总结”机器人；

- 

也可以创建一个“代码分析+修复建议”的工作流；

- 

甚至能做一个“网页爬取+内容提取+结果汇报”的自动流程。


![image]()



它能帮你做什么？

![image]()


功能亮点：

1. 

可视化拖拽编辑器

- 

通过拖放节点（Prompt、Sub-Agent、Skill、MCP、IfElse、AskUserQuestion）构建复杂工作流。


2. 

AI 辅助迭代式工作流改进

- 

使用自然语言描述修改需求，Claude AI 会根据上下文逐步优化工作流。


3. 

一键导出

- 

自动生成 .claude/agents/*.md 与 .claude/commands/*.md 文件，可直接在 Claude Code CLI 中运行。


4. 

Slack 集成（Beta）

- 

允许将工作流分享至 Slack，并支持一键导入。


5. 

本地安全执行

- 

所有操作在本地运行（除 MCP 节点外可能依赖网络连接）。


6. 

国际化支持

- 

支持五种语言：英语、日语、韩语、简体中文、繁体中文。




工作流组件详解



你在 VSCode 打开 Claude Code Workflow Studio 后，会看到一个“画布”界面：

![image]()

- 

Prompt Nodes：模板化提示词节点（支持变量与动态替换）

- 

Sub-Agent Nodes：独立智能体，具有自定义系统提示、模型选择（Opus、Sonnet、Haiku）

- 

Skill Nodes：可引用或创建 Claude Code Skills（带 YAML 元数据的技能模块）

- 

MCP Tool Nodes：基于 Model Context Protocol 的外部工具集成节点（如数据库、API、Playwright 浏览器）

- 

Conditional Branching：IfElse、Switch 实现条件分支逻辑

- 

AskUserQuestion Nodes：用户交互节点，支持多选项分支


![image]()


每个节点之间用“线”连起来，形成一个完整的自动化流程。


AI 辅助编辑（最强功能）



这部分是 Claude Code Workflow Studio 最独特的亮点。


传统工具要手动修改流程逻辑；
但在这里，你可以用“自然语言”告诉 AI 你想改什么。


例如：

> 

“帮我在开始节点后添加一个验证用户输入的步骤。”
“把输出结果改成保存成文件。”
“增加一个判断：如果文本超过1000字，就分段处理。”



AI 会自动：

- 

理解你的意图；

- 

修改流程；

- 

调整布局；

- 

确保逻辑正确；

- 

并让你审查、接受或撤销更改。



它不仅帮你生成，还能帮你“反复改进”流程。


如何安装和使用？



🪜 1. 安装依赖



首先你需要安装 Claude Code CLI：


```None
https://claude.com/claude-code

```



安装完成后输入：


```None
claude --version

```



确认可以正常运行。


---



🧩 2. 安装插件



两种方法：


✅ 从 VSCode 商店安装
1. 

打开 VSCode；

2. 

按 Ctrl+Shift+X；

3. 

搜索 Claude Code Workflow Studio；

4. 

点击安装。



💻 从源码安装


```None
git clone https://github.com/breaking-brake/cc-wf-studio.git
cd cc-wf-studio
npm install
npm run build
npx vsce package

```



然后在 VSCode 扩展管理器中选择“从 VSIX 安装”。


---



🎨 3. 打开编辑器



在 VSCode 命令面板中输入：


```None
Claude Code Workflow Studio: Open Editor

```



首次使用会启动一个交互式教学向导（带演示动画），
一步步教你如何添加节点、连接线、配置参数。


---



🧠 4. 创建一个简单工作流



举个例子：


目标：创建一个“自动问候”工作流。
1. 

添加一个 Prompt Node
内容：你好，我是Claude！

2. 

添加一个 AskUserQuestion 节点
内容：你现在感觉如何？（开心 / 忙碌 / 放松）

3. 

添加一个 Sub-Agent 节点
根据不同回答生成回应。

4. 

点击“导出”
自动生成 .claude/commands/greeting.md 文件。
现在你可以直接用 Claude CLI 执行！



---



Skill 与 MCP：让 Claude 更聪明



💡 Skill（技能）



类似“Claude 的插件”。
比如你有一个 PDF 解析技能，Claude 就能在工作流里自动用它读文件。


技能文件定义在：

- 

个人技能：~/.claude/skills/

- 

项目技能：.claude/skills/



每个技能都是一个带 SKILL.md 的 Markdown 文件，里面写着：


```None
name: pdf-reader
description: 从PDF中提取文本
tools: [Read]

```



然后你只需在可视化编辑器中选择该 Skill，Claude 就能用它。


---



🌐 MCP（Model Context Protocol）



MCP 是 Claude 的“扩展接口系统”。
你可以让 Claude 调用外部 API 或本地工具。


例如：

- 

Playwright MCP → 控制浏览器；

- 

API MCP → 访问网络接口；

- 

Database MCP → 查询数据库；

- 

Filesystem MCP → 访问文件系统。



添加 MCP 节点后，只需选择：

- 

服务器（MCP Server）

- 

工具名（Tool）

- 

参数配置（自动生成表单）



即可完成配置。

![image]()






---



常见问题（FAQ 精选）


![image]()


---



📘 总结一句话：


> 

Claude Code Workflow Studio 就是一个「让你像搭积木一样创建 AI 自动化工作流」的 VSCode 插件。


无需编程，只需想好流程，拖几个模块、点几下、和 AI 聊两句，它就能帮你生成一个真正能运行的智能系统。



---



GitHub：https://github.com/breaking-brake/cc-wf-studio

---

*来源：[Claude Code Workflow Studio： Claude Code 可视化工作流编辑器](https://www.xiaohu.ai/p/claude-code-workflow-studio-claude-code/28120737)*
