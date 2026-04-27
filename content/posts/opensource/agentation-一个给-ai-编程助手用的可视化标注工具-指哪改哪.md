---
title: "Agentation ：一个给 AI 编程助手用的“可视化标注工具” 指哪改哪"
date: 2026-01-23T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Agentation（名字来自 Agent + Annotation）是一个专为开发者和 AI 编程工具设计的“可视化反馈标注工具”。   你可以在自己做的网站页面上，直接用鼠标点出有问题的地方（比如某个按钮、文字、或图片），然后写上反馈，Agentation 会自动生成一段带结构信息的说明。"
source_url: "https://www.xiaohu.ai/p/agentation-ai/28918403"
xiahuid: "28918403"
---

## 📰 正文

Agentation（名字来自 Agent + Annotation）是一个专为开发者和 AI 编程工具设计的“可视化反馈标注工具”。


你可以在自己做的网站页面上，直接用鼠标点出有问题的地方（比如某个按钮、文字、或图片），然后写上反馈，Agentation 会自动生成一段带结构信息的说明。


这段说明你只要复制粘贴给 Claude Code、Cursor、Windsurf 这些 AI 助手，AI 就能立刻在代码里找到对应的地方，修改问题。


简单说：就是它能让你在自己的网站上“圈出问题”，生成带结构化信息的反馈，然后发给你的 AI 编码助手（比如 Claude Code、Cursor、或 Windsurf）。


AI 就能精准地定位出问题的代码位置并修复它，而不用再靠你模糊地描述“蓝色按钮那块有 bug”。

![image]()


用一句话解释：

> 

Agentation 让你“用鼠标指出问题”，而不是“用语言解释问题”。


它帮 AI 明白你到底指的是页面上的哪个元素，从而更准确地修改代码。



想象一下这个场景



你让 Claude 帮你写了一个网页。


网页打开后，你发现：

- 

按钮太小；

- 

文案有拼写错误；

- 

登录弹窗打不开。



现在你要告诉 Claude 怎么改，你得一个个解释，比如：

> 

“在首页右下角的那个蓝色按钮上，点击没反应，能帮我修一下吗？”



Claude 听完后，得猜半天是哪段代码。因为它不知道“右下角蓝色按钮”对应哪一个文件、哪个 class。


这就浪费了时间。


而有了 Agentation，你可以：
1. 

在网页上点击某个元素（比如一个按钮、一段文字、一个图片等）；

2. 

添加你的反馈说明（比如“这个按钮太小了”、“这个文字拼错了”）；

3. 

工具会自动记录该元素的技术信息，比如：

- 

元素的 class 名称

- 

元素在网页中的 CSS 选择器

- 

元素的 位置


4. 

然后它会帮你生成一个整齐的 Markdown 格式反馈，像这样👇：



```None
### Annotation
Selector: .sidebar > .nav-actions > button.primary
Issue: 按钮文字应为“提交”，但目前显示为“送出”
```


![image]()


这样一来，当你把这段文字复制给 AI 工具（Claude Code 或 Cursor）时，
AI 可以立刻定位到对应代码文件，并自动修改正确的内容。


几秒钟就能修好。


最佳使用技巧（开发者小贴士）


![image]()


它的核心原理是什么？



Agentation 的原理其实很简单，但非常聪明。


它做的事情就是：当你点击网页上的某个元素时，它会自动收集这个元素的：

- 

HTML 选择器（selector）

- 

类名（class）

- 

层级路径

- 

在页面中的位置坐标



这些信息组合在一起，就能唯一地标识出网页里的那个元素。


然后 Agentation 把这些数据打包成一段结构化 Markdown 文本。AI 拿到后就能直接在代码里定位这个元素所在的文件或组件。


换句话说：

> 

你指的是“看得见的按钮”，
AI 能立刻知道“代码里的哪一行”。



这就像是你给 AI 配上了“定位眼镜”。


如何安装使用？（超详细步骤）



首先要知道：

> 

Agentation 目前是 桌面端专用工具（Desktop Only），
主要作为一个 浏览器内开发调试插件（前端工具） 来运行。


⚠️ 当前仅支持桌面端（Desktop only）
需要 React 18+，仅限开发环境使用（dev-only）



它不是一个 Chrome 插件或 VS Code 插件，
而是一个可以嵌入在本地网页开发环境（如 localhost:3000）中的 React 工具。


安装依赖包



在你的 React 项目中运行以下命令之一：


```None
npm install agentation

```



或使用其他包管理器：


```None
yarn add agentation
# 或
pnpm add agentation
# 或
bun add agentation

```



---



在应用中添加组件



在你的 React 应用中（建议在根组件中）引入：


```None
import { Agentation } from "agentation";

function App() {
  return (
    <>
      <YourApp />
      {process.env.NODE_ENV === "development" && <Agentation />}
    </>
  );
}

```



✅ NODE_ENV 检查
确保 Agentation 只在开发模式下加载，
不会在生产环境中运行。


---



Claude Code 一键集成（可选）



如果你使用 Claude Code（Anthropic 的 AI 编码工具），
可以自动安装并配置 Agentation：


1️⃣ 安装技能：



```None
npx add-skill benjitaylor/agentation
```



2️⃣ 在 Claude Code 中运行：



```None
/agentation
```



Claude Code 会自动：

- 

检测你的框架；

- 

安装 Agentation 包；

- 

创建 Provider；

- 

自动接入布局文件。



如何使用


![image]()


1️⃣ 打开 Agentation 工具
它现在是桌面版（Windows、Mac、Linux 都行）。
启动后会在你的网站右下角出现一个小图标。


2️⃣ 激活标注模式
点击右下角的图标进入“标注状态”。
这时候，当你把鼠标移动到页面上的元素时，
每个元素都会被高亮显示。


3️⃣ 选择想反馈的元素
比如你看到一个按钮有问题，点击它。


4️⃣ 填写反馈文字
会弹出一个小框，让你写下你的想法，比如：
“按钮文字太模糊”、“动画卡顿”、“点击没反应”等。


5️⃣ 生成结果并复制
点击“Add”或“Copy”，
Agentation 会自动生成一段 Markdown 格式的输出。


6️⃣ 粘贴到你的 AI 编程助手
打开 Claude Code 或 Cursor，把这段文本粘进去。
它会立刻根据那段 selector 信息，在代码里找到问题的源头并修改。


整个过程完全可视化，几乎不需要动脑子。


背后的创意：



Agentation 的灵感来自一位开发者 Benji Taylor。他写了一篇文章 探讨——

> 

“为什么开发者和 AI 的沟通效率这么低？”



他发现：

- 

人类喜欢用视觉描述（“这里不对”）

- 

AI 只能读文字（“在文件 X.js 的第 45 行”）



于是他和两位同事（Dennis Jin 和 Alex Vanderzon）做了一个桥梁：让视觉反馈转成代码可读的信息。


这就是 “Agent + Annotation” = Agentation 的由来。


安全说明



Agentation 的所有操作均在本地浏览器中执行，
不会上传或收集任何数据。

- 

🚫 无网络请求（No network requests）

- 

🧱 所有数据仅在本地处理

- 

🧩 不存储或追踪任何用户信息

- 

🧠 仅用于开发环境（Dev-only）



在线体验：https://agentation.dev/

---

*来源：[Agentation ：一个给 AI 编程助手用的“可视化标注工具” 指哪改哪](https://www.xiaohu.ai/p/agentation-ai/28918403)*
