---
title: "Hibiki ：一个实时语音翻译系统 无需等到你说完整句话 边说话的同时边翻译 还能保留原说话人的音色"
date: 2025-02-06T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Hibiki 是一个实时语音翻译系统，可以在你说话的同时，立刻把语音翻译成另一种语言，并用自然的语音播放出来，不需要等到你说完整句话。   与传统的离线翻译不同，Hibiki 可以实时逐步生成目标语言的语音，而无需等待源语言句子完全结束，支持**语音传输（voice transfer）**及文本翻译"
source_url: "https://www.xiaohu.ai/p/hibiki/18425228"
xiahuid: "18425228"
---

## 📰 正文

Hibiki 是一个实时语音翻译系统，可以在你说话的同时，立刻把语音翻译成另一种语言，并用自然的语音播放出来，不需要等到你说完整句话。


与传统的离线翻译不同，Hibiki 可以实时逐步生成目标语言的语音，而无需等待源语言句子完全结束，支持**语音传输（voice transfer）**及文本翻译。


目前仅支持法语 → 英语，未来扩展到更多语言。


主要特点


- 

流式翻译：Hibiki 边听边翻译，不像传统翻译那样等到整个句子结束后再翻译。

- 

语音保持：翻译后，Hibiki 还能保留你的声音音色，让听起来更像你自己在说。

- 

实时文本翻译：除了语音翻译，还会生成同步的文本翻译，带有时间戳。

- 

可在手机上运行：Hibiki 有一个轻量版 Hibiki-M，可以在手机上本地运行。


![image]()


案例展示



这个例子来自一段幽默视频。源音频故意使用高音调，这是展示 Hibiki 如何很好地复制音调和韵律的一个好例子，并且它对背景噪音的鲁棒性很强，因为没有对输入 Hibiki 的音频进行降噪处理。


Hibiki-M 是一个小型化版本，仅1.7B 参数，可在移动设备上实时运行。例如，在 iPhone 16 Pro 上，Hibiki-M 可连续运行超过 1 分钟。


它是如何工作的？



Hibiki 基于 Moshi 语言模型，采用多流音频-文本处理架构，同时预测目标语音的离散音频 token，确保翻译的流畅性和连贯性。其核心技术 “内在独白”机制（Inner Monologue） 可优化文本翻译，并作为语音翻译的支撑结构。

- 

Hibiki 使用 AI 训练，学习不同语言之间的语音匹配关系。

- 

它的训练数据来自：

- 

人工标注的语音翻译数据（但很少）。

- 

AI 合成的翻译语音（用 TTS 技术生成）。


- 

翻译时，Hibiki 采用了一种“智能对齐”策略，确保翻译既准确又自然。


![image]()


多流音频-文本处理架构



Hibiki 采用 Moshi 语言模型 的多流处理机制，能够同时预测输入语音的文本翻译和目标语音的音频表示：

- 

通过 Transformer 预测离散音频 token（Discrete Audio Tokens），从而生成目标语音。

- 

采用 Moshi 的“内在独白”机制（Inner Monologue），在生成目标语音的同时生成目标文本，以确保翻译内容准确。



这种方法与 传统的级联（Cascade）方法 不同：

- 

传统级联方法：依次执行 ASR（自动语音识别） → MT（机器翻译） → TTS（文本转语音），容易累积错误，导致翻译不准确，流畅度下降。

- 

Hibiki 端到端方法：直接从 源语音 → 目标语音，避免了中间文本转换的误差，大幅提高翻译质量。



---



“内在独白”（Inner Monologue）机制



Hibiki 采用 Moshi 提出的“内在独白”机制（Inner Monologue），即：

- 

在预测音频 tokens（目标语音）时，同时生成文本 tokens（目标文本）。

- 

文本翻译作为支撑结构，优化语音预测。



🌟 关键优势
1. 

文本翻译优化：

- 

Hibiki 生成目标语音时，同时生成目标文本，可以用于对齐检查和翻译优化。

- 

这种机制确保文本和语音同步，提高可读性和理解度。


2. 

语音流畅度提升：

- 

文本 tokens 作为翻译支撑结构，提供上下文信息，帮助模型更流畅地预测目标语音的音频 tokens。

- 

避免语音输出时的卡顿、不自然停顿或语义错误，使翻译更加连贯。




Hibiki 运行时，仅需 Transformer 采样（Temperature Sampling），这种方式兼容实时推理，同时支持 批处理（batching），提升计算效率。


🎯 Hibiki 训练方法



1️⃣ 训练数据


- 

挑战：传统的翻译数据通常是文本对齐的，而 Hibiki 需要语音数据对齐。

- 

解决方案：

- 

生成合成数据（Synthetic Data）：

- 

使用文本翻译模型（MADLAD）进行对齐，确保翻译过程流畅。

- 

在目标语音中插入合理的静音，以保证同步性。


- 

优化音色匹配：

- 

采用**TTS（文本转语音）**生成翻译语音，匹配原说话人音色，提高翻译后的语音相似度。





2️⃣ 训练步骤

1. 

文本预训练：

- 

在多语言数据（Common Crawl、Wikipedia 等）上训练 Transformer 进行文本预测。


2. 

音频预训练：

- 

使用单语言语音数据训练模型，使其能处理语音输入。


3. 

语音翻译训练：

- 

采用40,000+ 小时的法语-英语语音数据，训练流式语音翻译模型。


4. 

微调（Fine-Tuning）：

- 

在900 小时高质量合成数据上微调，提高翻译的自然度和语音相似度。


5. 

Hibiki-M 轻量化：

- 

训练一个较小版本的模型，可以在智能手机上本地运行。






![image]()


---



🔬 关键技术



1️⃣ 上下文对齐（Contextual Alignment）


- 

问题：传统的翻译模型可能会提前生成错误翻译，或者翻译延迟过大。

- 

解决方案：

- 

使用文本翻译模型（MADLAD）计算翻译不确定性，选择最佳的翻译时机。

- 

通过插入静音或TTS 重新合成来优化同步性。




2️⃣ 语音编码（Neural Audio Codec）


- 

采用 Mimi 编码器（一种神经音频编解码器）将语音转换成低帧率的离散 tokens，再进行翻译。



3️⃣ 语音传输优化（Voice Transfer）


- 

训练过程中：

- 

通过条件训练（Conditional Training），引导模型学习音色相似度。

- 

采用Classifier-Free Guidance 调节音色，使翻译后语音更加接近原说话人。




---



📊 结果分析



Hibiki 在 CVSS 基准测试和新长文本翻译评测中表现优越：

- 

自动评测（BLEU 分数）表明其翻译质量优于现有模型。

- 

人工评测（翻译质量、自然度、说话人相似度）显示其接近人类口译员的水平。



Hibiki 在法语 → 英语的流式语音翻译任务中，超越了以往最先进的模型，包括：
1. 

翻译质量（Translation Quality）：

- 

ASR-BLEU 分数：Hibiki 达到 38.2，优于 StreamSpeech (26.4) 和 Seamless (37.0)。


2. 

音色相似度（Speaker Similarity）：

- 

Hibiki：0.41，显著高于 Seamless (0.30)。


3. 

自然度（Naturalness）：

- 

Hibiki 得分接近人类专业口译员，优于 Seamless。


4. 

推理速度（Inference Speed）：

- 

支持批量翻译（batching），可以在 GPU 上同时处理 100+ 句子，比 Seamless 和 StreamSpeech 更高效。

- 

Hibiki-M 轻量版可以在 iPhone 16 Pro 上实时运行，适用于移动端应用。






![image]()


GitHub：https://github.com/kyutai-labs/hibiki


论文：https://arxiv.org/pdf/2502.03382


模型：https://huggingface.co/kyutai

案例演示：https://huggingface.co/spaces/kyutai/hibiki-samples

---

*来源：[Hibiki ：一个实时语音翻译系统 无需等到你说完整句话 边说话的同时边翻译 还能保留原说话人的音色](https://www.xiaohu.ai/p/hibiki/18425228)*
