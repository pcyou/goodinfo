---
title: "DeepSeek 推出其最新实验性语言模型 DeepSeek-V3.2-Exp 大幅提升了推理效率并降低了计算成本"
date: 2025-09-29T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "DeepSeek 推出其最新实验性语言模型 DeepSeek-V3.2-Exp，这是基于前代 V3.1-Terminus 构建的新版本。此次更新的最大亮点是引入了 DeepSeek Sparse Attention（DSA）机制，该技术可在长上下文处理中实现稀疏注意力分配，显著提升了推理效率并降低了"
source_url: "https://www.xiaohu.ai/p/deepseek-deepseek-v3-2-exp/25491727"
xiahuid: "25491727"
---

## 📰 正文

DeepSeek 推出其最新实验性语言模型 DeepSeek-V3.2-Exp，这是基于前代 V3.1-Terminus 构建的新版本。此次更新的最大亮点是引入了 DeepSeek Sparse Attention（DSA）机制，该技术可在长上下文处理中实现稀疏注意力分配，显著提升了推理效率并降低了计算成本，同时几乎不会影响生成质量。


性能方面，基准测试显示 V3.2-Exp 在整体表现上与 V3.1-Terminus 持平，但效率更高。该模型目前已在 App、Web 和 API 平台全面上线，API 使用价格也下调超过 50%，极大降低了开发者的使用门槛。


模型定位



DeepSeek-V3.2-Exp 是 DeepSeek 团队在 2025 年发布的实验性大型语言模型。
它的主要目标是探索 长上下文（long-context）任务的计算效率优化，在保持模型质量的同时，大幅减少训练和推理的计算成本。


该版本基于 V3.1-Terminus，引入了新的 DeepSeek Sparse Attention（稀疏注意力机制，简称 DSA）。


---



技术核心：DeepSeek Sparse Attention (DSA)



传统 Transformer 使用全注意力机制，计算复杂度随着文本长度平方级增长。
DSA 的思路是 在注意力计算中引入稀疏性，只计算最有价值的部分，从而减少冗余计算。


新技术：引入了 稀疏注意力 (DSA)

- 

普通大模型在处理长文本时，计算量会随着文本变长而快速增加，很慢也很耗资源。

- 

稀疏注意力的思路是：只关注文本里重要的部分，而不是所有内容，这样速度更快，显存占用更少，但输出质量基本不变。



特点：

- 

细粒度控制：不是简单丢弃信息，而是智能筛选。

- 

效率提升：在长文本场景下，训练和推理速度显著提高。

- 

质量保持：在大多数基准测试中，输出效果与之前版本几乎一致。

![image]()



实际推理效率



论文里对比了 V3.1 和 V3.2 在 H800 GPU 集群上的运行成本（单位：美元 / 百万 tokens，按 2 USD/GPU·h 计价）。


结果如下：


Prefilling 阶段（输入长文本时）

- 

V3.1 成本 ≈ 0.6 美元/百万 tokens

- 

V3.2 成本 ≈ 0.3 美元/百万 tokens
➡️ 成本下降约 50%



Decoding 阶段（逐步生成输出时）

- 

V3.1 成本 ≈ 2.0 美元/百万 tokens

- 

V3.2 成本 ≈ 1.0 美元/百万 tokens
➡️ 成本下降约 50%



整体结果：

- 

速度：在长文本推理中，生成和输入阶段都快了一倍左右

- 

成本：整体 下降约 50%，特别适合处理 >32K tokens 的长文档/对话

- 

短文本场景：提升不大（甚至接近持平），优势主要体现在长上下文



---



模型规模与文件


- 

参数量：6850 亿（685B）参数

- 

数据类型：支持 BF16、FP8、FP32（兼顾精度和性能）

- 

权重格式：Safetensors

- 

许可证：MIT（开放源代码，允许研究和商用）



---



性能表现（与 V3.1 对比）



官方对比了多个公开基准，结果显示整体表现持平或略有差异。

- 

提升的领域：

- 

AIME 2025（数学推理）89.3 > 88.4

- 

Codeforces（编程题解）2121 > 2046

- 

中文浏览任务（BrowseComp-zh）47.9 > 45.0


- 

下降的领域：

- 

GPQA-Diamond（高难度问答）79.9 < 80.7

- 

HMMT 2025（数学测试）83.6 < 86.1


![image]()



➡️ 结论：V3.2 在长上下文、代码和中文任务中表现更好，总体质量与 V3.1 持平。


API 优惠：


- 

API 使用价格即日起下降超过 50%，用户成本大幅降低。

- 

兼容性支持：V3.1-Terminus 暂时仍可通过 API 使用，支持对比测试（截至 2025 年 10 月 15 日）。

![image]()



模型下载：https://huggingface.co/deepseek-ai/DeepSeek-V3.2-Exp 


技术报告：https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/DeepSeek_V3_2.pdf

---

*来源：[DeepSeek 推出其最新实验性语言模型 DeepSeek-V3.2-Exp 大幅提升了推理效率并降低了计算成本](https://www.xiaohu.ai/p/deepseek-deepseek-v3-2-exp/25491727)*
