---
title: "notebooklm-skill ：让 Claude Code） 可以直接查你在 NotebookLM 上的文档、笔记等"
date: 2025-11-04T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "notebooklm-skill 是一个为 Claude Code开发的插件（Skill），用于让 Claude Code 能直接与 Google NotebookLM 通信。   它让 Claude Code（AI 编程助手） 可以直接查你在 Google NotebookLM 上上传的文档，比如"
source_url: "https://www.xiaohu.ai/p/notebooklm-skill-claude-code-notebooklm/26590386"
xiahuid: "26590386"
---

## 📰 正文

notebooklm-skill 是一个为 Claude Code开发的插件（Skill），用于让 Claude Code 能直接与 Google NotebookLM 通信。


它让 Claude Code（AI 编程助手） 可以直接查你在 Google NotebookLM 上上传的文档，比如 PDF、网站、笔记等。


也就是说：

- 

你不用再打开浏览器去 NotebookLM 问；

- 

Claude 可以在命令行里直接帮你问；

- 

Claude 还会把答案引用到你自己的文档内容中；

- 

Claude 还能自动跟进问题，比如「能给我示例代码吗？」。



举个形象的例子：


以前：
1. 

你在 NotebookLM 浏览器问：“我上传的 PDF 里怎么配置数据库？”

2. 

复制 NotebookLM 的答案；

3. 

回到 Claude Code，把答案粘贴进去；

4. 

Claude 再根据答案帮你写代码。



现在：
Claude 直接帮你问 → 得到结果 → 写出正确代码。
你完全不用手动复制粘贴。


为什么要用这个插件？



Claude 自己找资料的方式有几个缺点：

![image]()


怎么安装？（真的很简单）



打开你的终端（命令行），复制下面几行：


```None
# 创建 Claude 技能文件夹（如果没有）
mkdir -p ~/.claude/skills

# 进入这个文件夹
cd ~/.claude/skills

# 克隆（下载）这个项目
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm

```



然后打开 Claude Code（本地版本，不是网页版），对它说：


```None
What are my skills?

```



它会告诉你：你现在有了一个新技能——notebooklm 🎉


怎么用？



1️⃣ 第一次用时，Claude 会提示你登录 Google。
它会自动打开 Chrome 浏览器，你登录就行了（安全的，本地执行）。


2️⃣ 去 https://notebooklm.google.com 上传你的文件：

- 

比如 PDF、网站链接、YouTube 视频都行。



3️⃣ 回到 Claude Code，告诉它：


```None
Add this NotebookLM to my library: [notebooklm链接]

```



这样它就“记住”你的笔记本。


4️⃣ 之后你可以直接问：


```None
Ask my Python notebook: how to use decorators?

```



Claude 会去 NotebookLM 查，然后告诉你答案，还标出引用出处。


GitHub：https://github.com/PleasePrompto/notebooklm-skill

---

*来源：[notebooklm-skill ：让 Claude Code） 可以直接查你在 NotebookLM 上的文档、笔记等](https://www.xiaohu.ai/p/notebooklm-skill-claude-code-notebooklm/26590386)*
