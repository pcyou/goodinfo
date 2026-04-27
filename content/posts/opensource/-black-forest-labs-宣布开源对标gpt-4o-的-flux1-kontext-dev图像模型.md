---
title: "Black Forest Labs 宣布开源对标GPT 4o 的 FLUX.1 Kontext [dev]图像模型"
date: 2025-06-26T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Black Forest Labs 发布了 FLUX.1 Kontext [dev]，这是其图像编辑模型 FLUX.1 Kontext [pro] 的开源开发版本，拥有 12B参数，具备 接近专有工具的图像编辑能力，并可在消费级硬件上运行。   其目标是提供一个性能接近闭源专有模型的免费工具。  -"
source_url: "https://www.xiaohu.ai/p/black-forest-labs-gpt-4o-flux-1-kontext-dev/22658674"
xiahuid: "22658674"
---

## 📰 正文

Black Forest Labs 发布了 FLUX.1 Kontext [dev]，这是其图像编辑模型 FLUX.1 Kontext [pro] 的开源开发版本，拥有 12B参数，具备 接近专有工具的图像编辑能力，并可在消费级硬件上运行。


其目标是提供一个性能接近闭源专有模型的免费工具。

- 

模型规模：12B 参数（对比 Stable Diffusion 约为 1B-2B）

- 

模型定位：仅用于图像编辑（非从零生成），强调局部精准控制与角色一致性。



🔓 开源与可用性


- 

模型在 FLUX.1 非商业许可下开源，支持研究与非商业用途。

- 

权重可通过 Hugging Face 获取，兼容 ComfyUI、HuggingFace Diffusers、TensorRT。

- 

由多个合作方（如 FAL、Replicate、Runware、DataCrunch、TogetherAI）提供云端或本地推理支持。



主要能力



FLUX.1 Kontext [dev]专注于 图像编辑任务：包括迭代编辑、角色保持、局部与全局精细控制。

- 

可以非常准确地“重绘”图片中的局部或全图，比如：

- 

把帽子加到人物头上

- 

改变背景风景

- 

把原图中的狗换成猫，人物保持原样


- 

多次修改也不会“跑偏”或者失真

- 

跟很多流行工具（如 ComfyUI）无缝结合，方便使用






![image]()


性能评估与对比


- 

评估基准：使用其自研的 KontextBench（一个新的图像编辑评测集）

- 

评估维度：

- 

编辑精度（是否能实现用户期望的修改）

- 

角色保持（人物面部/姿态的一致性）

- 

多场景迁移（是否能适应复杂背景与构图）


- 

对比模型：

- 

开源模型：

- 

Bytedance Bagel（文生图+编辑混合模型）

- 

HiDream-E1-Full（开源扩散图像编辑模型）


- 

闭源模型：

- 

Google's Gemini-Flash Image



- 

结果：Kontext [dev] 在多项任务中人类偏好得分优于上述所有模型，并由第三方机构 Artificial Analysis 独立验证。

![image]()



技术细节与优化



与 NVIDIA 合作，构建了专门针对全新 NVIDIA Blackwell 架构优化的 TensorRT 权重，该架构大幅提升推理速度并降低内存使用，同时保持高质量的图像编辑性能。


推理优化：

- 

与 NVIDIA 合作，为最新的 Blackwell 架构（B100 GPU）定制推理优化：

- 

提供 FP16、BF16、FP8、FP4 等低精度权重

- 

极大降低延迟与显存需求，适配边缘设备部署



![image]()


商业许可机制


- 

推出自助购买平台（Self-Serve Portal）

- 

支持在线获取商业授权，包括：

- 

FLUX.1 Kontext [dev]

- 

FLUX.1 Tools [dev]（辅助图像处理）

- 

FLUX.1 [dev]（文本生成图像模型）






![image]()


模型下载：https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev 


技术报告：https://arxiv.org/abs/2506.15742

---

*来源：[ Black Forest Labs 宣布开源对标GPT 4o 的 FLUX.1 Kontext [dev]图像模型](https://www.xiaohu.ai/p/black-forest-labs-gpt-4o-flux-1-kontext-dev/22658674)*
