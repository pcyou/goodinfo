---
title: "nanochat：ChatGPT的开源“教学版” 何人都能用不到100美元，自己动手从零构建一个可聊天的AI模型"
date: 2025-10-14T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "nanochat 是一个能让你自己“造一个小号ChatGPT”的开源项目。 你只需要一台GPU服务器、不到100美元，就能从零训练出一个会聊天的AI模型。   作者 Andrej Karpathy ——  -   前特斯拉AI负责人  -   OpenAI早期成员之一  -   大语言模型教育推广者"
source_url: "https://www.xiaohu.ai/p/nanochat-chatgpt-100-ai/25975335"
xiahuid: "25975335"
---

## 📰 正文

nanochat 是一个能让你自己“造一个小号ChatGPT”的开源项目。
你只需要一台GPU服务器、不到100美元，就能从零训练出一个会聊天的AI模型。


作者 Andrej Karpathy ——

- 

前特斯拉AI负责人

- 

OpenAI早期成员之一

- 

大语言模型教育推广者（他也做过 nanoGPT）



他把这个项目当作教学工具，让更多人能真正理解ChatGPT是怎么炼成的。


nanochat是干什么的



它是一个完整、简化版的ChatGPT系统。

> 

是一个从零开始构建的、极简且完整的 ChatGPT 级聊天模型（LLM）实现。


也就是说，它不仅有模型，还有从训练、测试到上线的全部环节。



Karpathy 将其定位为：

> 

“一个可在单机上用约100美元训练出 ChatGPT 类体验的全栈项目。”



即：
你可以在一台搭载 8×H100 GPU 的节点上，通过运行一条脚本（speedrun.sh），
在约 4小时 内完成：

- 

数据预处理（从文本中提取训练语料）

- 

分词（用Rust写的快速tokenizer））

- 

预训练（pretraining 用PyTorch在GPU上训练）

- 

微调（finetuning 在常见任务上测试性能）

- 

评估（evaluation 输出准确率、loss、速度等指标）

- 

推理与 Web 聊天界面部署（inference + web serving 像ChatGPT一样可以对话）



最终，你能从零获得一个可交互的“小型ChatGPT”。

![image]()


它的训练层级（不同预算）


![image]()


Karpathy想传达的理念


> 

“AI 不该只是大公司才能玩。
每个人都应该能理解、训练、修改、运行属于自己的LLM。”



所以，nanochat 是一种“AI民主化实验平台”：

- 

花小钱、跑全流程；

- 

看懂AI；

- 

改造AI。



一句话


> 

nanochat = ChatGPT的开源“教学版”。
它让任何人都能在本地或云端，
用不到100美元，自己动手从零构建一个可聊天的大语言模型。



GitHub：https://github.com/karpathy/nanochat

---

*来源：[nanochat：ChatGPT的开源“教学版” 何人都能用不到100美元，自己动手从零构建一个可聊天的AI模型](https://www.xiaohu.ai/p/nanochat-chatgpt-100-ai/25975335)*
