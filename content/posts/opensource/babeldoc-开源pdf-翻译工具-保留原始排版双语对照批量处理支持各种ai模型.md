---
title: "BabelDOC ： 开源PDF 翻译工具 保留原始排版、双语对照、批量处理、支持各种AI模型"
date: 2025-04-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "BabelDOC 是一个基于大语言模型（如GPT-4）的开源 PDF 文档翻译工具，它可以：  >   ✅ 把英文 PDF 翻译成中文， ✅ 翻译结果要像原文一样排版漂亮， ✅ 还能“对照阅读”原文和翻译， ✅ 支持自部署，支持离线使用！    主要特点：  -   结构感知翻译（保留原始排版）"
source_url: "https://www.xiaohu.ai/p/babeldoc-pdf-ai/20458944"
xiahuid: "20458944"
---

## 📰 正文

BabelDOC 是一个基于大语言模型（如GPT-4）的开源 PDF 文档翻译工具，它可以：

> 

✅ 把英文 PDF 翻译成中文，
✅ 翻译结果要像原文一样排版漂亮，
✅ 还能“对照阅读”原文和翻译，
✅ 支持自部署，支持离线使用！



主要特点：

- 

结构感知翻译（保留原始排版）

- 

LLM 接入灵活（支持 OpenAI 类接口）

- 

自部署能力强（支持 在线使用、命令行使用、自部署与 Python API 接入）

- 

插件式架构（方便扩展 OCR、段落分组等）



该项目优于传统基于 Word/PDF 的翻译流程，是中高端科研、出版、出海文档处理首选方案之一。

![image]()


主要功能：


![image]()

- 

🧾 支持中英翻译（支持英文→中文，基本支持中文→英文）

- 

📄 保留页面结构、图表、段落、字体排版等

- 

📦 一键生成双语 PDF（并排或交替展示）

- 

🧰 提供命令行 + Python API + Web 页面三种方式使用

- 

🔧 支持自定义配置（包括模型、页码、输出格式）

- 

🚫 不依赖传统翻译引擎（如 Google/Bing），完全 LLM 驱动

- 

🌐 支持连接多种兼容 OpenAI 接口的模型（支持本地模型如 Ollama）


![image]()

![image]()

![image]()


高级特性


![image]()


CLI 功能详解（babeldoc）

![image]()

- 

--pages: 指定翻译页码范围（如 1-5, 7, 10-）

- 

--lang-in / --lang-out: 设置原文/目标语言（如 en ➜ zh）

- 

--watermark-output-mode: 输出是否含水印 / 输出多个版本

- 

--use-alternating-pages-dual: 是否交替页展示中英文

- 

--max-pages-per-part: 对长文自动分页翻译

- 

--skip-clean: 跳过清理步骤（提升兼容性）

- 

--disable-rich-text-translate: 关闭加粗/斜体等复杂文本翻译

- 

--translate-table-text: 启用表格翻译（实验性）



支持通过 .toml 配置文件集中管理以上参数。


适合谁用？


![image]()


🚀 怎么用？



方式一：网页版（简单）

- 

网站入口：BabelDOC 在线版

- 

每月免费翻译 1000 页

- 

不需要安装任何东西



方式二：命令行（适合开发者）


```None
uv tool install --python 3.12 BabelDOC

babeldoc --files paper.pdf --openai --openai-model "gpt-4o-mini" --openai-api-key "你的密钥"
```



还可以设定翻译页数、输出路径、模型种类、翻译速度等。


方式三：自己部署（高级玩法）

- 

支持导出“离线包”

- 

可以在公司/服务器环境运行

- 

支持设置代理、API网关、本地模型



LLM 模型支持情况


- 

默认支持：OpenAI 系列模型（GPT-4o-mini、gpt-3.5、gpt-4）

- 

兼容接入：

- 

DeepSeek、GLM-4、Baichuan、Yi 等 OpenAI 接口兼容模型

- 

可通过 --openai-base-url + --api-key 实现私服部署（如 Ollama）


- 

使用建议：调用推荐通过 LiteLLM 接入多模型网关



技术架构与核心流程



🔧 核心模块流程（双阶段架构）

![image]()


🌉 插件机制（可插拔式）

- 

支持添加：

- 

LLM 翻译器

- 

OCR 模块

- 

结构优化器（段落重构、跨页处理）

- 

渲染器/导出器


- 

配置文件支持插件优先级与并行策略



GitHub：https://github.com/funstory-ai/BabelDOC 


在线体验：https://app.immersivetranslate.com/babel-doc/ 


测试结果：

---

*来源：[BabelDOC ： 开源PDF 翻译工具 保留原始排版、双语对照、批量处理、支持各种AI模型](https://www.xiaohu.ai/p/babeldoc-pdf-ai/20458944)*
