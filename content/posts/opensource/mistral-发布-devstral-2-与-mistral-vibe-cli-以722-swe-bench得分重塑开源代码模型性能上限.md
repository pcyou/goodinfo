---
title: "Mistral 发布 DevStral 2 与 Mistral Vibe CLI  以72.2% SWE-bench得分重塑开源代码模型性能上限"
date: 2025-12-10T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Mistral AI 发布了两个新的开源代码模型 —— Devstral 2（大型） 和 Devstral Small 2（小型）   以及一个智能命令行助手工具 Mistral Vibe CLI，能够直接在终端内实现自然语言驱动的代码探索、修改与执行。  -   Devstral 2 是一个超强的"
source_url: "https://www.xiaohu.ai/p/mistral-devstral-2-mistral-vibe-cli-72-2-swe-bench/27669943"
xiahuid: "27669943"
---

## 📰 正文

Mistral AI 发布了两个新的开源代码模型 —— Devstral 2（大型） 和 Devstral Small 2（小型）


以及一个智能命令行助手工具 Mistral Vibe CLI，能够直接在终端内实现自然语言驱动的代码探索、修改与执行。

- 

Devstral 2 是一个超强的 AI 编程助手模型，可以读懂并修改大规模代码库，修复 bug、优化架构、理解项目结构。

- 

它比很多闭源大模型（如 Claude Sonnet）便宜 7 倍，但性能接近。

- 

Devstral Small 2 是它的“轻量版”，可以在笔记本电脑上本地运行，支持图像输入。

- 

Mistral Vibe CLI 是一个命令行工具，能直接在终端或 IDE 中用自然语言写代码、运行命令、修改文件、管理 Git 项目。



Devstral 2 系列概览


![image]()

![image]()


🧠 模型能力

- 

理解超大代码库：256K 上下文窗口，这意味着它能理解整个项目架构，而不只是单个文件。

- 

自动调试与修复：能识别代码出错原因、自动重试、修复 bug。

- 

多文件协同修改：可以同时在多个文件中完成一致性修改，比如重构架构或迁移框架。

- 

支持特定语言优化：能微调成专攻某种语言（如 Python、Java、C++）。



📊 性能与效率

- 

在 SWE-bench Verified 测试中，Devstral 2 以 72.2% 得分，领先于其他开源同类模型。

- 

Devstral 2 (123B) 和 Devstral Small 2 (24B) 分别比 DeepSeek V3.2 小 5 倍和 28 倍，比 Kimi K2 小 8 倍和 41 倍，但性能几乎一样甚至更好。

![image]()

- 

评估中对比 Claude Sonnet 4.5、DeepSeek V3.2：

- 

胜率：对 DeepSeek V3.2 为 42.8%，略逊于 Claude Sonnet 4.5。


- 

性价比高达 Claude Sonnet 的 7倍。

- 

开源且可自定义微调，支持企业级本地部署与云端混合使用。

![image]()



💾 3模型体积与部署

- 

Devstral 2：适合服务器或数据中心（至少 4 块 H100 GPU）。

- 

Devstral Small 2：适合普通开发者，本地电脑或消费级 GPU 即可运行，甚至可以 CPU-only 运行。

- 

支持 NVIDIA NIM 部署（即将推出）。



💻 Mistral Vibe CLI —— 智能命令行助手



Vibe CLI 是一个基于 DevStral 模型的命令行智能代理（CLI Agent），用于实现终端层面的自然语言代码操作与项目自动化。


目标是将 AI 助理嵌入开发者日常的命令行工作流中，实现端到端代码自动化。


🧩 主要特性

- 

项目上下文感知：自动扫描文件结构与 Git 状态。

- 

自然语言交互：通过 @ 文件引用、! 执行命令、/ 配置命令。

- 

多文件编排：理解整个代码库，加速 Pull Request 周期（可减半）。

- 

插件与 IDE 支持：支持 Zed IDE 扩展与 Agent Communication Protocol。

- 

可编程控制：支持自动审批、配置本地模型与权限管理。

- 

可定制主题与历史记录保存。



```None
安装：curl -LsSf https://mistral.ai/vibe/install.sh | bash
```



📚与闭源体系的对比


![image]()


Mistral 的方向与 OpenAI、Anthropic 等闭源体系形成互补：
以开放性与高性价比为核心优势，推动开源智能体的工业化落地。


💰 定价与部署


- 

API 试用期免费，之后价格如下：

- 

Devstral 2: $0.40 / $2.00 每百万 tokens（输入/输出）

- 

Devstral Small 2: $0.10 / $0.30 每百万 tokens


- 

硬件要求：

- 

Devstral 2：≥4×H100 GPU（推荐数据中心环境）

- 

Devstral Small 2：单GPU甚至CPU-only即可运行


- 

支持平台：

- 

build.nvidia.com（试用）

- 

即将支持 NVIDIA NIM 框架

---

*来源：[Mistral 发布 DevStral 2 与 Mistral Vibe CLI  以72.2% SWE-bench得分重塑开源代码模型性能上限](https://www.xiaohu.ai/p/mistral-devstral-2-mistral-vibe-cli-72-2-swe-bench/27669943)*
