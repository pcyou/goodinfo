---
title: "微软 MarkItDown：一行命令把 PDF、Word、PPT、音频、YouTube 全转成干净 Markdown"
date: 2026-04-09T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "微软开源了一个 Python 工具叫 MarkItDown，干一件事：把各种格式的文件转成 LLM 能直接用的 Markdown。   PDF、Word、Excel、PowerPoint、HTML、图片、音频、YouTube 链接、JSON、XML、ZIP 压缩包，基本上你能想到的格式它都支持。"
source_url: "https://www.xiaohu.ai/p/markitdown-pdf-word-ppt-youtube-markdown/31499902"
xiahuid: "31499902"
---

## 📰 正文

微软开源了一个 Python 工具叫 MarkItDown，干一件事：把各种格式的文件转成 LLM 能直接用的 Markdown。


PDF、Word、Excel、PowerPoint、HTML、图片、音频、YouTube 链接、JSON、XML、ZIP 压缩包，基本上你能想到的格式它都支持。


一个 pip install 搞定，命令行或 Python API 都能用。


为什么需要这个



做 RAG 管线或者给 LLM 喂文档的人都知道，最头疼的不是模型，是数据预处理。


PDF 的表格解析错乱，Word 的样式被吃掉，PPT 的布局信息全丢，Excel 变成一堆逗号分隔的数字。每种格式要写一个解析器，写完还得维护，换个格式又得重来。


MarkItDown 把这一层全抹平了。不管输入什么格式，输出都是结构清晰的 Markdown：标题、列表、表格、链接、代码块全部保留。


支持哪些格式


![image]()


图片描述和音频转写需要接 LLM（支持 OpenAI API 格式），不接也能用，只是跳过这些功能。


怎么用



安装：


```None
pip install 'markitdown[all]'
```



也可以只装需要的格式：pip install 'markitdown[pdf,docx,pptx]'


命令行：


```None
markitdown report.pdf > report.md
markitdown slides.pptx -o slides.md
cat document.pdf | markitdown
```



Python API：


```None
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("quarterly-report.xlsx")
print(result.text_content)
```



如果要让图片生成描述文字：


```None
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("photo.jpg")
```



两个值得关注的能力



1. MCP Server


MarkItDown 现在有官方的 MCP（Model Context Protocol）服务器，可以直接接入 Claude Desktop 等支持 MCP 的 AI 客户端。


实际效果是：你在跟 Claude 对话的时候，可以直接让它读取并转换本地文件，不用提前手动处理。对话流程不中断，文件转换在后台自动完成。


2. 插件系统


0.1.0 版本引入了第三方插件支持。比如 markitdown-ocr 插件，给 PDF、Word、PPT、Excel 里的嵌入图片加上 OCR 能力，用 LLM Vision 提取图片中的文字。


社区可以自己开发新格式的转换器，不需要改源代码。在 GitHub 上搜 #markitdown-plugin 就能找到已有的插件。


已知限制



不回避几个短板：

- 

PDF 如果是扫描件且没有 OCR 层，提取不出文字

- 

PDF 转换时会丢失标题、列表等文本格式，全变成纯文本

- 

图片内容描述需要外接 LLM 客户端，不能开箱即用

- 

本质上是对 mammoth、pandas 等现有库的封装，不是从零写的转换引擎



对于 RAG 管道和批量文档处理的场景已经够用了。如果追求高保真的文档还原（比如保留排版给人看），这不是它的设计目标。


适合谁


- 

做 RAG 系统，需要批量把企业文档灌进向量数据库的开发者

- 

用 Claude Code 或其他 AI 编程工具，需要快速读取各种格式文件的人

- 

搭 AI Agent，需要让 Agent 自主处理文档的场景



GitHub：https://github.com/microsoft/markitdown

---

*来源：[微软 MarkItDown：一行命令把 PDF、Word、PPT、音频、YouTube 全转成干净 Markdown](https://www.xiaohu.ai/p/markitdown-pdf-word-ppt-youtube-markdown/31499902)*
