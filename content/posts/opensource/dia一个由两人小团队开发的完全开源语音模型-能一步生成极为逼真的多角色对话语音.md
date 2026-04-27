---
title: "Dia：一个由两人小团队开发的完全开源语音模型 能“一步生成”极为逼真的多角色对话语音"
date: 2025-04-23T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Dia 是由 Nari Labs 开发的一个超写实对话级文本转语音（TTS）模型，参数量为 16 亿，能够“一步生成”极为逼真的多角色对话语音。  -   可以生成极度逼真的对话并完全控制脚本和声音  -   由一个无资金的两人小团队开发  -   项目完全开源，采用 Apache 2.0 协议，权"
source_url: "https://www.xiaohu.ai/p/dia/20868460"
xiahuid: "20868460"
---

## 📰 正文

Dia 是由 Nari Labs 开发的一个超写实对话级文本转语音（TTS）模型，参数量为 16 亿，能够“一步生成”极为逼真的多角色对话语音。

- 

可以生成极度逼真的对话并完全控制脚本和声音

- 

由一个无资金的两人小团队开发

- 

项目完全开源，采用 Apache 2.0 协议，权重和推理代码公开，便于研究和二次开发。


![image]()


核心功能


- 

高保真文本转对话语音：能直接根据对话文本生成自然、有情感的多说话人语音。

- 

情感与语调可控：可用音频条件（prompt）进行控制，实现情感、语调的定制。

- 

非语言动作生成：支持如（笑声）、（咳嗽）、（叹气）等非言语声音的合成。

- 

语音克隆：可通过音频prompt实现声音克隆（voice cloning）。

- 

一键推理体验：支持 Gradio UI、本地命令行、Python API 直接调用。



性能对比



Input script  输入脚本

> 

[S1] Dia is an open weights text to dialogue model.  


[S2] You get full control over scripts and voices.  


[S1] Wow. Amazing. (laughs) 


 [S2] Try it now on Git hub or Hugging Face.



Dia-1.6B (ours)


ElevenLabs Studio


Sesame CSM-1B


Input script 

> 

[S1] Hey. how are you doing?  


[S2] Pretty good. Pretty good. What about you? 


[S1] I'm great. So happy to be speaking to you.  


[S2] Me too. This is some cool stuff. Huh?  


[S1] Yeah. I have been reading more about speech generation. 


[S2] Yeah. 


[S1] And it really seems like context is important. 


[S2] Definitely.



Dia-1.6B (ours)  


Sesame Website Example


Sesame CSM-1B


ElevenLabs Studio


架构设计与技术亮点


- 

单步对话生成：一次性生成完整对话（支持多说话人，如[S1]、[S2]标签）。

- 

非语言标签支持：支持丰富的非语言动作标签，增强真实感。

- 

硬件支持与推理效率：

- 

推荐在 GPU 上运行，支持 Pytorch 2.0+，CUDA 12.6。

- 

在企业级 GPU（如A4000）可实现近实时语音生成。

- 

后续会支持 CPU、模型量化、Docker 等。


- 

数据与工程实践：借鉴 SoundStorm、Parakeet、Descript Audio Codec 等前沿技术。

- 

可扩展性：未来计划优化推理速度、降低显存占用、支持更广泛硬件。



应用场景


- 

AI 对话助手、语音机器人

- 

数字人、虚拟主播

- 

影视动画配音、多角色游戏语音

- 

内容创作与 remix

- 

语音交互体验、辅助沟通等



使用与开发


- 

支持 pip 安装与 Gradio Web 界面体验。

- 

可直接作为 Python 库调用或本地 CLI 工具。

- 

支持在 HuggingFace 上云端体验，无需本地部署。

- 

社区活跃，持续优化升级。



GitHub：https://github.com/nari-labs/dia/ 


Hugging Face：https://huggingface.co/nari-labs/Dia-1.6B


更多演示：https://yummy-fir-7a4.notion.site/dia

---

*来源：[Dia：一个由两人小团队开发的完全开源语音模型 能“一步生成”极为逼真的多角色对话语音](https://www.xiaohu.ai/p/dia/20868460)*
