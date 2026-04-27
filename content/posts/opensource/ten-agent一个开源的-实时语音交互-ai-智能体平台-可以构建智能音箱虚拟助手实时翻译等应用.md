---
title: "TEN-Agent：一个开源的 实时语音交互 AI 智能体平台 可以构建智能音箱、虚拟助手、实时翻译等应用"
date: 2025-03-22T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "TEN-Agent 是一个开源的 实时语音交互 AI 智能体平台，由 TEN Framework 构建，支持“看、听、说、实时对话”能力。它集成了多个强大组件（如 DeepSeek、OpenAI、Gemini、ESP32、RTC）并支持跨平台部署。   该项目致力于构建可以在本地或边缘设备（如 ES"
source_url: "https://www.xiaohu.ai/p/ten-agent-ai/19801644"
xiahuid: "19801644"
---

## 📰 正文

TEN-Agent 是一个开源的 实时语音交互 AI 智能体平台，由 TEN Framework 构建，支持“看、听、说、实时对话”能力。它集成了多个强大组件（如 DeepSeek、OpenAI、Gemini、ESP32、RTC）并支持跨平台部署。


该项目致力于构建可以在本地或边缘设备（如 ESP32）上运行的 语音驱动多模态 AI 智能体。适用于构建智能音箱、虚拟助手、实时翻译系统等应用。


核心功能概览


![image]()


主要功能
1. 

实时多模态交互

- 

支持语音、视频、文本等多种模态的实时交互。

- 

提供超低延迟的响应能力，能够实现自然流畅的对话体验，支持实时打断功能。

- 

集成语音识别（ASR）、大语言模型（LLM）和文本转语音（TTS）模块，适用于复杂音视频场景。


2. 

强大的集成能力

- 

与多种主流 AI 服务兼容，例如 OpenAI Realtime API、Google Gemini、DeepSeek 等。

- 

支持实时通信技术（RTC），提供 AI 降噪等功能，确保高质量的音频交互。

- 

内置工具如天气查询、网络搜索、视觉识别（Vision）和检索增强生成（RAG），增强实用性。


3. 

跨平台与多语言支持

- 

支持在 Windows、Mac、Linux 以及移动设备上运行。

- 

开发者可以使用 C++、Go、Python 等多种编程语言创建模块化、可重用的扩展（未来计划支持 JavaScript/TypeScript）。

- 

可实现实时语言翻译，适用于跨语言沟通场景。


4. 

灵活的开发与部署

- 

提供拖拽式编程界面（Graph Designer），无需深入编码即可快速构建 AI 代理。

- 

支持边缘与云端扩展的灵活组合，兼顾隐私、成本和性能。

- 

可通过 Docker 部署，便于本地测试和生产环境上线。




技术方法与架构



🌐 技术集成


- 

语音识别：支持 Deepgram ASR

- 

语音合成：支持 ElevenLabs TTS、Neuphonic TTS 等

- 

语言模型：兼容 OpenAI API、DeepSeek、Gemini 2.0 等

- 

实时通信：集成 Agora RTC，实现多方语音对话场景

- 

部署平台：

- 

可通过 Docker Compose 快速搭建

- 

本地 playground 可视化配置和测试



![image]()


📦 模块化设计


- 

每个 Agent 支持选择 不同语音识别 / 合成模块、LLM 模块、扩展插件。

- 

所有配置通过 .env 文件和 playground 页面进行管理与切换。



🧱 技术栈


- 

后端语言：Python + Go + C

- 

前端与配置：TypeScript / Next.js 14

- 

支持多种集成模式，易于扩展与二次开发



---



应用场景


![image]()

- 

可用于构建实时语音助手（如讲故事并生成相关图像的儿童教育工具）。

- 

支持视频会议实时转录与翻译、虚拟伴侣、自动化客服等复杂应用。

- 

在硬件上（如 ESP32-S3 Korvo V3 开发板）实现实时 LLM 通信。


![image]()

![image]()


使用 TEN Agent 配合 Trulience 提供的免费虚拟人形象（Avatar），你还可以快速构建一个具有视觉形象的 AI 虚拟助手。只需两个简单步骤，就能让这个 AI 虚拟形象“动起来”并与你互动。
1. 

按照 README 中的说明，在本地运行 Playground（地址为 localhost:3000）

- 

这一步是启动 TEN Agent 的可视化配置界面。

- 

你可以在这个页面中设置 AI 智能体的功能和外观。


2. 

将你从 Trulience 获得的 Avatar ID 和 Token 填入设置中

- 

Trulience 是一个提供各种虚拟人形象的平台。

- 

你注册或登录后会获得某个 Avatar 的 ID 和访问 Token。

- 

将这些信息填入 TEN Agent 的配置中，就能让虚拟助手具备一个真实可见的“人设”。

![image]()




使用 TEN Agent 快速构建实时语音代理教程


使用 Ten Agent 构建自己的语音 AI 代理：分步指南


GitHub：https://github.com/TEN-framework/TEN-Agent 


在线体验：agent.theten.ai

---

*来源：[TEN-Agent：一个开源的 实时语音交互 AI 智能体平台 可以构建智能音箱、虚拟助手、实时翻译等应用](https://www.xiaohu.ai/p/ten-agent-ai/19801644)*
