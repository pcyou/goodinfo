---
title: "StepFun AI 发布LLM 级别的音频编辑模型： Step-Audio-EditX 拥有 情绪、语气、风格、副语言特征编辑能力"
date: 2025-11-09T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "StepFun AI （阶跃科技）发布 Step-Audio-EditX 语音开源模型，这是世界上第一个 LLM 级别的音频编辑模型。  它不仅能合成语音，还能编辑声音的情绪、语气、风格，让生成的语音更自然、更有表现力。  -   一个 基于大语言模型（LLM）架构 的音频模型；  -   30亿参"
source_url: "https://www.xiaohu.ai/p/stepfun-ai-llm-step-audio-editx/26746177"
xiahuid: "26746177"
---

## 📰 正文

StepFun AI （阶跃科技）发布 Step-Audio-EditX 语音开源模型，这是世界上第一个 LLM 级别的音频编辑模型。

它不仅能合成语音，还能编辑声音的情绪、语气、风格，让生成的语音更自然、更有表现力。

- 

一个 基于大语言模型（LLM）架构 的音频模型；

- 

30亿参数（从130B压缩而来）

- 

拥有 情绪、语气、风格、副语言特征编辑能力；

- 

支持 零样本语音克隆与多轮可迭代编辑；



StepFun AI 表示，这个模型代表了一种全新的音频编辑范式：

> 

不再从波形信号处理音频，而是像语言模型一样，用离散 token 表示语音，可通过自然语言指令完成情感、风格、语速等多维度的音频修改。



背景与定位



在过去两年中，语音生成（Text-to-Speech, TTS）模型出现了明显的技术分化趋势：

- 

一类模型（如 VALL-E、CosyVoice）侧重语音“克隆”能力，即在零样本条件下复制特定音色和韵律。

- 

另一类模型（如 FireRedTTS、Seed-TTS）强调合成质量和多语言适配。



然而，现有模型普遍存在一个瓶颈：

> 

语音属性（情感、风格、语气、语速等）难以独立控制。



换言之，虽然模型能模仿某人的声音，但无法灵活调整“说话方式”或“情绪表达”。


StepFun 团队提出的 Step-Audio-EditX 正是针对这一限制的系统性解决方案。
这是首个基于大型语言模型（LLM）架构的、开源的、支持多轮情感与风格可编辑语音生成的系统。


主要功能



Step-Audio-EditX 有四大核心功能：


1. 零样本语音克隆（Zero-shot Voice Cloning）



只需几秒钟的语音样本，就能让模型模仿说话者的声音去朗读新内容。
无需再训练，立即生成。

- 

支持语言：普通话、英语、四川话、粤语；

- 

无需额外训练；

- 

能保持音色和语调的一致性。

- 

可通过标签切换方言（如 [Cantonese] 表示粤语）。



Prompt Audio


Output Audio


Prompt Audio


Output Audio


---



2. 情绪编辑（Emotion Editing）



可以改变声音的情绪表现，如：

- 

Happy（开心）

- 

Sad（悲伤）

- 

Angry（生气）

- 

Excited（激动）

- 

Fearful（害怕）

- 

Surprised（惊讶）



只需给出一个标签，AI 就能让声音表现出相应的情感色彩。


Source


Edit 1st


Edit 2nd


Edit 3rd


---



3. 说话风格调整（Speaking Style Editing）



可让声音呈现不同人物风格或语气特征，例如：

- 

Whisper（低语）

- 

Child（儿童）

- 

Older（年长）

- 

Serious（严肃）

- 

Gentle（温和）

- 

Exaggerated（夸张）



适合用于角色配音或虚拟人物语音生成。


Source


Edit 1st


Edit 2nd


Edit 3rd


---



4. 副语言特征控制（Paralinguistic Editing）



除了情绪和语气外，还能添加一些自然的人类声音特征：
如呼吸声、笑声、叹气、犹豫音、惊叹音等。


例如：

- 

[Laughter] 会让语音中带上笑声；

- 

[Breathing] 添加自然呼吸声；

- 

[Sigh] 加入轻微叹息。



这使生成的语音更接近真实人声。


Source  


Paralinguistic Text  副语言文本


你说的这个计划听起来不错，我觉得可以试试 [Confirmation-en]，说不定真能成功呢。


Edit Output  


5）Extension（扩展功能）



模型可无缝扩展至其他音频编辑任务：

![image]()


系统架构



Step-Audio-EditX 的核心设计理念是：

> 

“语音也可以“像文本一样被编辑”。”



统一LLM架构


Step-Audio-EditX 完全继承了文本大模型的对话式结构：

- 

所有语音任务都被封装为“系统提示 + 用户指令”的对话形式；

- 

无论是TTS、情感编辑还是语速调整，都可在统一框架下完成；

- 

通过token化的音频序列输入，模型学习在token层面执行“编辑指令”。



这种统一语义接口极大降低了任务切换成本，也为后续RLHF对齐提供了统一格式。


整个系统由三个主要部分组成：

![image]()


流程图：

![image]()


```None
输入：文本 + 参考语音 + 指令（如情绪/风格）
     ↓
Audio Tokenizer：提取声音特征
     ↓
Audio LLM：生成或编辑音频符号
     ↓
Decoder：输出最终语音

```



这种设计让模型能灵活地理解语音的“语义”和“情感”，在技术上实现了“语音级的大模型理解与控制”。


性能评估



根据 StepFun 团队在技术报告（arXiv:2511.03601）中披露的结果，
Step-Audio-EditX 在多项指标上超越了闭源商用模型 Minimax 与 Doubao：

![image]()


实验结果表明：

- 

其在自然度、情感表达、音色一致性方面已接近甚至超越闭源商用系统。

- 

情绪与风格控制能力达到业内领先水准。

- 

技术架构兼具可解释性与可扩展性，为多模态语音生成研究提供了坚实基础。


![image]()


兼容性与泛化能力



Step-Audio-EditX 还能改进其他闭源 TTS 系统的输出。
包括：

- 

GPT-4o mini TTS

- 

ElevenLabs v2

- 

Doubao Seed TTS 2.0

- 

MiniMax Speech 2.6 HD



结果显示，仅一次 Step-Audio-EditX 编辑迭代即可显著提升这些系统的情感与风格表达精度。


项目地址：https://stepaudiollm.github.io/step-audio-editx/


论文：https://arxiv.org/pdf/2511.03601 


GitHub：https://github.com/stepfun-ai/Step-Audio-EditX 


在线体验：https://huggingface.co/spaces/stepfun-ai/Step-Audio-EditX

---

*来源：[StepFun AI 发布LLM 级别的音频编辑模型： Step-Audio-EditX 拥有 情绪、语气、风格、副语言特征编辑能力](https://www.xiaohu.ai/p/stepfun-ai-llm-step-audio-editx/26746177)*
