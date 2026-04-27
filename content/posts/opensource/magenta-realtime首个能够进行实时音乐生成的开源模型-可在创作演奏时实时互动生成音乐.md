---
title: "Magenta RealTime：首个能够进行实时音乐生成的开源模型 可在创作、演奏时实时互动生成音乐"
date: 2025-08-09T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Magenta RealTime（Magenta RT）是 Google Magenta 项目推出的开源权重实时音乐生成模型，可让用户在创作、演奏时实时互动生成音乐。  它是 Lyria RealTime（驱动 MusicFX DJ 模式与 Google AI Studio 实时音乐 API）的“开"
source_url: "https://www.xiaohu.ai/p/magenta-realtime/23965188"
xiahuid: "23965188"
---

## 📰 正文

Magenta RealTime（Magenta RT）是 Google Magenta 项目推出的开源权重实时音乐生成模型，可让用户在创作、演奏时实时互动生成音乐。

它是 Lyria RealTime（驱动 MusicFX DJ 模式与 Google AI Studio 实时音乐 API）的“开放版”，更偏向研究人员、艺术家和创意开发者，可以本地运行（目前可在 Colab 免费 TPU 上试用）。


它一个实时 AI 音乐生成器。

想象一下：

- 

你在现场表演时，不是播固定的音乐，而是让 AI 根据你的指令、节奏和风格“边想边演”。

- 

你说：“来点爵士”，它马上换成爵士；你加点电子节拍，它就变成爵士 + 电子混搭。

- 

你甚至可以用自己的音频样本去引导它。



它能：

- 

根据你给的文字（比如“funk”风格）和音频（比如一段鼓点）混合生成新音乐；

- 

实时输出高质量、无卡顿的音乐；

- 

在你的电脑或 Google Colab 上跑，不必依赖云端。



你告诉它：“来一段 80 年代 funk 风格的贝斯”，或者“混点我刚录的吉他 riff，再加点 heavy metal 的感觉”，它就能立刻给你生成高质量的音乐，而且能不停地接着演，像在现场 jam 一样。


它的特别之处是：

- 

实时性：音乐是边生成边播放，不需要等很久。

- 

可交互：你可以随时改变音乐风格、混入音频样本，AI 会立刻响应。

- 

开源可改：代码和模型权重都能获取，方便研究和个性化定制。

- 

高保真音质：生成 48kHz 立体声音乐，足够专业表演或制作使用。



它怎么做到“实时”的？



普通的 AI 音乐模型生成一整首曲子可能要好几分钟，但 Magenta RT 解决了三个大难题：
1. 

实时生成（Real-time factor > 1）

- 

每 2 秒的音乐，只要 1.25 秒就能生成出来。

- 

这样你一边操作，它一边播，不会卡。


2. 

分块生成（Block autoregression）

- 

它不是一次性做完，而是把音乐切成小块（chunk），一块一块地接着生成。

- 

每块音乐会参考上一块的内容和你的“风格指令”，这样音乐就连贯又能随时变风格。


3. 

低延迟控制（Low-latency control）

- 

你换风格的指令，最晚 2 秒后就能在音乐里听到变化。

![image]()




它能玩出什么花样？


- 

风格混搭：比如 50% 古典 + 50% 嘻哈，或者钢琴配鼓机。

- 

即兴探索：你调来调去，找出新奇的旋律、节奏和乐器组合。

- 

现场表演：像 DJ 一样，实时控制音乐流动。

- 

游戏/艺术装置背景音乐：根据场景变化，音乐自动适应氛围。



主要功能

1. 

实时音乐生成

- 

采用 2 秒一块的生成方式（Chunk-based generation），上下文长度 10 秒。

- 

边生成边播放，适合现场表演或即兴创作。

- 

用交叉淡化（crossfade）消除块与块之间的衔接痕迹。


2. 

多模态风格控制

- 

使用 MusicCoCa 模型，把文本和音频都转化为“风格向量”。

- 

可以混合多个风格并实时调整权重，比如：

> 
- 

70% Funk

- 

30% 你自己的吉他录音



- 

AI 会即时调整输出，音乐风格可平滑过渡。


3. 

高保真音频生成与压缩

- 

基于 SpectroStream（SoundStream 升级版）技术，生成 48kHz 立体声。

- 

内部通过“音频 token 化”压缩和解压，提高实时性能。


4. 

本地与云端运行

- 

官方提供 Colab 免费 TPU 演示（实时因子 1.6，即 2 秒音乐只需 1.25 秒生成）。

- 

未来将支持 GPU/CPU 本地运行，无需依赖云端。


5. 

可定制与微调（Finetuning）

- 

你可以用自己的音频数据训练个性化版本，让 AI 生成符合你风格的音乐。


6. 

交互式创作与探索

- 

可以在不同音乐风格的“潜在空间”里实时穿梭，发现新颖的音色组合。

- 

适合做互动音乐表演、艺术装置、游戏动态音效等。




控制方式



Magenta RT 有三种主要的实时控制手段：
1. 

文字 Prompt
输入描述音乐风格、情绪、速度等。

2. 

音频 Prompt
上传一段参考音乐，AI 会跟随其风格和音色生成。

3. 

混合控制
通过“风格嵌入加权”，把多个 Prompt 混合成新的风格。



---



应用案例



Magenta 团队基于 Lyria RealTime API 做了三个示例工具：

- 

PromptDJ：用文字即时切换音乐风格。

- 

PromptDJ MIDI：用 MIDI 控制音乐生成。

- 

PromptDJ Pad：用打击垫实时切换风格片段。



技术特点



模型简介

- 

Magenta RealTime (Magenta RT) 是一个开放权重的实时音乐生成模型，可实时交互式创作、控制和表演音乐。

- 

基于 Google DeepMind 的 Lyria RealTime 技术，但可本地运行（目前仅在 Colab TPU 免费版运行）。

- 

模型规模：8 亿参数的自回归 Transformer。

- 

训练数据：约 19 万小时的多源库存音乐（主要是器乐）。

1. 

块式自回归（Block Autoregression）

- 

改造自 MusicLM 架构

- 

每次生成 2 秒细粒度音频 token，条件依赖于之前的 10 秒粗粒度 token 和当前风格向量。


2. 

低延迟设计

- 

在 Colab TPU 上实时因子 1.6（生成速度快于播放速度）。

- 

可以缩短块时长进一步降低反应延迟（提高交互性）。


3. 

多模态嵌入（MusicCoCa）

- 

融合了 MuLan 和 CoCa 模型的思路，实现文本与音频共同的风格向量空间。

- 

允许任意比例混合不同来源的风格提示。


4. 

高保真音频编码（SpectroStream）

- 

比上一代 SoundStream 在音质和压缩率上都有提升。

- 

48kHz 立体声，专业制作水准。


5. 

上下文与风格控制

- 

上下文窗口：10 秒（用于保持旋律和节奏连续性）。

- 

风格控制是实时可调的，可以边演边改变音乐走向。




项目地址：https://magenta.withgoogle.com/magenta-realtime


GitHub：https://github.com/magenta/magenta-realtime 


论文：https://arxiv.org/abs/2508.04651


Demo：https://colab.research.google.com/github/magenta/magenta-realtime/blob/main/notebooks/Magenta_RT_Demo.ipynb

---

*来源：[Magenta RealTime：首个能够进行实时音乐生成的开源模型 可在创作、演奏时实时互动生成音乐](https://www.xiaohu.ai/p/magenta-realtime/23965188)*
