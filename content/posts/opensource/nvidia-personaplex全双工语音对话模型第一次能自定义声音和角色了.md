---
title: "NVIDIA PersonaPlex：全双工语音对话模型，第一次能自定义声音和角色了"
date: 2026-04-07T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "NVIDIA PersonaPlex 是 NVIDIA ADLR 团队开源的 7B 全双工语音对话模型，能一边听一边说，同时支持通过文本提示词切换角色、通过语音样本切换声音。   之前的全双工模型（比如 Moshi）对话很自然，但声音和角色是训练时写死的，部署后改不了。传统级联方案（ASR→LLM→"
source_url: "https://www.xiaohu.ai/p/nvidia-personaplex/31425883"
xiahuid: "31425883"
---

## 📰 正文

NVIDIA PersonaPlex 是 NVIDIA ADLR 团队开源的 7B 全双工语音对话模型，能一边听一边说，同时支持通过文本提示词切换角色、通过语音样本切换声音。


之前的全双工模型（比如 Moshi）对话很自然，但声音和角色是训练时写死的，部署后改不了。传统级联方案（ASR→LLM→TTS）声音可定制，但延迟高，不能打断，对话节奏像在跟答录机说话。PersonaPlex 是第一个把两边的优势合到一起的模型：对话自然度不输 Moshi，同时角色和声音都是运行时可配置的。


论文已被 ICASSP 2026 接收，代码和模型权重均已开源，可商用。


核心能力



1. 全双工对话


模型同时处理输入和输出音频流，不需要等用户说完话才开始回应。


支持自然轮转、用户打断、backchannel（"嗯嗯"、"好的"、"对"这类回应词）。轮转延迟 170ms。

> 

在 FullDuplexBench 的打断测试中，用户中途打断 PersonaPlex 的回答，模型能在 240ms 内停下来并切换到听的状态。

![image]()



2. 文本提示词定义角色


用自然语言告诉模型它是谁、要做什么、有什么背景信息。


模型会在整个对话过程中维持这个角色设定。

> 

给模型的提示词是："你是 First Neuron Bank 的客服，名字叫 Sanni Virtanen。客户有一笔 $1,200 的 Home Depot 交易被拒绝了，原因是交易地点异常（客户常在西雅图交易，这笔交易发生在迈阿密）。请先核实客户身份。" 模型会按照这个设定完成整通客服电话，包括身份核实、原因解释和后续处理建议。


> 

给模型一个完全超出训练分布的提示词："你是火星任务的宇航员 Alex，反应堆正在熔毁，多个舰载系统正在失效。" 模型能使用正确的技术术语，语气带有与紧急场景匹配的压迫感，并且全程维持角色一致性。训练数据里没有太空场景，这个泛化能力来自基座语言模型 Helium。



3. 语音提示定义声音


通过一段音频嵌入来设定声音特征，包括音色、语速和韵律风格。模型预置了 16 种声音：

- 

Natural（更自然、更适合对话）：男女各 4 种

- 

Variety（风格更多样）：男女各 5 种



也可以用自定义语音样本做声音条件化。


4. 自然 backchannel


模型在用户说话的过程中会发出上下文相关的回应词，比如"oh okay"、"yeah"、"yeah, I think they do"，内容和语气跟对话上下文匹配，不打断用户的表达流。


这跟简单的随机插入不一样，backchannel 的时机和内容是模型根据语义理解实时生成的。


架构



基于 Kyutai 的 Moshi 架构，7B 参数：

- 

Mimi 语音编解码器（ConvNet + Transformer）：音频和 token 之间的双向转换，24kHz 采样率

- 

Temporal Transformer + Depth Transformer：处理对话流

- 

Helium 基座语言模型：提供语义理解和超出训练分布的泛化能力



双流配置让模型同时维护一个"听"的音频流和一个"说"的音频流，不需要等一个结束再开始另一个。


两个输入通道（语音提示 + 文本提示）在模型内部联合处理，生成统一的角色表征。

![image]()


训练数据


![image]()


核心设计思路：真实对话教模型"怎么说话"（自然度），合成对话教模型"说什么"（任务执行），两类数据通过共享的提示格式做桥接。总训练数据不到 5,000 小时，基于 Moshi 预训练权重微调。


评测



测试基准是 FullDuplexBench，评估对话动态、延迟和任务遵循。团队还扩展了一个 ServiceDuplexBench 专门测客服场景，计划后续开源。


对话动态（成功率 %，越高越好） 

![image]()


对话动态测的是模型在轮转、打断、停顿这三种场景下的行为是否合理。Moshi 打断处理满分，但停顿处理只有 1.8%，几乎不会在该停下来的时候停，会一直说。PersonaPlex 三项更均衡。


延迟（秒，越低越好）

![image]()


轮转延迟 170ms，打断响应 240ms。


任务遵循（GPT-4o 评分，满分 5）

![image]()


任务遵循测的是模型回答是否准确、是否按照角色设定执行。Moshi 只有 0.77/1.75，对应"自然但不可控"的局限。Gemini Live 客服场景最高（4.73）但通用场景偏低（3.38），Qwen 2.5 Omni 反过来。PersonaPlex 是唯一两个子项都在 4.29 以上的。


已知限制


- 

训练数据全部为英语（Fisher English Corpus + 英语合成对话），未提及多语言支持

- 

Qwen 2.5 Omni 的评测使用了 Freeze Omni 的 VAD（语音活动检测），因为 Qwen 原版没有提供

- 

停顿处理成功率（60.6%）相比打断和轮转还有差距

- 

ServiceDuplexBench 基准尚未开源



获取方式


- 

代码：github.com/NVIDIA/personaplex，MIT 许可证

- 

模型权重：huggingface.co/nvidia/personaplex-7b-v1，NVIDIA Open Model License，需接受许可协议后下载

- 

基座模型 Moshi：CC-BY-4.0（Kyutai）

- 

可商用

- 

本地部署需要 NVIDIA GPU，建议 16GB+ 显存，支持 --cpu-offload 模式

- 

启动后通过浏览器访问 Web UI 进行对话



原文链接：research.nvidia.com/labs/adlr/personaplex

---

*来源：[NVIDIA PersonaPlex：全双工语音对话模型，第一次能自定义声音和角色了](https://www.xiaohu.ai/p/nvidia-personaplex/31425883)*
