---
title: "Manus 背后核心技术 Browser Use：使 AI能够让 AI 像人类一样浏览网页并自动执行 Web 任务"
date: 2025-03-10T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "X 用户@jianxliao 声称他通过简单地请求 Manus AI 提供其位于“/opt/.manus/”的内部文件，AI 直接提供了这些文件，包括其沙箱运行时代码。他随后列出了几个关键发现：  -   Manus AI 实际上基于 Claude Sonnet（Anthropic 开发的 AI 模"
source_url: "https://www.xiaohu.ai/p/manus-browser-use-ai-ai-web/19374181"
xiahuid: "19374181"
---

## 📰 正文

X 用户@jianxliao 声称他通过简单地请求 Manus AI 提供其位于“/opt/.manus/”的内部文件，AI 直接提供了这些文件，包括其沙箱运行时代码。他随后列出了几个关键发现：

- 

Manus AI 实际上基于 Claude Sonnet（Anthropic 开发的 AI 模型）。

- 

它集成了 29 种工具，并使用 @browser_use 提供浏览器功能。

- 

它不使用多代理（multi-agent）系统。

- 

@browser_use 的代码被混淆（obfuscated），可能意在隐藏其实现细节。

- 

工具和提示存在“越狱”（jailbreak）现象，暗示可能存在安全漏洞或未授权访问。



Manus 的联合创始人@peakji 随后证实了这一消息，的确是使用了@browser_use 的开源代码

![image]()


@peakji  还证实他们使用Claude 和不同的 Qwen 微调版本来构建Manus

![image]()


Browser Use 介绍



使 AI 代理能够让 AI 像人类一样浏览网页并自动执行 Web 任务，例如抓取数据、自动填写表单、执行操作等。

- 

主要功能： 

✅ 访问任意网站，并进行交互（比如自动登录、搜索信息、购买商品）。
✅ 抓取网页数据，整理成有用的格式（比如从电商网站提取商品价格、库存信息）。
✅ 自动填写表单、提交内容（比如注册账号、填写客户信息）。
✅ 执行复杂任务（比如读取简历，自动申请多个工作，或在 Google Docs 写信并导出 PDF）。
✅ 在多个标签页同时操作，提高效率（比如对比多个网站的价格，并生成报告）。

- 

技术特点

![image]()
1. 

视觉+HTML 解析


🧐 AI 不只是“看”网页，还能“理解”网页！

- 

结合 计算机视觉（Vision） 和 HTML 代码解析，让 AI 代理既能“看懂”网页内容，也能分析网页结构。

- 

比如：

- 

传统爬虫只能抓取文本，而 Browser Use 可以找到真正的交互按钮，比如“加入购物车”或“提交订单”按钮。

- 

AI 不仅能读取内容，还能做出决策，如自动选择航班、预订酒店等。



2. 

多标签页管理


📂 支持 AI 同时在多个网页上工作

- 

AI 代理可以同时打开多个标签页，进行复杂任务（比如比价、同步多个网站的数据）。

- 

适用于：

- 

市场分析：同时打开 Amazon、eBay、Walmart，分析同一商品的不同价格。

- 

多任务处理：同时搜索多个工作网站，自动提交申请。



3. 

交互式元素追踪


🔍 AI 代理能够精准点击网页上的按钮、输入框，而不是“瞎点”！

- 

记录 AI 点击过的网页元素（XPath），确保每次任务都可以重复执行，不会因网页结构变化而失效。

- 

比如：

- 

你让 AI “每天登录某个网站，检查库存并下单”，Browser Use 能确保 AI 每次都点击正确的按钮，而不是乱点一通。



4. 

自定义操作（Custom Actions）


🛠️ 支持 AI 代理执行复杂操作，比如：

- 

保存数据到本地文件（比如 CSV、Excel）

- 

发送数据到数据库

- 

发送通知到 Slack、邮件

- 

请求人工确认（如果遇到特殊情况，AI 代理可以暂停并等待人工指令）。


5. 

自动纠错 & 恢复


🔄 AI 代理不会因为一个小错误就崩溃！

- 

内置智能错误处理，AI 代理可以自动恢复操作，避免因网页加载失败、按钮位置变化而影响任务执行。

- 

比如：

- 

遇到验证码？AI 会暂停并等待用户输入，而不会直接崩溃！

- 

遇到页面出错？AI 会自动刷新，重新尝试执行任务！



6. 

兼容所有大语言模型（LLM）


🤖 支持各种 AI 模型（LLM），包括：

- 

GPT-4（OpenAI）

- 

Claude 3（Anthropic）

- 

Llama 2（Meta）

- 

DeepSeek、Mistral、Command R+ 等



- 

📈 AI 代理准确率：89% 

- 

Browser Use 在 WebVoyager 基准测试的586 个不同类型的网页任务中取得了 89.1% 的任务成功率，超越了其他 Web 代理技术。

![image]()

- 

🔍 Web 任务成功率

![image]()

- 

Hugging Face 达到了 100% 的任务完成率，AI 代理在该平台上的操作最为顺畅。

- 

Google Flights、Amazon、GitHub 也取得了 90% 以上的成功率，说明 AI 代理可以很好地适应复杂的网页结构。

- 

即使是表现“最差”的域名（Booking.com）仍然达到了 80%的成功率（该网站的动态内容较多，交互方式复杂。）

![image]()



- 

示例任务：

- 

将商品添加到购物车，并结账。任务：将杂货项目添加到购物车，并结账。

![image]()

- 

将 LinkedIn 关注者添加到 Salesforce 客户列表。提示：将我最新的 LinkedIn 关注者添加到 Salesforce 中的潜在客户。

![image]()

- 

读取简历并自动申请机器学习相关工作，提示：阅读我的简历并寻找机器学习职位，将它们保存到一个文件中，然后在新标签页中开始申请，如果你需要帮助，请问我。

- 

在 Google Docs 写信并导出为 PDF。提示：在 Google Docs 中写一封信给我的爸爸，感谢他所做的一切，并将文档保存为 PDF。

![image]()

- 

搜索 Hugging Face 上最受欢迎的开源模型。提示：在Hugging Face 上查找具有 cc-by-sa-4.0 许可证的模型，并按最受欢迎排序，保存前 5 个到文件中。




适用场景



✅ Web 自动化任务（电商、CRM、金融等行业）
✅ 数据采集 & 分析（爬虫、市场调研、SEO 分析）
✅ 智能 AI 助手（自动填写表单、搜索信息、执行任务）
✅ 企业级 AI 代理部署（SaaS 平台、客户支持、业务流程优化）


局限性 & 改进方向

1. 

部分任务评估有误，需要人工调整：

- 

WebVoyager 评估器（eval model）并不完美，对于某些任务无法正确判断成功/失败。

- 

研究团队手动检查并修正了部分“未知”或“失败”任务的评估结果。


2. 

部分任务因数据过期而失败：

- 

例如，机票预订、新闻查询等任务，如果数据过时，可能导致 AI 无法完成。


3. 

Cloudflare 防火墙拦截：

- 

在某些网站（如 Amazon、Booking.com）上，AI 代理会被 Cloudflare 拦截。

- 

未来会增加代理轮换（Proxy Rotation），避免 AI 被封锁。


4. 

任务 Prompt 可能过于模糊：

- 

研究团队发现，某些任务的 Prompt 可能缺乏明确指示，导致 AI 理解偏差。




GitHub：https://github.com/browser-use/browser-use 


网站：https://browser-use.com/


技术报告：https://browser-use.com/posts/sota-technical-report

---

*来源：[Manus 背后核心技术 Browser Use：使 AI能够让 AI 像人类一样浏览网页并自动执行 Web 任务](https://www.xiaohu.ai/p/manus-browser-use-ai-ai-web/19374181)*
