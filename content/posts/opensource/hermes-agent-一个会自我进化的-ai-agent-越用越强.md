---
title: "Hermes Agent 一个会自我进化的 AI Agent 越用越强"
date: 2026-03-29T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Nous Research 开源 Hermes Agent 一个会自我进化的 AI Agent，用越久越强，8.7k Stars   Nous Research 开源了 Hermes Agent，一个可以部署在你自己服务器上的自主 AI Agent，内置持久记忆、自动生成技能、跨平台消息网关，MIT"
source_url: "https://www.xiaohu.ai/p/hermes-agent-ai-agent/31118826"
xiahuid: "31118826"
---

## 📰 正文

Nous Research 开源 Hermes Agent 一个会自我进化的 AI Agent，用越久越强，8.7k Stars


Nous Research 开源了 Hermes Agent，一个可以部署在你自己服务器上的自主 AI Agent，内置持久记忆、自动生成技能、跨平台消息网关，MIT 协议。


这不是又一个套壳聊天机器人，也不是绑定在 IDE 里的编程助手。


Hermes Agent 的核心差异是：它会越用越强。 


它能记住跨会话的上下文，解决过的复杂问题会自动写成可复用的 Skill 文档，下次遇到类似问题直接调用。用得越久，它积累的技能和对你的了解就越多。


跟 Claude Code / Codex 有什么区别



Claude Code 和 Codex 是编程助手，主要活在 IDE 或终端里，服务的是写代码这件事。


Hermes Agent 的定位不一样：

![image]()


简单说：Claude Code 是你坐在电脑前的编程搭档，Hermes Agent 是一个住在服务器上、你不在的时候也能干活的自主体。


四个核心能力



① 越用越强的学习闭环



这是 Hermes Agent 最独特的地方。它有一套多层记忆系统：


会话记忆： 当前对话的上下文，跟普通 AI 一样。


持久记忆： 跨会话保留你的偏好、项目信息、历史任务。关掉再开，它还记得你。


技能记忆： 解决了一个复杂问题后，Agent 会自动把解题过程写成一个 SKILL.md 文件。下次遇到类似问题，它直接调用这个 Skill，不用重新推理。

> 

你让它修了一个 Docker 网络问题，它解决后自动生成了一个"Docker 网络排错"的 Skill。三周后你遇到类似问题，它直接调用那个 Skill，几秒钟搞定，不用你再从头描述一遍。



而且这些 Skill 会在使用中自我改进。用的次数越多，Skill 越精炼。


② 住在你的服务器上，不绑定笔记本



大多数 AI 助手都住在你的笔记本上，你合上盖子它就停了。


Hermes Agent 可以部署在 $5/月的 VPS 上、Docker 容器里、SSH 远程服务器上，甚至 Modal 和 Daytona 这种 serverless 环境（空闲时几乎不花钱）。

> 

你在服务器上启动了一个长时间的数据分析任务，然后关掉电脑去吃饭。半小时后手机上 Telegram 弹出消息："分析完了，结果如下……"



它支持六种运行环境：本地、Docker、SSH、Daytona、Singularity、Modal。


③ 跨平台消息网关



一个 Agent 同时连接 Telegram、Discord、Slack、WhatsApp、Signal、邮件和 CLI。在任何一个平台发消息都能跟它对话，所有平台共享同一份记忆和技能库。

> 

你在电脑上通过 CLI 跟它讨论了一个项目方案，出门后在 Telegram 上继续聊，它记得之前说过的所有内容。



还支持语音消息自动转文字，以及内置的 cron 定时任务，可以设定"每天早上 8 点给我发一份项目进度简报到 Telegram"。


④ 子 Agent 并行执行



可以派出多个隔离的子 Agent 同时处理不同任务，每个子 Agent 有自己独立的对话和终端环境，互不干扰。

> 

你让它同时做三件事：一个子 Agent 跑数据清洗，一个子 Agent 做代码审查，一个子 Agent 写文档。三个并行执行，结果汇总给你。



还支持用 Python 脚本通过 RPC 调用工具，把多步骤流程压缩成单次推理调用，节省 context 消耗。


40+ 内置工具



类别 工具 Web 搜索、浏览器自动化（点击/输入/截图） 系统 终端执行、文件系统操作、代码执行 AI 视觉分析、图片生成、文字转语音、多模型推理 规划 任务规划、cron 定时调度、记忆管理 协作 子 Agent 派发、RPC 工具调用


Skills 方面，内置 40+ 个覆盖 MLOps、GitHub 工作流、研究等场景，兼容 agentskills.io 开放标准，可以从 ClawHub、LobeHub 和 GitHub 安装社区贡献的 Skill。


安装



一行命令，60 秒搞定：


```None
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```



自动装 Python 3.11、克隆仓库、配置依赖。不需要 sudo。支持 Linux、macOS、WSL2。


装完之后：


```None
hermes setup    # 交互式配置，选模型
hermes          # 开始聊
```



要连接消息平台：


```None
hermes gateway setup    # 配置 Telegram / Discord / Slack 等
hermes gateway          # 启动网关
hermes gateway install  # 装成系统服务，开机自启
```



模型支持



不锁定任何模型，hermes model 一条命令随意切换模型：


Nous Portal、OpenRouter（200+ 模型）、OpenAI、z.ai/GLM、Kimi/Moonshot、MiniMax，或者你自己的 endpoint。


研究用途



这个部分可能只有做 AI 研究的人关心：Hermes Agent 内置了批量轨迹生成（parallel workers + checkpointing）、Atropos RL 训练集成、ShareGPT 格式导出（含轨迹压缩）。可以用它生成大量 tool-calling 训练数据来微调下一代模型。


已知限制


- 

Windows 原生不支持，必须用 WSL2

- 

消息网关模式下安全风险较高，一个被入侵的 Telegram 账号等于拿到了 Agent 的全部权限

- 

Skill 生态还比较年轻，社区贡献的 Skill 数量有限

- 

对非 Hermes 系列模型的 tool-calling 兼容性没有充分测试

- 

持久记忆依赖本地存储，没有云端同步方案



背景



Nous Research 是开源 AI 社区的知名团队，做过 Hermes、Nomos、Psyche 等系列模型。Hermes Agent 是他们从"提供模型权重"扩展到"提供完整 Agent 框架"的第一步。


2 月 25 日首次发布，一个月内从 44 Stars 涨到 8.7k Stars。v0.3.0 优化了子 Agent 和 cron 调度。


在 Agent 框架越来越多的当下，Hermes Agent 的差异化很明确：不是帮你写代码的助手，是一个住在服务器上、持续进化、不需要你在线也能干活的自主体。这个定位目前在开源领域还没有太多直接竞品。


这件事对行业的影响



从行业角度看，Hermes Agent 代表的是 AI Agent 从"工具"到"基础设施"的转变。


之前不管是 Claude Code 还是 Codex，本质上都是"你坐在电脑前，AI 帮你干活"。你关掉终端，它就停了。Hermes Agent 打破的是这个前提：Agent 不需要你在线，它自己住在服务器上，24 小时运转，持续学习，主动执行。


这其实是一个分水岭。当 Agent 不再依赖人类的实时在场，它就不再是"助手"了，它更像是一个"数字员工"，有自己的记忆、自己的技能库、自己的工作节奏。你不是在用一个工具，你是在雇一个不下班的同事。


开源加上 MIT 协议，意味着任何团队都可以拿来部署自己的"数字员工"。如果这个模式跑通，AI Agent 的竞争焦点就不再是"谁更聪明"，而是"谁积累的技能和记忆更多"，越早部署、用得越久的 Agent 就越强。这个飞轮一旦转起来，后来者很难追。


👉 官网 | GitHub | 文档

---

*来源：[Hermes Agent 一个会自我进化的 AI Agent 越用越强](https://www.xiaohu.ai/p/hermes-agent-ai-agent/31118826)*
