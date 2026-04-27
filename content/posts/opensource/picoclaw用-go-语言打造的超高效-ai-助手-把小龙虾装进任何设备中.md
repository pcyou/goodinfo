---
title: "PicoClaw：用 Go 语言打造的超高效 AI 助手 把小龙虾装进任何设备中"
date: 2026-02-12T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "PicoClaw 是Sipeed发布的一个超轻量级 AI 助手，用 Go 语言编写，主打在极低成本硬件上运行 AI Agent。  >   超轻量级 AI Agent 助手，专为“低成本硬件 + 超低内存”设计。    它不是在本地跑大模型，而是作为一个超轻量的Agent 客户端，通过 API"
source_url: "https://www.xiaohu.ai/p/picoclaw-go-ai/29608276"
xiahuid: "29608276"
---

## 📰 正文

PicoClaw 是Sipeed发布的一个超轻量级 AI 助手，用 Go 语言编写，主打在极低成本硬件上运行 AI Agent。

> 

超轻量级 AI Agent 助手，专为“低成本硬件 + 超低内存”设计。



它不是在本地跑大模型，而是作为一个超轻量的 "Agent 客户端"，通过 API 调用云端的大模型（比如 Claude、GPT、智谱 GLM 等），同时在本地执行文件操作、网页搜索、任务规划等 Agent 能力。


官方口号：

- 

💰 $10 硬件运行

- 

🧠 < 10MB 内存占用

- 

⚡ 1 秒启动

- 

🦐 “皮皮虾，我们走！


![image]()


之所以能做到这么轻，核心原因是用 Go 语言重写了整个项目。Go 编译出来就是一个单独的二进制文件，不需要 Node.js 运行时，不需要 Python 解释器和一堆依赖包，直接丢到设备上就能跑。


核心亮点：


- 

极致轻量：内存占用不到 10MB，启动时间 1 秒（0.6GHz 单核），单个二进制文件跨 RISC-V、ARM、x86 三种架构运行。对比 TypeScript 版的 "OpenClaw"（需要 1GB+ RAM）和 Python 版的 NanoBot（100MB+ RAM），资源消耗降了 99%。

![image]()

- 

超低成本部署：最低可以跑在 9.9 美元的 LicheeRV-Nano 上，也支持 NanoKVM、MaixCAM 等 Sipeed 自家硬件，适合做家庭助手、服务器运维自动化、智能监控等场景。

![image]()

- 

AI 自举开发：项目声称 95% 的核心代码是由 AI Agent 自主生成的，灵感来自 HKUDS 的 nanobot 项目，从 Python 重构到 Go 的过程也是 AI 驱动的。

- 

多渠道接入：支持 Telegram、Discord、QQ、钉钉等聊天平台，配合 OpenRouter、智谱、Anthropic、OpenAI 等多种 LLM 后端，还支持 Brave Search 做网页搜索。



主要功能特点



1. 全栈 AI Agent 能力



虽然体积小，但该有的 Agent 功能都有：

- 

对话交互：支持命令行聊天和交互模式

- 

工具调用：可以执行代码、操作文件、做任务规划

- 

网页搜索：集成 Brave Search API，能联网查资料

- 

语音转文字：配合 Groq 的 Whisper 服务，Telegram 上发语音消息也能识别



2. 多模型后端支持



不绑定某一家 LLM，支持的模型提供商包括：

- 

OpenRouter（推荐，一个 key 可以用 Claude、GPT-4 等多种模型）

- 

智谱 AI（国内用户友好，GLM-4 系列）

- 

Anthropic（Claude 直连）

- 

OpenAI（GPT 直连）

- 

Google Gemini

- 

DeepSeek

- 

Groq（免费额度，还支持语音转写）



3. 多聊天平台接入



不只是命令行工具，还能变成你的聊天机器人：

- 

Telegram（推荐，配置最简单）

- 

Discord

- 

QQ

- 

钉钉

- 

飞书（配置文件里有，但还在开发中）



也就是说，你可以在一块 10 美元的开发板上跑这个程序，然后通过 Telegram 跟它聊天，让它帮你干活。


4. 跨架构单文件部署



编译后就是一个二进制文件，支持三种 CPU 架构：

- 

x86_64（普通电脑）

- 

ARM64（树莓派、手机芯片等）

- 

RISC-V（Sipeed 自家的低成本开发板）



不需要安装任何依赖，拷贝过去就能用。


5. AI 自举开发



项目号称 95% 的核心代码是 AI Agent 自己写的，灵感来自香港大学的 nanobot 项目（Python 版），整个从 Python 到 Go 的架构迁移和代码优化都是 AI 驱动完成的。


6.记忆系统（结构很清晰）



它有一个本地工作空间：


```None
~/.picoclaw/workspace/

```



里面包括：

- 

sessions/ → 对话历史

- 

memory/ → 长期记忆

- 

cron/ → 定时任务

- 

skills/ → 自定义技能

- 

AGENTS.md → 行为规则

- 

IDENTITY.md → 身份设定

- 

SOUL.md → 性格设定



这个设计很有意思。


它把 Agent 的：

- 

人格

- 

行为

- 

偏好

- 

技能



都文件化。


这是一种非常“工程化”的 Agent 设计。


---



适合跑在哪些硬件上？



9.9美元的LicheeRV-Nano， 有带网口和WiFi6两个版本，是最低成本方案，适合做一个永远在线的家庭AI小助手。


30到100美元的NanoKVM， 这是一个远程KVM设备，本身就有联网能力和Linux系统，跑PicoClaw之后可以做服务器自动化运维，AI帮你巡检、排故障。


50到100美元的MaixCAM系列， 自带摄像头，跑PicoClaw之后可以做智能监控，比如检测到有人进入画面就自动通知你。


当然，这些只是推荐场景。任何能跑Linux的设备都可以，树莓派、旧手机刷Linux、甚至路由器理论上都行。


项目推荐了几个 Sipeed 自家的硬件场景：

![image]()


当然，任何能跑 Linux 的设备都行，树莓派、旧手机刷 Linux、云服务器都没问题。


怎么用？分三步



第一步：安装



方式一：下载预编译包（最简单）


去 GitHub Releases 页面 下载对应平台的二进制文件就行。


方式二：从源码编译（开发者推荐）


bash


```bash
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw
make deps
make build        # 编译当前平台
# 或者
make build-all    # 编译所有平台
make install      # 编译并安装到系统路径
```



第二步：配置



先初始化：


bash


```bash
picoclaw onboard
```



这会在 ~/.picoclaw/ 目录下生成配置文件。然后编辑 ~/.picoclaw/config.json，核心要填的就是 LLM 的 API Key：


json


```json
{
  "agents": {
    "defaults": {
      "model": "glm-4.7",
      "max_tokens": 8192,
      "temperature": 0.7
    }
  },
  "providers": {
    "zhipu": {
      "api_key": "你的智谱API Key",
      "api_base": "https://open.bigmodel.cn/api/paas/v4"
    }
  }
}
```



如果想用网页搜索功能，再加上 Brave Search 的 key（免费额度每月 2000 次查询）：


json


```json
{
  "tools": {
    "web": {
      "search": {
        "api_key": "你的Brave Search API Key",
        "max_results": 5
      }
    }
  }
}
```



API Key 从哪来？

![image]()


第三步：开聊



单次提问：


bash


```bash
picoclaw agent -m "帮我写一个Python脚本，批量重命名文件夹里的图片"
```



交互模式（持续对话）：


bash


```bash
picoclaw agent
```



启动聊天网关（接入 Telegram/Discord 等）：


bash


```bash
picoclaw gateway
```



---



常用命令速查


![image]()


典型应用场景


1️⃣ 家庭 AI 助手



部署在：

- 

LicheeRV-Nano（$9.9）

- 

NanoKVM

- 

MaixCAM



可以作为：

- 

本地 AI 管家

- 

自动化服务器助手

- 

智能监控助手



---



2️⃣ 低成本边缘设备部署



适合：

- 

IoT 设备

- 

嵌入式 Linux

- 

低算力服务器



---



3️⃣ 自动化运维



结合 cron + LLM：

- 

自动巡检

- 

自动维护

- 

定时报告



🔗 项目地址：https://github.com/sipeed/picoclaw

---

*来源：[PicoClaw：用 Go 语言打造的超高效 AI 助手 把小龙虾装进任何设备中](https://www.xiaohu.ai/p/picoclaw-go-ai/29608276)*
