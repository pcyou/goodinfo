---
title: "Paper2Video：将任何学术论文自动”变成“演讲视频”"
date: 2025-11-28T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "👉 Paper2Video 是一个让 AI 自动把“学术论文”变成“演讲视频”的系统。   它能自动生成类似会议上作者讲论文的视频展示： 你只需要提供：  -   论文（LaTeX 格式）  -   一张作者照片  -   一段语音样本 然后系统会自动：   >   生成 PPT + 字幕 + 语音"
source_url: "https://www.xiaohu.ai/p/paper2video/27333691"
xiahuid: "27333691"
---

## 📰 正文

👉 Paper2Video 是一个让 AI 自动把“学术论文”变成“演讲视频”的系统。


它能自动生成类似会议上作者讲论文的视频展示：
你只需要提供：

- 

论文（LaTeX 格式）

- 

一张作者照片

- 

一段语音样本
然后系统会自动：


> 

生成 PPT + 字幕 + 语音解说 + 光标动画 +（可选）作者虚拟讲解视频。



项目背景与意义



研究人员写完论文后，常常还得：

- 

做幻灯片；

- 

录讲解视频；

- 

加字幕、配音。



这些步骤既耗时又重复。


而 Paper2Video 的目标是：

> 

让 AI 来自动完成这些工作，
把论文“一键转成讲解视频”。



这对科研传播有两个意义：
1. 

让论文更容易被理解和传播（特别是跨领域读者）。

2. 

让研究者能更快发布视频讲解，提升曝光度与学术影响力。



系统组成模块



它是一个由多个 AI 智能体（agents）协作的多模块系统。


👇 整体流程如下

![image]()




![image]()


系统主要由两部分组成：


① PaperTalker：生成系统


多智能体（multi-agent）AI框架，用来“生成视频”。


② Paper2Video Benchmark：评估系统


一个专门的科研视频数据集与评估指标体系，用来“衡量AI视频质量”。


1️⃣ PaperTalker



负责“制作视频”的 AI 模块。


它能自动完成：

- 

提取论文核心内容；

- 

生成幻灯片（slides）；

- 

生成字幕；

- 

合成语音讲解；

- 

光标动作；

- 

虚拟人像口型同步（talking-head，可选）。



换句话说，它像一个“AI 论文讲解机器人”。


---



2️⃣ Paper2Video Benchmark



负责“评价视频效果”的模块。


因为科学视频不同于娱乐视频，它需要评估：

- 

是否准确传达研究核心；

- 

是否易于观众理解；

- 

是否突出了作者贡献。



他们为此提出了 4 个专门的指标：


指标含义Meta Similarity视频与论文内容的一致性PresentArena视频演讲的表现力PresentQuiz视频内容的知识可测性IP Memory观众是否能记住研究主题和作者

![image]()


---



系统运行流程（技术逻辑）



整个自动生成视频的流程如下：


```None
论文 (LaTeX)
   ↓
AI提取论文结构与核心内容
   ↓
生成幻灯片 (Beamer)
   ↓
生成字幕文本
   ↓
合成语音解说 (TTS)
   ↓
添加光标动画 (Cursor)
   ↓
生成虚拟讲者视频 (可选)
   ↓
输出完整演讲视频

```



💡 如果不需要“人像视频”，可以用“轻量模式（pipeline_light.py）”快速生成，仅需几分钟。


运行环境与依赖



主要技术环境：

- 

Python 3.10

- 

Conda 虚拟环境

- 

GPU 建议：NVIDIA A6000（48G显存）

- 

依赖模型：

- 

LLM：GPT-4.1、Gemini 2.5 Pro 或本地开源模型（如 Qwen）

- 

Talking Head 模块：基于 Hallo2

- 

视频评估模型：集成 OpenAI / Gemini API




一些案例



“The forward-forward algorithm: Some preliminary investigations.” by Hinton, Geoffrey.
🔗 “前向-前向算法：一些初步研究。” 作者：Geoffrey Hinton。


🔗 “SANA: Efficient high-resolution image synthesis with linear diffusion transformers.” by Jensen Huang
🔗 “SANA：基于线性扩散变换器的高分辨率图像高效合成。” 作者：黄仁勋


🔗 “Paper2Video: Automatic Video Generation from Scientific Papers.” by Tan Eng Chye
🔗 “Paper2Video：从科学论文自动生成视频。” 作者：陈庆炎


🔗 “Character-level Convolutional Networks for Text Classification.” by Yann LeCun
🔗 “用于文本分类的字符级卷积网络。” 作者：Yann LeCun


项目地址：https://showlab.github.io/Paper2Video/ 


技术报告：https://arxiv.org/abs/2510.05096


GitHub：https://github.com/showlab/Paper2Video

---

*来源：[Paper2Video：将任何学术论文自动”变成“演讲视频”](https://www.xiaohu.ai/p/paper2video/27333691)*
