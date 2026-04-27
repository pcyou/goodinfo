---
title: "OpenAI 宣布 SWE-bench Verified 不再能衡量前沿编程能力"
date: 2026-04-27T08:00:00+08:00
tags: ["OpenAI", "SWE-bench", "AI评估", "编程能力"]
categories: ["ai-tech"]
summary: "OpenAI 发布博客文章，正式宣布 SWE-bench Verified 基准测试已饱和，不再能够有效区分前沿 AI 模型的编程能力。"
sources:
  - name: "OpenAI Official Blog"
    url: "https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/"
    publisher: "OpenAI"
  - name: "Hacker News Discussion"
    url: "https://news.ycombinator.com/item?id=47341645"
    publisher: "Hacker News"
---

## 📰 正文

OpenAI 近日正式发表声明，宣布 **SWE-bench Verified** 基准测试已无法继续有效衡量前沿 AI 模型的编程能力。这一决定标志着 AI 代码生成领域的一个重要转折点。

### 背景

SWE-bench Verified 曾是业界衡量 AI 系统解决真实 GitHub 问题能力的黄金标准。该基准从真实开源项目中收集实际问题，要求 AI 模型生成可被直接合并的代码修复方案。然而，随着各家公司模型能力的快速提升，这一基准已经高度饱和。

SWE-bench 的联合创始人之一 Ofir Press 在 Hacker News 讨论中指出："SWE-bench Verified 目前已达到 93.9% 的饱和率（恭喜 Anthropic）。任何尚未达到这一水平的模型仍有提升空间，但该基准作为区分工具的效用已经显著下降。"

### 为什么不再有效？

OpenAI 在博客文章中阐述了多个关键原因：

- **基准饱和**：最先进模型在该测试上的得分已接近天花板，无法区分模型之间的实际能力差异
- **训练数据泄露**：随着基准测试的广泛使用，相关数据不可避免地进入模型训练集
- **静态测试的局限性**：固定不变的测试集容易受到针对性优化的影响，难以反映模型在未知问题上的泛化能力

### 行业影响

这一决定引发了 AI 社区的广泛讨论。多位研究者和从业者指出，任何公开基准都面临着被"游戏化"的风险。当行业存在巨大的优化激励时，模型往往会针对特定测试进行过度拟合，而非真正提升通用能力。

一些专家建议，AI 评估需要转向更加动态和对抗性的方法，例如持续更新的测试集、真人评估、以及在真实工作环境中的性能测量。

> "基准很难设计，而当整个行业都有动力去'刷分'时，它们变得更加困难。" —— AI 研究者社区共识

### 未来方向

OpenAI 没有公布替代 SWE-bench 的具体方案，但暗示未来的评估框架将更加注重动态性、对抗性和现实世界表现。这一转向反映了 AI 行业对评估方法论的深层思考：当基准成为目标时，它就不再是一个好的衡量标准。

---

*来源：[OpenAI 官方博客](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[Hacker News 讨论](https://news.ycombinator.com/item?id=47341645)*
