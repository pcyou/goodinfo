---
title: "🍎 Apple Accidentally Ships Claude.md Config Files in Support App Update, Issues Emergency Patch"
date: 2026-05-02T14:00:00+08:00
tags: ["Apple", "Anthropic", "Claude", "security leak", "Claude.md", "software engineering"]
categories: ["ai-tech"]
summary: "Apple accidentally bundled internal Claude.md configuration files in Apple Support app v5.13, exposing its Claude Code development workflow, then rushed out an emergency v5.13.1 fix."
sources:
  - name: "Apple accidentally left Claude.md files Apple Support app"
    url: "https://xcancel.com/aaronp613/status/2049986504617820551"
    publisher: "X (via XCancel)"
  - name: "Hacker News discussion"
    url: "https://news.ycombinator.com/"
    publisher: "Hacker News"
---

# Apple Accidentally Ships Claude.md Config Files in Support App Update, Issues Emergency Patch

On April 30, 2026, technology researcher Aaron (@aaronp613) posted on social media that Apple had accidentally bundled internal Claude.md configuration files in that day's Apple Support app update (v5.13).

## What Are Claude.md Files?

Claude.md is a configuration file designed by Anthropic for its Claude Code AI programming assistant. Developers use it to instruct Claude on how to understand a project's codebase structure, coding conventions, and development workflows. These files typically contain internal development agreements, architectural decisions, and best practices — essentially "telling the AI how to think and code like an insider."

Shipping these files in a publicly released app exposes Apple's internal software engineering workflows and development conventions.

## Apple's Rapid Response

The post quickly went viral, accumulating over 1.36 million views, 10,000+ reposts, and 662 quotes. Within hours, Apple responded.

Approximately 3 hours after the initial post, Aaron tweeted: "I guess Apple saw my tweet. Apple has released an emergency update to the Apple Support app (v5.13.1) to remove the Claude.md files."

This response speed is rare among tech companies, indicating Apple takes this type of information leak very seriously.

## The Bigger Picture This Reveals

The accidental leak sparked wide discussion about Apple's AI-assisted development practices:

- **Widespread Claude usage at Apple**: Multiple commenters noted that Apple employees have over $200 per day in Claude credits for daily development work, indicating Claude Code has become a significant tool in Apple's engineering workflow.

- **Mythos model usage**: One commenter revealed that Apple has been running the Mythos preview on its own infrastructure via the Glasswing platform. Given the Pentagon's recent designation of Mythos as a "separate national security issue," this detail is particularly notable.

- **AI-assisted development security risks**: As one commenter put it: "We used to worry about shipping API keys. Now we also have to worry about shipping the markdown file that tells the AI how the company thinks."

## Industry Impact

This incident highlights new security challenges in the era of AI-assisted software development. As more tech companies adopt AI coding tools like Claude Code, preventing the accidental leakage of configuration files, prompt engineering, and internal development conventions is becoming a pressing new problem.

*Source: [X/Twitter](https://xcancel.com/aaronp613/status/2049986504617820551), [Hacker News](https://news.ycombinator.com/)*
