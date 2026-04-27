---
title: "Meta 推出「SAM Audio」：让声音也能“像图像一样被分割”的 AI 模型"
date: 2025-12-17T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "SAM Audio 是 Meta 最新发布的 通用声音分离 AI 模型。 它可以理解并“分割”复杂音频中的任意声音元素，比如：  -   🎸 一键提取歌曲中的吉他或人声；  -   🚗 过滤户外视频的交通噪音；  -   🐶 去除播客录音里的狗叫声。    这意味着 ——  >   “就像 Phot"
source_url: "https://www.xiaohu.ai/p/meta-sam-audio-ai/27860136"
xiahuid: "27860136"
---

## 📰 正文

SAM Audio 是 Meta 最新发布的 通用声音分离 AI 模型。
它可以理解并“分割”复杂音频中的任意声音元素，比如：

- 

🎸 一键提取歌曲中的吉他或人声；

- 

🚗 过滤户外视频的交通噪音；

- 

🐶 去除播客录音里的狗叫声。



这意味着 ——

> 

“就像 Photoshop 能抠图，SAM Audio 能‘抠声音’。”



想象你拍了一段街头视频，背景有：

> 

人声 + 车声 + 风声 + 狗叫声 + 音乐



现在，用 SAM Audio，只要告诉它：

> 

“只保留人说话的声音”，
或者点一下视频中说话的人，
AI 就能瞬间把那部分声音提取出来，干净到像魔法一样。✨



不需要专业混音知识，也不必安装复杂软件。
它能像图像“抠图”那样“抠声音”——
真正让音频剪辑“像文字和图片一样简单”。


SAM Audio 的三大技术创新



AM Audio 属于 Meta 的 Segment Anything 系列（SAM Collection）。
这个系列最初从 图像分割（SAM for images） 开始，允许用户在图像上点击或输入文字即可分离出任意物体。

![image]()


而现在，Meta 将这一“可分割一切”的理念扩展到音频领域。


SAM Audio 代表了该系列的 多模态延伸：

> 

视觉 + 听觉 + 文本 三种输入方式
→ 全面理解并操作多媒体内容。



Meta 表示，SAM Audio 是首个统一的多模态声音分割模型，支持三种“提示方式（prompting）”，使声音编辑更加直观、精准：

![image]()


可以组合使用，比如：

> 

“在 0:30–1:00 之间，提取女声。”



这些提示方式可以单独使用，也可以任意组合，让创作者能够精准控制音频分离的细节。

- 

Text prompting: Type “dog barking” or “singing voice” to extract specific sounds.
文本提示：输入"狗叫声"或"唱歌声"等文字来提取特定的声音。


Visual prompting: Click on the person or object in the video that’s making a sound to isolate their audio.
视觉提示：点击视频中发出声音的人或物体来隔离其音频。


Span prompting: An industry first, this method lets you mark time segments where target audio occurs.
跨度提示：这是行业首创的方法，让你可以标记目标音频出现的时间段。



核心技术架构



🧩 1. Perception Encoder Audiovisual (PE-AV) —— SAM Audio 的“大脑与耳朵”



PE-AV 是 SAM Audio 的核心引擎，
基于 Meta 早前开源的 Perception Encoder 模型拓展而来。


✳️ 功能：

- 

同时理解视觉帧与音频信号；

- 

建立“看见的画面”和“听到的声音”之间的时间对应；

- 

让模型在分离声音时知道“谁在发声、从哪里发出”。



🧠 比喻：

> 

PE-AV 就像 “耳朵 + 大脑”：它听见声音，同时看到是谁发出的声音。



🧪 技术细节：

- 

使用 多模态对比学习 (Multimodal Contrastive Learning)；

- 

训练数据规模：超过 1 亿条视频；

- 

核心组件：

- 

PyTorchVideo（高效视频处理）

- 

FAISS（语义检索）

- 

Transformer 主干网络


- 

输出：时间对齐的语义特征（time-aligned semantic features），用于多模态分离任务。

![image]()



---



🌀 2. 模型架构：基于生成式扩散变换器（Flow-Matching Diffusion Transformer）



SAM Audio 使用一种生成式框架：

- 

将音频混合信号 + 提示信息编码为共享表征；

- 

再通过扩散生成机制输出：

- 

🎯 目标音频轨（目标声源）；

- 

🌀 残余音轨（背景或剩余声音）。




此外，Meta 建立了一个庞大的数据引擎，
通过：

- 

自动合成音频混合数据；

- 

自动生成文本与时间提示；

- 

伪标签化（pseudo-labeling）；
来训练模型，以确保其在真实世界音频中具备强泛化能力。



应用场景与潜在影响



Meta 强调，SAM Audio 将改变音频与视频编辑的工作流程，适用范围极广：

![image]()


“以前的音频分离工具往往针对单一场景（如人声消除），
SAM Audio 是第一个像人一样思考声音结构的 AI 模型。”


如何体验与下载


- 

🧪 在线体验：可在 Segment Anything Playground 平台上试用；
用户可选择 Meta 提供的音频/视频素材，或上传自己的文件进行测试。

- 

💾 模型开放下载：SAM Audio 模型可供开发者和研究者自由下载使用。



Meta 表示：“SAM Audio 是目前为止我们认为最强的音频分离模型。”


详细介绍：https://ai.meta.com/blog/sam-audio/

---

*来源：[Meta 推出「SAM Audio」：让声音也能“像图像一样被分割”的 AI 模型](https://www.xiaohu.ai/p/meta-sam-audio-ai/27860136)*
