---
title: "Google 发布开源医疗模型 MedGemma 1.5 4B 和医疗语音识别模型 MedASR"
date: 2026-01-14T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Google 在 2024 年发布了 MedGemma 系列：一套开放的医疗生成式AI模型，用于医疗文本与影像任务。 这一系列属于 Health AI Developer Foundations（HAI-DEF） 计划的一部分，允许开发者基于 Google Cloud 和 Vertex AI 自主定"
source_url: "https://www.xiaohu.ai/p/google-medgemma-1-5-4b-medasr/28603292"
xiahuid: "28603292"
---

## 📰 正文

Google 在 2024 年发布了 MedGemma 系列：一套开放的医疗生成式AI模型，用于医疗文本与影像任务。
这一系列属于 Health AI Developer Foundations（HAI-DEF） 计划的一部分，允许开发者基于 Google Cloud 和 Vertex AI 自主定制医疗AI应用。


发布后，MedGemma 模型在 Hugging Face 上被下载数百万次，衍生出数百种社区版本。


此次更新发布了 MedGemma 1.5 4B 模型（40亿参数），主打：

- 

支持多模态（文本 + 图像 + 医学报告）

- 

优化医疗影像的理解与结构化分析

- 

可本地运行，也可在云端扩展（Google Cloud / Vertex AI）



它能理解的内容包括：

1. 

医学影像：CT、MRI、X光、病理切片等；

2. 

医学文本：病历记录、化验报告、病理描述等；

3. 

多时间点数据：同一个病人的影像随时间变化，例如对比两次胸片；

4. 

解剖学定位：识别出影像中具体的器官或结构位置；

5. 

实验室数据提取：从化验单中提取数值、单位和检测类型。

![image]()



MedGemma 1.5 的性能提升



Google在这次更新中，不只是增加功能，还大幅提高了准确率。下面是关键指标的变化：

![image]()

![image]()


影像理解能力更强了，尤其是在CT、MRI、病理和结构定位方面。

![image]()


Google还指出，这个模型的3D影像理解能力在开源领域属于“首创”，是第一个公开能解释三维医学数据的开源模型。

![image]()


模型的使用方式



MedGemma 1.5 有多种用法。

- 

开发者可以用它来训练新的医学 AI 系统；

- 

医院可以基于它定制特定科室的辅助工具；

- 

医学研究者可以用它来分析大规模影像数据集。



这个模型支持DICOM格式，也就是医院通用的医学影像标准文件，所以几乎能无缝地接入现有医疗系统。


MedASR：专为医疗语音打造的语音识别模型



除了图像模型，Google 还发布了一个全新的医疗语音识别模型——MedASR。


在医疗场景里，医生最常用的沟通方式其实是“口述”。
无论是病历录音、影像描述，还是医患交流，都依赖语音。

![image]()


这款专为医疗场景优化的语音识别系统（ASR），可以：

- 

将医生口述的病历、影像描述转成文字；

- 

与 MedGemma 联动，实现“语音输入 + AI推理”。



性能对比：


谷歌将 MedASR 与 OpenAI 的 Whisper large-v3（通用语音模型）进行了比较：

- 

在胸片口述任务中，MedASR 的错误率为 5.2%，Whisper 为 12.5%；

- 

在综合医学口述任务中，MedASR 的错误率为 5.2%，Whisper 为 28.2%。



也就是说，MedASR 比通用模型的语音识别准确率高出了一倍以上。
对于需要口述病历或生成医疗报告的医生来说，这会极大地提升效率。

![image]()


开放性



Googl继续保持了开放策略：

- 

所有 HAI-DEF 模型，包括 MedGemma、MedASR、MedSigLIP，都是免费可商用的；

- 

模型可在 Hugging Face 上下载，也能直接在 Vertex AI 上运行；



详细内容：https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/ 


模型下载：https://huggingface.co/google/medgemma-1.5-4b-it

---

*来源：[Google 发布开源医疗模型 MedGemma 1.5 4B 和医疗语音识别模型 MedASR](https://www.xiaohu.ai/p/google-medgemma-1-5-4b-medasr/28603292)*
