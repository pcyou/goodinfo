---
title: "Meta AI发布 Omnilingual ASR：一个覆盖超过 1600 种语言 的开源语音识别框架"
date: 2025-11-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Meta AI（FAIR团队）发布了 Omnilingual ASR（全语种自动语音识别系统）：一个覆盖超过 1600 种语言 的开源语音识别框架，其中包括 500 种此前从未被 AI 系统识别过的低资源语言。   这项计划的目标十分宏大：  >   让任何语言都能被机器理解，让任何人都能用自己的语"
source_url: "https://www.xiaohu.ai/p/meta-ai-omnilingual-asr-1600/26808799"
xiahuid: "26808799"
---

## 📰 正文

Meta AI（FAIR团队）发布了 Omnilingual ASR（全语种自动语音识别系统）：一个覆盖超过 1600 种语言 的开源语音识别框架，其中包括 500 种此前从未被 AI 系统识别过的低资源语言。


这项计划的目标十分宏大：

> 

让任何语言都能被机器理解，让任何人都能用自己的语言与世界沟通。



Omnilingual ASR 不是一个单一模型，而是一整套工具链，包括：

- 

Omnilingual wav2vec 2.0：一个拥有 70 亿参数 的多语言自监督语音模型；

- 

Omnilingual ASR Corpus：一个包含 350 种稀缺语言 的语音转录数据集；

- 

开放探索 Demo：用于展示各语言识别效果的在线交互工具。



Meta 的野心：让语音识别不再属于“主流语言”



当今市面上的语音识别系统（如 Whisper、Google ASR、Amazon Transcribe）
虽然对英语、普通话、西班牙语等主流语言的识别精度已接近完美，
但全球 7000 多种语言中，超过 80% 没有被 AI 听见过。


原因在于：

- 

大多数语言缺乏标注语音数据；

- 

模型训练成本高昂；

- 

AI 架构难以规模化泛化。



Meta 的 Omnilingual ASR 旨在解决这些结构性问题：

> 

从“多语言（multilingual）”迈向“全语言（omnilingual）”。



核心技术突破：从 wav2vec 到 LLM-ASR



1️⃣ 70 亿参数的「Omnilingual wav2vec 2.0」



Meta 将经典的 wav2vec 2.0（自监督语音表示模型）扩展至 7B 参数规模，
能从未经标注的语音数据中学习出跨语言的语义表征。


这使模型不必依赖大量人工标注语料，也能理解多语言语音特征。


2️⃣ 双解码架构：CTC 与 Transformer



系统包含两种语音转文本的解码器：

- 

CTC 解码器：传统高效的时间序列对齐方法；

- 

Transformer 解码器（被称为 LLM-ASR）：
将大语言模型（LLM）的序列建模能力应用于语音识别，
在低资源语言上大幅提升性能。

![image]()



成果惊人：

> 

在 1600+ 种语言中，78% 的语言字符错误率（CER）低于 10%，达到目前业内最高水平。



突破性创新：支持「自带语言（Bring Your Own Language）」



以往想让 AI 支持一种新语言，必须收集大量训练数据、聘请专家标注，代价极高。


而 Omnilingual ASR 的最大创新在于：

> 

任何人都能通过提供几段自己的语音样本 + 对应文本，就能让系统“学习”你的语言。



这种能力来自 LLM 式的 in-context learning（上下文学习）：

- 

无需再训练；

- 

无需专业硬件；

- 

几个样本即可获得可用识别结果。

![image]()



这意味着：

- 

语言学家可快速测试稀有方言；

- 

小语种社区可轻松建立本地语音识别系统；

- 

人工智能的语言包容性大幅提升。

![image]()



模型、数据、工具全开源



Meta 以 Apache 2.0 许可证 发布模型代码，并将数据集以 CC-BY 许可 开源。
所有模型基于 fairseq2 框架（PyTorch 生态），方便研究者复用。


提供的模型系列包括：

![image]()


🔗 相关资源


- 

📘 Omnilingual ASR 项目主页

- 

🎙 Language Exploration Demo

- 

🗣 Language Technology Partner Program

---

*来源：[Meta AI发布 Omnilingual ASR：一个覆盖超过 1600 种语言 的开源语音识别框架](https://www.xiaohu.ai/p/meta-ai-omnilingual-asr-1600/26808799)*
