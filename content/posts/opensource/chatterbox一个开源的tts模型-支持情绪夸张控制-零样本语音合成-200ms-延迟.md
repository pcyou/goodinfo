---
title: "Chatterbox：一个开源的TTS模型 支持情绪夸张控制 零样本语音合成 <200ms 延迟"
date: 2025-05-29T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Chatterbox 是由 Resemble AI 发布的一个 开源、生产级别的文本转语音（Text-to-Speech, TTS）系统，主打：  -   高质量语音合成（state-of-the-art）  -   零样本合成能力（zero-shot TTS）  -   情绪夸张控制（exagge"
source_url: "https://www.xiaohu.ai/p/chatterbox-tts-200ms/21910141"
xiahuid: "21910141"
---

## 📰 正文

Chatterbox 是由 Resemble AI 发布的一个 开源、生产级别的文本转语音（Text-to-Speech, TTS）系统，主打：

- 

高质量语音合成（state-of-the-art）

- 

零样本合成能力（zero-shot TTS）

- 

情绪夸张控制（exaggeration control）

- 

语音转换支持（voice conversion）



其输出质量在对比测试中 优于 ElevenLabs 等主流闭源 TTS 产品。


主要功能特点


- 

🔊 零样本语音合成（Zero-shot TTS）

- 

🎭 支持语音情绪/夸张控制（Exaggeration Control）

- 

🔁 简单集成的语音转换（Voice Conversion）

- 

🔐 嵌入式水印（PerTh Watermarking）





![image]()


它兼顾高音质、高速度（<200ms 延迟）与高度可调性，适用于游戏、AI Agent、内容创作等语音场景。


🧠 1. 零样本文本转语音（Zero-shot TTS）


- 

仅需提供一段短的参考音频（即 audio prompt），即可模仿该声音合成任意文本内容。

- 

无需专门训练新说话人的模型，具备高度泛化能力。



---



🎭 2. 语音风格与情绪调节（Emotion & Style Control）


- 

通过两个核心参数实现语音风格控制：

- 

exaggeration：控制情绪/语气夸张程度

- 

cfg_weight：调节语音生成中内容 vs 声音匹配度


- 

支持生成：

- 

夸张、激昂的演讲语调

- 

冷静、平稳的语音助手语调

- 

更具表现力或更自然的语音内容




---



🔁 3. 简单易用的语音转换功能（Voice Conversion）


- 

将一个人的语音内容**“转换成另一个人的声音风格”**。

- 

适用于角色配音、语音模仿、个性化语音合成等场景。

- 

使用 voice_conversion.py 和 example_vc.py 提供完整样例。



---



🔐 4. 内嵌式神经水印系统（PerTh Watermarking）


- 

每段语音合成结果都嵌入不可察觉的神经水印，可防篡改识别。

- 

具备以下鲁棒性：

- 

不会被 MP3 压缩破坏

- 

不会因裁剪或编辑丢失

- 

可检测并识别音频来源（AI 合成 vs 真实）




---



🚀 5. 实时、稳定的高质量音频生成（Low-Latency Inference）


- 

推理延迟小于 200 毫秒，适合实时语音交互应用。

- 

使用alignment-informed inference，可保持语速与发音的一致性与流畅性。

- 

声码器采用 HiFi-GAN / HiFT-GAN 改进模型，保证清晰度与自然度。



---



🧱 6. 模块化设计与开发友好性（Developer-Friendly Structure）


- 

提供 example_tts.py 和 gradio_tts_app.py 等脚本帮助快速部署和测试。

- 

支持 Hugging Face Gradio 页面在线体验。

- 

代码结构清晰，易于自定义与迁移。



架构与核心技术



🎯 1. 主体模型架构


- 

模型基础：Llama 0.5B 级参数的模型作为语言理解/生成基础。

- 

训练数据：使用了 50 万小时清洗过的音频数据进行训练。



🧩 2. 技术细节解析


![image]()


GitHub：https://github.com/resemble-ai/chatterbox 


更多演示：https://resemble-ai.github.io/chatterbox_demopage/ 


在线体验：https://huggingface.co/spaces/ResembleAI/Chatterbox

---

*来源：[Chatterbox：一个开源的TTS模型 支持情绪夸张控制 零样本语音合成 <200ms 延迟](https://www.xiaohu.ai/p/chatterbox-tts-200ms/21910141)*
