---
title: "LiteParse：世界上最快的 PDF 解析器 小文档解析最快提速 100 倍 支持 50 多种不同的文档类型"
date: 2026-05-30T08:00:00+08:00
tags: []
categories: ["opensource"]
summary: "LiteParse 是 LlamaIndex 的开源文档解析器，从 PDF 和 Office 文档里抽出结构化文本，全程不用大模型，它纯本地算，不烧 token。   现在解析复杂文档，很多人会直接把文件丢给大模型（比如 LlamaIndex 自家的 LlamaParse 云服务），让模型看图说话"
source_url: "https://www.xiaohu.ai/p/liteparse-pdf-100-50/33081443"
xiahuid: "33081443"
---

## 📰 正文

LiteParse 是 LlamaIndex 的开源文档解析器，从 PDF 和 Office 文档里抽出结构化文本，全程不用大模型，它纯本地算，不烧 token。


现在解析复杂文档，很多人会直接把文件丢给大模型（比如 LlamaIndex 自家的 LlamaParse 云服务），让模型"看图说话"。准确是准确，但要联网、要花钱、要等响应。


LiteParse 走的是另一条路：纯本地、不花钱、不联网，代价是碰上特别花哨的版面时，能力不如大模型那条路。文档没那么刁钻、又追求快和省，LiteParse 这条路更划算。


LlamaIndex 重写了 LiteParse，把这个原本绑死在 Node 上的工具变成了哪都能跑的零依赖组件。


v2.0 的核心变化：

- 

整个项目用 Rust 重写。原来只能在 Node 环境里跑，现在 Rust、Python、Node、浏览器、边缘运行时都能直接装。

- 

速度大涨。小文档最快提速 100 倍，大文档提速约 3 倍，一份 457 页、100MB 的 PDF，0.777 秒就能解析完。

- 

出了 WASM 版本，能在浏览器里本地跑，文档全程不上传，也能部署到 Cloudflare Workers 这类边缘节点。

- 

能当 skill 直接装进编程 Agent，Claude Code、Codex、OpenCode 一行命令接入。

- 

一套 Rust 核心，多语言绑定同步更新，改一处，Python、Node、Rust 全跟着变。



从「只能跑在 Node 上」到「哪都能跑」



旧版是个 Node/TypeScript 包。问题不在功能，在于你想在别的语言、别的环境里用它，得先扛一个 Node 环境的硬依赖，延迟和分发都很别扭。社区当时收到最多的请求就是「支持别的语言」。


他们先试了个偷懒的办法，给 Python 包了一层壳去调命令行，但这没解决根上的问题，Node 这个硬依赖还在。接着试着把 TypeScript 直接编译成二进制，结果复杂的系统依赖让这条路彻底走不通。


最后选了 Rust 全部重写。现在四个安装入口并排摆着，用哪个语言装哪个：


```bash
pip install liteparse              # Python
npm i @llamaindex/liteparse        # Node
cargo install liteparse            # Rust
npm i @llamaindex/liteparse-wasm   # WASM

```


![image]()


快了多少



用 Rust 重写之后，速度提升很明显。原来慢，主要慢在每次解析都要启动一个 Node 进程，这个启动开销在小文档上占了大头。所以越小的文档，提速越夸张。


提速幅度大致是这样：

- 

小文档：最快 100 倍，之前主要耗在启动 Node 进程上。

- 

大文档：约 3 倍。

- 

极端例子：457 页、100MB 的 PDF，0.777 秒解析完。


![image]()


底层用的是 PDFium 的一个定制分支（Chrome 渲染 PDF 用的就是 PDFium），OCR 默认走 tesseract-rs。团队说，对那些需要实时读文档的 Agent 和应用，这个速度是够用的。


WASM 这步最值得看，但有个 OCR 的坑



光支持 Rust、Node、Python 还不够，他们想要完整的浏览器和边缘端支持。这事社区其实已经趟过路，Simon Willison 之前就证明了 LiteParse 能在浏览器里跑，代价是得用 Vite 把一堆函数打桩占位（stub）。官方干脆把这套做法收编了，写进文档当成官方的浏览器支持路径。


但用了 Rust 之后，他们能自己掌控构建流程，做出了专门的 WASM 目标和 @llamaindex/liteparse-wasm 包，浏览器和边缘运行时都能跑。你打开他们那个演示网页就能直接试，所有解析全在你自己浏览器本地完成，文档一个字节都不上传。对隐私敏感的场景，这点比提速实在得多。


这里有个限制不能美化：WASM 版还是得把系统依赖打桩掉，所以它只能直接解析文件字节，OCR 不再是内置默认项，而是要你传一个回调进去（比如接 tesseract-js）。说白了，纯文本 PDF 在浏览器里直接解析没问题，但要识别扫描件、图片里的字，得你自己接一个 JS 的 OCR 上去，它不自带了。


装进编码 Agent 当 skill 用



对已经在用编码 Agent 的人，这条最对口。它能直接作为 skill 装进去：


```bash
# Claude Code、Codex、OpenCode 等
npx skills add run-llama/llamaparse-agent-skills --skill liteparse
```



另外也提供了 Pi 编码 Agent 的扩展。


几个能立刻想到的用例


![image]()


获取方式



四个包按语言选其一，命令见上文。文档和源码：

- 

Getting Started：https://developers.llamaindex.ai/liteparse/getting_started/

- 

GitHub：https://github.com/run-llama/liteparse

- 

PyPI：https://pypi.org/project/liteparse/

- 

npm：https://www.npmjs.com/package/@llamaindex/liteparse

- 

WASM：https://www.npmjs.com/package/@llamaindex/liteparse-wasm

- 

Rust（crates.io）：https://crates.io/crates/liteparse

---

*来源：[LiteParse：世界上最快的 PDF 解析器 小文档解析最快提速 100 倍 支持 50 多种不同的文档类型](https://www.xiaohu.ai/p/liteparse-pdf-100-50/33081443)*
