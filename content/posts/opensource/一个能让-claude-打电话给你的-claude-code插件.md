---
title: "一个能让 Claude 打电话给你的 Claude Code插件"
date: 2026-01-10T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Call Me 是一个为 Claude Code插件   当你让 Claude 全自动任务，你出去潇洒的施工和，如何它遇到问题、或需要你做决定时，它会主动打电话找你帮助。😂   告诉你它遇到的问题、请你做决定、或者汇报结果。   比如：  -   Claude 跑完代码后给你打电话说： “我测试完了"
source_url: "https://www.xiaohu.ai/p/claude-claude-code/28477695"
xiahuid: "28477695"
---

## 📰 正文

Call Me 是一个为 Claude Code插件


当你让 Claude 全自动任务，你出去潇洒的施工和，如何它遇到问题、或需要你做决定时，它会主动打电话找你帮助。😂


告诉你它遇到的问题、请你做决定、或者汇报结果。


比如：

- 

Claude 跑完代码后给你打电话说：
“我测试完了，你要我继续部署吗？”

- 

Claude 卡在一个报错时打电话说：
“出错了，你要我重启服务吗？”

- 

Claude 在你外出时打电话说：
“我写完接口了，还有一个改进建议。”



就像 AI 成了一个“会打电话的助手”，帮你盯着任务。


你可以：

- 

通过手机、手表直接和 Claude 语音对话

- 

而且Claude 还可以一边讲电话，一边查资料


![image]()



安装步骤也不复杂：注册电话平台（Telnyx/Twilio）、设置环境变量、装上插件，就能让 Claude 给你打电话了。


价格也很低：一分钟通话几分钱。

![image]()


主要功能


- 

✅ 单一功能：让 Claude 能打电话给你，无需复杂设置。

- 

🔄 多轮对话：可以在电话中来回交流。

- 

🌍 多设备兼容：手机、智能手表、甚至座机都能用。

- 

🧩 可组合工具：Claude 可以在通话时同时进行其他任务（如网页搜索）。



怎么实现的？（原理）



简单说，就是下面这条链路👇：


```None
Claude → Call Me 插件 → ngrok（网络通道） → 电话服务商（Telnyx/Twilio） → 你的手机
```



也就是：
1. 

Claude决定要打电话时，

2. 

它调用 Call Me 插件，

3. 

插件通过 ngrok 建一个安全通道到外部网络，

4. 

再联系到一个电话服务平台（Telnyx 或 Twilio），

5. 

电话平台拨打你的号码，

6. 

你接电话后，AI 说话的内容通过 OpenAI 的语音功能转成声音，

7. 

你说的话再被转成文字发回 Claude。



于是你和 AI 就真的能“打电话聊天”了。📞🤖


怎么用？



这部分看起来复杂，但其实照着一步步来很简单 👇


① 你需要准备 3 个账号：

![image]()


② 配置环境变量（告诉插件账号信息）


就像给插件一份“电话通讯录”和“凭证”。


```None
{
  "env": {
    "CALLME_PHONE_PROVIDER": "telnyx",
    "CALLME_PHONE_ACCOUNT_SID": "你的Telnyx连接ID",
    "CALLME_PHONE_AUTH_TOKEN": "你的Telnyx API密钥",
    "CALLME_PHONE_NUMBER": "+15551234567",      // Claude打出的号码
    "CALLME_USER_PHONE_NUMBER": "+15559876543", // 你的手机号
    "CALLME_OPENAI_API_KEY": "sk-xxx",          // 用于语音功能
    "CALLME_NGROK_AUTHTOKEN": "你的ngrok token"
  }
}
```



---



③ 安装插件命令


在 Claude Code 里输入命令：


```None
/plugin marketplace add ZeframLou/call-me
/plugin install callme@callme

```



然后重启 Claude Code。搞定。


插件能干的几件事


![image]()


举个实际例子：


```None
const { callId } = await initiate_call({
  message: "我完成注册系统了，要不要加上限流？"
});

await speak_to_user({
  call_id: callId,
  message: "好的，我查一下接口性能。"
});

await continue_call({
  call_id: callId,
  message: "我发现系统每分钟可处理500请求，要不要再优化？"
});

await end_call({
  call_id: callId,
  message: "好的，那我开始干活啦！"
});

```



是不是就像你和一个远程助理打完一次工单电话？


打电话要花多少钱？



其实非常便宜 💵👇

![image]()


➡️ 总成本大概 $0.03~$0.04 一分钟
也就是一块人民币能聊十几分钟。


GitHub：https://github.com/ZeframLou/call-me

---

*来源：[一个能让 Claude 打电话给你的 Claude Code插件](https://www.xiaohu.ai/p/claude-claude-code/28477695)*
