---
title: "Vercel 开源 Chat SDK：让你的聊天机器人同时适配各种即时通信软件"
date: 2026-02-26T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: ">   你有没有想过，做一个聊天机器人要同时适配四五个平台，光是对接不同平台的接口，代码量就翻了好几倍？Vercel 刚刚开源了一个工具，直接把这个问题解决了。    这是什么    Vercel 发布了一个新的开源项目，叫 Chat SDK：一个用 TypeScript 写的工具包，让开发者只写一"
source_url: "https://www.xiaohu.ai/p/vercel-chat-sdk/30084752"
xiahuid: "30084752"
---

## 📰 正文

> 

你有没有想过，做一个聊天机器人要同时适配四五个平台，光是对接不同平台的接口，代码量就翻了好几倍？Vercel 刚刚开源了一个工具，直接把这个问题解决了。



这是什么



Vercel 发布了一个新的开源项目，叫 Chat SDK：一个用 TypeScript 写的工具包，让开发者只写一套聊天机器人的代码，就能同时部署到 Slack、GitHub、Microsoft Teams、Discord 这四个主流平台上。


一套代码，四个平台同时跑。不用为每个平台写一遍逻辑，不用维护四套代码库。


目前已经进入公开测试阶段，任何人都可以去试用。

![image]()





为什么这件事值得关注



如果你做过任何跟聊天机器人相关的事，你就知道痛点在哪：


每个平台的消息格式不一样，API 接口不一样，认证方式不一样，甚至连"用户点了一个按钮"这种简单交互，在不同平台上的处理方式都完全不同。


这意味着什么？一个功能相同的机器人，你要写 4 份代码，维护 4 套逻辑，修一个 bug 要改 4 个地方。


Chat SDK 做的事情，就是在这些平台之间加了一个"翻译层"。你只需要用统一的方式写逻辑：收到什么消息、怎么回复、怎么处理命令，SDK 自动帮你翻译成各个平台能理解的格式。


核心技术特性



事件驱动架构， 内置类型安全的事件处理器，覆盖，

- 

@mentions（被提及）

- 

消息接收

- 

表情反应（Reactions）

- 

按钮点击

- 

斜杠命令（Slash Commands）



JSX 原生 UI 组件， 可以用 JSX 编写卡片（Cards）和弹窗（Modals），SDK 负责将其渲染为各平台原生界面，不需要为每个平台单独写 UI 代码。


分布式状态管理， 通过可插拔适配器支持，

- 

Redis

- 

ioredis

- 

内存存储



目前的状态



Chat SDK 现在是 公开测试版（Public Beta），支持的平台包括 Slack、GitHub、Microsoft Teams 和 Discord。


作为开源项目，代码和文档都可以在 Vercel 官网找到，感兴趣的开发者可以直接上手试用。


---



 Vercel 这次的 Chat SDK 抓住了一个很实际的痛点：跨平台适配太费时间了。"写一次，到处跑"这个理念在前端领域已经被验证过了（React Native 就是这么做的），现在轮到聊天机器人了。


对于想做 AI 机器人的团队来说，这个工具值得关注。


官方介绍及示例：https://vercel.com/changelog/chat-sdk 


GitHub：https://github.com/vercel/chat 


文档：https://www.chat-sdk.dev/docs

---

*来源：[Vercel 开源 Chat SDK：让你的聊天机器人同时适配各种即时通信软件](https://www.xiaohu.ai/p/vercel-chat-sdk/30084752)*
