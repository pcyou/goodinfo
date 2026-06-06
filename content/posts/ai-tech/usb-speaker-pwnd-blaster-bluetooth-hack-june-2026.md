---
title: "USB音箱可蓝牙入侵电脑：Pwnd Blaster漏洞曝光，厂商拒绝修复"
date: 2026-06-06T05:00:00+08:00
categories: [ai-tech]
tags: ["网络安全", "蓝牙漏洞", "USB设备", "Pwnd Blaster"]
description: "安全研究人员发现Pwnd Blaster漏洞，可通过Creative蓝牙音箱在用户无感知的情况下入侵连接USB的电脑，厂商确认无修复计划。"
---

## 核心摘要

安全研究人员发现了一种名为"Pwnd Blaster"的新型攻击方式，利用Creative品牌的蓝牙音箱通过蓝牙连接入侵与其USB连接的电脑。该漏洞无需用户进行任何操作即可触发，且硬件厂商已确认不会提供修复补丁。

## USB Speaker Vulnerability Allows PC Infection Without User Interaction

Security researchers have discovered a novel attack vector dubbed "Pwnd Blaster" that exploits Bluetooth speakers manufactured by Creative to compromise connected PCs without any user interaction. The vulnerability allows attackers to infiltrate computers simply by being within Bluetooth range of the speaker, which is connected to the PC via USB.

The exploit targets a firmware vulnerability in Creative's popular Bluetooth speaker line, which sells for approximately three hundred dollars. When the speaker is connected to a PC via USB for charging or audio input, the compromised firmware can execute arbitrary code on the host system through the USB interface, effectively turning the speaker into a stealthy attack platform.

What makes this vulnerability particularly concerning is that it requires no action from the user. An attacker only needs to be within Bluetooth range of the speaker to initiate the exploit. The attack chain leverages the speaker's Bluetooth receiver to receive malicious payloads, which are then relayed to the connected PC through the USB connection.

Security experts have described the discovery as alarming. One researcher noted, "This makes me want to unplug every mic and speaker," reflecting the broader concern in the cybersecurity community about the expanding attack surface created by Internet of Things devices.

Compounding the concern, Creative has confirmed that no firmware patch will be released to address the vulnerability. The company's position is that the risk is limited to scenarios where attackers have physical proximity to the device, and that users can mitigate the risk by disconnecting the speaker when not in use.

## 全景透视

Pwnd Blaster漏洞的曝光揭示了物联网设备安全问题的深层次挑战。随着越来越多的消费电子产品具备蓝牙和USB连接功能，攻击面正在以前所未有的速度扩大。这类设备通常缺乏严格的安全审计，其固件更新机制也往往不完善。

从更广泛的角度来看，这一事件反映了整个消费电子行业在安全设计上的系统性缺陷。制造商在追求功能丰富性和成本控制的同时，往往忽视了安全性的基本需求。蓝牙协议的复杂性使得安全验证变得困难，而USB接口的高权限特性则意味着一旦设备被攻破，攻击者可以获得对宿主系统的完全控制。

对于企业和普通用户而言，这一漏洞提醒我们需要重新审视"信任连接设备"的默认假设。零信任安全模型不应仅限于网络层面，还应延伸到物理设备层面。在物联网时代，每一个智能设备都可能成为攻击入口，安全意识的提升和防御策略的转变迫在眉睫。

## 多方观点

Ars Technica的深入分析指出，Pwnd Blaster漏洞利用了蓝牙音频协议和USB通信之间的信任链断裂，这是一个典型的跨协议攻击案例。TechRadar报道了安全社区对此发现的广泛担忧，多位专家呼吁行业建立更严格的物联网设备安全标准。

Notebookcheck引用Creative的官方回应称，该漏洞需要攻击者具备物理接近条件，实际风险有限。然而，安全研究人员反驳称，在办公环境或公共场所，攻击者完全可以悄无声息地接近目标设备，物理接近的门槛远比厂商声称的要低。
