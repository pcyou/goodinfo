---
title: "Spark-TTS：基于Qwen2.5模型的高效文本转语音（TTS）系统 支持细粒度语音控制"
date: 2025-03-06T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Spark-TTS：一种基于大语言模型（Qwen2.5）的高效文本转语音（TTS）系统 ，针对当前 TTS 领域的效率问题，提出了一种新的 BiCodec 语音编码方法，使得语音合成更加自然，可控，并支持零样本语音克隆。   ✅ 采用 BiCodec 编码，简化架构，提升推理效率。   ✅ 支持细粒"
source_url: "https://www.xiaohu.ai/p/spark-tts-qwen2-5-tts/19260022"
xiahuid: "19260022"
---

## 📰 正文

Spark-TTS：一种基于大语言模型（Qwen2.5）的高效文本转语音（TTS）系统 ，针对当前 TTS 领域的效率问题，提出了一种新的 BiCodec 语音编码方法，使得语音合成更加自然，可控，并支持零样本语音克隆。


✅ 采用 BiCodec 编码，简化架构，提升推理效率。


✅ 支持细粒度语音控制（性别、音调、语速等），远超传统 TTS。


✅ 领先的零样本语音克隆（Zero-Shot TTS），能生成高质量个性化声音。


✅ 在多个基准测试上超越现有 TTS 方法，并结合 Qwen2.5 LLM 进行端到端生成。


---



Spark-TTS 解决了什么问题？



❌ 传统 TTS 系统的痛点


1. 复杂的多阶段架构：


• 现有的 TTS 方法通常需要多个步骤（文本编码、声学模型、音频合成等），效率低下，难以集成到 LLM 生态中。


2. 代码本（Codebook）预测困难：


• 许多 TTS 系统依赖于 多流（multi-stream）代码预测，需要多个模型协作，导致推理复杂度增加。


3. 语音属性控制有限：


• 传统的 TTS 方法难以做到精准控制语音特征（如音高、语速、音色），多数只能基于参考音频进行模拟。


---



🚀 Spark-TTS 的创新点


![image]()
1. 

💡 BiCodec：全新单流语音编码器

- 

BiCodec 结合了两种不同类型的语音编码（tokens）：

- 

语义 tokens（Semantic Tokens）：低比特率（low-bitrate），用于捕捉语言内容。

- 

全局 tokens（Global Tokens）：固定长度，用于捕捉说话人属性（如音色、性别、音调）。


- 

这样能够同时保留语音内容和语音特性，同时降低计算复杂度，使得 LLM 可以直接进行 TTS 任务。

![image]()

![image]()

![image]()


2. 

⚡ 更快、更高效

- 

采用单流（single-stream）语音编码方式，相比于传统的双生成模型（dual-generative model）方法，推理更快。

- 

与 Qwen2.5 语言模型集成，使 TTS 任务可以直接由 LLM 处理，无需额外的声学模型。


3. 

🎛️ 强大的语音可控性

- 

Spark-TTS 支持两种层次的语音控制：

- 

粗粒度控制（Coarse-grained）：如性别、说话风格、情感等。

- 

细粒度控制（Fine-grained）：可以精准调整**音高（Pitch）、语速（Speaking Rate）**等参数。


- 

允许用户通过文本描述语音风格，甚至能生成全新的虚拟声音，突破传统 TTS 只能基于参考音频合成的限制。


4. 

🎙️ 领先的零样本语音克隆（Zero-Shot Voice Cloning）

- 

Spark-TTS 结合 Qwen2.5 语言模型和 BiCodec，在无需目标声音样本的情况下就能生成高质量的个性化语音。

- 

在**音色一致性（speaker similarity）**方面表现优异，可用于配音、语音助手、虚拟人物等应用。

![image]()


5. 

📚 VoxBox：新开源数据集

- 

还收集了一个新的 10 万小时语音数据集 VoxBox，其中每个音频样本都带有详细的语音属性标注（性别、音高、语速等）。

- 

该数据集为后续可控 TTS 研究提供了标准化的基准测试。




---



主要功能



🚀 1. 高效语音合成

- 

采用 BiCodec 语音编码，使 TTS 任务可以直接由 LLM 处理，无需额外的声学模型。

- 

语音合成流程更短，推理速度更快，比传统 TTS 方案更高效。



✅ 优势

- 

无需多阶段处理（如声学模型、声码器），减少计算开销。

- 

整合 Qwen2.5 LLM，让语音生成更自然流畅。



---



🎙️ 2. 零样本语音克隆（Zero-Shot Voice Cloning）

- 

无需额外训练，可以仅凭文本生成个性化声音。

- 

可以模仿指定说话人的音色，实现个性化语音合成。



---



🎛️ 3. 可控语音生成


Spark-TTS 提供 细粒度语音控制，可以通过参数精准调整语音特性：

![image]()


✅ 优势

- 

高度可控，能生成带有指定语音特征的音频。

- 

适用于个性化 TTS 应用，如 AI 朗读、播客、智能语音助手等。



---



🌍 4. 多语言 & 代码切换

- 

支持 中英文双语 语音合成。

- 

能够自然切换不同语言，不需要单独训练模型。



---



📊 5. 领先的语音合成质量

- 

通过基准测试 STOI、PESQ、MOS 评分 评估：

- 

语音自然度（MOS 评分**> 4.5**）。

- 

语音重建质量 超越现有 TTS 模型。


- 

采用 BiCodec 语音编码，在低比特率下仍能保持高音质。



---



🔬 主要实验结果

1. 

语音重建（Speech Reconstruction）

- 

Spark-TTS 的 BiCodec 编码方式 在 语音质量（STOI、PESQ、SIM 等指标） 上超越了其他主流 TTS 系统。

- 

比现有低比特率（sub-1kbps）编码方法效果更好，在保持高音质的同时减少计算资源需求。


2. 

语音控制（Speech Control）

- 

Spark-TTS 能精确控制音高、语速，在定量实验中证明了其比其他 TTS 方法更稳定、准确。

- 

对比 VoxInstruct 和 Parler-TTS，Spark-TTS 的语音性别控制准确率高达 99.77%（比其他方法更高）。


3. 

零样本语音克隆（Zero-Shot TTS）

- 

在 Seed-TTS 评测集 上，Spark-TTS 在中英文语音合成的字符错误率（CER）和语音相似性（SIM）指标上排名前列。

- 

与 LLaMA-8B 训练的 Llasa-TTS 相比，Spark-TTS 在更少的参数（0.5B vs 8B）和更少训练数据（10 万小时 vs 25 万小时）情况下仍表现更优。




项目及演示：https://sparkaudio.github.io/spark-tts/


GitHub：https://github.com/SparkAudio/Spark-TTS


论文：https://arxiv.org/pdf/2503.01710

---

*来源：[Spark-TTS：基于Qwen2.5模型的高效文本转语音（TTS）系统 支持细粒度语音控制](https://www.xiaohu.ai/p/spark-tts-qwen2-5-tts/19260022)*
