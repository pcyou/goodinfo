---
title: "OpenAI 发布了一个插件 把 Codex 塞进了 Claude Code：竞争对手的代码审查员，现在随叫随到"
date: 2026-03-31T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "OpenAI 官方发布了一个 Claude Code 插件 codex-plugin-cc，让你在 Claude Code 里直接调用 Codex 做代码审查、对抗性审查，甚至把整个任务丢给 Codex 接管。   这件事有意思的地方不在插件本身，在于谁做的：OpenAI，主动把自己的工具送进了 A"
source_url: "https://www.xiaohu.ai/p/openai-codex-claude-code/31183880"
xiahuid: "31183880"
---

## 📰 正文

OpenAI 官方发布了一个 Claude Code 插件 codex-plugin-cc，让你在 Claude Code 里直接调用 Codex 做代码审查、对抗性审查，甚至把整个任务丢给 Codex 接管。


这件事有意思的地方不在插件本身，在于谁做的：OpenAI，主动把自己的工具送进了 Anthropic 的地盘。


Claude Code 有自己的插件生态，OpenAI 这次以官方身份入场，等于说"你用 Claude 写代码没问题，但让 Codex 帮你再看一眼"。


能干什么：三个核心命令



① /codex:review 标准代码审查



最基础的用法。跑一遍你当前的未提交改动，或者指定一个分支做 diff 对比审查。只读，不改代码，审完给你一份报告。


```None
/codex:review --base main
```



效果和在 Codex 里直接跑 /review 一样，审查质量不打折。好处是你不用切窗口，在 Claude Code 的对话流里就能拿到第二个 AI 的意见。


② /codex:adversarial-review 对抗性审查



这个比普通审查狠。它不是帮你找 bug，是专门挑战你的设计决策，试图把你代码里的隐藏假设翻出来。


```None
/codex:adversarial-review --base main "重点看权限校验逻辑"
```


> 

你在做数据库迁移、改鉴权逻辑、写基础设施脚本这类高风险操作时，Claude 写完你不放心，让 Codex 以"找茬"的视角再过一遍。两个 AI 从不同角度看同一段代码，比一个 AI 自己审自己靠谱得多。



同样是只读，不动你的代码。你可以加 --background 让它后台跑，回头用 /codex:status 看进度。


③ /codex:rescue 任务移交



Claude 写代码写到一半卡住了，或者你觉得这个任务换个 AI 来可能更合适，直接把活交给 Codex：


```None
/codex:rescue "排查这个内存泄漏问题"
```



Codex 会启动一个独立的子 Agent 来接手。支持 --resume 继续上次的进度，也支持 --fresh 从头来过。任务完成后用 /codex:result 拿结果，还能拿到 Codex 的 session ID，方便你后续直接在 Codex 里继续跟进。


技术架构：没有额外运行时



插件不是一个独立的服务。它通过你本地已经装好的 Codex CLI 和 app server 做中转，复用你现有的认证、配置、环境变量、MCP 设置。


换句话说，如果你的 Codex 已经配好了（模型选择、推理强度、工具权限），插件直接继承这些配置，不用重新设一遍。


你也可以在项目级别或用户级别的 config.toml 里调默认参数：


```None
model = "gpt-5.4-mini"
model_reasoning_effort = "xhigh"
```



五步安装



```None
# 1. 添加插件市场
/plugin marketplace add openai/codex-plugin-cc

# 2. 安装插件
/plugin install codex@openai-codex

# 3. 重载插件
/reload-plugins

# 4. 运行安装检查
/codex:setup

# 5. 如果没登录过 Codex，认证一下
!codex login
```



/codex:setup 会自动检测你有没有装 Codex CLI，没装的话会提示全局安装。


前提条件


- 

ChatGPT 订阅（免费版也行）或 OpenAI API key

- 

Node.js 18.18 或更高版本

- 

Codex 的用量会计入你的 ChatGPT/API 额度



Review Gate：好用但危险的自动门控



插件有一个可选功能叫 Review Gate。开启后，Claude Code 每次执行完操作，会自动触发一次 Codex 审查。如果 Codex 发现问题，Claude 会被阻止退出，必须先处理审查意见。


听起来很美：写完代码自动审查，有问题自动修。


但 VB Srivastav（插件作者）自己提醒了：这可能导致 Claude 和 Codex 互相触发，形成循环。Claude 改了代码触发 Codex 审查，Codex 提了意见 Claude 又改，改完又触发审查... 额度会被快速消耗。


建议： 只在你盯着屏幕的时候开 Review Gate，别开着就去泡茶。


更大的背景：Codex 插件生态



codex-plugin-cc 不是一个孤立的动作。OpenAI 同期给 Codex 上线了完整的插件系统，包括：

- 

Skills： 自动化工作流，可以把自然语言指令和脚本打包成可复用的技能

- 

MCP 集成： 通过 Model Context Protocol 连接外部服务

- 

配置同步： 团队成员之间共享 Codex 配置，避免代码风格不一致



插件目录里已经有十几个预置集成，能编辑 Google Drive 文件、审查 GitHub 仓库变更等。Anthropic 大约五个月前给 Claude Code 做了类似的生态（子 Agent、第三方工具接入），OpenAI 这次算是正面跟上了。


codex-plugin-cc 这步棋很巧妙：把 Codex 变成 Claude Code 用户工作流里的一部分。你继续用 Claude Code 写代码，审查和兜底交给 Codex。用着用着，Codex 的存在感就建立起来了。


已知限制


- 

多文件变更的审查可能比较慢，建议用 --background 后台运行

- 

Review Gate 有额度消耗失控风险，需要人工监控

- 

插件依赖本地 Codex CLI，不是云端服务，你的机器需要保持运行

- 

目前只能从 Claude Code 调 Codex，反过来不行



获取方式



GitHub 仓库已开源，按上面五步安装即可。不需要额外申请，有 ChatGPT 账号（包括免费版）就能用。


原推文附有视频演示，可以看到插件在 Claude Code 中的实际操作效果。


👉 GitHub 仓库 | OpenAI 社区公告 |

---

*来源：[OpenAI 发布了一个插件 把 Codex 塞进了 Claude Code：竞争对手的代码审查员，现在随叫随到](https://www.xiaohu.ai/p/openai-codex-claude-code/31183880)*
