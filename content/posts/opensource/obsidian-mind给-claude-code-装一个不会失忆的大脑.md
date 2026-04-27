---
title: "Obsidian Mind：给 Claude Code 装一个不会失忆的大脑"
date: 2026-04-06T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Obsidian Mind，一个开源的 Obsidian 库模板，给 Claude Code 用户设计的跨会话记忆系统。   Claude Code 有个根本问题：每次关了再开，它什么都不记得。你昨天跟它聊的架构决策、定下的目标、踩过的坑，新会话里全部从零开始。   Claude Code 自带的"
source_url: "https://www.xiaohu.ai/p/obsidian-mind-claude-code/31396824"
xiahuid: "31396824"
---

## 📰 正文

Obsidian Mind，一个开源的 Obsidian 库模板，给 Claude Code 用户设计的跨会话记忆系统。


Claude Code 有个根本问题：每次关了再开，它什么都不记得。你昨天跟它聊的架构决策、定下的目标、踩过的坑，新会话里全部从零开始。


Claude Code 自带的 memory 能存一些偏好，但容量有限，也不支持结构化的知识管理。


Obsidian Mind 的解决办法是用 Obsidian 笔记库当 Claude Code 的外部大脑。你的目标、决策、工作记录、踩过的坑、记住的模式，全部以 Markdown 笔记的形式存在 Obsidian 里。每次 Claude Code 启动，自动加载这些上下文；每次会话结束，自动把新学到的东西写回去。笔记库就是记忆，记忆跟着库走。

![image]()


核心思路：用 Obsidian 的结构给 AI 做记忆



记忆怎么运作



模板的记忆机制分三层。


自动加载。一个 SessionStart Hook 在每次启动 Claude Code 时自动把库的文件列表注入上下文，Claude 一开始就知道库里有什么。然后 CLAUDE.md 里定义的启动流程会让 Claude 依次读取：Home.md（vault 入口和仪表盘）→ North Star（你的目标和关注点）→ Index（活跃项目）→ Memories（跨会话记忆索引）→ 待办任务。不用你每次手动交代背景。


自动写回。每次会话结束时（你说"wrap up"就行），Claude 自动执行收尾流程：把新的关键决策写入 Key Decisions、新发现的模式写入 Patterns、踩的坑写入 Gotchas、有价值的成果登记到 Brag Doc、更新索引。会话里产生的知识不会随着对话窗口关闭而消失。


链接聚合。所有笔记通过 Obsidian 的 wikilink 互相关联。规则是每条笔记至少链接到一条已有笔记，没有链接的笔记被视为 bug。随着笔记越来越多，知识之间的关联自动在链接图谱里积累。Claude 可以通过反向链接发现"哪些工作笔记跟这个决策相关""这个模式在哪些项目里出现过"。


记忆存在哪里



模板把不同类型的知识放在不同文件夹里，Claude 按需读取。

![image]()


Claude Code 自带的 memory（~/.claude/）和 vault 记忆分工明确：前者存会话级偏好（比如代码风格、常用命令），后者存需要结构化管理和链接浏览的深度知识。


在记忆之上能做什么



有了持久记忆，一些之前做不了的事变得可行了。


绩效追踪。工作笔记完成后关联到能力项，Brag Doc 按季度聚合成果。到评审季用 /review-brief 命令从积累的记录里自动生成评审简报。日常记录和绩效输出是同一套数据，不用另外整理。


决策回溯。所有架构决策都记录在案，三个月后想知道"当初为什么选了方案 A 而不是方案 B"，直接查 Key Decisions，不用翻聊天记录。


团队知识管理。人员笔记记录每个同事的角色、合作历史、关键时刻。1:1 会议笔记自动提取行动项。组织变动时更新 People & Context 索引。


事故复盘。/incident-capture 命令从 Slack 提取事故信息，结构化写入 vault。根因分析、时间线、影响范围都有固定格式，方便以后回查类似问题。


还有什么



预装了 kepano（Obsidian CEO）的官方 obsidian-skills，包括 Obsidian Markdown 语法、CLI 命令、Canvas 画布和 Bases 数据库视图。


8 个自定义斜杠命令：

![image]()


怎么开始

1. 

克隆仓库或用 GitHub Template 创建

2. 

用 Obsidian 打开文件夹

3. 

启用 Obsidian CLI（设置 → 核心插件，需要 Obsidian 1.12+）

4. 

在 vault 目录下运行 claude

5. 

填写 brain/North Star.md，写入当前目标



需要 Obsidian 1.12+、Claude Code 和 Git。


可选装 QMD 做语义搜索（npm install -g @tobilu/qmd），不装也能用，Claude 会降级到 Obsidian CLI 和 grep。


如果你已经有自己的 Obsidian 笔记库，/vault-upgrade ~/my-old-vault 可以把旧内容迁移过来，Claude 会自动分类每个笔记，把工作记录、人物、事故、1:1、决策归到正确的目录。


需要知道的几件事


- 

需要 Obsidian 1.12+、Claude Code、Python 3、Git，缺一不可

- 

整套设计面向工程师工作流（项目管理、代码开发、绩效复盘），非技术岗需要自己改造目录结构和命令

- 

Slack 相关命令（incident-capture、slack-scan）需要你自己配 Slack 接入

- 

笔记库会通过 Git 管理，意味着你的工作笔记会在 Git 仓库里，注意敏感信息

- 

目前 41 个 commit，项目还在快速迭代中



👉 GitHub 仓库

---

*来源：[Obsidian Mind：给 Claude Code 装一个不会失忆的大脑](https://www.xiaohu.ai/p/obsidian-mind-claude-code/31396824)*
