---
title: "StarVector：SVG 向量图形生成模型 可以输入任意图像或者通过描述生成生成高质量 SVG 文件"
date: 2025-03-21T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "StarVector 是一个专为 SVG 向量图形生成 设计的基础模型，其目标是：  >   用大模型（VLM）从图像或文本中理解语义结构，并自动生成标准可编辑的 SVG代码，适用于图标、技术图、LOGO、表情等。   也就是将 SVG 矢量图的生成转化为“代码生成任务”，支持从图像或文本生成高质量"
source_url: "https://www.xiaohu.ai/p/starvector-svg-svg/19768891"
xiahuid: "19768891"
---

## 📰 正文

StarVector 是一个专为 SVG 向量图形生成 设计的基础模型，其目标是：

> 

用大模型（VLM）从图像或文本中理解语义结构，并自动生成标准可编辑的 SVG代码，适用于图标、技术图、LOGO、表情等。


也就是将 SVG 矢量图的生成转化为“代码生成任务”，支持从图像或文本生成高质量 SVG 文件。

![image]()



它能干什么？



✅ 看图 → 画图（生成 SVG）


你给它一张图标、LOGO 或技术图（比如流程图、电路图）
👉 它就能自动“转描”为一份 可编辑的矢量图（SVG 文件）

> 

SVG 是一种像素不会失真的图形格式，设计师、前端开发和工程师都常用它。



✅ 看文字 → 画图


你告诉它一句话，比如：

> 

“画一个圆形中有星星的徽章”



👉 它能根据这句话 生成一张可用的 SVG 图像


📦 举个例子


你手里有一个 PNG 格式的黑白 LOGO 图片：


🖼️ → 你输入给 StarVector
🧠 → 它会看懂图中是什么（圆形 + 星星 + 字母）
🖊️ → 它会写一份 SVG 代码（就像写程序）
🎨 → 输出一个缩放不失真、可调颜色的矢量图！


模型亮点功能



✅ 1. 双模态架构（图像 + 文本）


- 

使用 Vision-Language 架构，既能理解图像，也能处理文本指令

- 

支持：

- 

图像 → SVG（Image-to-SVG）

- 

文本 → SVG（Text-to-SVG）


- 

模型结构包括：

- 

ViT 图像编码器

- 

LLM 语言解码器

- 

视觉-语言桥接器（LLM Adapter）

![image]()




---



✅ 2. 高复杂度图形处理能力


- 

能自动识别并生成复杂的 SVG 元素：

- 

圆形、多边形、路径（path）、文字（text）等


- 

特别擅长处理：

- 

技术图、连接结构、图层层级

- 

图标/LOGO 重建




📌 相比传统矢量化算法（如 Potrace、AutoTrace、DiffVG），StarVector 在细节保留和结构清晰度上表现更佳。


它为什么厉害？



传统的“图像转矢量图”（矢量化）方法：

- 

只能处理简单图形

- 

不能识别结构和语义

- 

不会画文字或连接线等复杂图形



而 StarVector：

- 

是 AI 大模型（懂图也懂语言）

- 

能画图标、流程图、LOGO、字体、表情……

- 

图形很干净，还能自动识别“这是什么”

- 

能输出标准的 SVG 代码，直接用于网页、设计软件



应用场景



这意味着什么？
1. 

对普通人：

- 

你不需要学复杂的绘图软件，就能轻松把照片或想法变成专业级的矢量图。比如设计 logo、制作网页图标，都变得简单了。


2. 

对设计师和开发者：

- 

节省时间：不用手动写 SVG 代码或修图。

- 

文件更小：生成的 SVG 代码紧凑，加载速度快，适合网站使用。

- 

更灵活：可以用文字描述直接生成图形，创意实现更快。


3. 

对科技领域：

- 

推动了 AI 在图形设计中的应用，未来可能扩展到自然图片（比如风景照）或更复杂的矢量编辑。

- 

提出了新标准：传统的评价方法（像 MSE）不适合矢量图，StarVector 团队搞了个新指标（DinoScore），更贴近人类审美。




---



举个例子


想象你有一张手绘的太阳图片（圆形加光线），想用在网站上：

- 

老方法：用工具描出很多曲线，文件可能有几千行代码，放大后还有瑕疵。

- 

StarVector：直接认出“这是个圆加几条直线”，生成几十行代码，完美还原，放大到月球大小都清晰。



再比如，你说“给我画个蓝色的五角星”，StarVector 就能立刻生成对应的 SVG 代码，不需要你动手画。

![image]()


🚧 限制说明

- 

不适用于 自然图像或照片（如人脸、风景）

- 

主要训练在图标、图形、符号、图解等二维几何数据上



实验结果



StarVector 在图像到 SVG 的结构化图形生成任务中，达到了当前最强性能，在多个数据集上全面超越传统矢量化工具与通用大模型。

![image]()


✅ StarVector-8B 优势明显：


- 

在所有任务中表现最强

- 

特别擅长结构复杂图形（Diagrams）

- 

相较传统工具（如 Potrace）表现更加稳定、智能



🆚 与 GPT-4V 对比：


- 

GPT-4V 是多模态大模型，但在 SVG 精度上略逊 StarVector

- 

GPT-4V 更泛用，而 StarVector 专注于结构生成，精度更高


![image]()




![image]()




![image]()


在图标、表情、字体和复杂图结构生成任务中全面超越传统方法与 GPT-4V，精度稳定，结构可控。


只需几行代码即可开始使用 StarVector



```None
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoProcessor
from starvector.data.util import process_and_rasterize_svg
import torch

# Load the model
model_name = "starvector/starvector-8b-im2svg"

starvector = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, trust_remote_code=True)
processor = starvector.model.processor
tokenizer = starvector.model.svg_transformer.tokenizer

# Move model to GPU and set to evaluation mode
starvector.cuda()
starvector.eval()

# Load and process the input image
image_pil = Image.open('assets/examples/sample-18.png')

image = processor(image_pil, return_tensors="pt")['pixel_values'].cuda()
if not image.shape[0] == 1:
    image = image.squeeze(0)
batch = {"image": image}

# Generate SVG from the image
raw_svg = starvector.generate_im2svg(batch, max_length=4000)[0]
svg, raster_image = process_and_rasterize_svg(raw_svg)
```



上述代码演示了如何使用 Transformers 库加载预先训练的 StarVector 模型、处理输入图像并生成 SVG 代码。该模型处理了理解视觉元素并将其转换为结构化矢量图形代码的所有复杂性。


注意： 要使用图像光栅化功能，您需要安装 starvector 库。请访问 StarVector 存储库以获取安装说明并确保所有依赖项均已正确安装。


项目地址：https://starvector.github.io/


GitHub：https://github.com/joanrod/star-vector


论文：https://arxiv.org/pdf/2312.11556

---

*来源：[StarVector：SVG 向量图形生成模型 可以输入任意图像或者通过描述生成生成高质量 SVG 文件](https://www.xiaohu.ai/p/starvector-svg-svg/19768891)*
