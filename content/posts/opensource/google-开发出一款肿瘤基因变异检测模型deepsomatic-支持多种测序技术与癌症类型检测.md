---
title: "Google 开发出一款肿瘤基因变异检测模型：DeepSomatic 支持多种测序技术与癌症类型检测"
date: 2025-10-19T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "研究背景：AI 正进入癌症基因学的核心环节    癌症的本质是一种 基因调控失衡 导致的疾病。 当细胞的 DNA 损伤修复系统或分裂控制基因被突变破坏时， 细胞可能无限制分裂、逃避免疫系统、甚至入侵身体其他组织。   每种癌症都拥有独特的 基因突变组合（mutational signature），"
source_url: "https://www.xiaohu.ai/p/google-deepsomatic/26121311"
xiahuid: "26121311"
---

## 📰 正文

研究背景：AI 正进入癌症基因学的核心环节



癌症的本质是一种 基因调控失衡 导致的疾病。
当细胞的 DNA 损伤修复系统或分裂控制基因被突变破坏时，
细胞可能无限制分裂、逃避免疫系统、甚至入侵身体其他组织。


每种癌症都拥有独特的 基因突变组合（mutational signature），
这些突变决定了癌症的性质、发展速度和对药物的反应。


在现代肿瘤学中，
识别这些突变（尤其是“驱动突变”，即推动癌变的关键基因变异）
是**精准医学（Precision Medicine）**的基础。


但目前这项工作仍存在困难：

- 

测序数据复杂且噪声多；

- 

肿瘤细胞异质性高（不同细胞突变不同）；

- 

体细胞突变比例极低，常被测序误差掩盖。



因此，Google Research 与 UC Santa Cruz Genomics Institute 及美国国家癌症研究所合作开发的
一款基于深度学习的肿瘤基因变异检测模型：DeepSomatic。——一款专门识别肿瘤基因突变的深度学习系统，旨在让 AI 成为分子肿瘤学的“显微镜”。


---



什么是 DeepSomatic？



DeepSomatic 是一个基于卷积神经网络（CNN）的 AI 工具，
能够从基因测序数据中精准地识别肿瘤细胞的 体细胞突变（somatic variants）。


体细胞突变不同于从父母遗传的“生殖系突变（germline variants）”，
它们是癌症发生后在身体细胞中产生的新突变，
通常由紫外线、化学致癌物、放射线或 DNA 复制错误引起。


DeepSomatic 能够自动：

- 

从基因组测序数据中分辨出真实突变与测序误差；

- 

判断哪些突变只存在于肿瘤细胞中；

- 

支持多种测序技术与癌症类型。

![image]()



Google 称它为：

> 

“首个跨测序平台、跨癌种的 AI 突变检测系统。”



---



技术机制：把基因数据“变成图像”交给 AI



DeepSomatic 的核心创新是：将基因组数据转换为视觉图像，再用深度学习识别突变模式。


步骤详解：

1. 

基因测序与比对
从患者获取肿瘤样本（Tumor）与正常样本（Normal），
通过 Illumina / PacBio / Oxford Nanopore 等平台测序，
得到每个 DNA 片段的碱基序列。

2. 

数据可视化
DeepSomatic 将测序输出的数据（序列比对、信号强度、错误概率等）
转换为一张多通道图像（类似热图），
每个像素代表 DNA 上一个位置的多维信号。

3. 

卷积神经网络分析
CNN 网络学习这些“基因图像”中的复杂模式，
并区分：

- 

正常基因序列；

- 

遗传性变异（存在于所有细胞中）；

- 

癌症特有的体细胞突变；

- 

测序噪声或技术误差。


4. 

突变报告输出
模型最终输出一份突变列表（mutation list），
包括变异类型（SNV、Indel 等）、位置、可信度及潜在致病性。



这种“图像化建模”方式让 AI 能跨平台学习通用特征，
无需依赖某个特定测序厂商的数据结构。


---



为什么这是突破？



📉 以往的问题：


- 

现有工具（如 MuTect2、Strelka2、SomaticSniper）多基于统计模型；

- 

不同测序技术的误差模式不同（Illumina 短读 vs PacBio 长读）；

- 

模型无法泛化到其他癌种；

- 

对 Indel（插入/缺失）检测尤其不稳定。



🚀 DeepSomatic 的改进：


![image]()


---



核心数据集：CASTLE



为训练 DeepSomatic，Google 构建了一个全新的高质量标准数据集：

> 

🧫 CASTLE（Cancer Standards Long-read Evaluation）Dataset

![image]()



特点：


![image]()


这套数据集不仅用于 DeepSomatic，也公开发布，
成为肿瘤突变检测研究的通用参考标准。


---



模型训练与性能结果



Google 团队在 6 个样本上训练并测试模型。
实验包括多种交叉验证方法（例如保留一个样本和一个染色体用于独立测试）。

![image]()


📈 结果要点：


![image]()

> 

在实验中，研究团队使用六个标准化肿瘤细胞系及一个保存组织样本进行验证，
DeepSomatic 共识别出 329,011 个肿瘤体细胞突变，
表现出卓越的检测灵敏度与可靠性。


尤其在识别 插入或缺失类型（Indels） 的基因变异时，
该模型的性能大幅超越现有技术。


这类 Indel 变异是癌症中最具挑战性、但又最关键的突变类型之一，
因为它们往往会导致基因编码框架的移位，从而改变蛋白质功能。


在衡量模型平衡性能的 F1 指标 上——
该指标同时考虑了检出率（召回 recall）与准确率（精度 precision）——
DeepSomatic 取得了显著提升：

- 

在 Illumina 测序数据中，第二优秀的算法 Indel 检测得分为 80%，
而 DeepSomatic 达到 90%；

- 

在 Pacific Biosciences（PacBio）长读长数据中，
其他工具的准确率不足 50%，
而 DeepSomatic 超过了 80%。



换言之，DeepSomatic 在最具挑战性的突变类型上，
准确率与召回率均实现了跨平台的跃升，
标志着 AI 模型在肿瘤基因变异识别领域的重大进步。





![image]()


此外，DeepSomatic 还在**降质样本（FFPE）与仅测外显子（WES）**的数据上保持领先，
显示其在实际临床环境中具备高度可用性。


---



跨癌种与特殊样本测试



研究团队进一步在不同癌症类型与不同样本条件下测试 DeepSomatic：

![image]()


✅ 结果表明：

> 

DeepSomatic 具有跨癌种、跨测序平台的强泛化能力，
可用于多种临床与科研场景。



1️⃣ 脑癌（Glioblastoma）


DeepSomatic 能在训练数据之外的癌症中识别突变。
在胶质母细胞瘤样本中，它准确发现了关键驱动变异。
➡️ 说明模型具备跨癌种迁移能力。


2️⃣ 儿童白血病（Leukemia）


白血病存在于血液中，无法获得“正常对照”样本。
DeepSomatic 的“肿瘤单样本模式（tumor-only mode）”仍能识别出：

- 

已知突变；

- 

10 个新发现突变。
➡️ 证明模型可在无对照条件下运行。



3️⃣ FFPE 样本


这种组织保存方式会引入 DNA 损伤，常使传统算法失效。
DeepSomatic 成功识别真实突变并排除假阳性，
让历史样本重新具备分析价值。


---



模型的临床价值


![image]()


DeepSomatic 的意义不仅是“更准”，
而是让AI 能在现实医学中可靠使用。


临床应用 说明 精准诊疗 精确识别驱动突变，匹配靶向药或免疫疗法 个体化治疗 根据突变特征预测药物敏感性 罕见癌症研究 帮助揭示未知致癌机制 样本修复 拯救因保存损伤而失去分析价值的 FFPE 样本 低成本检测 支持 WES 数据，适合资源受限实验室


---



开放共享与合作伙伴



Google 已将：

- 

DeepSomatic 模型；

- 

CASTLE 数据集；

- 

训练管线与工具；
全部开放源代码与数据。



合作机构：


- 

UC Santa Cruz Genomics Institute

- 

美国国家癌症研究所（NCI）

- 

Frederick 国家实验室

- 

儿童慈善医院（Children’s Mercy Hospital）

- 

纽约大学（NYU）



这一开放生态将大幅降低研究门槛，
促进全球癌症基因学研究的标准化与复现性。


---



官方介绍：https://research.google/blog/using-ai-to-identify-genetic-variants-in-tumors-with-deepsomatic


论文：https://www.nature.com/articles/s41587-025-02839-x

---

*来源：[Google 开发出一款肿瘤基因变异检测模型：DeepSomatic 支持多种测序技术与癌症类型检测](https://www.xiaohu.ai/p/google-deepsomatic/26121311)*
