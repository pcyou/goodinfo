---
title: "Google 开源了一个Deep Research 系统模板 让你可以基于Gemini 2.5轻松构建一个Deep Research"
date: 2025-06-03T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google 开源了一个Deep Research 系统模板，详细演示了如何基于 Google Gemini 2.5 模型 和 LangGraph 框架 构建一个具备「搜索 + 推理 + 引用」能力的AI 研究助理的智能体系统，适合做“深度问答与研究型信息检索”。   你可以把这个项目理解为一个**"
source_url: "https://www.xiaohu.ai/p/google-deep-research-gemini-2-5-deep-research/22024767"
xiahuid: "22024767"
---

## 📰 正文

Google 开源了一个Deep Research 系统模板，详细演示了如何基于 Google Gemini 2.5 模型 和 LangGraph 框架 构建一个具备「搜索 + 推理 + 引用」能力的AI 研究助理的智能体系统，适合做“深度问答与研究型信息检索”。


你可以把这个项目理解为一个**“Deep Research的标准模板”**，具备多轮反思能力，不只是回答，而是能：

- 

自动找资料

- 

判断是否信息不完整

- 

多次优化搜索

- 

引用来源更可信



比起普通的大模型聊天机器人，这个更接近真实研究员的行为逻辑。


可以像人一样完成如下任务：

> 

“理解你要问的问题 → 自动生成合适的搜索词 → 从网络上查资料 → 判断信息是否足够 → 再补充搜索 → 汇总整理成带有引用来源的回答。”



✅ 核心能力



🔄 循环式智能体流程


> 

智能体具备“研究-反思-再研究”的循环机制，直到它获取到足够全面、可信的信息。
→ 模仿人类研究行为，能自动判断信息是否充分，并不断优化搜索。



🔍 动态搜索 + 深度推理


> 

自动生成搜索关键词，通过 Gemini 原生 Google 搜索能力获取网页内容，并结合推理逻辑进行分析。
→ 不仅搜索，而且“理解”搜索结果，判断是否还需要进一步挖掘。



🧠 支持多种搜索策略（低、中、高）


> 

可设定搜索强度，控制搜索的广度和深度，以适配不同类型问题的复杂度。
→ 灵活应对不同业务场景，从快速概览到深入调研都可处理。



🛠️ 现代前后端技术架构


> 

前端使用 React + Tailwind CSS + Shadcn UI，后端使用 LangGraph 驱动 Gemini 模型逻辑。
→ UI 美观，后端逻辑强大，开发体验友好。



🐳 本地运行 & Docker 部署支持


> 

提供 Docker 镜像和配置，可一键部署到本地或云端环境。
→ 易于开发、测试和上线生产系统。



📄 引用来源透明


> 

所有答案都来自实时网页数据，并标注清晰的引用链接。
→ 提高回答的可追溯性**，适用于对信息准确性有较高要求的领域。**



---



🧩 适合应用场景


- 

企业级智能搜索助理

- 

法律/医学/科研内容摘要与引用

- 

新闻聚合与事实核查工具

- 

教育/培训内容自动整理

- 

多语言信息调研系统（可拓展）

![image]()



核心技术栈


![image]()





![image]()


🚀 部署生产环境



该项目支持使用 Docker 和 docker-compose 来一键部署到生产环境，并支持：

- 

Redis：用于实时推理流式输出（让结果一边生成一边显示）

- 

PostgreSQL：用于保存用户对话、状态、长期记忆



```None
docker build -t gemini-fullstack-langgraph -f Dockerfile .
docker-compose up
```



GitHub：https://github.com/google-gemini/gemini-fullstack-langgraph-quickstart

---

*来源：[Google 开源了一个Deep Research 系统模板 让你可以基于Gemini 2.5轻松构建一个Deep Research](https://www.xiaohu.ai/p/google-deep-research-gemini-2-5-deep-research/22024767)*
