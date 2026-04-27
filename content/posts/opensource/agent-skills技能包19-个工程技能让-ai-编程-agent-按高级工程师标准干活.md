---
title: "Agent Skills技能包：19 个工程技能让 AI 编程 Agent 按高级工程师标准干活"
date: 2026-04-06T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google Chrome 团队工程负责人 Addy Osmani 开源了一套叫 Agent Skills 的技能包，专门解决 AI 编程 Agent 的一个通病：它们默认走最短路径，跳过规范、跳过测试、跳过安全审查，代码写完就算完事。   Agent Skills 把 Google 内部的工程实践"
source_url: "https://www.xiaohu.ai/p/agent-skills-19-ai-agent/31391606"
xiahuid: "31391606"
---

## 📰 正文

Google Chrome 团队工程负责人 Addy Osmani 开源了一套叫 Agent Skills 的技能包，专门解决 AI 编程 Agent 的一个通病：它们默认走最短路径，跳过规范、跳过测试、跳过安全审查，代码写完就算完事。


Agent Skills 把 Google 内部的工程实践（来自《Software Engineering at Google》和 Google 工程实践指南）打包成 19 个结构化技能，覆盖从想法到上线的完整开发流程。


安装之后，Agent 不再是"能写代码"，而是"按高级工程师的标准写代码"。


MIT 协议，纯 Markdown 格式，适配 Claude Code、Cursor、Windsurf、GitHub Copilot 等几乎所有主流编程 Agent。


六个阶段，七个命令


![image]()


整套技能围绕软件开发的六个阶段组织，每个阶段对应一个斜杠命令：


```None
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
/spec    /plan   /build   /test    /review   /ship
```



加上一个 /code-simplify 做代码简化，一共七个命令。你不用记 19 个技能各叫什么，敲命令就行，对应的技能会自动激活。写 API 时 api-and-interface-design 自动加载，写前端时 frontend-ui-engineering 自动触发。


19 个技能都覆盖了什么


![image]()


每个技能不是一段笼统的提示词，是一套完整的工作流程：有步骤、有检查点、有退出标准。


最有意思的设计：反借口表



每个技能里都有一张 "Anti-Rationalization Table"，列出了 AI Agent 常用的偷懒借口和对应的反驳。比如：

> 

Agent 说："测试以后再补。"
技能反驳："不行，Red-Green-Refactor，先写测试再写代码。"


Agent 说："这个改动很小，不用走 review。"
技能反驳："100 行以内也要过五轴审查。"



这个设计抓住了 AI Agent 最大的问题：它们不是不会写测试，是会给自己找理由不写。光说"要写测试"没用，得把每种借口的反驳也写进去。


验证是硬性要求



每个技能最后都有 Evidence Requirements，不是"看起来对了"就行，得有实际证据：测试全绿、构建产物、运行时数据。没有证据，技能流程就没完成。


除了技能本身，还有什么



3 个预配置 Agent 角色：

- 

code-reviewer：Staff Engineer 视角做代码审查，标准是"一个 Staff Engineer 会不会批准这个 PR"

- 

test-engineer：QA 视角检查测试策略和覆盖率

- 

security-auditor：安全工程师视角做漏洞检测和威胁建模



配合4 个参考检查清单（测试模式、安全检查、性能检查、无障碍检查），覆盖了审查阶段最常见的盲区。

![image]()


7 个斜杠命令（Claude Code 专属）

![image]()


Hooks 系统（Claude Code 专属）。session-start 在会话开始时自动加载技能路由；simplify-ignore 允许用注释标记不希望 Agent 碰的代码块（比如手工优化过的性能关键代码），Agent 简化代码时这些块会被替换成占位符，会话结束后恢复。


怎么用



最快的方式是通过 skills.sh CLI 一键安装全部 19 个技能：


```None
npx skills add addyosmani/agent-skills
```



也可以只装某个特定技能：


```None
npx skills add https://github.com/addyosmani/agent-skills --skill code-review-and-quality
```



Claude Code 有原生插件支持：


```None
claude plugin add agent-skills
```



Cursor 用户把 SKILL.md 文件复制到 .cursor/rules/ 目录即可。GitHub Copilot 用户把 Agent 角色文件放到 .github/agents/ 目录，在 Copilot Chat 里用 @code-reviewer 调用。


因为所有内容都是纯 Markdown，任何接受文本指令的 Agent 都能用，包括 OpenCode、Codex、Gemini CLI、Cline 等 40 多个兼容工具。


官方建议一次加载 2-4 个技能，不要全部加载。仓库里有一个 meta-skill 叫 using-agent-skills，功能是根据当前任务类型自动路由到对应技能，适合作为起点。


兼容哪些工具


![image]()


Claude Code 和 Gemini CLI 支持最好，一行命令安装。Cursor 和 Windsurf 需要手动复制文件。


跟自己写 CLAUDE.md 规则有什么区别



很多人已经在 CLAUDE.md 里写了自己的规则，Agent Skills 的区别在于：


1. 结构化程度不同。 自己写的规则通常是"要做什么"的清单，Agent Skills 是完整的工作流程，有步骤顺序、有检查门禁、有退出条件。Agent 不是"知道应该写测试"，而是"在这个步骤必须写测试，不写不能进入下一步"。


2. 反借口机制。 自己写的规则说"不要跳过测试"，Agent 换个说法就绕过了。Agent Skills 把各种绕过的说法和反驳都列出来了。


3. Google 工程文化沉淀。 Hyrum's Law 在 API 设计里、Beyonce Rule 在测试里、Chesterton's Fence 在代码简化里、Shift Left 在 CI/CD 里。这些不是抽象原则，直接嵌入了每个步骤。


需要知道的几件事


- 

19 个技能全部安装会占用不少上下文窗口。技能设计了渐进加载（只在触发时加载），但复杂项目同时激活多个技能时，token 消耗会明显上升

- 

技能面向生产级代码设计。如果你在快速原型阶段，每次写代码都跑完整规范和测试流程可能太重

- 

目前 76 个 commit，还在快速迭代。部分技能的流程可能会调整

- 

如果你已有自己的 CLAUDE.md 规则，需要注意冲突。技能可以单独安装，不必全装



👉 GitHub 仓库  | webreactiva: 19 Skills 详解

---

*来源：[Agent Skills技能包：19 个工程技能让 AI 编程 Agent 按高级工程师标准干活](https://www.xiaohu.ai/p/agent-skills-19-ai-agent/31391606)*
