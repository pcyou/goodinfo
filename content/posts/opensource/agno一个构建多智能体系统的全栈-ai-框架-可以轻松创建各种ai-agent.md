---
title: "Agno：一个构建多智能体系统的全栈 AI 框架  可以轻松创建各种AI Agent"
date: 2025-06-03T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Agno 是一个为构建多智能体系统（Multi-Agent Systems）设计的全栈 AI 框架。   它集成了 推理（Reasoning）、记忆（Memory）、知识管理（Knowledge）、工具调用（Tooling） 和 Agent 团队协作（Agent Teams）。  >   你可以把它"
source_url: "https://www.xiaohu.ai/p/agno-ai-ai-agent/22028496"
xiahuid: "22028496"
---

## 📰 正文

Agno 是一个为构建多智能体系统（Multi-Agent Systems）设计的全栈 AI 框架。


它集成了 推理（Reasoning）、记忆（Memory）、知识管理（Knowledge）、工具调用（Tooling） 和 Agent 团队协作（Agent Teams）。

> 

你可以把它理解为一个“帮你快速创建 AI 助手团队”的开发工具箱。


这些 AI 助手可以具备：

- 

记忆力（记住用户上下文和历史）

- 

知识库（访问公司资料、文档等）

- 

推理能力（做决策、分析数据、生成总结）

- 

联网搜索（自动查找网页信息）

- 

多个助手分工协作（一个查资料，一个算数据，一个写报告）




它能做什么？


Agno 可以帮助你：

![image]()


✅ 支持的智能体系统 5 个等级


![image]()


亮点与优势


![image]()

- 

模型支持（Model Agnostic）：支持 23+ 个模型提供商（包括 OpenAI、Anthropic 等），不受模型平台绑定。

- 

高性能架构：

- 

启动时间：约 3 微秒

- 

平均内存占用：仅 6.5 KiB


- 

三种推理机制支持：

- 

内置推理模型

- 

ReasoningTools 工具集

- 

自定义 Chain-of-Thought（思维链）流程


- 

原生多模态支持：输入/输出可为文本、图像、音频、视频等

- 

Agentic RAG 与向量搜索：集成 20+ 向量数据库，支持异步、高效的实时搜索

- 

内建长期记忆与会话存储（Memory & Session Storage）

- 

结构化输出支持：支持 JSON 类型化结构输出（含 json_mode）

- 

一键部署 API 接口：内置 FastAPI 路由，助力从开发到上线一键切换

- 

实时监控：通过 agno.com 实时监控 agent 的运行和性能



主要模块与组件说明



1. agno.agent.Agent


- 

核心构建单体 agent 的类。

- 

参数说明：

- 

model: 使用的语言模型（如 Claude、GPT-4）

- 

tools: 工具列表（可查股价、搜索网页等）

- 

instructions: 给 agent 的行为指令

- 

markdown: 输出是否启用 markdown 格式




2. agno.models


- 

提供统一接口支持超过 23 个模型提供商，包括：

- 

OpenAI（gpt-3.5、gpt-4）

- 

Anthropic（Claude）

- 

Google、Mistral、Cohere 等




3. agno.tools


- 

工具库，包括：

- 

YFinanceTools: 获取股票价格、公司信息

- 

DuckDuckGoTools: 网页搜索

- 

ReasoningTools: 提供结构化推理逻辑

- 

可自定义扩展自有工具（如爬虫、数据库等）




4. agno.team.Team


- 

多个 Agent 组成一个团队，每个 agent 分配职责。

- 

参数包括：

- 

members: agent 成员列表

- 

mode: 协作模式（如 "coordinate"）

- 

success_criteria: 成功判定标准

- 

instructions: 整体任务指令




5. agno.memory 与 agno.storage


- 

支持长短期记忆与会话状态存储。

- 

可对接向量数据库用于 RAG 检索。



性能测试（vs LangGraph）


- 

在 Apple M4 MacBook Pro 上对比测试：

- 

Agno 启动时间远快于 LangGraph

- 

更低内存开销，适用于高并发 Agent 系统


- 

提供脚本进行 agent instantiation 与 memory usage 基准测试



案例展示



你想做一个「自动生成公司财报摘要」的 AI 助手系统：
1. 

它用网页搜索 Agent 去查行业新闻

2. 

再用财经数据 Agent 去拉股价和财报数据

3. 

最后由总结 Agent 整合出一份 PDF 报告



这就是 Agno 可以帮你做的系统。 你只需要配置这些 Agent，然后它会自动调用工具、合作执行任务。


🧪 示例：构建金融推理智能体


```None
from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            company_info=True, 
            company_news=True
        )
    ],
    instructions=[
        "Use tables to display data", 
        "Only output the report, no other text"
    ],
    markdown=True
)

agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True
)
```



🤝 多智能体协作示例（Agent Teams）


```None
from agno.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True
)

team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    success_criteria="A comprehensive financial news report with clear sections and data-driven insights.",
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True
)

team.print_response(
    "What's the market outlook and financial performance of AI semiconductor companies?",
    stream=True
)
```



部署方式



Agno 提供了预构建的 FastAPI 路由，可以做到 0 到部署只需几分钟：


```None
# 创建环境并安装依赖
uv venv --python 3.12
source .venv/bin/activate
uv pip install agno anthropic yfinance duckduckgo-search
export ANTHROPIC_API_KEY=sk-xxx
python reasoning_agent.py

```



GitHub 地址：https://github.com/agno-agi/agno
文档官网：https://docs.agno.com/

---

*来源：[Agno：一个构建多智能体系统的全栈 AI 框架  可以轻松创建各种AI Agent](https://www.xiaohu.ai/p/agno-ai-ai-agent/22028496)*
