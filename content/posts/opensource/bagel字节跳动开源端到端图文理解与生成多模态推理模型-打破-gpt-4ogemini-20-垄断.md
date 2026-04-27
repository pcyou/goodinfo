---
title: "BAGEL：字节跳动开源端到端图文理解与生成多模态推理模型 打破 GPT-4o、Gemini 2.0 垄断"
date: 2025-05-25T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "BAGEL（Batched Attention Generalist for Emergent Learning） 是由字节跳动开发的一个具备端到端图文理解与生成能力的开源多模态大模型，目标是打造：  -   开源可控的 GPT-4o、Gemini 2.0 替代方案  -   支持图像 + 文本输入"
source_url: "https://www.xiaohu.ai/p/bagel-gpt-4o-gemini-2-0/21787797"
xiahuid: "21787797"
---

## 📰 正文

BAGEL（Batched Attention Generalist for Emergent Learning） 是由字节跳动开发的一个具备端到端图文理解与生成能力的开源多模态大模型，目标是打造：

- 

开源可控的 GPT-4o、Gemini 2.0 替代方案

- 

支持图像 + 文本输入输出

- 

能够进行自由形式的图文生成与理解，包括图像编辑、推理、组合建模、世界建模等；

- 

能处理编辑、生成、风格转化、导航推理等复杂任务



其最大亮点是：统一多模态架构（Unified Multimodal Model） + 开放可用性。


BAGEL 想做的，是一个“统一”的大模型，能同时理解和生成文本、图片、视频等内容，而不是像传统方法那样：一个模型负责理解，一个模型负责生成，还要彼此沟通协作。


它的关键目标是：

- 

一个模型统一完成理解和生成

- 

支持多种模态混合输入，比如图片夹杂文字、视频夹杂描述

- 

能思考、会推理，处理复杂任务时不是“一步到位”，而是“先想清楚再动手”



自己会“思考”



BAGEL 具备 推理链机制（Reasoning Chain），就是说：

- 

在生成图像或编辑内容前，模型可以先用文字“自己思考”该怎么做。

- 

例如：你说“把图片里的猫变成蓝色的”，它会先在内部整理为：

- 

确认图像里有猫

- 

猫是哪一部分

- 

应该保留哪些细节

- 

如何在不破坏背景的前提下改变颜色


- 

然后再执行这个生成或编辑任务



这种“先思考后行动”的方式，使得 BAGEL 能够处理复杂的生成任务，而不仅仅是表面响应。

![image]()




![image]()


主要功能



1、 多模态聊天与理解


![image]()


模型能同时处理和理解文本、图像、视频等不同模态的信息，回答用户问题、识别内容、提取知识。


📌 支持的理解任务：

- 

图文问答（VQA）：理解图像并回答相关问题；

- 

图像内容识别：如物体检测、属性识别、场景分析；

- 

复杂推理：理解多张图之间的关系、时间顺序、空间关系等；

- 

文档理解：识别表格、图表、OCR文本等；

- 

数学与科学推理：支持在图像中推理数学公式、物理现象等。

![image]()



2 、图像生成（Image Generation）


![image]()


根据用户提供的文字描述，生成高质量图像，支持多样风格、复杂语义、现实或幻想场景。


📌 特性亮点：

- 

支持中英文自然语言生成

- 

丰富场景控制能力（人物、风格、构图、动作等）

- 

支持长句理解与细节还原

- 

支持自由设置图片尺寸与比例

![image]()


- 

支持自然语言生成照片级图像或视频帧

- 

训练于大规模交错式图文数据（视频帧 + 文本）

- 

使用 “思考后生成（<think>）”机制，生成更合理的细节

- 

此外，BAGEL 可以生成任意尺寸与宽高比的图像，这使其具备适应多种内容展示需求的能力。



3、 图像编辑（Image Editing）


![image]()


对已有图片进行编辑，包括局部修改、风格变换、物体添加/删除、结构变换等。


📌 支持的编辑类型：

- 

普通编辑任务：

- 

替换背景、换颜色、裁剪、旋转、局部修改等；

- 

多图连续编辑（如漫画连环变化）；


- 

智能编辑任务（Intelligent Editing）：

- 

需要推理与生成相结合，如“把这辆车变成未来版本”；

- 

根据用户目标进行复杂合成，例如"猫变成火龙，背景是火山爆发"；

- 

零样本图像构造（没有参考图也能准确合成）；


![image]()

![image]()

![image]()



4、导航与世界建模（Navigation & Motion Modeling）


![image]()


BAGEL 不仅能生成单一静态图像，还能模拟“真实世界的演化”。


模拟或推理物理世界中事件变化、时序动态、空间迁移，具备基本的物理/认知模拟能力。


这包括从视觉连续性（如视频帧）、三维构图、多视角推理，到真实物理场景的建模。


📌 关键能力：

- 

未来帧预测：给定视频/图片序列，预测下一帧场景；

- 

空间导航：给定地图或图像，推理/生成不同视角内容；

- 

3D 视角转换：多视图图像生成；

- 

概念变换：如“日间转为夜景”、“黑白画转彩色油画”。

![image]()



这些能力表明 BAGEL 不仅是“图像工具”，而是具备推理和“想象力”的认知模型。

- 

学习自视频数据，对世界建模能力强

- 

能模拟现实或虚拟环境中“移动与导航”的动作序列

- 

应用于机器人控制、虚拟游戏角色导航等场景



---



5、组合能力与推理（Composition + Thinking）


![image]()


BAGEL 引入了“Think”机制，在生成图片前先进行文字形式的“推理”，提升目标明确性与生成质量。


这种机制让 BAGEL 的 解释性 与 控制力 显著提升。

- 

拥有多轮推理能力，可将一个简单命令展开为复杂操作序列

- 

支持“思考”模块处理图文生成任务中的多步骤逻辑结构



📌 流程：
1. 

用户输入：“你能展示一下这块布料展开后的样子吗？”；

2. 

模型先“思考”：


```None
<think> The question_image shows a rolled-up piece of fabric with a colorful patchwork design featuring floral patterns and striped sections. The question_text asks for the fabric to be displayed unrolled, which implies the user wants to see its full layout and design. To address this, I would consider unrolling the fabric flat on a surface, ensuring all patterns and details are visible. The answer_image should depict the fabric laid out in a way that highlights its patchwork design, including the floral and striped sections. The arrangement should be neat and symmetrical, possibly with the fabric centered on a flat surface like a table or floor. In forming the answer_text, I would describe the fabric as fully unrolled and showcase its vibrant design. The answer_image would likely feature the fabric spread out, revealing its complete patchwork pattern, including the flowers and stripes, and possibly showing the edges of the fabric to give a sense of its size and shape. This approach ensures the user's request is fulfilled. </thinK>

<think>Question_image 展示了一块卷起的布料，上面布满了色彩鲜艳的拼布图案，点缀着花卉图案和条纹部分。Question_text 要求将布料展开显示，这意味着用户希望看到其完整的布局和设计。为了解决这个问题，我会考虑将布料平铺在一个表面上，确保所有图案和细节都清晰可见。answer_image 应该以突出其拼布图案（包括花卉和条纹部分）的方式展示布料的布局。布料的排列应该整齐对称，最好将布料放在桌子或地板等平面的中心位置。在生成 answer_text 时，我会将布料描述为完全展开的状态，并展示其充满活力的设计。answer_image 可能会将布料展开，展现其完整的拼布图案，包括花朵和条纹，并可能显示布料的边缘，以展现其大小和形状。这种方法确保满足用户的需求。</think>
```


3. 

然后执行图像生成，效果更加精确。

![image]()



6、自由视觉操控（Free-form Visual Manipulation）



✅ 功能说明：


用户无需提供具体图像，仅通过自然语言描述或粗略草图引导，模型自动生成复杂、高质量图像。


📌 典型案例：

- 

“用小汽车拼成一辆大汽车”；

- 

“雕像被樱花包围”；

- 

“根据儿童画生成真实玻璃雕塑”；

- 

“画面变暗并加入月光效果”；



这种能力代表模型拥有创意构图与具象生成的合成理解能力。

![image]()


技术方法



用的是什么样的架构？



BAGEL 使用了一种叫做 “混合专家模型”（Mixture-of-Transformers，MoT） 的结构


核心设计：Mixture-of-Transformers（MoT）结构

- 

一个模型中并行使用两个 Transformer 专家：

- 

一个用于理解（文本 + 图像编码）

- 

一个用于生成（图像解码 + 文本生成）


- 

共享注意力层，统一处理多模态 token 序列

- 

这种架构消除了任务之间的“瓶颈接口”，让信息能无损流动



简单来说：

- 

主体框架是一个大型 Transformer 模型，跟 GPT 系列类似。

- 

它在内部设置了两个“专家”：一个擅长理解内容（比如看图、读文），另一个擅长生成内容（比如写字、画图）。

- 

这两个专家可以共享信息，但各自有专长，相当于一个模型里有两个部门，一起工作。



这种结构避免了过去那种“多个模型拼起来”的麻烦，效率更高，能力更统一。




![image]()


输入模态支持：

- 

文本：使用 Qwen2.5 LLM（阿里开源大模型）作为主干

- 

图像理解：采用 SigLIP2 的 ViT 编码器

- 

图像生成：使用来自 FLUX 的 VAE 进行编码和解码

- 

视频数据：用于补充物理连续性与场景动态信息



它是怎么处理图像的？



理解图像时：

- 

用一个叫做 ViT（视觉 Transformer） 的视觉编码器，把图片切成很多小块，然后理解每块的内容，再综合起来理解整张图。



生成图像时：


用另一个叫做 VAE（变分自编码器） 的模块，先把图像转换成一组“图像 token”（类似于文字的拼音），在模型内部处理这些 token，最后再还原出图像。

- 

为了让生成图像的质量更高，BAGEL 使用了一种叫 Rectified Flow 的技术，能更平滑地生成清晰细致的图像。



这些模块是预训练好的，类似给模型安装了“视觉眼睛”和“绘画手”。


它是怎么训练的？



总训练 token 超过 5.6 万亿，构成如下：

- 

文本数据：维持语言能力

- 

图文对（理解+生成）：构建基础视觉语言建模能力

- 

视频交错数据：增强时序建模与运动识别能力

- 

网页交错数据：提供结构化知识与上下文推理能力

- 

推理增强数据（Reasoning-Augmented）：引入链式思考结构，提升模型思维能力



BAGEL 采用了“先打好基础，再不断进阶”的四步训练方法：
1. 

对齐阶段：先把图像和文字输入对齐，训练模型理解两者之间的关系。

2. 

基础预训练阶段：输入大量文本和图文数据，让模型学会基础的语言、图像和生成能力。

3. 

进阶训练阶段：逐步加入更复杂的数据，比如视频帧、网页教程、长图文描述，让模型学会多模态推理。

4. 

监督微调阶段：加入人类标注的高质量训练数据，对模型进行细节调教，让它更贴近人类表达。



每个阶段都会用不同的数据和策略，目标是让模型的能力“层层涌现”。


它还做了哪些技术优化？



为了让模型运行更快、成本更低，BAGEL 还做了一些工程优化：

- 

使用 FlexAttention 加速训练和推理，比原来的方法快一倍以上；

- 

在推理过程中只缓存必要的数据，减少显存使用；

- 

支持任意尺寸的图像输入和输出，适配不同任务；

- 

使用语言位置编码（RoPE）和注意力归一化方法（QK-Norm）保持数值稳定。



评估结果



BAGEL 的整体性能在理解、生成、编辑、推理四个方向上均表现优异，在多数评测中超过所有开源模型，在某些任务上甚至接近或逼近闭源模型（如 GPT-4o、Gemini 1.5 Pro）。


特别地，BAGEL 展现出极强的“能力涌现”特征——随着训练 token 增加（尤其在 3T 以上），模型能力从基础生成逐步跃迁到复杂推理与组合式生成。


1、图文理解能力评估



BAGEL 在以下多模态理解任务中进行了评估：

- 

MME（Multimodal Evaluation for Language and Vision）

- 

MMBench：中文多模态理解能力测试

- 

MMMU：大规模多学科题库（数学、物理、生物等）

- 

MathVista：视觉数学题

- 

MMVet：图像推理与常识问答



结果：

- 

BAGEL 在多数理解类任务中，全面超越所有开源模型，包括 InternVL2.5、Qwen-VL-Max、LLaVA-Next、MiniGPT-v2。

- 

在 MME、MMBench、MMMU 三大标准测试中均排在开源模型第一。

- 

对图表、公式、复杂语义结构等内容表现稳定，尤其在中文理解任务中展现出较强适应能力。

![image]()



---



2、图像生成能力评估



图像生成任务使用两个广泛认可的评估基准：

- 

GenEval：评估图像生成的语义一致性、细节保真度、美学质量

- 

WISE（World Knowledge Image Synthesis Evaluation）：评估模型生成符合世界知识背景的图像能力



结果：

- 

BAGEL 在这两个评估中表现稳定，与最强开源生成模型 FLUX 持平，并在一些子任务上优于 FLUX。

- 

能够生成包含文字、结构清晰、细节丰富的图像。

- 

支持中英文双语 prompt，生成质量在中文条件下没有显著下降。

![image]()



---



3、图像编辑能力评估



图像编辑任务使用专门设计的数据集：

- 

GEdit-Bench：涵盖用户日常图像编辑需求，如内容替换、细节调整、风格修改



结果：

- 

BAGEL 是当前图像编辑任务中性能最强的开源模型之一。

- 

编辑精度、语义理解准确率均高于 Stable Diffusion + InstructPix2Pix 等传统编辑方案。

- 

在复杂结构变换和局部高精度修改中，逼近 GPT-4o 的表现。



---



4、推理型生成与组合能力评估



使用新提出的高质量 benchmark：

- 

IntelligentBench：专门测试模型在图像任务中如何结合语言理解、推理步骤与视觉执行进行组合任务处理。



该评测场景涉及：

- 

图像生成前需要分析用户需求

- 

图像编辑任务需先进行语言分解

- 

多步生成需要保持上下文一致



结果：

- 

BAGEL 得分为 55.3 分（满分 100），远高于所有开源模型（多数为 20～40 分区间）。

- 

仅次于 GPT-4o（78.9）和 Gemini 1.5 Pro（66.8），在多个子任务中表现可与 Gemini 持平。

- 

尤其在“图像→描述→再编辑”的闭环任务中，展现出明显的推理计划能力。



---



5、能力涌现趋势分析



BAGEL 在训练过程中展现出明显的“阶段性涌现”特征，随着训练 token 数量的积累，其表现能力如下：


数据量（训练 token）能力阶段< 0.5T基础图文理解和简单图像生成0.5T ~ 1.5T出现高质量图像合成能力，理解增强1.5T ~ 3.5T图像编辑、指令控制、多轮图文一致性能力涌现> 3.5T推理式图像编辑、多模态组合能力快速增长，接近闭源模型水平


这说明其能力不仅仅来源于架构本身，还依赖数据质量、交错模态训练与推理链构建策略。

![image]()




![image]()


和其他模型对比：


![image]()

![image]()


---



🔚 总结：BAGEL 评估结果的整体地位


- 

图文理解能力：开源第一，中文表现尤为突出

- 

图像生成质量：开源一线，媲美 FLUX，与闭源模型差距缩小

- 

图像编辑能力：强于所有开源系统，逼近 GPT-4o

- 

推理型生成与组合：能力突出，是首个开源模型在 IntelligentBench 上突破 50 分

- 

整体模型能力排名：在公开基准测试中，BAGEL 是最强的开源多模态模型之一，多项指标接近 GPT-4o 和 Gemini



项目地址及更多演示：https://bagel-ai.org/


GitHub：https://github.com/bytedance-seed/BAGEL


论文：https://arxiv.org/pdf/2505.14683

在线体验：https://demo.bagel-ai.org/

---

*来源：[BAGEL：字节跳动开源端到端图文理解与生成多模态推理模型 打破 GPT-4o、Gemini 2.0 垄断](https://www.xiaohu.ai/p/bagel-gpt-4o-gemini-2-0/21787797)*
