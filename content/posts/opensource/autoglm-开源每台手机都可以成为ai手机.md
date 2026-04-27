---
title: "AutoGLM 开源：每台手机，都可以成为AI手机"
date: 2025-12-13T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "智谱 AI AutoGLM 团队宣布正式开放其核心项目 AutoGLM（Automated General Learning Model） 的全部源代码与模型。   什么是 AutoGLM    AutoGLM 是一个让 人工智能能够自主使用智能手机 的系统。   它的核心理念是：AI 不应局限在对"
source_url: "https://www.xiaohu.ai/p/autoglm-ai/27768612"
xiahuid: "27768612"
---

## 📰 正文

智谱 AI AutoGLM 团队宣布正式开放其核心项目 AutoGLM（Automated General Learning Model） 的全部源代码与模型。


什么是 AutoGLM



AutoGLM 是一个让 人工智能能够自主使用智能手机 的系统。


它的核心理念是：AI 不应局限在对话框中回答问题，而应能够像人类一样，直接在应用程序中执行具体操作。


该系统可让 AI 完成以下任务：

- 

打开应用、点击按钮、滚动页面、输入文字；

- 

在外卖、社交、银行、办公等 App 中完成完整的任务流程；

- 

通过视觉识别与操作反馈，自主处理复杂界面与多步任务。



AutoGLM 的目标是赋予 AI “设备代理能力”（Device Agency）——即理解界面、执行动作、感知反馈、持续学习。


举个例子：

- 

你说“帮我点份午餐”，AI 能自己打开美团外卖、选餐、结账；

- 

你说“发个红包给小张”，AI 能自动打开微信或支付宝完成操作；

- 

它还能帮你处理通知、点赞、打卡、回复客户消息。



核心功能与技术亮点



AutoGLM 的功能体系覆盖从视觉理解到动作执行的完整链条。

![image]()


1️⃣ 真实设备操作能力



识别手机界面上的按钮、文字、图标，知道该点哪里、该怎么滑动。


AI 能在智能手机或云端虚拟手机上：

- 

自动识别屏幕元素；

- 

将自然语言指令转化为可执行操作序列；

- 

在网络波动、广告弹窗、界面变化等真实条件下完成任务。



2️⃣ 云端虚拟环境与安全沙箱



AutoGLM 提供了一个 虚拟手机（Cloud Phone） 训练与运行环境。

- 

所有操作均在云端沙箱中执行，可回放、可审计；

- 

敏感数据与真实设备完全隔离；

- 

支持多实例并行训练与强化学习（MobileRL、ComputerRL、AgentRL）。



3️⃣ 强化学习驱动的智能控制



系统通过大规模并行强化学习（Reinforcement Learning）训练，让 AI 能在上千个虚拟环境中同时学习操作技能，快速提升对不同应用与界面的泛化能力。


4️⃣ 视觉理解与任务分解



AutoGLM 能“看懂”屏幕内容，理解按钮、文字、图标的语义关系，并自动分解自然语言任务为有序的交互步骤。


例如，它能把一句自然语言指令（比如“打开微博发条动态”）分解成一连串动作：
打开 App → 定位输入框 → 输入文字 → 点击发布。


开源初衷



AutoGLM 团队表示，选择在此阶段开源的原因有三：
1. 

推动产业共建，避免能力垄断
手机操作智能将成为 AI 时代的基础能力，必须由开放社区共同完善。

2. 

让数据和隐私回归用户
通过私有化部署，企业和个人可在本地或自有云环境中运行 AutoGLM，确保数据自主。

3. 

推动 Agent 生态的全面爆发
AutoGLM 的研发路径可复用，为构建下一代 AI Phone、Agent 研究、垂直应用提供可直接使用的起点。



模型：https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual


GitHub：https://github.com/zai-org/Open-AutoGLM


Open-AutoGLM 一步安装使用指南（新手版）



---



✅ 一、准备工作（5分钟）



在开始前，确保你有：


1️⃣ 一台电脑（Windows / macOS / Linux 都可以）
2️⃣ 一部安卓手机（Android 7.0 以上）
3️⃣ 一根能传输数据的 USB 数据线（不是只充电线）
4️⃣ 手机要开启：

- 

开发者模式

- 

USB 调试



📱 开启方法：

- 

打开 “设置 → 关于手机 → 连续点击版本号 7 次”

- 

返回设置，进入 “开发者选项 → 打开 USB 调试”



---



✅ 二、安装 ADB（Android Debug Bridge）



ADB 是电脑控制手机的桥梁。


💻 Windows 用户：

1. 

下载官方工具包：
👉 https://developer.android.com/tools/releases/platform-tools

2. 

解压到任意位置，比如：C:\adb

3. 

在命令行里加入路径：



```None
setx PATH "%PATH%;C:\adb"

```

1. 

测试是否安装成功：



```None
adb version

```



出现版本号就 OK ✅


---



🍎 macOS 用户：



直接在终端运行：


```None
brew install android-platform-tools

```



---



✅ 三、连接手机并授权

1. 

手机插上 USB 数据线。

2. 

电脑运行：



```None
adb devices

```

1. 

手机上会弹出提示框 → 点击“允许 USB 调试”

2. 

如果看到输出：



```None
List of devices attached
XXXXXXX device

```



说明连接成功 🎉


---



✅ 四、安装 Python 环境

1. 

检查 Python 是否安装：



```None
python --version

```



如果没有，去官网安装：
👉 https://www.python.org/downloads/
1. 

推荐使用 Python 3.10 或以上。



---



✅ 五、下载并安装 Open-AutoGLM



在命令行执行以下命令（一步步复制就行）👇


```None
git clone https://github.com/zai-org/Open-AutoGLM.git
cd Open-AutoGLM
pip install -r requirements.txt
pip install -e .

```



安装完就是运行环境准备完成 ✅


---



✅ 六、让 AI 控制手机（两种方式）



✅ 方式 1：使用远程模型（推荐！不用 GPU）



直接调用官方模型服务，最方便！


执行下面这条命令：


```None
python main.py \
 --base-url https://open.bigmodel.cn/api/paas/v4 \
 --model "autoglm-phone" \
 --apikey "你的API密钥" \
 "打开美团搜索附近的火锅店"

```



💡 获取 API Key：
在 https://open.bigmodel.cn 免费注册即可获得。


运行后，如果你的手机屏幕自动亮起并打开美团 App，就说明部署成功了 ✅


---



✅ 方式 2：本地部署模型（适合有 GPU 的用户）



如果你有显卡（24GB 显存或以上），可以自己部署模型。


```None
pip install vllm
python3 -m vllm.entrypoints.openai.api_server \
 --model zai-org/AutoGLM-Phone-9B \
 --port 8000

```



模型会自动下载到本地（大约 20GB）。
启动后服务地址为：


```None
http://localhost:8000/v1

```



再运行：


```None
python main.py --base-url http://localhost:8000/v1 --model "autoglm-phone-9b" "打开微信发消息给文件传输助手"

```



手机会自动执行这个任务 🚀


---



✅ 七、小贴士（非常重要）


![image]()


---



✅ 八、快速测试命令合集



```None
# 检查连接的手机
adb devices

# 运行 AI 控制手机（BigModel 云服务）
python main.py --base-url https://open.bigmodel.cn/api/paas/v4 --model "autoglm-phone" --apikey "你的key" "打开微信发消息给文件传输助手"

# 列出所有支持的应用
python main.py --list-apps

```



---



✅ 九、验证是否安装成功



当你运行上面的命令后：

- 

手机自动亮屏；

- 

打开你指定的 App；

- 

并执行指令（比如搜索、发消息、打开页面）；



就说明：🎉 Open-AutoGLM 已成功安装并运行！


安装教程：https://github.com/zai-org/Open-AutoGLM/blob/main/README.md

---

*来源：[AutoGLM 开源：每台手机，都可以成为AI手机](https://www.xiaohu.ai/p/autoglm-ai/27768612)*
