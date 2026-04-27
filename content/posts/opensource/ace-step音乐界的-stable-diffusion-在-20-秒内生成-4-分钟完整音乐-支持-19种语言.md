---
title: "ACE-Step：音乐界的 Stable Diffusion 在 20 秒内生成 4 分钟完整音乐 支持 19种语言"
date: 2025-05-06T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "ACE-Step 是一个面向音乐生成的“基础模型”（foundation model）项目。由 ACE Studio 与 StepFun 联合开发。  它的目标不是简单生成一首歌曲，而是提供一个通用、可扩展、可控的音乐生成系统架构，可广泛应用于创作、编曲、歌词生成、人声模拟、伴奏生成、说唱AI等领域"
source_url: "https://www.xiaohu.ai/p/ace-step-stable-diffusion-20-4-19/21237909"
xiahuid: "21237909"
---

## 📰 正文

ACE-Step 是一个面向音乐生成的“基础模型”（foundation model）项目。由 ACE Studio 与 StepFun 联合开发。

它的目标不是简单生成一首歌曲，而是提供一个通用、可扩展、可控的音乐生成系统架构，可广泛应用于创作、编曲、歌词生成、人声模拟、伴奏生成、说唱AI等领域。


通俗说，它试图成为“音乐界的Stable Diffusion”——即音乐版本的通用生成平台。


它可以：

- 

读歌词 → 写旋律、唱出来；

- 

读风格标签 → 自动编曲、生成伴奏；

- 

修改已有歌曲的一小段歌词，而不影响旋律；

- 

生成带风格的说唱、电子乐、人声、配器等；

- 

模拟你“输入一句歌词，它帮你快速写歌”的流程。



📌 性能如何：在 A100 GPU 上，ACE-Step 可在 20 秒内生成 4 分钟音乐，比主流模型快 15 倍以上。


✅ 与现有方法对比：

![image]()


ACE-Step 的核心创新是混合多种技术，解决这三者之间的矛盾：

- 

使用 扩散模型（diffusion） + 压缩自编码器（DCAE） 快速合成音乐；

- 

用 轻量 Transformer 模块提高结构连贯性；

- 

融合 语义对齐模型 MERT 和 m-Hubert，使模型对“歌词与旋律”之间的关系理解更精准；

- 

最终支持包括歌词修改、局部重绘、声音变化等在内的精细控制。



技术核心


![image]()


ACE-Step 采用混合架构设计：

- 

🔄 扩散生成器（Diffusion）：保证高质量音频输出

- 

🧱 深度压缩自编码器（DCAE）：降低生成维度、加快速度

- 

⚡ 线性 Transformer：捕捉长程结构，提升音乐连贯性

- 

🧬 语义对齐模块（MERT + m-Hubert）：用于训练中对歌词/语义信息的对齐，生成结构更清晰



🎯 性能亮点：

- 

在 A100 GPU 上 20 秒生成 4 分钟音乐，比传统方法快 15 倍以上；

- 

在旋律、节奏、歌词结构方面保持更强的一致性。



主要功能与特色


![image]()

![image]()


🎶 核心能力：多模态、结构化、高质量音乐生成
1. 

文本 → 音乐（Text-to-Music）
输入短语、描述、歌词，自动生成风格一致的音乐段落。

2. 

歌词 → 人声（Lyric-to-Vocal）
输入歌词，生成完整“AI唱歌”的人声输出，支持多语言、风格变化。

3. 

说唱生成（RapMachine）（即将发布）
模拟说唱演绎，支持 AI freestyle、节奏对齐。

4. 

人声 → 伴奏（Singing-to-Accompaniment）
给定一段清唱音频，自动匹配并生成合适的伴奏音乐。

5. 

乐器Stem生成（StemGen）
针对指定乐器（如鼓、吉他、钢琴），生成与已有音轨协同的独立音轨。

6. 





🧩 可控性与创作工具：

- 

🎚 变体生成：通过噪声调整生成多样版本

- 

🎨 局部重构（repainting）：可只修改一段旋律或歌词

- 

✏ 歌词编辑（flow-edit）：精准修改局部歌词，不影响旋律

- 

🎛 音轨再组合：支持 remix、伴奏反推（singing2accompaniment）等功能



🌐支持的语言与风格

- 

✅ 支持 19种语言（其中英语、中文、日语、韩语、法语等表现最佳）；

- 

✅ 支持 多风格：流行、民谣、爵士、电子、古典、摇滚等；

- 

✅ 支持多种描述输入方式：简短标签、句子、故事性文本、使用场景等。



典型应用模块（LoRA 支持）


![image]()


性能实测（生成速度）


![image]()


说明：RTF越高，生成越快（例如27.27x意为1分钟音乐生成仅耗2.2秒）。


项目地址及更多演示：https://ace-step.github.io/ 


GitHub：https://github.com/ace-step/ACE-Step 


在线演示：https://huggingface.co/spaces/ACE-Step/ACE-Step

---

*来源：[ACE-Step：音乐界的 Stable Diffusion 在 20 秒内生成 4 分钟完整音乐 支持 19种语言](https://www.xiaohu.ai/p/ace-step-stable-diffusion-20-4-19/21237909)*
