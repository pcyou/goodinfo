---
title: "Fish Audio 开源 S2：4B 参数的 TTS 模型，100ms 出声，还能让 AI 笑出来"
date: 2026-03-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Fish Audio 发布 S2，这是继 S1 之后的新一代旗舰 TTS 模型，在多项公开 benchmark 上，S2 的表现已全面超越 ElevenLabs、MiniMax Speech-02、Qwen3-TTS 等闭源竞品，拿下开源 + 闭源全榜最优 WER。   这次发布的 S2 是他们的新"
source_url: "https://www.xiaohu.ai/p/fish-audio-s2-4b-tts-100ms-ai/30528326"
xiahuid: "30528326"
---

## 📰 正文

Fish Audio 发布 S2，这是继 S1 之后的新一代旗舰 TTS 模型，在多项公开 benchmark 上，S2 的表现已全面超越 ElevenLabs、MiniMax Speech-02、Qwen3-TTS 等闭源竞品，拿下开源 + 闭源全榜最优 WER。


这次发布的 S2 是他们的新一代模型，核心卖点三个：开源、快、情感控制粒度细到离谱。


训练数据超过 1000 万小时音频，覆盖约 80+种语言，模型分为两个版本：S2（基础版）和 S2 Pro（旗舰版）。


S2 的模型权重、微调代码、推理引擎全部开源，研究和非商用免费，但是商用需要联系授权。


技术参数：几个数字感受一下



S2 用了一个叫 Dual-AR 的双层架构。上层 4B 参数负责语义理解，下层 400M 参数负责声学细节，加起来 44 亿参数。


训练数据量很猛：1000 万小时以上的音频，覆盖约 80 种语言。


实际跑起来的表现（在 NVIDIA H200 上测的）：

- 

首次出声延迟：约 100ms

- 

实时因子（RTF）：0.195，意思是生成 1 秒语音只需要 0.195 秒

- 

吞吐量：每秒 3000+ 个声学 token

- 

中文语音识别错误率（WER）：0.54%，英文 0.99%



放到 benchmark 里比，S2 在 Audio Turing Test（听众分辨真人还是 AI）上拿到 0.515 分，比字节的 Seed-TTS 高了 24%。简单说，已经有一半以上的人分不出这是 AI 生成的声音了。

![image]()


最大升级：从固定标签到自然语言情感控制



这是 S2 和上一代 S1 最本质的区别。

- 

自然语言情绪控制（最大亮点），S2 支持在文本中任意位置嵌入自由格式的自然语言描述标签，例如 [whisper in small voice]、[professional broadcast tone]、[pitch up]，不再限于预定义的固定标签集合，实现词级别的细粒度表达控制。 

- 

S2 Pro 支持超过 15,000 种独特标签：包括 [pause]、[emphasis]、[laughing]、[excited]、[whisper]、[singing] 等，泛化能力强，未见过的自然语言描述也能有效执行。

- 

上下文增强表现力，得益于模型上下文的扩展，模型现在可以利用前文信息来提升后续生成内容的表现力，从而提高内容的整体自然度。



S1 用圆括号固定标签控制情感，比如 (excited) (sad) (laughing)，标签集合是封闭的，你只能从预定义列表里选。


S2 改成了方括号 + 自由描述。你可以在文本任意位置插入自然语言指令：

> 

今天的会议结果 [用很沮丧的语气] 不太理想，但 [振作起来] 我们明天继续。


![image]()


系统会理解这些描述并直接反映在语音里，而不是匹配固定关键词。官方支持的独特标签超过 15000 个，包括 [pause]、[emphasis]、[laughing nervously]、[whisper in small voice]、[professional broadcast tone]、[pitch up] 等等。由于模型是在开放描述上训练的，即便是训练时没见过的新描述，泛化能力也相当不错。副语言控制单项胜率高达 91.61%。


这个能力在实际场景里很有用：做有声书可以让角色有情绪起伏，做播客可以让 AI 主播听起来不像在念稿，做游戏配音可以省掉大量录音成本。

![image]()


多角色一次生成



原生多说话人支持，用户只需上传一段包含多个说话人的参考音频，模型通过 <|speaker:i|> token 自动处理每位说话人的特征，单次推理即可生成多人对话，无需再为每个说话人分别上传音频。


声音克隆也很方便，只需要 10 到 30 秒的参考音频，不用额外微调就能克隆出高度相似的声音。语音克隆时，参考音频 token 放在 system prompt 中，SGLang 自动缓存 KV 状态，同一声音复用时前缀缓存命中率平均达 86.4%，参考音频预填充开销几乎可以忽略。

![image]()


语言支持：80+ 种语言



S2 Pro 支持 80+ 种语言，第一梯队（质量最高）：日语、英语、中文。第二梯队：韩语、西班牙语、葡萄牙语、阿拉伯语、俄语、法语、德语。在 MiniMax 的多语言测试集上，S2 在 24 种语言中有 11 种拿到了最低错误率，17 种拿到了最高说话人相似度。

![image]()


推理性能（单卡 H200）



S2 的 Dual-AR 架构与标准自回归 LLM 在结构上同构，可以直接继承 SGLang 的全套 LLM 原生服务优化，包括连续批处理、分页 KV 缓存、CUDA graph 重放和 RadixAttention 前缀缓存。


语音克隆时，参考音频 token 放在 system prompt 中，SGLang 自动缓存 KV 状态，同一声音复用时前缀缓存命中率平均达 86.4%，峰值超过 90%，参考音频预填充开销几乎可以忽略不计。


实测数据：RTF 0.195，首帧延迟约 100ms，吞吐量超过每秒 3000 个 acoustic token。


---



如何获取



模型权重和代码完全开源，研究和非商业用途免费：


GitHub：https://github.com/fishaudio/fish-speech


HuggingFace：https://huggingface.co/fishaudio/s2-pro


在线体验：https://fish.audio/s2/


技术报告：https://arxiv.org/abs/2603.08823

> 

本文参考：Fish Audio 官方推文 | 原文链接 | S2 产品页 | 开源博客

---

*来源：[Fish Audio 开源 S2：4B 参数的 TTS 模型，100ms 出声，还能让 AI 笑出来](https://www.xiaohu.ai/p/fish-audio-s2-4b-tts-100ms-ai/30528326)*
