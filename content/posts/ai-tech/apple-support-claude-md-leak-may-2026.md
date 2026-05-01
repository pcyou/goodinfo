---
title: "🍎 苹果 Apple Support 应用意外泄露 Claude.md 配置文件，紧急发布补丁修复"
date: 2026-05-02T14:00:00+08:00
tags: ["Apple", "Anthropic", "Claude", "安全漏洞", "Claude.md", "软件工程"]
categories: ["ai-tech"]
summary: "苹果在 Apple Support 应用 v5.13 更新中意外泄露了 Claude.md 配置文件，暴露了其使用 Claude Code 进行软件开发的内部工作流程，随后紧急发布 v5.13.1 修复版本。"
sources:
  - name: "Apple accidentally left Claude.md files Apple Support app"
    url: "https://xcancel.com/aaronp613/status/2049986504617820551"
    publisher: "X (via XCancel)"
  - name: "Hacker News discussion"
    url: "https://news.ycombinator.com/"
    publisher: "Hacker News"
---

# 苹果 Apple Support 应用意外泄露 Claude.md 配置文件，紧急发布补丁修复

> 🕐 更新时间：2026-05-02 14:00 CST | 这起意外事件引发了关于 AI 辅助开发安全和苹果软件工程实践的热议。

---

2026年4月30日，科技研究员 Aaron（@aaronp613）在社交媒体上爆料称，苹果在当天的 Apple Support 应用更新（v5.13）中，意外地将内部 Claude.md 配置文件打包进了应用安装包中。

## 什么是 Claude.md？

Claude.md 是 Anthropic 为 Claude Code AI 编程助手设计的配置文件，开发者使用它来指导 Claude 理解项目的代码库结构、编码规范和开发流程。这类文件通常包含公司内部的开发约定、架构决策和最佳实践——相当于"告诉 AI 如何像公司内部开发者一样思考和编码"。

将这类文件泄露到公开发布的应用中，相当于暴露了苹果内部软件工程的工作流程和开发规范。

## 苹果的紧急响应

该推文在发布后迅速走红，获得了超过 136 万次浏览、1 万多次转发和 662 次引用。在舆论发酵后，苹果迅速作出了反应。

大约 3 小时后，Aaron 发布后续推文称："我猜苹果看到了我的推文。苹果已紧急发布 Apple Support 应用 v5.13.1 更新，移除了 Claude.md 文件。"

这一响应速度在科技公司中相当罕见，表明苹果对此类信息泄露事件高度重视。

## 事件揭示的更大背景

这次意外泄露引发了关于苹果 AI 辅助开发实践的广泛讨论：

- **Claude 在苹果内部的广泛使用**：多位评论者指出，苹果员工每天拥有超过 200 美元的 Claude 额度用于日常开发工作。这表明 Claude Code 已成为苹果软件工程流程中的重要工具。

- **Mythos 模型的使用**：有评论者透露，苹果已通过 Glasswing 平台在其自有基础设施上运行 Mythos 预览版。考虑到五角大楼刚刚将 Mythos 标记为"独立的国家安全问题"，这一信息格外引人注目。

- **AI 辅助开发的安全隐患**：正如一位评论者所言："过去我们担心泄露 API 密钥，现在我们还得担心泄露告诉 AI 公司思考方式的 Markdown 文件。"

## 行业影响

这起事件凸显了 AI 辅助软件开发时代的新安全挑战。随着越来越多的科技公司采用 Claude Code 等 AI 编程工具，如何防止配置文件、提示词工程和内部开发约定的意外泄露，正成为一个亟待解决的新问题。

*Source: [X/Twitter](https://xcancel.com/aaronp613/status/2049986504617820551), [Hacker News](https://news.ycombinator.com/)*
