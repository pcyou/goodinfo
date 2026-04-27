---
title: "小米开源多语言 TTS 模型 OmniVoice：0.8B 小模型，600+ 语言零样本语音克隆"
date: 2026-04-04T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "语音克隆领域又冒出一个狠角色。   OmniVoice 是一个开源的零样本多语言 TTS 模型，来自小米 k2-fsa 团队。  -   0.8B 参数的小模型  -   支持 600 多种语言的语音克隆  -   推理速度是实时的 40 倍  -   训练数据和过程全部公开    646 种语言、"
source_url: "https://www.xiaohu.ai/p/tts-omnivoice-0-8b-600/31350912"
xiahuid: "31350912"
---

## 📰 正文

语音克隆领域又冒出一个狠角色。


OmniVoice 是一个开源的零样本多语言 TTS 模型，来自小米 k2-fsa 团队。

- 

0.8B 参数的小模型

- 

支持 600 多种语言的语音克隆

- 

推理速度是实时的 40 倍

- 

训练数据和过程全部公开



646 种语言、58.1 万小时训练数据，官方声称是目前语言覆盖最广的开源 TTS 项目。中文、英文、日文、阿拉伯文、斯瓦希里语、卢奥语……Demo 页面列了 102 种语言的对比样本，基本是目前同类开源项目里没见过的量级。


几个细节让人印象挺深的：耳语和 ASMR 效果做得相当好，零样本克隆在方言和多语言场景下也很稳。


三个核心能力



① 语音克隆：给一段参考音频就行



零样本语音克隆，不需要微调，不需要训练数据。给模型一段参考音频，它就能用这个声音说任何内容。

> 

你录一段 10 秒的语音，模型就能用你的声音生成任意文本的朗读。方言、口音、语调特征都能保留。



适用场景：有声书、虚拟主播、配音本地化，任何需要复刻特定声音的情况。


② 语音设计：用文字控制声音特征



除了克隆已有声音，OmniVoice 还支持"语音设计"模式：通过文字描述来定义声音的特征。


你可以指定性别、年龄、音高、方言/口音，甚至是耳语模式。不需要参考音频，直接用属性组合出你想要的声音。


同类别只能选一个，不同类别可以自由组合。比如 "male, elderly, low pitch, British accent" 这样的描述直接出音频。模型自动识别 instruct 语种，中英混写也行。


这对需要批量生成不同角色声音的场景很实用，比如有声书、游戏配音。

![image]()


③ 推理速度：RTF 0.025



推理速度 RTF 0.025，生成 40 秒音频只需约 1 秒，比实时快 40 倍。论文在 H20 GPU 上测试，16 步推理 batch size 1 的情况下 RTF 为 0.0319，同配置下比 ZipVoice（0.0557）更快。


对比一下：大部分同类模型的 RTF 在 0.1 到 0.5 之间，OmniVoice 快了一个量级。这个速度跑批量任务基本不用等。


底层架构是 Diffusion Language Model，这是一个比较新的方向，兼顾了生成质量和速度。


其它特性



副语言与发音精细控制



非语言表达标签


直接在合成文本里插入标签触发非语言音效：


python


```python
audio = model.generate(text="[laughter] You really got me. I didn't see that coming.")
```



目前支持的标签完整列表：[laughter]、[sigh]、[sniff]、[confirmation-en]、[question-en]、[question-ah/oh/ei/yi]、[surprise-ah/oh/wa/yo]、[dissatisfaction-hnn]，共 13 个。


发音纠错


中文用拼音带声调数字，可以纠正多音字：


python


```python
audio = model.generate(text="这批货物打ZHE2出售后他严重SHE2本了，再也经不起ZHE1腾了。")
```



英文用 CMU 音素词典（大写，括号内），覆盖默认发音之外的读法。


多说话人对话


用 [Speaker_N]: 标签分配不同说话人，一次性生成多人对话音频，每个 Speaker 可以指定不同的参考音频或声音设计属性。


---



跨语言克隆



用某种语言的参考音频，生成另一种语言的语音，声线特征保持一致。比如用中文录音做 prompt，生成日语输出，说话人特征不丢失。


---



噪声鲁棒性



参考音频质量不理想时（有背景噪音、录音条件差），模型仍能稳定提取声线特征。论文验证了 prompt denoising 的效果：开启后 UTMOS 从 4.23 提升至 4.32（合成语音更干净），声音相似度 SIM-o 略降（0.697 → 0.668），符合设计预期，模型生成的是干净版本，而不是复刻噪音。


架构：绕开两段式流水线



现有的离散 NAR TTS 模型普遍走「文本→语义 token→声学 token」的两段式路子，中间多一层语义编解码器，结构复杂、误差容易叠加。

![image]()


OmniVoice 直接把文本映射到多码本声学 token，省掉了语义层这一跳。能做到这一点，靠两个关键设计：


1. 全码本随机掩码（Full-Codebook Random Masking）


训练时对所有码本的 token 做随机 mask，让模型同时学多个码本的重建，效率和效果都比分阶段训练好。


2. 预训练 LLM 初始化


直接用预训练语言模型的权重初始化解码器，把语言模型积累的语言理解能力迁移进来，大幅提升合成语音的可懂度，在低资源语言上尤其明显。


整体是扩散语言模型（Diffusion Language Model）风格的非自回归架构，生成速度比自回归模型快，质量上对标当前 SOTA。


获取方式



在线试用： HuggingFace Space 有网页 demo，直接上传参考音频就能试。


本地部署：


```None
# 方式一：pip
pip install omnivoice

# 方式二：uv
uv pip install omnivoice
```



支持 NVIDIA GPU 和 Apple Silicon，两行命令就能跑。


Demo 页面： zhu-han.github.io/omnivoice 有预生成的音频样本可以试听。


已知局限


- 

0.8B 小模型在复杂场景下质量不如大模型，长文本朗读可能出现节奏问题

- 

600+ 语言覆盖广但质量参差不齐，主流语言效果好，小语种需自己测

- 

项目比较新（GitHub 仅 5 次 commit），还在快速迭代中，API 可能变动

- 

训练数据和过程公开，但论文中的具体训练细节需看 arXiv 原文



开源，Apache-2.0 许可证，可商用。GitHub 1.2k star。


👉 GitHub 仓库 | HuggingFace | arXiv 论文 | Demo

---

*来源：[小米开源多语言 TTS 模型 OmniVoice：0.8B 小模型，600+ 语言零样本语音克隆](https://www.xiaohu.ai/p/tts-omnivoice-0-8b-600/31350912)*
