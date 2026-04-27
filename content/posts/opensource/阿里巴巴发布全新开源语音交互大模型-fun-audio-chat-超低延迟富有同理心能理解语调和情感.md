---
title: "阿里巴巴发布全新开源语音交互大模型 Fun-Audio-Chat 超低延迟富有同理心、能理解语调和情感"
date: 2025-12-24T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "阿里云 Tongyi Fun 团队 发布全新的开源语音大模型 Fun-Audio-Chat ，在实现 自然、低延迟的语音交互（Voice Interaction），专为实现自然、低延迟的语音交互而设计。   你不需要打字，只要用语音对它说话，它就能实时理解、思考、回答你，并用自然流畅的语音回复。"
source_url: "https://www.xiaohu.ai/p/fun-audio-chat/28032367"
xiahuid: "28032367"
---

## 📰 正文

阿里云 Tongyi Fun 团队 发布全新的开源语音大模型 Fun-Audio-Chat ，在实现 自然、低延迟的语音交互（Voice Interaction），专为实现自然、低延迟的语音交互而设计。


你不需要打字，只要用语音对它说话，它就能实时理解、思考、回答你，并用自然流畅的语音回复。


它可以：

- 

回答语音问题（比如“帮我总结这段语音”）

- 

理解语音内容（比如识别情绪、音色、命令）

- 

按语音执行任务（比如“帮我打开音乐”、“拨打电话”）

- 

语音生成语音（你说话它直接“开口”回应）

- 

模拟语音情感（比如开心、温柔、严肃）



它可以完成端到端的语音问答、语音理解、语音函数调用、语音指令执行与语音共情等任务。

![image]()


该模型的设计目标是：
1. 

在低延迟条件下实现自然的语音交互体验；

2. 

在保持大语言模型语义理解能力的同时增强语音感知与生成能力；

3. 

提供统一框架支持语音→语音、语音→文本等多模态任务。



技术创新



Fun-Audio-Chat 的核心目标是：

> 

在统一的大语言模型框架下，实现自然、实时的语音理解与语音生成。



为此，它引入两个核心创新：


🧩 1. 双分辨率语音表示（Dual-Resolution Speech Representations）



传统语音模型采样频率高（12.5Hz 或 25Hz），虽然声音细节多，但计算量很大、延迟高。
Fun-Audio-Chat 采用了一种聪明的折中方法：

- 

主干部分（5Hz）：负责理解语音的“意思”，计算量低；

- 

精细部分（25Hz）：负责保留声音细节，让语音听起来自然。



👉 好处：

- 

推理速度快（延迟低）

- 

将 GPU 成本降低约 50%

- 

声音依旧高质量自然



这就像你看电影时，主干剧情是5帧/秒，人物表情用25帧补足，看起来流畅又省资源。


---



🧪 2. 核心混合训练（Core-Cocktail Training）



它结合了“语音模型”和“文本大模型”的训练方式：

- 

从 文本大模型（LLM） 那里学到理解能力；

- 

从 语音模型 那里学到听觉与说话能力。



👉 这样，它既能像 ChatGPT 一样理解语义，又能像 Siri 一样“听懂说话”。


🔷 3.模型架构


- 

Encoder：把语音转成语义特征（听懂你说啥）；

- 

LLM Backbone：理解语义、做推理（想清楚怎么回答）；

- 

TTS Head (CosyVoice)：把结果转成自然语音（说出来）。



🔄 4.全双工语音交互（Full-Duplex Interaction）



传统语音助手是“单工”的：说完一句 → 等回答。
Fun-Audio-Chat 实现了全双工语音，即边说边听、可打断、可轮换发言。


技术上，它通过：
1. 

模拟重叠语音数据；

2. 

加入“轮次控制（Turn-taking Control）”信号；

3. 

同步语音输入与输出流。



实验显示：

- 

在 Turn-Taking 精度上，Fun-Audio-Chat-Duplex 达到 100%；

- 

响应延迟 < 400ms；

- 

可在语音打断场景中稳定对话。



性能和测试结果


- 

在多个语音理解与对话基准上达到 同类模型最优（SOTA）；

- 

在 效率、音质、延迟 三方面取得均衡；

- 

Fun-Audio-Chat-30B-A3B 版本性能与 GPT-Audio、Gemini-2.5-Pro 相当；

- 

Fun-Audio-Chat-8B 版本在开源模型中表现最强。

![image]()



Fun-Audio-Chat 的 8B 模型在多个公开语音任务上都拿到了同级模型中的最高分

![image]()


项目及演示：https://funaudiollm.github.io/funaudiochat/


GitHub：https://github.com/FunAudioLLM/Fun-Audio-Chat


技术报告：https://github.com/FunAudioLLM/Fun-Audio-Chat/blob/main/Fun-Audio-Chat-Technical-Report.pdf 


模型：https://huggingface.co/FunAudioLLM/Fun-Audio-Chat-8B

---

*来源：[阿里巴巴发布全新开源语音交互大模型 Fun-Audio-Chat 超低延迟富有同理心、能理解语调和情感](https://www.xiaohu.ai/p/fun-audio-chat/28032367)*
