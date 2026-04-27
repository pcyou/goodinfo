---
title: "微软发布 Co-op Translator 可一次性将Markdown文件和图像翻译成多种语言"
date: 2024-12-24T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "微软发布Co-op Translator，这是一款开源工具，旨在简化多语言翻译的过程，特别是针对技术文档和嵌入文本的图像。它结合了 Azure OpenAI 和 Azure Computer Vision 服务，能够高效完成 Markdown 文件和图像的翻译工作，帮助开发者突破语言障碍，将项目推广"
source_url: "https://www.xiaohu.ai/p/co-op-translator-markdown/17267567"
xiahuid: "17267567"
---

## 📰 正文

微软发布Co-op Translator，这是一款开源工具，旨在简化多语言翻译的过程，特别是针对技术文档和嵌入文本的图像。它结合了 Azure OpenAI 和 Azure Computer Vision 服务，能够高效完成 Markdown 文件和图像的翻译工作，帮助开发者突破语言障碍，将项目推广到全球。


可以在不到 2 小时内完成了 276 张图像和 153 个 Markdown 文件的翻译。




![image]()



工具简介


Co-op Translator 利用 Azure AI 服务，包括：

- 

Azure OpenAI：处理 Markdown 文件中的文本翻译。

- 

Azure Computer Vision：提取图像中的文本，并通过 Azure OpenAI 翻译。

- 

自动生成组织化的多语言翻译文件夹，方便管理。



功能亮点
1. 

多语言支持：可一次性翻译成多种语言，包括韩语、中文（简体和繁体）、法语、西班牙语、日语等。

2. 

Markdown 格式保护：翻译过程中保留了 Markdown 文件的结构与格式，包括标题、链接和代码区块。

3. 

图像文本翻译：支持从图像中提取文本并翻译，自动保存为目标语言版本。

4. 

自动化流程：通过命令行工具轻松运行翻译任务。

5. 

技术代码完整性保护：在翻译过程中跳过代码区块，避免破坏技术文档。同时未来计划支持注释的精准翻译。



挑战与解决方案
1. 

代码区块的处理：

- 

Markdown 文件中的代码区块在翻译过程中可能被破坏。

- 

解决方法：将代码区块替换为占位符，在翻译后恢复原样。

- 

未来改进方向：支持翻译代码注释。


2. 

图像文本翻译的复杂性：

- 

当图像中的文本密度过高或排版复杂时，翻译结果可能不够理想（如文本过长导致布局混乱）。

- 

解决方法：对文本提取和排版进行优化，并手动调整。


3. 

多语言版本的管理：

- 

为每种语言自动生成链接表格，便于用户在不同语言版本间切换。




案例：Phi-3 Cookbook 翻译

- 

背景：Phi-3 Cookbook 是一款针对 Phi-3 和 Phi-3.5 小型语言模型的开源技术指南。为了让全球开发者和研究者使用，该项目需要进行多语言翻译。

- 

实施步骤：
1. 

准备：清理手动翻译的历史文件，确保自动化翻译的起点干净。

2. 

Azure 设置：配置 Azure OpenAI 和 Azure Computer Vision，分别处理文本和图像翻译。

3. 

安装工具：通过 Poetry 或 pip 安装 Co-op Translator。

4. 

翻译：运行 translate 命令完成多语言翻译（支持西班牙语、法语、韩语、中文等）。

5. 

校验与优化：检查翻译后的文件是否准确。对 Markdown 文件中的翻译错误或格式问题进行手动调整（如需要）。



![image]()



Phi-3 Cookbook 多语言翻译结果：


https://github.com/microsoft/Phi-3CookBook?tab=readme-ov-file#-multi-language-support


Phi-3 Cookbook 的 Markdown 示例，使用 Co-op Translator 翻译成韩语：

![image]()




![image]()


关于如何使用Co-op Translator翻译器的简要 18 分钟介绍和快速指南


官方介绍及教程：https://techcommunity.microsoft.com/blog/educatordeveloperblog/automate-markdown-and-image-translations-using-co-op-translator-phi-3-cookbook-c/4263474


GitHub：https://github.com/Azure/co-op-translator

---

*来源：[微软发布 Co-op Translator 可一次性将Markdown文件和图像翻译成多种语言](https://www.xiaohu.ai/p/co-op-translator-markdown/17267567)*
