---
title: "Google 发布 Open Knowledge Format：给 AI 一个统一的知识库格式"
date: 2026-06-16T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google Cloud 发布了 Open Knowledge Format（OKF），一个开源的知识表示规范。    就是把过去一年大家各自在搞的AI 知识库模式，统一成了一个标准格式。   核心信息：  -   知识用 Markdown 文件 + YAML 头部元数据表示，不依赖任何特定云平"
source_url: "https://www.xiaohu.ai/p/google-open-knowledge-format-ai/33660900"
xiahuid: "33660900"
---

## 📰 正文

Google Cloud 发布了 Open Knowledge Format（OKF），一个开源的知识表示规范。 


就是把过去一年大家各自在搞的"AI 知识库"模式，统一成了一个标准格式。


核心信息：

- 

知识用 Markdown 文件 + YAML 头部元数据表示，不依赖任何特定云平台、数据库或 AI 框架

- 

本质上是把 Karpathy 提出的 LLM Wiki 模式从"个人实践"变成了"行业规范"

- 

同步发布了三个配套工具：BigQuery 数据集自动生成 OKF 的 Agent、静态可视化查看器、三个示例知识库

- 

规范本身只有一页纸，已开源在 GitHub



---



这东西解决什么问题



先说背景。


过去一年，给 AI 喂上下文知识这件事，几乎每个团队都在做，但做法五花八门。


有人用 Obsidian 建知识库挂到编程 Agent 上。


有人在代码仓库里放 CLAUDE.md、AGENTS.md 这类约定文件。


有人维护一堆 index.md 和 log.md，让 Agent 干活之前先去读一遍。


还有数据团队把表结构、指标定义、SQL 模板写成 Markdown 当内部 Wiki 用。


这些做法的共同点是：都在用 Markdown + 前置元数据的方式给 AI 组织知识。问题是，每个团队的格式都是自己定的。你的 Wiki 和我的 Wiki 长得差不多，但字段名不一样，文件结构不一样，元数据规范不一样。一个团队辛苦整理的知识库，换个 Agent 框架就读不了，换个团队就对不上。


Karpathy 在他那篇很火的 LLM Wiki 提案里说过一句话：LLM 不会无聊，不会忘记更新交叉引用，一次能改 15 个文件。人类维护个人 Wiki 最容易放弃的那些琐碎工作，恰好是 LLM 最擅长的。


道理大家都认，但"人人都在做自己的版本"这个状态持续了一年多，始终缺一个公共标准。


OKF 做的就是这件事：不做平台，不做服务，只做格式。


格式长什么样



极简


一个 OKF 知识库就是一个文件夹，里面放 Markdown 文件。每个文件代表一个"概念"，可以是一张数据表、一个指标定义、一份运维手册、一个 API 文档。


```None
sales/
├── index.md
├── datasets/
│   ├── index.md
│   └── orders_db.md
├── tables/
│   ├── index.md
│   ├── orders.md
│   └── customers.md
└── metrics/
│   ├── index.md
     └── weekly_active_users.md
```



文件开头是一小段 YAML 元数据，只有一个字段是必填的：type（这个概念是什么类型）。其他字段（title、description、resource、tags、timestamp）都是可选的。


文件正文就是普通 Markdown，想写什么写什么。概念之间用标准 Markdown 链接互相引用，整个文件夹就自然形成了一个知识图谱。


举个例子，一个描述"订单表"的 OKF 文件大概长这样：最上面 YAML 写清楚这是一张 BigQuery 表、叫什么名字、在哪能找到，下面 Markdown 正文写表结构、字段说明、跟哪些表怎么关联。


没有新的运行时，没有专用 SDK，没有压缩方案。文件可以用任何编辑器打开，可以放在任何 Git 仓库里，可以被任何搜索工具索引。


```None
---
type: BigQuery Table
title: Orders
description: One row per completed customer order.
resource: https://console.cloud.google.com/bigquery?p=acme&d=sales&t=orders
tags: [sales, revenue]
timestamp: 2026-05-28T14:30:00Z
---

# Schema

| Column        | Type      | Description                              |
|---------------|-----------|------------------------------------------|
| `order_id`    | STRING    | Globally unique order identifier.        |
| `customer_id` | STRING    | FK to [customers](/tables/customers.md). |

# Joins

Joined with [customers](/tables/customers.md) on `customer_id`.
```



三个设计原则



最小约束： 整个规范对每个概念只要求一件事：你得告诉我它的类型。至于有哪些类型、正文怎么组织、要不要加额外字段，全部由内容生产者自己决定。规范管的是互通的最小公约数，不管内容模型。


生产者和消费者解耦：人写的知识库可以被 Agent 消费。数据管道自动导出的知识库可以被人用可视化工具浏览。一个 LLM 生成的知识库可以被另一个 LLM 查询。两端的工具可以独立替换，格式本身就是契约。


格式而不是平台：不绑定任何云厂商、数据库、模型供应商或 Agent 框架。读写 OKF 永远不需要专有账号或 SDK。Google 把它作为开放标准发布，因为一个知识格式的价值取决于有多少方在用它，而不是谁拥有它。


配套工具



Google 同步发布了三个参考实现：


一个自动生成 Agent，输入一个 BigQuery 数据集，它会遍历每张表和视图，为每个对象生成一份 OKF 文档，然后跑第二轮 LLM 去爬官方文档补充引用、Schema 和关联路径。


一个静态 HTML 可视化器，把任意 OKF 知识库渲染成交互式图谱，单文件打开，不需要后端，不需要安装，数据不离开页面。


三个现成的示例知识库：GA4 电商数据集、Stack Overflow、比特币公开数据集，都是用上面那个 Agent 自动生成的。


这些工具是概念验证，不是唯一实现。格式本身不依赖任何特定的 Agent 框架或可视化方式。


为什么这件事有意思



单看 OKF 本身，它做的事情不复杂，甚至可以说很朴素。但放到 AI Agent 生态的大背景下，它补了一个一直缺着的位置。


现在的 AI Agent 开发，最大的瓶颈往往不是模型能力，而是上下文组装。Agent 需要回答"怎么从我们的事件流里算周活跃用户"，但答案散落在元数据目录、内部 Wiki、代码注释、几个老工程师的脑子里。每个 Agent 开发者都在从零解决同一个上下文拼装问题，每个知识管理工具都在重新发明同一套数据模型。


OKF 不解决"怎么获取知识"的问题，它解决的是"知识怎么流通"的问题。一个团队整理好的数据文档，换个部门、换个工具链、换个 Agent 框架，能直接用，不用再翻译一遍。


这跟之前 MCP 做的事情有点像。MCP 标准化的是"AI 怎么调用外部工具"，OKF 标准化的是"AI 怎么读取外部知识"。一个管手，一个管脑子。


当然，一个格式标准最终能不能立住，取决于有没有足够多的人用它。OKF v0.1 还很早期，规范只有一页纸，生态基本为零。但方向是对的：这个领域需要的不是又一个知识管理平台，而是一个让知识能在平台之间流动的公共格式。

> 

OKF 规范和示例代码：https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf



官方介绍：https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing

---

*来源：[Google 发布 Open Knowledge Format：给 AI 一个统一的"知识库格式"](https://www.xiaohu.ai/p/google-open-knowledge-format-ai/33660900)*
