---
title: "R1-Omni：多模态情感识别模型  可以精准识别和分析视频中人类情感 并能解释其识别推理过程"
date: 2025-03-14T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "R1-Omni 是什么？    R1-Omni 是一种全模态（Omni-Multimodal）的大语言模型（LLM），专注于情感识别任务，能够从 视频、音频、文本 中综合分析人物的情感状态。   由阿里巴巴通义实验室开发。   这是首个结合视觉（视频）和音频信息，将强化学习（RL）和可验证奖励机制（"
source_url: "https://www.xiaohu.ai/p/r1-omni/19537451"
xiahuid: "19537451"
---

## 📰 正文

R1-Omni 是什么？



R1-Omni 是一种全模态（Omni-Multimodal）的大语言模型（LLM），专注于情感识别任务，能够从 视频、音频、文本 中综合分析人物的情感状态。


由阿里巴巴通义实验室开发。


这是首个结合视觉（视频）和音频信息，将强化学习（RL）和可验证奖励机制（RLVR）应用到多模态情感识别中的模型，显著提升了推理能力、情感识别准确性和泛化能力。


📌 简单来说：

如果你给 R1-Omni 一段电影片段或某人的讲话视频，它可以分析人物的表情、动作、语气、语音，然后告诉你这个人可能的情绪，还能解释它是如何得出这个结论的。

核心技术
1. 

强化学习与可验证奖励（RLVR）：不同于传统监督微调（SFT），RLVR 通过可验证的奖励机制优化情感识别任务。

2. 

全模态信息处理：融合视频帧和音频流，提升情感识别的全面性。

3. 

群体相对策略优化（GRPO）：优化强化学习过程中对高质量输出的筛选，提升训练效率和模型稳定性。



---



R1-Omni 解决了什么问题？



1. 现有情感识别的痛点


目前的情感识别技术主要依赖单一模态（如纯文本或图像），或采用传统**监督学习（SFT）**的方法，但它们有以下问题：

- 

❌ 无法结合多种信息：很多模型只能分析文本或静态图像，但真实情感表达往往是多模态的（表情+声音+动作）。

- 

❌ 推理能力弱，像黑箱：传统 AI 只是预测情感，但无法解释为什么得出这个情绪，导致决策不透明。

- 

❌ 泛化能力差：在陌生的环境（如不同风格的视频）中表现不佳，容易受到数据集限制，无法适应新场景。



2. R1-Omni 如何解决？


✅ 结合多种信息源，提高情感识别准确率

- 

传统模型可能只看脸部表情，但 R1-Omni 还会结合语气、语调、对话，让判断更加精准。



✅ 强化学习让模型变得更聪明，推理更强

- 

采用RLVR（强化学习+可验证奖励），不仅让模型学会正确识别情感，还让它学会解释自己的判断，避免“黑箱”问题。



✅ 适应不同环境，泛化能力更强

- 

训练时不仅使用了电影片段，还用了演员配音数据，让它能识别更复杂的情绪，适应不同风格的视频内容。



3. 效果如何

- 

情感识别能力提升：比 SFT 模型在情感识别准确性上提高了 5-10%。

- 

推理能力增强：模型可以清楚地解释视觉和音频在情感推理中的作用，避免“黑箱”问题。

- 

泛化能力提升：在分布外（OOD）数据上的表现更稳定，如 RAVDESS 数据集上的 UAR 提高了 14%。



---



R1-Omni 的主要功能



1. 识别视频中人物的情绪


📌 输入：一段带声音的视频
📌 输出：

- 

该人物的情绪（如愤怒 Angry、快乐 Happy、悲伤 Sad）

- 

详细的推理过程，说明它是如何判断的



🛠 示例： 如果给 R1-Omni 一个电影片段，人物的脸上带着怒容，声音语气强硬。


它可能会输出：


```None
User: As an emotional recognition expert; throughout the video, which emotion conveyed by the characters is the most obvious to you?  Output the thinking process in <think> </think> and final emotion in <answer> </answer> tags.

R1-Omni: <think>In the video, a man in a brown jacket stands in front of a vibrant mural. He is wearing a pink shirt underneath his brown jacket, and his hair is dark and curly. His facial expression is complex, with wide eyes, slightly open mouth, raised eyebrows, and furrowed brows, revealing surprise and anger. Speech recognition technology suggests that his voice contains words like "you", "lower your voice", "freaking out", indicating strong emotions and agitation. Overall, he displays an emotional state of confusion, anger, and excitement.</think>

<answer>angry</answer>

GT:angry

 用户：作为一名情感识别专家，在整个视频中，你认为角色最明显传达的情感是什么？请在<think> </think>标签中输出思考过程，并在<answer> </answer>标签中输出最终情感。

R1-Omni：

<think>在视频中，一个穿棕色夹克的男人站在一幅色彩鲜艳的壁画前。他在棕色夹克下穿着一件粉色衬衫，头发是深色卷发。他的面部表情很复杂，睁大的眼睛、微张的嘴、扬起的眉毛和皱起的眉头，显示出惊讶和愤怒。语音识别技术表明，他的声音包含“你”、“降低你的声音”、“吓坏了”等词语，表明他情绪激动且强烈。总体来看，他表现出困惑、愤怒和兴奋的情绪状态。</think>

<answer>愤怒</answer>

GT：愤怒
```



💡 区别于普通 AI：普通 AI 可能只会告诉你“愤怒（angry）”，但 R1-Omni 会告诉你它是如何得出这个结论的。


2. 解释性推理

普通的情感识别模型只是告诉你答案，但 R1-Omni 采用 RLVR 强化模型的推理能力，使其能够详细解释如何得出情感判断。

它会详细解释它的思考过程，就像一个人类专家一样。


```None
R1-Omni: 

<think>In the video, in the opening scene, we see a woman with her eyes slightly closed and mouth slowly opening as if she is laughing. Her facial expression appears somewhat joyful, which may indicate that she is experiencing some pleasant or amusing situation at that moment. In the audio, there are no pauses between sentences, they flow continuously, and the tone is light and cheerful. Combined with the text content, it can be felt that the character is in a very happy and positive emotional state. In the text, the subtitle reads: "It was interesting." This sentence may express the woman's satisfaction and curiosity towards something or someone. Based on the laughter and joyful emotion displayed by the woman in the video clues, as well as the description of continuous flowing, light and cheerful tone in the audio clues, we can infer that this sentence expresses the woman's interest and curiosity towards something. The joy in this sentence aligns with the overall display of happiness and positivity.</think>

<answer>happy</answer>

GT:happy

R1-Omni：

<think>在视频的开场场景中，我们看到一个女人眼睛微微闭合，嘴巴慢慢张开，好像在笑。她的面部表情显得有些愉悦，这可能表明她当时正经历一些愉快或有趣的情况。在音频中，句子之间没有停顿，语流连贯，语气轻松欢快。结合文本内容，可以感觉到角色处于一种非常快乐和积极的情绪状态。文本中的字幕显示：“它很有趣。”这句话可能表达了女人对某事或某人的满意和好奇。根据视频线索中女人展现的笑声和快乐情绪，以及音频线索中描述的连贯流动、轻松欢快的语气，我们可以推断这句话表达了女人对某事物的兴趣和好奇。这句话中的愉悦与整体表现出的快乐和积极情绪一致。</think>

<answer>快乐</answer>

GT：快乐
```


- 

🔍 对比示例：

![image]()



3. 适用于不同类型的视频


R1-Omni 在多个数据集上进行了训练，能适应不同风格的视频，包括：

- 

🎬 电影/电视剧（例如分析电影角色的情感）

- 

🎤 访谈/新闻（例如判断新闻主播的真实情绪）

- 

🏫 教育视频（例如分析学生的学习情绪）

- 

🎮 游戏直播（例如分析主播的情绪变化）

- 

🏥 心理健康分析（例如分析患者语音情绪波动）


- 

训练数据：

- 

MAFW、DFEW（电影场景）

- 

RAVDESS（专业演员表演情绪）


- 

可用于电影、社交媒体、教育、心理健康等领域的情感分析任务。



---



实验结果



R1-Omni 与其他方法的对比如下：

![image]()


🔍 实验结论：
1. 

准确率提升：R1-Omni 在 DFEW 和 MAFW 数据集上 的 WAR 和 UAR 均优于传统 SFT 模型（提升 5%～10%）。

2. 

泛化能力增强：在RAVDESS 数据集（未训练过的 OOD 数据）上，R1-Omni 的 WAR 提升了 13.67%，UAR 提升了 13.94%，展现了更强的适应能力。

3. 

RLVR 比 SFT 更有效：RLVR 训练的模型比单纯的监督微调（SFT）方法表现更优。



研究团队还对不同模型在情绪识别任务中的推理过程进行了对比：

![image]()


📌 为什么 R1-Omni 更强？

- 

传统模型 仅关注面部表情，可能错误识别为“fear”。

- 

R1-Omni 结合视频和音频，正确理解了语气中的愤怒情绪，推理更加精准。



泛化能力测试


在陌生数据（RAVDESS）上的表现

- 

传统模型在新数据上的 UAR 仅 30.75%，R1-Omni 提升至 44.69%，说明它能适应不同场景的情感分析任务。

- 

例如，在陌生的视频中：

- 

普通模型 可能会误判一个激动的角色为“高兴”。

- 

R1-Omni 能结合音频中的愤怒语气，正确分类为“生气”。




尽管 R1-Omni 已在实验中表现优越，但研究团队也发现了一些可优化的点：
1. 

字幕识别不够精准：如果视频字幕有错误，可能影响模型的情感推理。

2. 

部分推理存在幻觉（Hallucination）：在某些案例中，模型可能会生成与实际内容不符的推理。

3. 

音频信号利用不足：在某些情况下，音频特征的贡献低于视觉特征，需要进一步优化音频理解能力。



---



GitHub：https://github.com/HumanMLLM/R1-Omni


论文：https://arxiv.org/pdf/2503.05379


模型：https://huggingface.co/StarJiaxing/R1-Omni-0.5B

---

*来源：[R1-Omni：多模态情感识别模型  可以精准识别和分析视频中人类情感 并能解释其识别推理过程](https://www.xiaohu.ai/p/r1-omni/19537451)*
