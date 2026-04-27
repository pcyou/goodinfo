---
title: "MiroThinker： 突破Scaling Law瓶颈 开创深度交互 Scaling让 AI 自我进化"
date: 2025-11-14T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "MiroMind 团队推出了一款全新的开源智能体模型——MiroThinker v1.0。   它的最大创新是提出了一个新概念：   “深度交互 Scaling（Interactive Scaling）” ——让 AI 不只是“大”，而是能“更聪明地行动和思考”。   这个概念突破了传统“模型规模越"
source_url: "https://www.xiaohu.ai/p/mirothinker-scaling-law-scaling-ai/26917304"
xiahuid: "26917304"
---

## 📰 正文

MiroMind 团队推出了一款全新的开源智能体模型——MiroThinker v1.0。


它的最大创新是提出了一个新概念：


“深度交互 Scaling（Interactive Scaling）” ——让 AI 不只是“大”，而是能“更聪明地行动和思考”。


这个概念突破了传统“模型规模越大→性能越好”的线性增长规律，转而强调 “模型与环境交互的深度和频次” 才是智能增长的关键因素。


MiroThinker 因此成为首个以“交互深度”为核心训练策略的开源智能体基座。


有哪些突破？
1. 

工具增强推理：MiroThinker 支持与外部工具（如搜索引擎、Linux 沙箱、语音识别等）进行多次互动和推理，能够灵活使用工具来获取信息、完成任务。

2. 

256K 上下文：能记得非常多的信息（几十万字）。

3. 

单次可执行600 次工具调用：AI 能持续使用搜索、代码执行、计算、翻译等外部工具。

4. 

能进行复杂推理和长时间任务：不是简单回答问题，而是能分步骤思考、查资料、比较方案。



什么是「深度交互 Scaling」？



传统 Scaling（扩展定律）


> 

性能 ∝ 模型参数量 × 数据量



但这种方法正在接近“边际收益递减”阶段。
即使再大的模型，也无法获得质变的智能行为。


MiroMind 的新思路：Interactive Scaling


> 

性能 ∝ 模型与环境的交互深度 × 反思频率



换句话说：

- 

模型不是被动吸收知识，而是主动与环境互动；

- 

每次试错与反思都会让模型在策略空间中“自我进化”；

- 

AI 越“动手”——越能纠正错误、提升推理质量。

- 

就像人类通过“反复试错、动手实践”才能真正学会复杂的事情一样。


![image]()


🧩 举例说明：

> 

就像人类学习烹饪，单看食谱是远远不够的，必须亲自尝试、失败、修正、再尝试。
对 AI 而言，多轮环境交互 + 反馈修正 = 智能进化的真正燃料。


每次交互都是一次“学习”，智能就会越来越强。



因此，MiroThinker 将“上下文长度”和“交互轮数”都提升至极限，形成真正的“深度思考循环（Thinking Loop）”。

![image]()


三大核心亮点



① 256K 超长上下文 + 600 轮工具调用


传统大模型虽然可以记忆大量文本（上下文），但在实际推理和操作中往往“思考一会儿就忘”，无法连续行动。
MiroThinker 的创新点是：

- 

256K 上下文窗口：具备长期记忆能力，能连续处理数十万字级别的信息。

- 

600 次工具调用：模型在一次任务中可多次调用外部工具（搜索引擎、代码执行环境等），形成类似人类“反复思考—试错—验证”的行为模式。



🔹 本质突破：从“被动回答问题的语言模型”，变成“主动规划、验证、执行的研究型智能体”。


② 性能全面超越主流开源模型


多个国际评测中


成绩接近甚至超过 GPT-5 高级版：

- 

在复杂网页理解测试（BrowseComp）中得分 47.1%，逼近 OpenAI 的 DeepResearch (51.5%)。

- 

在人类终极推理测试（HLE）中，超过 GPT-5-high。

- 

在中文任务上超越 DeepSeek-v3.2 约 7.7 个百分点。


![image]()




![image]()


这些数据说明 MiroThinker 已跻身开源智能体的“第一梯队”，在部分复杂任务中甚至超越了 GPT-5 + 工具模式的组合。


③ 完全开源与可复现性



MiroThinker v1.0 的所有核心资源全部开源，包括：

- 

模型权重（HuggingFace 提供）；

- 

推理与交互框架（MiroFlow）；

- 

训练与强化学习基础设施（MiroTrain / MiroRL）；

- 

评测数据集（MiroVerse）；

- 

完整技术报告（Technical Report）。



团队的理念是：

> 

“开放架构 + 社区共创 = 让智能体成为科研的共同语言。”



模型矩阵与生态结构


![image]()


生态组件包括：

- 

🧩 MiroFlow：推理与工具框架（相当于 AgentOS）

- 

🧠 MiroVerse：14.7 万条研究数据，用于代理训练

- 

⚙️ MiroTrain / MiroRL：高效训练与强化学习系统

- 

🧪 Benchmark Suite：GAIA、HLE、FutureX 等研究标准集



团队还在招人



他们希望招募对 AI Agent / 自主智能体 / 强化学习 / 开源科研 有兴趣的人，一起推进研究。
📩 邮箱：talent@miromind.ai
📱 微信小助手：miromind001


模型下载：https://huggingface.co/collections/miromind-ai/mirothinker-v10 


GitHub：https://github.com/MiroMindAI/MiroThinker 


论文：https://github.com/MiroMindAI/MiroThinker/blob/main/assets/MiroThinker_v1.0_Technical_Report.pdf 


在线体验：https://dr.miromind.ai/

---

*来源：[MiroThinker： 突破Scaling Law瓶颈 开创深度交互 Scaling让 AI 自我进化](https://www.xiaohu.ai/p/mirothinker-scaling-law-scaling-ai/26917304)*
