---
title: "MiroThinker 1.5：全球最强搜索智能体"
date: 2026-01-08T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "MiroThinker 是由 MiroMindAI 团队 开发的开源研究代理（search agent），旨在提升 AI 的“工具增强推理（tool-augmented reasoning）”与“信息检索”能力。  -   模型参数规模：  -   MiroThinker-v1.5-30B  -"
source_url: "https://www.xiaohu.ai/p/mirothinker-1-5/28399936"
xiahuid: "28399936"
---

## 📰 正文

MiroThinker 是由 MiroMindAI 团队 开发的开源研究代理（search agent），旨在提升 AI 的“工具增强推理（tool-augmented reasoning）”与“信息检索”能力。

- 

模型参数规模：

- 

MiroThinker-v1.5-30B

- 

MiroThinker-v1.5-235B


- 

主要特性：

- 

支持 256K 上下文窗口。

- 

支持 400 次工具调用。

- 

强化 多步推理与长程任务管理。




传统大模型的路线是 “把世界背进参数里”，依赖统计与记忆。


而 MiroMind 的理念是：

> 

“真正的智能不靠全知，而靠研究能力。”



也就是说，
智能体不应只是“会答题（做题家）”，
而应像“科学家”那样：
1. 

主动查证；

2. 

识别不确定；

3. 

自我修正；

4. 

通过证据收敛得到可靠结论。


![image]()


MiroThinker 不仅仅是一个模型，而是一整套可复现、可扩展的 AI 研究代理框架（Research Agent Framework），能够在复杂的真实世界任务中实现：

- 

自动化信息搜索；

- 

支持多步思考与自我纠错；

- 

具备长时记忆与上下文理解

- 

工具调用与执行；

- 

研究级信息整合与评估。



你可以把它理解为：


👉 一个会思考、能查资料、还能动手实验的 ChatGPT。


它不是单纯的“对话机器人”，而是一个能：

- 

打开网页、抓取信息；

- 

能运行代码并分析结果；

- 

汇总研究结果；

- 

还会自己检查答案准确性；
的智能“研究助理”。



MiroThinker v1.5 在广泛的基准测试中展现了强大的通用研究性能，在 HLE-Text、BrowseComp、BrowseComp-ZH 和 GAIA-Val-165 上分别达到 39.2%、69.8%、71.5% 和 80.8%。


超越了之前的开源代理，创造了新的业界领先 BrowseComp 性能。


MiroThinker-v1.5-30B 仅用 1/30 的参数规模跑出了比肩众多 1T 模型的性能表现，其 235B 的版本在多个搜索智能体基准测试中跻身全球第一梯队。

![image]()


它能干什么？（主要功能）



MiroThinker 能完成的事情可以分为四大类👇：


主体智能体（MiroThinker）



这就是“AI 大脑”。
它能理解问题、规划步骤，然后调用各种工具去解决任务。


比如：

> 

你问它：“请总结过去一个月AI领域的新研究趋势。”



它会：
1. 

自动去 Google 搜索；

2. 

抓取各个论文网页；

3. 

提取信息；

4. 

分析关键词；

5. 

最后写出一篇总结。



整个过程 全自动 完成！


---



工具系统（MiroFlow）



MiroThinker 的“手脚”。
它提供了各种可以被调用的工具，比如：

- 

🔍 搜索（Serper API）

- 

🧾 网页抓取（Jina）

- 

🧠 LLM摘要（小模型总结内容）

- 

💻 执行 Python 代码（E2B 沙盒环境）


> 

举个例子：
MiroThinker 发现要算某个统计结果，它会自己用 E2B 执行 Python 代码。



---



核心技术概念



1️⃣ 工具增强推理（Tool-Augmented Reasoning）



MiroThinker 通过内置的工具接口系统（Tool API），
使模型能在推理过程中主动调用外部工具（搜索引擎、爬取器、代码执行环境等）以辅助推理。


支持的典型工具包括：

- 

Serper API：访问 Google 搜索；

- 

Jina API：网页抓取与语义摘要；

- 

E2B Sandbox：代码执行与结果验证；

- 

LLM-as-a-Judge：基于 GPT 或 Qwen 的模型评估器。



这一设计使模型能够执行如：

> 

“搜索论文 → 抓取内容 → 提取要点 → 执行验证脚本 → 汇总结论”
的完整研究任务流程。



🧠 优势

- 

提升了模型的“信息访问能力（Information Access Capability）”；

- 

减少幻觉（Hallucination）；

- 

能处理真实世界任务（如科研报告生成、技术文档分析）。



---



2️⃣ 交互扩展（Interactive Scaling）



传统性能扩展依赖于：

- 

模型规模（parameters）

- 

上下文长度（context window）



MiroThinker 提出了第三维：

> 

交互深度（interaction depth）



即模型在任务中能主动进行多轮外部环境交互，
例如多次搜索、分析、运行代码、再验证。


MiroThinker 引入 “交互维度” 作为性能第三维：

![image]()


🧠 核心机制


通过 memory-managed multi-round reasoning：

- 

保留最近 5 次对话上下文；

- 

清理无关历史；

- 

维持信息完整性与低资源开销。



这种交互循环让模型具备了“自主探究式学习（self-directed inquiry）”能力。


在 v1.5 版本中，单任务可支持 多达400次工具交互，
使模型能在复杂任务中形成递归式、层级化的推理链。


MiroThinker vs DeepResearch  有什么不同


![image]()


🧠 MiroThinker 架构 = 「AI 大脑 + 工具生态 + 环境交互」



它采用模块化设计：

![image]()


🔧 支持外部 API 工具（如 Serper、Jina、E2B），能：

- 

搜索网页；

- 

抓取文本；

- 

执行 Python 代码；

- 

评估结果。



➡️ 你可以理解为：
它是一个完整的 AI 研究操作系统，不只是一个模型。


🔍 DeepResearch 架构 = 「网页爬虫 + 推理引擎 + 内容压缩器」



DeepResearch（尤其是 DeepResearcher、DeepSearchQA 等）更多是：

- 

聚焦于信息检索 + 内容理解；

- 

强调“深度网页搜索”和“内容压缩总结”。



结构更轻量，通常包括：
1. 

搜索模块（基于 Google / Bing API）

2. 

抓取模块（BeautifulSoup / Jina）

3. 

LLM 总结模块（通常是 GPT-4/5）

4. 

结果聚合模块（评分 + 排序）



➡️ 它更像一个智能搜索引擎 + 总结机器人。


举例说明：两者在同一任务下的行为差异



任务：


> 

“请总结过去一个月人工智能安全领域的主要研究成果。”



---



🔍 DeepResearch 的做法：
1. 

搜索 “AI safety research December 2025 site:arxiv.org”

2. 

抓取前5页；

3. 

提取摘要；

4. 

拼接总结（无代码执行，无引用验证）。



输出结果：

> 

“近期AI安全领域关注模型可解释性与鲁棒性，多篇论文聚焦于...（简略）”



优点：快。
缺点：浅，缺乏验证或多源交叉。


---



🧠 MiroThinker 的做法：
1. 

搜索 arXiv 最新论文；

2. 

抓取 + 提取多篇；

3. 

运行文本聚类分析；

4. 

对比引用来源；

5. 

生成结构化总结（附论文编号）。



输出结果：

> 

“在2025年12月，AI安全研究主要集中在三大方向：

- 

对抗鲁棒性（6篇）

- 

AI伦理检测与防护（4篇）

- 

LLM溯源与安全验证（3篇）
主要代表作包括 arXiv:2512.1034、arXiv:2512.2155 等。”




优点：全面、有分析、有出处。
缺点：执行时间更长。


想了解更多？



官方网站：🌐 https://miromind.ai
GitHub 项目页：📦 https://github.com/MiroMindAI/MiroThinker
论文引用：



在线体验：https://dr.miromind.ai/

---

*来源：[MiroThinker 1.5：全球最强搜索智能体](https://www.xiaohu.ai/p/mirothinker-1-5/28399936)*
