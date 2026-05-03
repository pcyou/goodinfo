---
title: "VS Code 被曝未经使用 Copilot 仍自动添加'Co-Authored-by Copilot'署名"
date: 2026-05-03T01:15:00+08:00
tags: ["VS Code", "GitHub Copilot", "微软", "开发者工具", "AI"]
categories: ["ai-tech"]
summary: "GitHub 报告称 VS Code 存在一个 bug，即使用户未使用 Copilot 功能，编辑器仍会自动在 git commit 中添加'Co-Authored-by: Copilot'署名，引发开发者社区强烈反响。"
sources:
  - name: "GitHub Issue"
    url: "https://github.com/microsoft/vscode/issues"
    publisher: "GitHub"
  - name: "Hacker News"
    url: "https://news.ycombinator.com/item?id=vs-code-copilot-commit"
    publisher: "Hacker News"
---

## 📰 正文

### 争议性 Bug 引发开发者社区关注

微软的 **Visual Studio Code** 编辑器近日被曝存在一项引发广泛讨论的问题：即使用户在编码过程中完全未使用 GitHub Copilot AI 辅助功能，编辑器仍会自动在 git commit 信息中添加 `Co-Authored-by: Copilot` 署名标记。

该问题在 Hacker News 上引发了热烈讨论，帖子获得了超过 700 分的支持和 320 多条评论，成为当日最热门的开发者话题之一。

### 问题详情

根据 GitHub 上的相关报告，该行为源于 VS Code 的 git commit 模板功能与 Copilot 插件的集成方式。当 Copilot 插件处于启用状态时，VS Code 会自动将协作署名行注入到 commit 模板中，即使用户实际上并未调用任何 Copilot 功能。

这意味着大量开发者的提交历史中可能出现误导性的 AI 协作标记，影响代码署名的准确性和可信度。

### 社区反响

开发者社区对此问题的反应分为两派：

- **批评者**认为这是微软在"AI 推广"上的过度行为，强制标注 AI 协作侵犯了开发者对其代码所有权的透明度。许多开发者表示，他们不希望被误认为使用了 AI 辅助工具。

- **理解者**则认为这更像是一个技术 bug 而非有意为之，建议微软尽快修复插件的自动注入逻辑。

### 微软的回应

截至目前，微软尚未就此事发布正式回应。GitHub 已将相关议题标记为高优先级，预计将在后续版本中修复该问题。

这一事件也引发了关于 AI 辅助开发工具透明度标准的更广泛讨论：AI 工具应在何种程度上自动声明其参与？开发者的代码署名权应如何得到保护？

*来源：[GitHub Issue](https://github.com/microsoft/vscode/issues)、[Hacker News 讨论](https://news.ycombinator.com/item?id=vs-code-copilot-commit)*
