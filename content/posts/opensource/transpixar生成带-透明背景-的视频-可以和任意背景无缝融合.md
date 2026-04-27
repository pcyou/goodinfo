---
title: "TransPixar：生成带 透明背景 的视频 可以和任意背景无缝融合"
date: 2025-01-09T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "项目背景    TransPixar 是一个创新的生成视频模型，专注于生成包括透明度通道（alpha 通道）的 RGBA 视频。相比传统的 RGB 视频，RGBA 视频能够实现更丰富的视觉效果（VFX），例如透明的烟雾、反射等，方便这些元素无缝地与场景融合。   该项目由香港科技大学（HKUST）与"
source_url: "https://www.xiaohu.ai/p/transpixar/17594622"
xiahuid: "17594622"
---

## 📰 正文

项目背景



TransPixar 是一个创新的生成视频模型，专注于生成包括透明度通道（alpha 通道）的 RGBA 视频。相比传统的 RGB 视频，RGBA 视频能够实现更丰富的视觉效果（VFX），例如透明的烟雾、反射等，方便这些元素无缝地与场景融合。


该项目由香港科技大学（HKUST）与 Adobe Research 合作完成。


TransPixar 是什么？



TransPixar 的核心功能之一是生成带 透明背景 的视频。


这是通过 AI 技术生成视频 的新方法。传统的视频生成技术通常只能输出普通的彩色画面（RGB格式），而 TransPixar 在此基础上增加了 alpha 通道，这意味着它可以生成具有透明背景的视频（RGBA格式）。这类视频中的透明部分可以无缝叠加到其他背景上，比如：

- 

一只松鼠在透明背景下摆动尾巴，可以直接放到任意背景中。

- 

一团烟雾在透明背景中扩散，用于电影特效制作。

- 

透明水杯中的冰块旋转，可以直接用于广告设计。





![image]()





这些透明的效果（就像你看电影里的烟雾、火焰、玻璃等特效）在制作电影或者广告时非常重要。


---



它解决了什么问题？



普通的 AI 视频生成技术只能处理不透明的视频（例如直接生成一个完整的画面），无法生成透明的部分（比如你看得到背后东西的玻璃或烟雾）。而 TransPixar：
1. 

加了“透明度”功能：生成的视频可以带透明部分，像电影中的玻璃、烟雾、或者水面。

2. 

不需要重新训练：它是在已经很厉害的 AI 视频生成模型上，直接扩展出了透明度功能。



---



怎么做到的？



它用了 DiT（扩散变换器） 的技术，通过特别设计的方法让 AI 学会同时生成视频画面和透明效果。而且：

- 

用了特别的“微调”方式（LoRA技术），让模型只需少量训练就能生成高质量的透明视频。

- 

改进了 AI 的注意力机制，确保生成的视频画面和透明效果一致，不会出现奇怪的地方。



---



有什么用？


- 

影视和广告：省下做透明特效的人工工作量，比如爆炸的烟雾、水波等。

- 

教育和互动内容：生成透明的动态效果，能更直观地演示科学原理或者产品功能。

- 

设计和创意：让设计师用更少的时间做出更炫的透明效果视频。





![image]()


技术创新点

1. 

核心技术架构：

- 

使用 扩散变换器（Diffusion Transformer, DiT） 架构，在原有 RGB 模型基础上扩展，添加生成 alpha 通道的能力。

- 

引入了专门的 alpha 通道 token，并通过 LoRA（Low-Rank Adaptation）微调，使模型能够同时生成 RGB 和 alpha 通道数据。

- 

采用优化的注意力机制，改进了 RGB 和 alpha 通道的对齐性，同时避免有限训练数据对模型性能的负面影响。

![image]()


2. 

关键改进：

- 

新增的 alpha 通道 token 被重新初始化了位置嵌入，并添加了零初始化的域嵌入（domain embedding）来区分 RGB 和 alpha token。

- 

使用分组注意力机制（Grouped Attention），保留了原有模型的 RGB 性能，同时加强了 RGB 对 alpha 的关注，避免文本直接与 alpha 通道关联导致的潜在风险。


3. 

生成方式：

- 

文本到 RGBA 视频：生成诸如透明水杯中旋转的冰块、太空中的小行星带、快速摆动的松鼠尾巴、以及爆炸般扩散的尘土云等逼真的透明效果视频。

- 

图像到 RGBA 视频：输入一张图像，模型可以生成带有透明度效果的动态视频。

![image]()




项目地址：https://wileewang.github.io/TransPixar/ 


GitHub：https://github.com/wileewang/TransPixar 


论文：https://wileewang.github.io/TransPixar/paper/paper.pdf 


在线体验：https://huggingface.co/spaces/wileewang/TransPixar

---

*来源：[TransPixar：生成带 透明背景 的视频 可以和任意背景无缝融合](https://www.xiaohu.ai/p/transpixar/17594622)*
