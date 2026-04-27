---
title: "Google 正式推出新一代开源轻量级多模态大模型：Gemma 3n 是目前最先进的移动端和边缘设备模型"
date: 2025-06-26T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google 正式推出的 新一代开源轻量级多模态大模型：Gemma 3n，专为**端侧部署（on-device）**而优化。  它支持图像、音频、视频和文本输入输出，致力于在移动设备上实现接近云端模型的能力。   设计目标是：  >   高性能、多模态、轻量部署、可自定义、全设备适配。    它是"
source_url: "https://www.xiaohu.ai/p/google-gemma-3n/22660819"
xiahuid: "22660819"
---

## 📰 正文

Google 正式推出的 新一代开源轻量级多模态大模型：Gemma 3n，专为**端侧部署（on-device）**而优化。

它支持图像、音频、视频和文本输入输出，致力于在移动设备上实现接近云端模型的能力。


设计目标是：

> 

高性能、多模态、轻量部署、可自定义、全设备适配。



它是 Gemma 系列模型家族的一部分，之前的版本已经累积下载超过 1.6 亿次，广泛用于计算机视觉、医疗模型、内容生成等领域。


Gemma 3n 是迄今为止该系列中最先进、专为 移动端和边缘设备打造的版本。


🚀 核心亮点


![image]()


原生多模态支持


Gemma 3n 支持：

- 

图像、音频、视频、文本 输入

- 

文本 输出



适用于语音识别、图像理解、视频处理等多场景。


---



轻量高效：两种模型规格

![image]()


💡 使用创新架构，实际运行内存相当于传统 2B/4B 模型。


性能优异

- 

文本处理支持 140+ 种语言；

- 

多模态理解支持 35 种语言；

- 

在数学、编程和推理方面有显著增强；

- 

E4B 是首个参数少于 10B 的模型，在 lmarena.ai 测试中突破了 1300 分；成为首个参数量低于 100 亿且达到此基准的模型。


![image]()


核心技术架构



🧬 MatFormer（Matryoshka Transformer）

- 

像“俄罗斯套娃”一样，一个模型包含多个子模型（可嵌套推理）。

- 

支持两种使用方式：
1. 

预提取模型：使用已经分离好的 E2B 和 E4B。

2. 

Mix-n-Match：通过调整隐藏维度、跳层等方法，自定义模型大小，适配特定硬件。



> 

后续还将支持部署时动态切换子模型路径（弹性推理）。

![image]()

![image]()



---



📦 PLE（Per-Layer Embeddings）

- 

每一层嵌入独立加载，大幅减小显存压力。

- 

只需将核心 Transformer 权重载入显存，其他在 CPU 上计算即可。

![image]()



---



🧠 KV Cache Sharing（上下文缓存共享）

- 

针对音频/视频等长序列输入场景，显著加速首次响应时间。

- 

Prefill 阶段性能提升 2 倍。



---



音频处理：内置语音理解能力


- 

基于 USM（Universal Speech Model） 构建语音编码器。

- 

每 160ms 生成一个 token，提供细粒度上下文感知。

- 

支持：

- 

ASR（自动语音识别）

- 

AST（自动语音翻译）



> 

特别适合英语与西语、法语、意大利语、葡语之间的翻译任务。



---



视觉处理：全新 MobileNet-V5 编码器


- 

架构：MobileNet-V5-300M

- 

特性：

- 

原生支持分辨率：256×256，512×512，768×768

- 

实时处理：可达 60fps（Google Pixel）

- 

视觉语言理解准确率超越 SoViT

- 

参数减少 46%，显存减少 4 倍，速度提升 13 倍（量化后）




如何开始使用 Gemma 3n？



✅ 在线体验：


- 

Google AI Studio → 选择 Gemma 3n 即可运行。



✅ 模型下载：


- 

Hugging Face

- 

Kaggle

- 

Google Cloud Vertex AI



官方介绍：https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/

---

*来源：[Google 正式推出新一代开源轻量级多模态大模型：Gemma 3n 是目前最先进的移动端和边缘设备模型](https://www.xiaohu.ai/p/google-gemma-3n/22660819)*
