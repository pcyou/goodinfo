---
title: "在手机上实时监控Claude Code 工作进度并下达指令干活"
date: 2026-01-22T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "你在电脑上用 Claude Code 或 Codex 写代码。   如果你临时出门、拿着手机，也想看看 AI 现在写到哪了？是否遇到问题？   该怎办？   这个开源的程序可以帮到你   Happy 是一个 AI 编程助手的“远程控制器”。   它可以让你：  -   在手机、网页、平板上查看 Cl"
source_url: "https://www.xiaohu.ai/p/claude-code/28870995"
xiahuid: "28870995"
---

## 📰 正文

你在电脑上用 Claude Code 或 Codex 写代码。


如果你临时出门、拿着手机，也想看看 AI 现在写到哪了？是否遇到问题？


该怎办？


这个开源的程序可以帮到你


Happy 是一个 AI 编程助手的“远程控制器”。


它可以让你：

- 

在手机、网页、平板上查看 Claude/Codex 的运行进度；

- 

直接对话或语音下指令；

- 

实时切换设备（比如从手机控制切回电脑只需按键）。

![image]()



并且整个通信过程是 端到端加密（End-to-End Encrypted） 的，你的代码不会泄露到服务器。


核心功能概览


![image]()


它不是用来写代码的编辑器，而是一个AI 代码助手的遥控器 + 通信桥。


也就是说，它不帮你写代码，而是帮你随时随地控制那个帮你写代码的 AI。


比如说👇

- 

你在电脑上让 Claude 写一个 React 项目；

- 

你去吃饭或出门，手机上打开 Happy App；

- 

它会显示 Claude 当前在干嘛、输出了什么；

- 

你还可以直接在手机上输入新指令，甚至用语音说：“Claude，重命名文件夹”；

- 

Claude 会立刻执行，然后 Happy 实时同步更新结果。



你不用远程桌面、也不用 VPN。


一切都通过 Happy 自建的加密连接实现。


项目的工作原理（简单解释）



Happy 实际上由三部分组成👇：

![image]()


安全 + 隐私


> 

“我们不看你的代码，也不保留任何日志。”



Happy 的所有通信都是 端到端加密（End-to-End Encryption）。
也就是说：

- 

你写的内容不会上传到他们的服务器；

- 

就算有人中间拦截，也只能看到加密数据；

- 

只有你的设备能解密。



而且项目是 完全开源的，
你可以自己看代码确认它真的没偷数据（他们还写了隐私政策 PRIVACY.md）。


所以它非常适合那些担心隐私的开发者。


在哪些设备上能用？



Happy 几乎支持所有常见平台：

- 

iPhone / Android 手机：有官方 App；

- 

网页端：直接登录网页版就能用（happy.engineering）；

- 

macOS 桌面端：支持通过 Tauri 框架本地运行；

- 

Windows / Linux：通过命令行（CLI）使用。



而且你可以非常自由地在设备之间来回切换。


比如，你在电脑上运行 Claude，
走开时拿出手机打开 Happy App，它会立即显示当前 Claude 的状态。
如果想重新在电脑上接管，只要按键盘上的任意键，Claude 就自动切回本地控制。


这个过程几乎是无缝的。


怎么用？上手很简单



Happy 的设计目标就是“让你一分钟内上手”。
以下是一个新手能理解的完整流程👇


第一步：安装命令行工具



在电脑上运行这条命令（需要 Node.js 环境）：


```None
npm install -g happy-coder
```



第二步：启动 Claude / Codex



平常你可能直接在命令行输入：


```None
claude
```



或者：


```None
codex

```



现在只要改成：


```None
happy
```



或者：


```None
happy codex
```



这样 Claude/Codex 就会在 Happy 的“加密控制模式”下启动。


第三步：用手机连接



下载「Happy Coder」App（iOS/Android 都有），
登录后就能看到 Claude 当前的运行状态。


此时你可以：

- 

看 Claude 输出的结果；

- 

让它继续执行任务；

- 

用语音对它说话；

- 

或直接在手机上编辑代码段。



整个过程不需要公网 IP、不需要 VPN，
因为它会自动建立一条加密隧道来同步数据。


GitHub：https://github.com/slopus/happy 


iOS下载


安卓下载 


官网：https://happy.engineering/

---

*来源：[在手机上实时监控Claude Code 工作进度并下达指令干活](https://www.xiaohu.ai/p/claude-code/28870995)*
