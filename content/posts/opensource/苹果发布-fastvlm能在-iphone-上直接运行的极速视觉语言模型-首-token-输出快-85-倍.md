---
title: "苹果发布 FastVLM：能在 iPhone 上直接运行的极速视觉语言模型 首 token 输出快 85 倍"
date: 2025-05-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "FastVLM（Fast Vision Language Model） 是 苹果公司开发的一种高效视觉语言模型（VLM）编码器系统。   它专注于将高分辨率图像高效转换为 LLM 可处理的视觉 token，从而大幅提升图文理解的速度与效能。   你可以把它理解为：  >   📷 FastVLM：先把"
source_url: "https://www.xiaohu.ai/p/fastvlm-iphone-token-85/21391360"
xiahuid: "21391360"
---

## 📰 正文

FastVLM（Fast Vision Language Model） 是 苹果公司开发的一种高效视觉语言模型（VLM）编码器系统。


它专注于将高分辨率图像高效转换为 LLM 可处理的视觉 token，从而大幅提升图文理解的速度与效能。


你可以把它理解为：

> 

📷 FastVLM：先把图像看懂（图像 → token）
🧠 大语言模型（比如 GPT、Claude、Qwen）：再根据 token 生成回答或描述（token → 语言）



这种模型可以用于：

- 

给图片自动生成描述（Image Captioning）

- 

回答“这张图是什么”的问题（VQA，视觉问答）

- 

分析图中的数据或对象（图像识别）


> 

✅目标是为图文任务提供轻量、高速、低延迟的视觉前端模块


✅支持高分辨率图像输入（推理速度仍远快于主流 VLM 架构）


✅极致性能（Time-to-First-Token）：

- 

FastVLM-0.5B：相较于 LLaVA-OneVision-0.5B，首 token 输出快 85 倍，模型体积小 3.4 倍。

- 

FastVLM-7B（+ Qwen2-7B LLM）：优于 Cambrian-1-8B，在相同精度下 首 token 输出快 7.9 倍。



✅能够兼容主流 LLM 并轻松适配 iOS/Mac 生态，特别适合落地在边缘设备、端侧 AI 应用和实时图文任务场景。

![image]()



它和传统做法有什么不同？



以前的模型（比如 LLaVA、BLIP）在图像处理方面存在两个问题：
1. 

慢：图像编码器太复杂，处理一张图要几十秒

2. 

大：模型体积庞大，占内存，耗资源，不适合放在手机或小设备上



而 FastVLM 专门解决这两个问题：


🧩 小：模型体积小，容易部署在 iPhone、iPad、Mac 上


⚡ 快：速度非常快，首个 token 输出速度提升 85 倍（相对同类模型）


🧠 兼容强：可以和现有的大语言模型组合（如 GPT-4、Qwen2-7B）


📱 移动友好：专门优化了苹果芯片（M系列）和 iOS 系统


模型结构与技术特点



1. 模型架构与模块：


- 

Vision Encoder：FastViTHD（核心视觉主干）

- 

Text Decoder：可与 Open Source LLM（如 Qwen2-7B）联合使用

- 

支持 LLaVA-style 的训练与推理流程，兼容 HuggingFace 接口



2. 模型规模与版本（共 3 个）：


- 

FastVLM-0.5B

- 

FastVLM-1.5B

- 

FastVLM-7B



每个版本均有 stage2 和 stage3 两阶段微调权重（模型已开放下载）


 它怎么工作的？



FastVLM 用了一个叫 FastViTHD 的轻量视觉模型，它的工作原理如下：
1. 

输入一张图片（比如一张猫的照片）

2. 

把这张图片“看一眼”后转成非常简洁的“token”表示

3. 

把这些 token 输入给语言模型（比如 Qwen、Claude）

4. 

LLM 再根据这些 token，说出一句话，比如“这是一只正在晒太阳的橘猫”



所以它的定位是：

> 

📷 把图片 → 转换为 → 语言模型能理解的形式（token），而且又快又小



适用场景


![image]()


GitHub：https://github.com/apple/ml-fastvlm 


论文：https://www.arxiv.org/abs/2412.13303

---

*来源：[苹果发布 FastVLM：能在 iPhone 上直接运行的极速视觉语言模型 首 token 输出快 85 倍](https://www.xiaohu.ai/p/fastvlm-iphone-token-85/21391360)*
