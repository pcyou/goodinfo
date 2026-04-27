---
title: "GPT Newspaper ：AI自动新闻生成系统 自动创建属于你个人的“定制报纸”"
date: 2025-12-11T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "GPT Newspaper 是一个由人工智能驱动的自动新闻生成系统。 它的目标是：  >   根据用户的兴趣、喜好和偏好来源，自动创建属于你个人的“定制报纸”。   它会自动上网找新闻、写文章、排版、出版，让你每天收到只包含你感兴趣内容的个性化报纸。    这个项目基于 OpenAI GPT 模型"
source_url: "https://www.xiaohu.ai/p/gpt-newspaper-ai/27710276"
xiahuid: "27710276"
---

## 📰 正文

GPT Newspaper 是一个由人工智能驱动的自动新闻生成系统。
它的目标是：

> 

根据用户的兴趣、喜好和偏好来源，自动创建属于你个人的“定制报纸”。


它会自动上网找新闻、写文章、排版、出版，让你每天收到只包含你感兴趣内容的个性化报纸。



这个项目基于 OpenAI GPT 模型 + LangChain LangGraph 框架，通过多个智能子代理（agents）协同工作，实现从“找新闻”到“排版出版”的全流程自动化。


主要功能特点


- 

个性化内容：根据你的偏好（如主题、地区、来源）自动定制新闻。

- 

多元来源：聚合多个可信新闻网站内容。

- 

自然语言写作：由 GPT 模型生成流畅文章。

- 

自动设计与排版：生成类似真实报纸的美观布局。

- 

高质量审稿流程：由 Critique Agent 多轮反馈修正，保证内容质量。

- 

轻松使用：用户只需设置兴趣偏好，即可定期收到个性化报纸。



系统组成（六大智能代理）



GPT Newspaper 拥有 6 个独立但互相协作的 AI 代理（Agents），每个都有独特职责：
1. 

🔎 Search Agent（搜索代理）

- 

自动在网络上搜集最新、最相关的新闻内容。

- 

使用 Tavily API 来执行搜索。


2. 

🗂️ Curator Agent（策展代理）

- 

根据用户定义的兴趣和偏好筛选新闻。

- 

确保内容贴合用户口味（比如科技、体育、财经等）。


3. 

✍️ Writer Agent（写作代理）

- 

基于选中的新闻生成流畅、自然、可读的文章。

- 

相当于 AI 记者。


4. 

🧩 Critique Agent（审稿代理）

- 

对 Writer 生成的内容进行反馈和修改，直到达到“可发表”标准。

- 

起到人工主编审核的作用。


5. 

🎨 Designer Agent（排版代理）

- 

负责报纸的视觉设计和版面布局。

- 

确保阅读体验美观、有层次感。


6. 

📰 Editor & Publisher Agent（编辑与出版代理）

- 

整合所有文章、图片、版式，生成完整的“报纸”。

- 

可自动发布到前端网站或电子邮箱。





![image]()



安装与使用（简易指南）



🧩 前置条件



你需要：

- 

一个 OpenAI API Key

- 

一个 Tavily API Key



🧱 安装步骤



```None
# 1. 克隆项目
git clone https://github.com/rotemweiss57/gpt-newspaper.git
cd gpt-newspaper

# 2. 设置环境变量
export OPENAI_API_KEY=<你的OpenAI密钥>
export TAVILY_API_KEY=<你的Tavily密钥>

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行项目
python app.py
```



🌐 打开浏览器访问：



```None
http://localhost:5000/
```



然后你可以在网页界面设置兴趣和偏好，生成属于你的“AI 报纸”。

---

*来源：[GPT Newspaper ：AI自动新闻生成系统 自动创建属于你个人的“定制报纸”](https://www.xiaohu.ai/p/gpt-newspaper-ai/27710276)*
