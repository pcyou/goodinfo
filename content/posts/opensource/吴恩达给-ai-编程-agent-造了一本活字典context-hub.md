---
title: "吴恩达给 AI 编程 Agent 造了一本活字典：Context Hub"
date: 2026-03-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: ">   你的 AI 编程助手写代码时，用的可能是半年前的 API 文档。    用 Claude Code、Cursor 这些 AI 编程工具写代码的时候，有没有遇到过这种情况：你让它调用某个 API，它信誓旦旦写出一段代码，结果一跑就报错，因为那个参数早就废弃了，或者压根就是它编出来的。   这个"
source_url: "https://www.xiaohu.ai/p/ai-agent-context-hub/30526122"
xiahuid: "30526122"
---

## 📰 正文

> 

你的 AI 编程助手写代码时，用的可能是半年前的 API 文档。



用 Claude Code、Cursor 这些 AI 编程工具写代码的时候，有没有遇到过这种情况：你让它调用某个 API，它信誓旦旦写出一段代码，结果一跑就报错，因为那个参数早就废弃了，或者压根就是它编出来的。


这个问题在开发者圈子里有个名字，叫 Agent Drift（Agent 漂移）。AI 的训练数据是有截止日期的，但 API 文档天天在更新。训练结束的那一刻，AI 的知识就开始"过期"了。


斯坦福大学教授、DeepLearning.AI 创始人吴恩达（Andrew Ng）刚刚开源了一个工具来解决这个问题：Context Hub。

![image]()


一句话说清它是什么



Context Hub 是一个命令行工具（CLI），相当于给 AI 编程 Agent 配了一本实时更新的 API 字典。Agent 写代码之前先查字典，拿到最新的官方文档，就不用靠记忆瞎猜了。


安装就一行命令：


```bash
npm install -g @aisuite/chub
```


![image]()


能干什么



1. 搜索和获取文档


Agent 可以通过 chub search 搜索需要的 API 文档，用 chub get 拉取对应的最新版本。支持按编程语言筛选（Python 版或 JavaScript 版），只拿需要的内容，不浪费 token。


```bash
chub search "stripe payments"     # 搜索 Stripe 支付相关文档
chub get openai/chat --lang py    # 拉取 OpenAI 聊天 API 的 Python 版文档
```



目前已经收录了 68 个主流 API 提供商的文档，包括 Stripe、OpenAI、Anthropic、Supabase、Firebase、Twilio、Shopify、AWS 等。


2. 本地注解：Agent 的"长期记忆"


这是我觉得最有意思的功能。Agent 在调用 API 的过程中发现了一个坑（比如 Stripe 的 webhook 验证必须用原始请求体，不能用解析后的 JSON），它可以把这个经验记下来：


```bash
chub annotate stripe/api "Needs raw body for webhook verification"
```



下次不管是这个 Agent 还是同一台机器上的其他 Agent 再查 Stripe 文档，这条笔记会自动附在文档后面。Agent 不用每次从头踩坑了。


3. 社区反馈：大家一起维护"字典"


Agent 还能给文档打分，标记"准确""过时""示例有误"等标签。这些反馈会汇总给文档维护者，帮助整个社区保持文档的新鲜度。


4. MCP Server 原生集成


Context Hub 还提供了 MCP（Model Context Protocol）Server，Claude Code、Cursor、Windsurf 这些工具可以直接通过 MCP 调用，连命令行都不用敲。


实际场景


- 

调新 API 不踩坑： 让 Agent 调用 OpenAI 最新的 Responses API 时，先 chub get openai/chat --lang py 拉一份当前版本的文档，避免它用已经过时的 Chat Completions API

- 

跨项目复用经验： 在项目 A 里踩过 Firebase Auth 的一个坑，注解写好后，做项目 B 时 Agent 自动就知道了

- 

团队协作： 同一台开发机上，不同 Agent 共享本地注解，避免团队成员重复踩同一个坑

- 

省 token： 按语言筛选文档、增量拉取，只给 Agent 最精准的上下文

- 

技能集成： 在 Claude Code 里创建一个 skill（~/.claude/skills/get-api-docs/），Agent 写代码前自动查文档，形成"查字典→写代码→记笔记"的闭环



现实地说几句



Context Hub 目前的定位是"人工策展 + 社区维护"。68 个 API 听起来不少，但全球活跃的 API 有几千个，覆盖率还差得远。如果你用的是小众 API 或者企业内部 API，目前是用不上的。


另外，注解功能目前只存在本地，没有跨机器同步。吴恩达在推文里提到了"长期目标是让 Agent 之间共享学到的知识"，但这还是愿景阶段，不是当前能力。


文档质量也完全依赖社区贡献。GitHub 上目前 3400 多个 star、87 个 commit，活跃度不错，但能不能持续维护、跟上 API 更新的速度，还得看后续。


怎么在体系中理解它



如果把 AI 编程工具的知识来源分个层：

- 

底层： 模型训练数据（静态，会过期）

- 

中层： RAG / 网页搜索（动态，但噪音大、格式不统一）

- 

上层： Context Hub（人工策展、格式统一、Agent 可读、可注解）



Context Hub 想做的是"上层"这个位置。它和 RAG 不冲突，RAG 解决的是"去哪找信息"，Context Hub 解决的是"信息的质量和 Agent 友好度"。


---


> 

GitHub：https://github.com/andrewyng/context-hub

---

*来源：[吴恩达给 AI 编程 Agent 造了一本"活字典"：Context Hub](https://www.xiaohu.ai/p/ai-agent-context-hub/30526122)*
