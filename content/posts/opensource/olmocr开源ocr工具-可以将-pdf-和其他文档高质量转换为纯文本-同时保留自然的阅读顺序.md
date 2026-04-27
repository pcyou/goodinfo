---
title: "olmOCR：开源OCR工具 可以将 PDF 和其他文档高质量转换为纯文本 同时保留自然的阅读顺序"
date: 2025-03-01T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "olmOCR 是由 Allen Institute for AI (AI2) 开发的一款 开源 OCR（光学字符识别）工具，专门用于 高精度从 PDF 文本提取，能保持文本的 阅读顺序，并支持 表格、数学公式、手写内容 的解析。   主要优势包括：   -   高性能：在 25 万页 多样化 PDF"
source_url: "https://www.xiaohu.ai/p/olmocr-ocr-pdf/19103916"
xiahuid: "19103916"
---

## 📰 正文

olmOCR 是由 Allen Institute for AI (AI2) 开发的一款 开源 OCR（光学字符识别）工具，专门用于 高精度从 PDF 文本提取，能保持文本的 阅读顺序，并支持 表格、数学公式、手写内容 的解析。


主要优势包括：


- 

高性能：在 25 万页 多样化 PDF 训练数据上进行微调，涵盖 电子文档 以及 扫描书籍，能精准提取文本。

- 

低成本：相比使用 GPT-4o API 进行 PDF 解析，处理 100 万页 PDF 仅需约 190 美元，成本仅为 1/32。

- 

Markdown 输出：生成易解析的 Markdown 格式文本，保留 表格、数学公式、手写文本，并确保 正确阅读顺序。

- 

完整开源：基于 Qwen2-VL-7B-Instruct 训练，开源提供模型权重、训练数据、推理代码，方便社区使用和优化。

![image]()



主要技术亮点



1. 文档锚定（Document Anchoring）技术

- 

通过 结合 PDF 的文本和元数据，改进文本提取质量。

- 

方法：

- 

提取 页面图像 和 文本块 并合并。

- 

使用 GPT-4o 处理 25 万页数据，生成高质量标注数据。

- 

数据集包括 60% 学术论文，12% 宣传册，11% 法律文档，6% 图表，5% 幻灯片，4% 其他类型。




  

![image]()


2. 高效推理（Inference）

- 

使用 SGLang 和 vLLM 进行推理，支持 单 GPU 到多 GPU 扩展。

- 

批量处理优化，单页成本 远低于 GPT-4o API。



3. 优秀的 OCR 质量

- 

对比实验：

- 

与 Marker、GOT-OCR 2.0、MinerU 等工具对比，在 2017 份 PDF 的 452 次对比实验 中：

- 

比 Marker 更好 61.3%

- 

比 GOT-OCR 2.0 更好 58.6%

- 

比 MinerU 更好 71.4%


- 

通过 ELO 评分，olmOCR 显著领先 其他工具，评分超过 1800。






![image]()


一些案例：



手写稿

![image]()


历史文献

![image]()


数学教科书

![image]()


GitHub：https://github.com/allenai/olmocr 


技术报告：https://olmocr.allenai.org/papers/olmocr.pdf 


在线体验：https://olmocr.allenai.org/

---

*来源：[olmOCR：开源OCR工具 可以将 PDF 和其他文档高质量转换为纯文本 同时保留自然的阅读顺序](https://www.xiaohu.ai/p/olmocr-ocr-pdf/19103916)*
