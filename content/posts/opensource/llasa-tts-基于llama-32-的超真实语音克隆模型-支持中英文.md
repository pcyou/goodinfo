---
title: "Llasa TTS： 基于Llama 3.2 的超真实语音克隆模型 支持中英文"
date: 2025-01-25T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Llasa TTS：是由香港科技大学开发的一个文本到语音（TTS）系统，基于 LLaMA 语言模型（ 1B、3B 和 8B 参数规模），通过整合 XCodec2 的语音 token 提供语音生成功能。   模型训练使用了 250,000 小时的中英双语语音数据，可实现以下两种语音生成模式： 1."
source_url: "https://www.xiaohu.ai/p/llasa-tts-llama-3-2/18052766"
xiahuid: "18052766"
---

## 📰 正文

Llasa TTS：是由香港科技大学开发的一个文本到语音（TTS）系统，基于 LLaMA 语言模型（ 1B、3B 和 8B 参数规模），通过整合 XCodec2 的语音 token 提供语音生成功能。


模型训练使用了 250,000 小时的中英双语语音数据，可实现以下两种语音生成模式：
1. 

从纯文本生成语音。

2. 

基于给定的语音（15秒）提示生成目标语音。



功能与技术特点

1. 

模型架构

- 

Llasa-3B 使用了 LLaMA 的文本生成框架，加入了 XCodec2 的语音 token（65,536 种）。

- 

支持输入文本的语音生成，或结合语音提示生成目标语音。


2. 

训练数据

- 

采用包含 250,000 小时的中英语音数据进行训练。


3. 

语音生成方式

- 

纯文本模式：直接输入文本生成语音。

- 

语音提示模式：结合提示语音和目标文本生成自然语音，保持语调与提示语音一致。


4. 

语音提示模式的情感传递：

- 

Llasa-3B 可以通过输入一个带有情感特征的语音提示（Prompt），在生成目标语音时保留提示语音中的情感特征。

- 

这种方式确保生成的语音能够模仿提示语音的语气、情绪和语调。


5. 

模型大小与参数

- 

模型大小：4.01B 参数。

- 

Tensor 类型：BF16（适合现代硬件加速）。


6. 

推理工具与配置

- 

使用 PyTorch 和 Hugging Face 的 Transformers 库。

- 

支持 GPU 加速（CUDA 环境）。

- 

支持 16kHz 音频输出。




Llasa-1B ：https://huggingface.co/HKUSTAudio/Llasa-1B 


Llasa-3B ：https://huggingface.co/HKUSTAudio/Llasa-3B 


在线体验：https://huggingface.co/spaces/srinivasbilla/llasa-3b-tts

---

*来源：[Llasa TTS： 基于Llama 3.2 的超真实语音克隆模型 支持中英文](https://www.xiaohu.ai/p/llasa-tts-llama-3-2/18052766)*
