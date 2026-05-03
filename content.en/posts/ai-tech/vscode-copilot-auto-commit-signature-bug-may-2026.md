---
title: "VS Code Bug Automatically Adds 'Co-Authored-by Copilot' to Commits Regardless of Usage"
date: 2026-05-03T01:15:00+08:00
tags: ["VS Code", "GitHub Copilot", "Microsoft", "developer tools", "AI"]
categories: ["ai-tech"]
summary: "GitHub reports that VS Code has a bug where the editor automatically adds 'Co-Authored-by: Copilot' to git commits even when users haven't used Copilot, sparking significant debate in the developer community."
sources:
  - name: "GitHub Issue"
    url: "https://github.com/microsoft/vscode/issues"
    publisher: "GitHub"
  - name: "Hacker News"
    url: "https://news.ycombinator.com/item?id=vs-code-copilot-commit"
    publisher: "Hacker News"
---

## 📰 Article

### Controversial Bug Sparks Developer Community Debate

Microsoft's **Visual Studio Code** editor has been found to have an issue generating significant discussion: even when users haven't used the GitHub Copilot AI assistance feature at all during their coding session, the editor automatically adds a `Co-Authored-by: Copilot` attribution line to git commit messages.

The issue ignited a heated discussion on Hacker News, with the post garnering over 700 upvotes and more than 320 comments, making it one of the hottest developer topics of the day.

### The Issue

According to reports on GitHub, the behavior stems from how VS Code's git commit template feature integrates with the Copilot extension. When the Copilot extension is enabled, VS Code automatically injects the co-authorship line into the commit template, even if the user never actually invoked any Copilot functionality.

This means many developers' commit histories may contain misleading AI collaboration markers, affecting the accuracy and credibility of code attribution.

### Community Response

The developer community's reaction has been divided:

- **Critics** view this as an overreach in Microsoft's "AI push," arguing that forced AI attribution undermines developer transparency regarding their code ownership. Many developers expressed that they don't want to be falsely labeled as having used AI assistance.

- **Understanding voices** see this as more of a technical bug than intentional behavior, suggesting Microsoft should quickly fix the extension's auto-injection logic.

### Microsoft's Response

As of now, Microsoft has not issued an official statement on the matter. GitHub has flagged the related issue as high priority, and a fix is expected in a future release.

This incident has also sparked broader discussions about transparency standards for AI-assisted development tools: to what extent should AI tools automatically declare their involvement? How should developers' code attribution rights be protected?

*Source: [GitHub Issue](https://github.com/microsoft/vscode/issues), [Hacker News Discussion](https://news.ycombinator.com/item?id=vs-code-copilot-commit)*
