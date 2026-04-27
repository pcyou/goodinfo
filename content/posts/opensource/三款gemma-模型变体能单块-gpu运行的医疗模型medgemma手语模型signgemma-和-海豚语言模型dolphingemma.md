---
title: "三款Gemma 模型变体：能单块 GPU运行的医疗模型MedGemma、手语模型SignGemma 和 海豚语言模型DolphinGemma"
date: 2025-05-25T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google发布了三款新的 Gemma 系列模型的变体：MedGemma、SignGemma 和 DolphinGemma，分别针对医学 AI、辅助技术以及跨物种通信三大创新领域。  它们体现了语言模型（LLMs）和多模态模型在专业垂直领域的深度应用潜力，也展示了开放、安全和可访问性在未来 AI 发"
source_url: "https://www.xiaohu.ai/p/gemma-gpu-medgemma-signgemma-dolphingemma/21788020"
xiahuid: "21788020"
---

## 📰 正文

Google发布了三款新的 Gemma 系列模型的变体：MedGemma、SignGemma 和 DolphinGemma，分别针对医学 AI、辅助技术以及跨物种通信三大创新领域。

它们体现了语言模型（LLMs）和多模态模型在专业垂直领域的深度应用潜力，也展示了开放、安全和可访问性在未来 AI 发展中的重要地位。

![image]()


MedGemma：面向医疗的多模态 AI 模型



功能与用途

- 

专门为医学领域打造的 Gemma 3 模型家族成员，用于加速医学文本与图像类 AI 应用的开发。

- 

应用场景包括：医学图像分析、临床推理等。



技术规格

- 

提供两个版本：

- 

4B 多模态模型：能处理图像与文本的组合任务。采用SigLIP图像编码器,针对医疗数据进行预训练,包括胸部X光片、皮肤科图像、眼科图像和病理切片等。

- 

27B 文字推理模型：更强大的纯文本处理能力，适合深入推理任务。针对医疗文本和图像数据进行预训练,覆盖放射影像、病理切片、眼科图像、皮肤科图像等。


- 

两种模型都支持在单块 GPU 上进行推理和微调，降低部署门槛。

![image]()



使用场景（Common Use Cases）



1. 🖼 医学图像分类（Image Classification）


- 

适用于：X 光、病理切片、眼底图像、皮肤病图像等；

- 

MedGemma 4B 的预训练提供强大起点；

- 

注意：尚未达到临床级标准，需后续微调和验证。



---



2. 🔍 医学图像解读（Image Interpretation）


- 

任务包括图像问答、图像报告生成；

- 

能生成自然语言报告，回答“图像中发生了什么”；

- 

强于同尺寸模型，但仍需专业适配以满足临床应用需求。



---



3. 📖 医学文本理解与临床推理


- 

适用于：患者问诊摘要、病历三分、诊断建议、临床决策支持等；

- 

推荐使用 27B 文本模型 版本；

- 

基线表现良好，适合作为构建智能问诊与摘要工具的底座。



模型适配方式（Model Adaptation Methods）



1. 🎯 Prompt Engineering / In-context Learning


- 

通过设计提示词、few-shot 示例进行提示增强；

- 

可引导模型将任务拆解为子任务执行（结构化推理）；

- 

虽然无需修改模型参数，但仍需进行严格验证。



2. 🧪 微调（Fine-tuning）


- 

支持使用 LoRA 等高效微调方法；

- 

可微调：

- 

语言模型部分：提升视觉 token 解读能力；

- 

图像与文本联合模型：提升端到端性能；


- 

官方提供了示例 Notebook 说明微调方法。



3. 🤖 Agentic Orchestration（代理系统编排）


- 

将 MedGemma 集成进更大的智能体系统；

- 

与其他工具联动：

- 

Web 检索引擎；

- 

FHIR 解析器；

- 

Gemini Live（语音对话）；

- 

Gemini Pro（函数调用与推理）；


- 

支持局部处理私密数据，结果上传至中心模型继续处理。



---



📎 使用须知与限制


- 

非临床级模型：尽管在医疗领域表现强劲，但 MedGemma 仍需开发者对实际任务进行验证与改进；

- 

遵循 Health AI Developer Foundations terms of use；

- 

仅限于合规、非商业、非治疗直接用途场景中使用。



GitHub：https://github.com/google-health/medgemma


模型下载：https://huggingface.co/collections/google/medgemma-release-680aade845f90bec6a3f60c4 


Demo：https://huggingface.co/spaces/google/rad_explain 


官方文档：https://developers.google.com/health-ai-developer-foundations/medgemma


---



SignGemma：手语识别与翻译模型



SignGemma 是一款手语理解模型，将于今年晚些时候推出。   它是一个大规模多语言模型，最擅长将 ASL 翻译成英文文本，从而进一步为聋人和听力障碍用户提供技术访问权限。 


功能与用途

- 

用于理解和翻译手语，尤其是 ASL（美式手语） 转换成英文文本。

- 

目标用户为听障与聋人社区，帮助其更方便地接入数字技术与通信工具。



技术特点

- 

多语言支持：具备识别多种手语方言的能力。

- 

提升辅助技术的可达性，是 Google 推进 AI 包容性的一个重要项目。



状态与后续

- 

预计将在今年晚些时候发布。

- 

正在收集社区反馈，用户可登记参与早期测试计划。



---



DolphinGemma：模拟海豚语言的模型


- 

模型类型：Gemma 系列衍生的大语言模型，参数量约 400M

- 

输入输出：音频输入 - 音频输出

- 

类似人类语言模型预测“下一个词”，DolphinGemma 预测“下一个海豚音”




功能与用途

- 

能够合成新型海豚声音信号，用于研究跨物种的声音交流方式。

- 

有潜力成为实现“人-海豚对话”式交互的第一步。



研究背景

- 

模型基于超过 40 年的海豚声音数据和研究成果训练而成。

- 

是语言模型（LLM）与动物行为研究相结合的一次创新尝试。



潜在影响

- 

开启“人类与动物沟通”研究的新阶段。

- 

可能在动物保护、行为研究、海洋探索等领域带来突破。



DolphinGemma 的研究目标与功能



✅ 1. 分析自然交流


- 

捕捉声音结构和复合模式，如：

- 

“签名哨音”：个体身份呼叫

- 

“爆发脉冲”：打斗或社交互动时出现

- 

“点击声”：求偶或驱赶鲨鱼


- 

帮助研究者识别声学模式的结构、上下文关系及序列规则



---



✅ 2. 预测和生成海豚声音


- 

基于已知序列生成逼真的“海豚语音段”，如哨音或脉冲；

- 

早期实验已经能生成仿真度高的样本，支持进一步研究互动语境。



---



✅ 3. 建立互动词汇系统（通过 CHAT 系统）


- 

与 Georgia Tech 合作研发的 CHAT（Cetacean Hearing Augmentation Telemetry）系统用于建立人类-海豚共用词汇表。

- 

步骤包括：

- 

使用合成哨音代指物体（如海藻、玩具等）；

- 

海豚通过模仿这些哨音来“请求”物体；

- 

研究人员通过骨传导耳机收到“翻译反馈”，实时回应。


- 

DolphinGemma 可用来预测模仿意图，提高响应速度与交互自然性。



详细介绍：https://blog.google/technology/ai/dolphingemma/

---

*来源：[三款Gemma 模型变体：能单块 GPU运行的医疗模型MedGemma、手语模型SignGemma 和 海豚语言模型DolphinGemma](https://www.xiaohu.ai/p/gemma-gpu-medgemma-signgemma-dolphingemma/21788020)*
