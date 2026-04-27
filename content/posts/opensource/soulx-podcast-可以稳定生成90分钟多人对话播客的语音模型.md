---
title: "SoulX-Podcast ：可以稳定生成90分钟多人对话播客的语音模型"
date: 2025-10-29T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "SoulX-Podcast 是由 Soul AI Lab（Soul应用背后的AI实验室） 开发的 高保真播客生成推理框架，旨在从文本直接生成长篇、多说话人、对话式语音内容。   SoulX-Podcast ：  >   实现了高真实度、长时段、多说话人、多语种（中英双语 + 多方言）播客式语音生成，"
source_url: "https://www.xiaohu.ai/p/soulx-podcast-90/26412892"
xiahuid: "26412892"
---

## 📰 正文

SoulX-Podcast 是由 Soul AI Lab（Soul应用背后的AI实验室） 开发的 高保真播客生成推理框架，旨在从文本直接生成长篇、多说话人、对话式语音内容。


SoulX-Podcast ：

> 

实现了高真实度、长时段、多说话人、多语种（中英双语 + 多方言）播客式语音生成，具备方言与副语言（如笑声、叹气等）控制能力。


实验证明模型可连续生成 90 分钟以上 的对话内容而不失稳定性。



SoulX-Podcast 在传统 TTS（Text-to-Speech）基础上进行了扩展，能够：

- 

生成多说话人、多轮对话形式的语音内容；

- 

在语音中融入副语言特征（paralinguistic cues）；

- 

支持普通话、英语及多种中文方言；

- 

在零样本（zero-shot）条件下完成声音与语气的克隆与迁移。



主要功能



1. 多说话人长对话生成



系统可在无外部干预下，生成长达 90 分钟以上 的自然多轮对话。

- 

音色与说话风格在整段对话中保持稳定；

- 

不同角色语气和节奏自然衔接，无明显断层；

- 

语义层面具备“话题延展性”，可保持上下文关联。


> 

该成果在播客、访谈、虚拟角色对话等场景中具有高应用潜力。



---



2. 方言控制与切换能力



系统支持多种方言生成与实时切换，包括：

- 

粤语（Cantonese）

- 

四川话（Sichuanese）

- 

河南话（Henanese）



特点：

- 

方言转换后仍保持原说话人音色一致；

- 

能根据语境自动调整节奏与语调；

- 

在跨方言对话中实现平滑语音过渡。



示例对话显示，模型可生成两位主持人分别使用不同方言交流的播客片段，听感自然流畅。


---



3. 副语言控制（Paralinguistic Controls）



该模块允许文本中显式标注副语言符号，如：


```None
<|laughter|>, <|sigh|>, <|breathing|>, <|coughing|>

```



在生成语音中体现为自然的笑声、叹息声、呼吸声等。
其作用包括：

- 

提升语音表达的真实感与感染力；

- 

改善播客式语音的韵律变化与情绪丰富度；

- 

支持情境化生成（如“幽默场景”“紧张对话”）。



---



4. 长时播客生成（Long-form Generation）



模型在长达 60–90分钟 的播客生成中展示出以下特性：

- 

音色稳定，未出现“音质漂移”或“声色坍塌”；

- 

情感延续性强，能根据语义逻辑自然调整语气；

- 

语速与语调符合人类自然交流规律；

- 

听觉效果接近真实人声播客。



实验表明，该模型在 自然度（MOS） 与 连贯性（Coherence） 指标上均优于现有TTS系统。


---



SoulX-Podcast 模型结构


![image]()


该模型基于多说话人 TTS 框架扩展，具有以下特征：

![image]()


实验结果



在多项客观与主观评测中，SoulX-Podcast 均达到 SOTA（state-of-the-art）性能：

![image]()


此外，主观听感实验表明：

- 

92% 的听众认为生成音频“接近真人播客”；

- 

87% 的听众在盲测中无法区分AI生成与真实语音。



项目地址：https://soul-ailab.github.io/soulx-podcast/


GitHub：https://github.com/Soul-AILab/SoulX-Podcast


模型下载：https://huggingface.co/collections/Soul-AILab/soulx-podcast

---

*来源：[SoulX-Podcast ：可以稳定生成90分钟多人对话播客的语音模型](https://www.xiaohu.ai/p/soulx-podcast-90/26412892)*
