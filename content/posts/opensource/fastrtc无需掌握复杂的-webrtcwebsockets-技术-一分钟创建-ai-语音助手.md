---
title: "FastRTC：无需掌握复杂的 WebRTC、WebSockets 技术 一分钟创建 AI 语音助手"
date: 2025-03-04T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "💡 背景：随着 OpenAI、Google 等公司发布 实时语音 AI 模型（如 ChatGPT 语音、Gemini 语音），以及 Moshi、Qwen2-Audio、Fixie.ai 等开源音频大模型的崛起，开发 流式音频 AI 应用 变得至关重要。然而，大多数机器学习工程师并不熟悉 WebRTC"
source_url: "https://www.xiaohu.ai/p/fastrtc-webrtc-websockets-ai/19184451"
xiahuid: "19184451"
---

## 📰 正文

💡 背景：随着 OpenAI、Google 等公司发布 实时语音 AI 模型（如 ChatGPT 语音、Gemini 语音），以及 Moshi、Qwen2-Audio、Fixie.ai 等开源音频大模型的崛起，开发 流式音频 AI 应用 变得至关重要。然而，大多数机器学习工程师并不熟悉 WebRTC 等实时通信技术，因此 FastRTC 旨在让 Python 开发者能够轻松实现 AI 语音应用。


因此Hugging Face 推出了一个专门为 Python 开发者打造的实时通信（RTC）库：FastRTC ，专门用于构建 实时音频和视频 AI 应用。


该库大大降低了开发门槛，让你可以 快速构建 语音识别、语音合成和 AI 语音对话应用。而无需掌握复杂的 WebRTC、WebSockets 技术。


🔹 你可以用 FastRTC 轻松实现： 


✅ 实时语音聊天（像 ChatGPT 语音模式一样）
✅ 语音 AI 机器人（自动语音助手、客服机器人）
✅ AI 语音播客（自动朗读文章并转换为播客）
✅ 语音翻译（实时多语言翻译）
✅ 电话接入 AI 语音（让用户拨打电话，AI 自动应答）


目前的 AI 语音开发痛点



❌ 传统 WebRTC 方案难以集成 → 需要掌握复杂的网络通信、音视频处理知识
❌ 现有 Python 库支持有限 → 语音识别（STT）、语音合成（TTS）和 AI 互动需要多个 API 组合
❌ AI 语音交互延迟高 → 语音输入后等待 AI 处理，响应速度慢，不适合实时应用

![image]()


✅ FastRTC 解决了这些问题！

- 

开箱即用：集成 语音识别（STT）、语音合成（TTS）、AI 对话，提供一站式解决方案

- 

自动 UI：内置 WebRTC + Gradio 界面，随时测试和部署

- 

低延迟：支持 WebRTC & WebSockets，让语音交互更加流畅



---



🔹 FastRTC 的核心功能



1️⃣ 自动语音检测（VAD）& 轮流对话

- 

AI 自动检测语音输入，无需手动控制说话时机。

- 

内置 VAD（语音活动检测），只在用户讲话时触发 AI 处理，减少不必要的计算。



💡 你只需要写对话逻辑，FastRTC 自动处理语音交互！


---



2️⃣ 自动生成 WebRTC UI

- 

FastRTC 内置 Gradio 界面，可以直接在 Web 浏览器中测试 AI 语音应用！

- 

支持 WebRTC 实时流式通信，让音频处理更高效、低延迟。



💡 你不需要写前端代码，FastRTC 直接帮你生成可用 UI！


---



3️⃣ AI 语音助手支持（STT + TTS）


📌 STT（语音转文本） → 自动识别用户语音，并转换为文字
📌 TTS（文本转语音） → 让 AI 语音回答用户，而不是文字输出


💡 让 AI “听得懂”、“说得出”，构建 ChatGPT 语音助手一样的体验！


---



4️⃣ 电话接入 AI 语音（FastPhone API）


📌 只需 一行代码，你就可以让用户 拨打电话 与 AI 语音助手交流！
📌 FastRTC 自动生成电话号码，用户可以直接打电话进入 AI 语音流！


💡 这让 AI 语音助手可以无缝连接到传统电话系统！


🛠 快速入门：一分钟创建 AI 语音助手



📌 1️⃣ 安装 FastRTC



```None
pip install fastrtc

```



---



 2️⃣ 创建一个实时语音回声（Echo）应用



👉 这个示例会实时播放用户说的话


```None
from fastrtc import Stream, ReplyOnPause
import numpy as np

def echo(audio: tuple[int, np.ndarray]) -> tuple[int, np.ndarray]:
    yield audio  # 直接返回用户输入的音频数据

stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")
stream.ui.launch()

```



✅ 自动识别用户语音，并实时播放回来
✅ 无需手动处理 WebRTC，FastRTC 自动帮你搞定！


---



3️⃣ 创建 AI 语音助手（STT + LLM + TTS）



📌 使用 LLM 来响应用户。FastRTC 具有内置的语音转文本和文本转语音功能，因此使用FastRTC非常容易。


📌 这个示例让 AI 先把语音转换为文本，再调用 LLM（如 Llama-3.2），最后转换回语音回答用户！


```None
import os
from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
from openai import OpenAI

# 连接 SambaNova AI 语言模型
sambanova_client = OpenAI(api_key=os.getenv("SAMBANOVA_API_KEY"), base_url="https://api.sambanova.ai/v1")

# 获取语音识别 & 语音合成模型
stt_model = get_stt_model()
tts_model = get_tts_model()

def ai_conversation(audio):
    prompt = stt_model.stt(audio)  # 语音转文本
    response = sambanova_client.chat.completions.create(
        model="Meta-Llama-3.2-3B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    reply = response.choices[0].message.content
    for audio_chunk in tts_model.stream_tts_sync(reply):  # 文本转语音
        yield audio_chunk

stream = Stream(ReplyOnPause(ai_conversation), modality="audio", mode="send-receive")
stream.ui.launch()

```



✅ STT（语音转文本）+ LLM（自然语言处理）+ TTS（文本转语音），形成完整 AI 语音助手。
✅ 使用 Meta-Llama-3.2 作为 LLM，可替换为 OpenAI、Gemini、Claude 等 AI 模型。


4️⃣  Bonus：让用户拨打电话进入 AI 语音流



📌 FastRTC 提供 "FastPhone" API，让用户可以通过拨打电话与 AI 语音助手互动。


```None
stream.fastphone()

```



📌 终端显示：


```None
INFO: Your FastPhone is now live! Call +1 877-713-4471 and use code 530574 to connect to your stream.
INFO: You have 30:00 minutes remaining in your quota (Resetting on 2025-03-23)

```



✅ 用户可以拨打这个电话号码，直接进入 AI 语音流！
✅ PRO 账户可以增加使用时长和并发量。


📌 官方文档：FastRTC Docs
📌Cookbook：https://fastrtc.org/cookbook/
📌 GitHub 代码库：https://github.com/freddyaboulton/fastrtc
📌 Hugging Face Space：https://huggingface.co/fastrtc


官方介绍：https://huggingface.co/blog/fastrtc

---

*来源：[FastRTC：无需掌握复杂的 WebRTC、WebSockets 技术 一分钟创建 AI 语音助手](https://www.xiaohu.ai/p/fastrtc-webrtc-websockets-ai/19184451)*
