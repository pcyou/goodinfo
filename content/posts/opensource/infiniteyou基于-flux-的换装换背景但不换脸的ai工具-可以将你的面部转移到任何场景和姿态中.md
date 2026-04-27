---
title: "InfiniteYou：基于 FLUX 的“换装换背景但不换脸”的AI工具 可以将你的面部转移到任何场景和姿态中"
date: 2025-03-23T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "InfiniteYou（简称 InfU） 是字节跳动推出的首个基于 DiT（ FLUX）的稳定身份保持图像生成系统。它可以根据一张人脸图像和一段文本描述，生成一张 保留该人身份特征、同时 满足文字描述 的高质量图像。   也就是，它是一个能“换装换背景但不换脸”的AI工具。你可以输入一张人脸照片和一"
source_url: "https://www.xiaohu.ai/p/infiniteyou-flux-ai/19821109"
xiahuid: "19821109"
---

## 📰 正文

InfiniteYou（简称 InfU） 是字节跳动推出的首个基于 DiT（ FLUX）的稳定身份保持图像生成系统。它可以根据一张人脸图像和一段文本描述，生成一张 保留该人身份特征、同时 满足文字描述 的高质量图像。


也就是，它是一个能“换装换背景但不换脸”的AI工具。你可以输入一张人脸照片和一句文字描述（如“在花园里的亚洲女孩”），它就能生成一张保持这个人脸身份、场景和风格一致的照片。


这意味这你可以将你的面部转移到任何场景和姿态中。


它解决了什么问题？ 以往方法生成的图片虽然“像”，但经常：

- 

人脸不像（比如套壳复制）：传统方法（如 Stable Diffusion、IP-Adapter）容易出现人脸不准确，像“复制粘贴”一样的结果，缺乏细节和自然感。

- 

和文字描述不一致：即使生成了图像，也可能与输入的文本描述不符合，比如描述“穿金色裙子的女孩”，图像可能穿成了白色婚纱。

- 

图像质量和审美差：很多方法生成的图像存在模糊、面部扭曲、背景错误、手指畸形等问题，缺乏美感和真实感。

- 

缺乏灵活性和可扩展性：早期方法大多基于 U-Net 架构，限制了生成能力，缺乏对新模型（如 DiTs）的适配性，也难以与控制插件（如 ControlNet、LoRA）配合使用。

![image]()



它怎么解决的？ 它用了三个高招：
1. 

用新的“Diffusion Transformer”模型（像FLUX）来提升生成质量；

2. 

发明了一个“身份注入器”InfuseNet，把人脸信息通过“旁路”加入主模型，避免干扰图像生成；

3. 

先用真实人脸数据做基础训练，再用自制的高质量图像做精细微调。



效果如何？

- 

图像更像真人、更符合描述、也更漂亮。

- 

用户测试中大多数人都更喜欢它生成的图。



能用在哪？ 可以用于头像生成、AI写真、虚拟人建模、换装换背景换风格等各种定制场景。


🚀InfiniteYou 的主要功能


![image]()


---



🛠️ 技术细节详解



🌐 核心架构：InfU（InfiniteYou Framework）


- 

基座模型：FLUX（DiT）

- 

身份注入模块：InfuseNet

- 

类似 ControlNet，但专门为身份特征设计

- 

使用残差连接（residual connection）将身份特征“注入”模型

- 

不修改注意力层，避免 IPA 带来的文本混淆和画质下降问题



![image]()


🧠 多阶段训练策略（Multi-stage Training）


![image]()

![image]()


引入的采用合成单人多样本 (SPMS) 数据和监督微调 (SFT) 的多阶段训练策略。


🧩 插拔式设计（Plug-and-Play）



兼容模块包括：

- 

✅ FLUX.1-dev / FLUX.1-schnell（快推理版本）

- 

✅ ControlNet（姿势/边缘控制）

- 

✅ LoRA（快速注入风格或新能力）

- 

✅ IP-Adapter（用于风格迁移、参考图像）

![image]()



📊 性能对比（与 SOTA 方法）


![image]()

![image]()

- 

InfiniteYou 的结果在身份保持、文本控制、美观程度上全面优于现有方法

- 

避免了 PuLID-FLUX 中出现的“脸贴图感”、手部变形等问题

![image]()



---



🌈 应用场景


![image]()


项目地址：https://bytedance.github.io/InfiniteYou/


GitHub：https://github.com/bytedance/InfiniteYou


技术报告：https://arxiv.org/pdf/2503.16418 


模型下载：https://huggingface.co/ByteDance/InfiniteYou 


在线体验：https://huggingface.co/spaces/ByteDance/InfiniteYou-FLUX

---

*来源：[InfiniteYou：基于 FLUX 的“换装换背景但不换脸”的AI工具 可以将你的面部转移到任何场景和姿态中](https://www.xiaohu.ai/p/infiniteyou-flux-ai/19821109)*
