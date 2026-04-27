---
title: "Google 推出 FunctionGemma 模型 能理解自然语言 并将其转换为操作各种设备的命令"
date: 2025-12-19T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google 推出了一个新的 AI 模型，叫做 FunctionGemma。   它是 Google 自家的 Gemma 3 270M 模型 的一个特别版本，专为函数调用（Function Calling）任务优化的语言模型。   基于 Gemma 3 270M 模型进行二次微调（fine-tuni"
source_url: "https://www.xiaohu.ai/p/google-functiongemma/27930315"
xiahuid: "27930315"
---

## 📰 正文

Google 推出了一个新的 AI 模型，叫做 FunctionGemma。


它是 Google 自家的 Gemma 3 270M 模型 的一个特别版本，专为函数调用（Function Calling）任务优化的语言模型。


基于 Gemma 3 270M 模型进行二次微调（fine-tuning）。


其主要目标是：

> 

将自然语言转换为结构化、可执行的操作指令（如 API 调用或系统函数执行），
并能够在低功耗、离线设备（Edge Devices）上本地运行。



它是能把你“说的话”自动转成“可执行动作”的小型 AI 模型，将你的语言转换成能在移动设备上执行的命令。


比如：“播放我最常听的播放列表，并把空调调到 23 度。”


它可以自动理解并操作各种智能设备。


这一模型的推出，标志着 Google 从传统的“对话式语言模型”
向“可执行的智能代理（Action-oriented Agent）”方向过渡。


为什么 Google 要做 FunctionGemma？



现在很多 AI 模型（包括聊天机器人）都只是“语言理解器”，
能聊天、能回答，但不会执行命令。


可未来的 AI 趋势，是从：

> 

“会说话” → “能做事”



也就是所谓的 “Agent（智能代理）”。
比如，AI 不光能告诉你天气，还能自动帮你订机票、设置提醒、发送邮件。


要实现这些功能，AI 模型必须：
1. 

理解自然语言（听懂你说什么）；

2. 

调用函数 / API（知道该执行什么命令）。



而 FunctionGemma 就是为此设计的模型。


FunctionGemma 是怎么工作的？



你可以把它想成是一个“语言转命令引擎”。


例子：



你说：“帮我加个提醒，晚上8点喂猫。”


→ 模型会：
1. 

分析语句的含义；

2. 

生成对应的函数调用，比如：


```None
{
  "function": "create_reminder",
  "parameters": {
    "time": "20:00",
    "content": "喂猫"
  }
}
```


3. 

系统执行这个命令（比如通过手机的提醒功能）。



它的特点


![image]()


适用场景



FunctionGemma 适用于以下类型的开发需求：

![image]()


实际效果



Google 做了一个测试集，叫 “Mobile Actions”（移动操作任务集）。


模型要做的事情包括：

- 

创建日历事件

- 

添加联系人

- 

调整系统设置

- 

启动手机功能（如手电筒）



结果：

- 

原始模型（未微调）准确率：58%

- 

微调后的 FunctionGemma 准确率：85%

![image]()



也就是说，经过专门训练后，FunctionGemma 的理解与执行能力提升显著。


可以在哪用？



Google 给出了几个典型场景，帮助开发者理解用途。


1️⃣ 手机本地助手（Mobile Actions）



离线运行，不依赖网络。
用户通过自然语言发出系统命令，例如：

- 

“创建一个明天 12 点的会议。”

- 

“添加联系人 John。”

- 

“打开手电筒。”



模型自动将这些语句解析为底层系统函数调用。
执行逻辑完全本地化，不依赖任何云端服务。


这类应用展示了 FunctionGemma 在移动操作系统层级代理中的可行性，
尤其适合 Android、WearOS、车载设备等生态。


2️⃣ 智能游戏（TinyGarden Demo）



在一个小游戏中，玩家通过语音控制农场：

- 

“种向日葵在最上排”

- 

“给它们浇水”



模型会将语言转换为代码指令：


```None
plantCrop("sunflower", row="top")
waterCrop(row="top")
```



整个过程在手机本地执行，不经过任何服务器，无需联网。


这验证了模型在“多步逻辑解析”与“函数参数分解”方面的能力。


3️⃣ 本地 AI 实验（Physics Playground）



一个基于 Transformers.js 的浏览器内物理模拟实验。
用户通过自然语言描述物理场景（如添加物体、设定重力方向），模型直接在前端执行命令。


这展示了模型的轻量化与跨平台能力。


玩家可以用语音控制物理模拟，比如：

- 

“让球从左往右滚动”

- 

“添加一个木块”
运行完全在浏览器中，通过 FunctionGemma 和 Transformers.js 实现。



下载：在 Hugging Face 或 Kaggle 上获取该模型。


指南：https://ai.google.dev/gemma/docs/functiongemma 


官方介绍：https://blog.google/technology/developers/functiongemma/

---

*来源：[Google 推出 FunctionGemma 模型 能理解自然语言 并将其转换为操作各种设备的命令](https://www.xiaohu.ai/p/google-functiongemma/27930315)*
