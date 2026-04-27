---
title: "Claude-scientific-skills：一套 Claude 的科学技能库 138个即插即用的科学技能 覆盖20+领域"
date: 2026-01-05T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "Claude Scientific Skills 是由 K-Dense Inc. 团队开发的开源项目，旨在为 Anthropic 的 Claude 模型提供系统化的 科学计算与研究能力扩展插件集。   该项目包含 138 个预构建科学技能（Scientific Skills），覆盖从 生命科学、化学"
source_url: "https://www.xiaohu.ai/p/claude-scientific-skills-claude-138-20/28278512"
xiahuid: "28278512"
---

## 📰 正文

Claude Scientific Skills 是由 K-Dense Inc. 团队开发的开源项目，旨在为 Anthropic 的 Claude 模型提供系统化的 科学计算与研究能力扩展插件集。


该项目包含 138 个预构建科学技能（Scientific Skills），覆盖从 生命科学、化学、医学、材料科学、物理学、工程学到机器学习 的主要科研领域。


项目通过 MCP（Model Context Protocol） 框架使 Claude 能够直接调用高水平科研工具和数据库，实现从数据检索到建模分析、从多组学集成到报告生成的全流程科研任务自动化。


Claude Scientific Skills 的核心目标是：

> 

将 Claude 从通用语言模型扩展为具备专业科研能力的 AI 研究助理（AI Co-Scientist）。



它通过标准化接口封装科研工具，使 Claude 能够：
1. 

调用专业数据库与科学计算库；

2. 

执行复杂多步科研分析流程；

3. 

生成可重复、可审查的科学结果；

4. 

进行科学写作、文献综述与可视化。



该体系的核心优势在于 跨领域融合 —— 用户无需自行集成不同的科学库与API，Claude可在单一环境中完成从数据采集 → 分析建模 → 结果可视化 → 科学写作的全流程任务。

> 

一句话就是：一个能让 Claude变成“AI 科学家”的工具箱。它为 Claude 加上了 138 个科学技能，能自动完成科研分析、建模、图表制作，甚至撰写论文。

![image]()



主要功能与模块



Claude Scientific Skills 包含 138 项科学技能，分布在多个科研领域中：


1️⃣ 生物与医学类


![image]()

- 

生物信息学与基因组学：序列分析、单细胞RNA-seq、变异注释、系统生物学等。

- 

化学与药物发现：分子性质预测、虚拟筛选、分子对接、药物优化（RDKit、DiffDock、DeepChem）。

- 

蛋白质组学与质谱学：LC-MS/MS 分析、蛋白鉴定与定量。

- 

临床研究与精准医疗：药物安全性分析、临床试验检索、变异解释、药物基因组学。

- 

医学影像与病理学：DICOM 图像分析、数字病理切片识别。



2️⃣ AI与计算科学类


![image]()

- 

机器学习与AI：深度学习、强化学习、时序分析、贝叶斯推断、模型可解释性。

- 

多组学整合与系统生物学：多模态整合、通路富集、网络生物学。

- 

材料科学与物理：晶体结构分析、量子计算（Qiskit、PennyLane）。

- 

工程与仿真：系统建模、优化仿真、流体动力学。



3️⃣ 数据与科研支持类


![image]()

- 

数据分析与可视化：统计分析、网络可视化、出版级图表绘制（Matplotlib、Seaborn）。

- 

实验室自动化：实验协议自动化、LIMS系统集成、Opentrons控制。

- 

科学传播与写作：文献综述、同行评审、论文写作、幻灯片与海报生成。

- 

研究方法学：假设生成、科研思维、基金申请、学者评估。



典型科研工作流实例



1. 药物筛选与分子优化


> 

任务：筛选潜在的 EGFR 抑制剂用于肺癌治疗。



自动化流程：
1. 

查询 ChEMBL 获取已知 EGFR 抑制剂（IC50 < 50nM）；

2. 

使用 RDKit 分析分子结构与SAR关系；

3. 

借助 Datamol 生成衍生物并评估ADMET性质；

4. 

利用 DiffDock 进行虚拟对接；

5. 

查询 COSMIC 获取突变背景；

6. 

使用 PubMed 搜索耐药机制文献；

7. 

生成整合报告。



涉及技能： RDKit, DiffDock, DeepChem, PubMed, COSMIC, ReportLab


---



2. 单细胞RNA-seq分析


> 

任务：分析10X Genomics单细胞数据集，识别细胞类型并进行通路富集。



执行步骤：
1. 

读取10X数据 → Scanpy进行质量控制；

2. 

移除双细胞并整合Cellxgene数据库；

3. 

基于 NCBI Gene 标记识别细胞类型；

4. 

使用 PyDESeq2 进行差异表达分析；

5. 

通过 Reactome/KEGG 进行通路富集；

6. 

自动生成报告与可视化图表。



涉及技能： Scanpy, Arboreto, KEGG, Reactome, PyDESeq2


---



3. 临床变异解释


> 

任务：解读VCF文件以评估遗传性肿瘤风险。



执行步骤：
1. 

使用 pysam 解析VCF文件；

2. 

查询 Ensembl VEP 注释变异；

3. 

联合 ClinVar / COSMIC 获取致病性信息；

4. 

查询 ClinPGx 提取药物基因组学关联；

5. 

使用 ReportLab 自动生成临床报告。



涉及技能： pysam, Ensembl, ClinVar, COSMIC, ClinPGx, ReportLab


安装与配置流程（技术说明）



环境要求


- 

Python ≥ 3.9（推荐3.12）

- 

系统：macOS / Linux / Windows (WSL2)

- 

依赖管理工具：uv

- 

客户端：Claude Code / Cursor / 任意MCP兼容客户端



安装示例



```None
# 1. 安装 Claude Code
curl -fsSL https://claude.ai/install.sh | bash

# 2. 注册科学技能插件
/plugin marketplace add K-Dense-AI/claude-scientific-skills

# 3. 安装技能集
Open Claude Code → Plugins → Install “scientific-skills”

```



Claude 将自动检测科研任务并加载对应技能。

- 

🌐 GitHub地址：https://github.com/K-Dense-AI/claude-scientific-skills

- 

📄 许可证：MIT（允许商业使用）

- 

⭐ Star 数：4.2k+

- 

🧑‍💻 作者：K-Dense Inc.

- 

🧩 兼容平台：Claude Code、Cursor IDE、任意 MCP 客户端（包括 ChatGPT、OpenAI Agent SDK 等）

---

*来源：[Claude-scientific-skills：一套 Claude 的科学技能库 138个即插即用的科学技能 覆盖20+领域](https://www.xiaohu.ai/p/claude-scientific-skills-claude-138-20/28278512)*
