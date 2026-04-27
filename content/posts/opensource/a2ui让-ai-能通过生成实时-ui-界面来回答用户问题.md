---
title: "A2UI：让 AI  能通过生成实时 UI 界面来回答用户问题"
date: 2025-12-22T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "A2UI（全称 Agent-to-User Interface）是 Google 推出的一个开源项目，目标是让 AI 智能体（agent）能自动生成安全的图形化界面（UI）。  >   🧠 一句话解释： A2UI 是一种“让 AI 能说 UI 的语言”。   让智能体（Agents）能生成上下文相关"
source_url: "https://www.xiaohu.ai/p/a2ui-ai-ui/27978119"
xiahuid: "27978119"
---

## 📰 正文

A2UI（全称 Agent-to-User Interface）是 Google 推出的一个开源项目，目标是让 AI 智能体（agent）能自动生成安全的图形化界面（UI）。

> 

🧠 一句话解释：
A2UI 是一种“让 AI 能说 UI 的语言”。


让智能体（Agents）能生成上下文相关的、动态的、可交互的用户界面（UI）。



传统上，AI 只能输出文字（比如 ChatGPT 给你一段文本），但它不能生成一个安全可交互的界面。


有两个难题：
1. 

安全问题：如果让 AI 输出 HTML/JS 代码，会有执行任意代码的风险（如 XSS、RCE）。

2. 

跨平台问题：HTML、Flutter、React、SwiftUI 各有不同的渲染方式，AI 生成的代码往往不能通用。



A2UI 的出现就是为了解决这两个问题


它定义了一种开放的 UI 描述标准，让 AI 不直接生成代码，而是生成一种声明式的数据结构（JSON），用于描述界面的结构和行为。


客户端程序（前端 App）再根据这份数据结构，用自己的安全组件库去“解释并绘制”UI。


这样：

- 

AI 不需要知道具体框架；

- 

UI 可以跨平台；

- 

安全性得到保证；

- 

交互体验可以动态更新。


> 

它让 AI 能用一种安全、标准的格式（JSON）告诉应用该怎么生成界面，而不是直接写代码。


举个例子：

- 

以前你问 AI：“帮我查下东京餐厅”
→ AI 只能回一句文字说明；

- 

用了 A2UI 后
→ AI 能“生成”一个可交互的界面，比如地图上标出东京餐厅的位置。



也就是说，AI 不再只是“说话”，还能“画界面”。
但它不是写代码（这会有安全风险），而是生成一种安全的数据描述（JSON），告诉应用程序要显示什么界面。


![image]()


A2UI 的核心特性


> 

让智能体安全地生成 UI，而不是执行代码。



也就是说：

- 

AI 只输出结构化 JSON；

- 

客户端渲染 UI；

- 

所有组件都来自安全的“组件白名单”。



🚫 不再发送代码



过去的远程 UI 往往通过 HTML/JS 传递，这会带来：

- 

安全隐患（执行脚本）；

- 

样式不一致；

- 

难以跨平台。


![image]()


A2UI 为什么重要？



让我们看一个例子 👇


---



❌ 传统做法



AI 想生成一个界面（比如一个“酒店预订表单”），可能会输出：


```None
<form>
  <input type="text" placeholder="Destination">
  <input type="date">
  <button>Book</button>
</form>
```



但是：

- 

这个代码可能包含恶意脚本（安全风险⚠️）；

- 

前端框架可能不兼容（React、Flutter、SwiftUI 各不相同）；

- 

更新 UI 很难做到“动态增量修改”。



---



✅ 用 A2UI 的做法



AI 不直接写代码，而是输出一个安全的 JSON：


```None
{
  "type": "form",
  "children": [
    { "type": "text-field", "label": "Destination", "id": "input_destination" },
    { "type": "date-picker", "label": "Check-in Date", "id": "input_date" },
    { "type": "button", "text": "Book", "onClick": "submit_form" }
  ]
}
```



前端（比如 Flutter、Lit、React）拿到这个 JSON 后，
会自动用本地的组件库去渲染出界面。


这样：

- 

不运行 AI 生成的“可执行代码”，只解析数据 ✅

- 

不限前端框架 ✅

- 

AI 可以随时“增量更新 UI” ✅



---



技术结构与架构



A2UI 本质上是一个：

> 

“声明式 UI 消息规范” + “跨平台渲染协议”



可以理解为：


```None
AI → 生成 A2UI JSON → 前端解析 → 渲染本地组件
```



可以把整个 A2UI 的工作过程分为四个阶段。

![image]()


1. 生成（Generation）



智能体（Agent）——例如使用 Gemini 或其他大型语言模型（LLM）——生成一个符合 A2UI 规范的 JSON。
这个 JSON 包含界面的结构、组件类型、内容、事件标识等。


2. 传输（Transport）



这个 JSON 数据通过网络传给客户端。
A2UI 支持的传输协议包括：

- 

A2A Protocol（Agent-to-Agent 协议）

- 

WebSocket

- 

未来可能支持 REST、gRPC 等形式



3. 解析（Resolution）



客户端应用收到 JSON 后，由 A2UI Renderer（渲染器）进行解析。
渲染器负责识别组件类型（如 “button”）并找到相应的本地实现。


4. 渲染（Rendering）



渲染器将这些抽象组件映射到真实的 UI 元素上。
例如：

- 

在 Flutter 中，"type": "button" 映射为 ElevatedButton

- 

在 Web 上，映射为 Lit 或 React 的 <button>

- 

在 iOS 上，映射为 SwiftUI 的 Button



最终，用户看到的是一个真实、可交互的界面。


技术栈


- 

语言：TypeScript（95% 以上）

- 

辅助语言：HTML、Python

- 

主要框架支持：

- 

Web（Lit Renderer）

- 

Flutter（GenUI SDK）


- 

兼容生态：A2A 协议、AG UI、Gemini API、CopilotKit



典型应用场景



A2UI 并不是一个单纯的 UI 工具，而是面向“智能体系统”的界面协议。它的应用非常广泛：
1. 

智能表单生成
智能体根据上下文生成动态表单，例如会议预订、客户调查、设备配置等。

2. 

可视化问答界面
聊天式应用中，智能体根据用户问题动态生成卡片、图表、列表等视觉信息。

3. 

企业工作流系统
智能体在审批、报告、数据分析系统中，动态生成业务界面。

4. 

多智能体协作系统
一个主智能体可以调用子智能体（如旅行、餐馆、天气服务），每个子智能体返回自己的 UI 模块嵌入主界面。



景观建筑师案例：

> 

一个用户（景观设计师）上传了一张自家庭院的照片，
智能体（由 Gemini 驱动）理解图片内容，
然后根据图片自动生成一个“定制化表单”，
用于填写景观设计需求，比如草坪、照明、水景等偏好。



最终，AI 并不是给出一段文字建议，
而是自动生成了一个“完整的应用界面”——一个可交互的表单，里面有输入框、选择项、图片预览等。


交互式图表和地图


使用图表组件来回答数值汇总问题。然后代理选择 Google Map 组件来回答位置问题


假设用户输入：

> 

“过去三个月的销售总额分别是多少？”



Gemini 识别到：

- 

这是一个“数值汇总类问题”；

- 

用文字描述太笼统；

- 

最合适的回答方式是图表。



接下来，用户又问：

> 

“这些销售来自哪些地区？”



这个问题涉及“地理位置数据”，
最合适的可视化方式是地图（Map）。





实际使用方式（以示例项目为例）



Google 在仓库中提供了一个名为 Restaurant Finder Demo 的示例。
这个示例展示了从智能体生成 UI 到前端渲染的完整流程。

- 

后端（Agent）：Python 编写，负责生成 A2UI JSON。

- 

前端（Renderer）：使用 Lit（Web Components）渲染 UI。

- 

数据来源：Gemini 模型，通过 API 生成 UI。



运行步骤：


```None
git clone https://github.com/google/A2UI.git
cd A2UI
export GEMINI_API_KEY="your_api_key"

# 启动后端智能体
cd samples/agent/adk/restaurant_finder
uv run .

# 启动前端
cd ../../renderers/lit
npm install && npm run build
cd ../../samples/client/lit/shell
npm install && npm run dev

```



浏览器中即可看到一个智能助手界面：
用户输入请求，AI 生成 JSON，前端实时渲染界面。


总结


A2UI 的核心思想是让 AI 用数据描述界面，而不是写代码。
它提供了一种安全、统一的方式，让智能体能够输出丰富的用户界面，并在不同平台上以原生方式渲染。


它的价值体现在三个层面：
1. 

安全性：避免 LLM 输出可执行代码带来的安全风险。

2. 

通用性：跨框架、跨平台、跨语言的 UI 通信标准。

3. 

动态性：让 UI 成为智能体交互的一部分，而不再是静态容器。



GitHub：https://github.com/google/A2UI/ 


官网：https://a2ui.org/ 


教程：https://dev.to/copilotkit/a2ui-in-practice-build-agent-to-user-interfaces-using-a2a-ag-ui-3ng5 


官方介绍：https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/

---

*来源：[A2UI：让 AI  能通过生成实时 UI 界面来回答用户问题](https://www.xiaohu.ai/p/a2ui-ai-ui/27978119)*
