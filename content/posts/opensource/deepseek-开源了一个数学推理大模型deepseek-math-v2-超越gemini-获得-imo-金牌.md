---
title: "DeepSeek 开源了一个数学推理大模型：DeepSeek-Math-V2  超越Gemini 获得 IMO 金牌"
date: 2025-11-28T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: ">   DeepSeek-Math-V2 是一个能“自己检查自己是否算对”的数学推理大模型。    以往的数学大模型（比如 ChatGPT、Gemini、Claude）可以解题，但常常：  -   过程不严谨；  -   中间步骤错误；  -   虽然“答案对”，但“推理错”。    DeepSee"
source_url: "https://www.xiaohu.ai/p/deepseek-deepseek-math-v2-gemini-imo/27333817"
xiahuid: "27333817"
---

## 📰 正文

> 

DeepSeek-Math-V2 是一个能“自己检查自己是否算对”的数学推理大模型。



以往的数学大模型（比如 ChatGPT、Gemini、Claude）可以解题，但常常：

- 

过程不严谨；

- 

中间步骤错误；

- 

虽然“答案对”，但“推理错”。



DeepSeek 团队认为：

> 

真正的数学AI，不只是算出正确答案，而是能验证自己的推理是否合理。



于是，他们在 DeepSeek-V3.2 模型基础上，
训练出了这个**“可自验证（Self-Verifiable）”的数学模型** —— DeepSeek-Math-V2。


模型能：
1. 

自动生成数学证明；

2. 

自行检查每一步是否合理；

3. 

修正推理错误后再输出最终证明。



模型核心思想（Self-Verification 自验证）



DeepSeek-Math-V2 的核心创新是一个“生成 + 验证+复审”的自我验证系统”。

![image]()


这三个模块通过**循环训练（iterative RL loop）**协同进化：
验证器让生成器变强，生成器反过来制造更难的题让验证器变强。


模型通过一种循环训练方式，让生成器和验证器相互提升：
1. 

生成器写出数学推理步骤；

2. 

验证器审查逻辑是否自洽、是否满足推理规则；

3. 

错误部分被标注为“负样本”；

4. 

系统自动修正并重新生成；

5. 

形成“自我批改式学习闭环”。



📈 这与传统“RL强化学习”不同：


- 

旧方法：只看“最后答案对不对”；

- 

DeepSeek方法：关注“每一步推理是否正确”。



这让模型不仅会算，还能“会讲、会证、会查错”。


关键技术详解



1️⃣ Proof Verifier（验证器）



训练目标：让LLM像数学专家一样打分证明的“严谨度”。


评分标准：

- 

1.0：完全正确、逻辑严谨

- 

0.5：总体正确但有小错误

- 

0.0：逻辑错误或关键步骤缺失



训练过程：

- 

从 AoPS（Art of Problem Solving）网站收集了 17,503 道数学证明题；

- 

由专家人工评分形成初始数据；

- 

模型通过强化学习学习“怎样像专家那样打分”；

- 

使用奖励函数衡量预测分数与专家分数的一致性。



---



2️⃣ Meta-Verifier（元验证器）



问题：验证器有时“幻觉”出错误，比如明明正确却说有问题。


解决：再训练一个“检查验证器”的AI —— 元验证器。


功能：

- 

判断验证器指出的问题是否真实存在；

- 

检查验证理由是否逻辑自洽；

- 

如果验证器乱判错，元验证器会惩罚它。



结果：

> 

在验证数据集上，验证器的评分质量从 0.85 → 0.96，大幅提升可信度。



---



3️⃣ Proof Generator（生成器）



基于验证器作为奖励模型（reward model）训练生成器：

- 

生成器写证明；

- 

验证器给分；

- 

分高代表证明严谨；

- 

分低则生成器自动改进。



新增创新：自验证训练（Self-Verification）


生成器不仅写证明，还要“批改自己”，
用和验证器一样的标准给自己打分。


奖励设计：

- 

承认错误比撒谎得分高；

- 

诚实分析+修正错误能得到最高分。



通过这种机制，AI被引导学会“真实反思与改进”。


---



4️⃣ 自动标注循环（Auto-Labelling Pipeline）



为了摆脱人工标注，DeepSeek还设计了一个全自动循环：
1. 

生成大量证明；

2. 

多次由验证器审查；

3. 

由元验证器验证这些审查；

4. 

自动生成“真标签”；

5. 

继续训练下一轮验证器。



最后两轮训练已完全不需要人工参与。
AI自己生成、检查、打分、进化。


性能与评估结果



DeepSeek-Math-V2 在多个高难度数学测试上表现优异


在五大数学领域（代数、几何、数论、组合、 不等式）中：

> 

DeepSeekMath-V2 全面超越 GPT-5-Thinking 和 Gemini 2.5 Pro。



模型能通过多轮自检与修正提高证明质量：

- 

连续8轮自验证后，正确率显著提升；

- 

模型能准确识别并修复自己的推理错误；

- 

“自己挑出的最佳证明”与外部验证结果高度一致。



结论：

> 

DeepSeekMath-V2 能可靠地区分“好证明”和“坏证明”，
并能自主改进逻辑。



此外：

- 

在 DeepMind 的 IMO-ProofBench 数据集上超过 Gemini DeepThink，获得第一

- 

对最难题（IMO-hard）仍有挑战，但模型能准确指出自己的逻辑漏洞。

![image]()

![image]()


🏆 竞赛表现

- 

IMO 2025（国际数学奥赛）：解出 6 题中 5 题，金牌水平。

- 

CMO 2024（中国数学奥赛）：解出 4 题 + 1 题部分得分，金牌水平。

- 

Putnam 2024（美国大学数学赛）：118/120 分，几乎满分。

![image]()



---



🧠 能力特点

- 

准确率高：答案正确率超过 GPT-5 与 Gemini 系列；

- 

推理严谨：每一步逻辑都能自检，避免跳步或幻觉；

- 

自我改进能力强：能在多轮验证中不断提升证明质量；

- 

解释性好：输出不仅有结论，还有完整推理过程；




GitHub：https://github.com/deepseek-ai/DeepSeek-Math-V2


模型下载：https://huggingface.co/deepseek-ai/DeepSeek-Math-V2


技术报告：https://github.com/deepseek-ai/DeepSeek-Math-V2/blob/main/DeepSeekMath_V2.pdf

---

*来源：[DeepSeek 开源了一个数学推理大模型：DeepSeek-Math-V2  超越Gemini 获得 IMO 金牌](https://www.xiaohu.ai/p/deepseek-deepseek-math-v2-gemini-imo/27333817)*
