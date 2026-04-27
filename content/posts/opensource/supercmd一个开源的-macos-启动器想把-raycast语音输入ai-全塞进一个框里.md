---
title: "SuperCmd：一个开源的 macOS 启动器，想把 Raycast、语音输入、AI 全塞进一个框里"
date: 2026-04-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "SuperCmd，一个开源的 macOS 启动器应用，可以理解为免费版 Raycast + Wispr Flow + Speechify + AI 助手的缝合体。   听起来野心很大，但思路其实很清晰：Mac 用户日常高频用的几个效率工具，能不能合成一个？  ![image]()   它能干什么"
source_url: "https://www.xiaohu.ai/p/supercmd-macos-raycast-ai/31570098"
xiahuid: "31570098"
---

## 📰 正文

SuperCmd，一个开源的 macOS 启动器应用，可以理解为免费版 Raycast + Wispr Flow + Speechify + AI 助手的缝合体。


听起来野心很大，但思路其实很清晰：Mac 用户日常高频用的几个效率工具，能不能合成一个？

![image]()


它能干什么



打开方式和 Raycast、Alfred 一样，快捷键呼出一个搜索框，然后从这个框里做所有事情。


基础启动器功能，搜索应用、搜索文件、快速打开，这些是标配就不多说了。值得单独讲的是下面几个：


无限剪贴板历史。每次复制的内容都会被记录下来，可以搜索、置顶、回溯粘贴。这个功能很多人单独装一个 app 来做（Paste、Maccy 之类的），SuperCmd 直接内置了。


Markdown 笔记和画布。启动器里直接写笔记，支持 Markdown 格式。还内置了 Excalidraw 画布，可以随手画个流程图或者草图。不用切到 Notion 或者 Obsidian，临时记个东西很方便。


文本片段展开。设一个缩写，打出来自动展开成完整文本。比如输入 ;addr 自动变成你的完整地址，输入 ;sig 变成邮件签名。写邮件、回消息的时候省很多重复打字。


窗口管理。用快捷键调整窗口大小和位置，不需要再装 Rectangle 或 Magnet。

![image]()


语音输入是个亮点



SuperCmd 内置了基于 Whisper 的语音输入，体验类似 Wispr Flow：按住快捷键说话，松开就自动转成文字输入到当前光标位置。


它不是简单的语音转文字，会自动去掉嗯啊这些填充词，还会做一些语法修正。在任何 app 里都能用，不限于 SuperCmd 自己的界面。


另外还有反向功能，选中一段文字，让它用自然语音朗读出来，体验类似 Speechify。校对文章或者解放眼睛的时候挺实用。


AI 集成：带记忆的



AI 对话功能支持三个 provider：

- 

OpenAI：填 API Key，用 GPT 系列

- 

Anthropic：填 API Key，用 Claude

- 

Ollama：连本地模型，完全离线，数据不出本机



有意思的是它集成了 Supermemory，AI 可以记住你之前告诉它的内容。比如你说"记住我的项目用的是 Next.js + Supabase"，下次问相关问题它会带上这个上下文。


语音合成方面，支持 Edge TTS（免费，不需要 Key）和 ElevenLabs（需要 Key，声音更自然）。


兼容 Raycast 扩展生态



这是 SuperCmd 最有野心的部分。它实现了一套 @raycast/api 的兼容层，可以直接安装和运行 Raycast 的扩展。


Raycast 的扩展商店里有几千个扩展，覆盖 GitHub、Slack、Notion、Spotify、1Password、Google Translate 等等。SuperCmd 想直接借用这个生态，而不是从零开始建自己的。


不过要说实话，这个兼容层目前还不完整。OAuth 认证、部分边缘 API 还在 TODO 状态，不是所有 Raycast 扩展都能完美运行。但核心的搜索类、工具类扩展已经可以用了。

![image]()


技术栈和项目状态



用 Electron + React + TypeScript 做的，macOS 原生功能（快捷键、取色器、语音）用 Swift 写的原生模块桥接。


GitHub 上 309 star，4 个贡献者，245 个 commit，最新版本 1.0.14。项目还比较早期，但更新频率不低。有意思的是贡献者列表里有一个叫"Claude"的，看来开发过程本身也在大量用 AI。


开源，免费，代码全部公开。


适合谁



如果你现在在用 Raycast 免费版并且觉得够用了，SuperCmd 暂时不会给你更多东西。


但如果你符合下面几种情况，可以试试：

- 

想要 Raycast Pro 的 AI 功能但不想每月付费，自己有 OpenAI / Anthropic 的 API Key

- 

想要一个启动器 + 剪贴板管理 + 语音输入 + 窗口管理的一体化方案，不想装四五个 app

- 

喜欢折腾开源工具，愿意接受一些粗糙换来完全的可定制性

- 

对隐私敏感，想用 Ollama 跑本地模型，所有数据不出本机



已知的不足



直接说：

- 

Electron 应用，内存占用比原生 app 高

- 

Raycast 扩展兼容层不完整，部分扩展会报错

- 

只支持 macOS，没有 Windows 和 Linux 版本

- 

项目早期，UI 细节和稳定性还有打磨空间

- 

文档不算完善，有些功能需要自己摸索



怎么装



直接去 GitHub Releases 下载 dmg 安装：

- 

Apple Silicon Mac：https://github.com/SuperCmdLabs/SuperCmd/releases/download/1.0.14/SuperCmd-1.0.14-arm64.dmg

- 

Intel Mac：https://github.com/SuperCmdLabs/SuperCmd/releases/download/1.0.14/SuperCmd-1.0.14.dmg



或者从源码编译：


```None
git clone https://github.com/SuperCmdLabs/SuperCmd.git
cd SuperCmd
npm install
npm run dev
```


> 

官网：https://supercmd.sh 


GitHub：https://github.com/SuperCmdLabs/SuperCmd 


Discord：https://discord.gg/CsdbknHqx5

---

*来源：[SuperCmd：一个开源的 macOS 启动器，想把 Raycast、语音输入、AI 全塞进一个框里](https://www.xiaohu.ai/p/supercmd-macos-raycast-ai/31570098)*
