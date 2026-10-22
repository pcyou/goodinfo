---
title: "US Banks Block Third-Party AI Agents From Customer Accounts"
title_en: "US Banks Block Third-Party AI Agents From Customer Accounts"
date: "2026-10-23T04:15:00+08:00"
draft: "false"
tier: "1"
description: "US banks have begun detecting and blocking unvetted third-party AI agents at the account and payment-instruction layer, according to sources cited by Reuters. Automated instructions that did not originate from the bank's own application triggered risk flags, and some accounts were refused service outright."
summary: "Several US banks have started blocking unvetted third-party AI agents at the account and payment-instruction layer, according to sources cited by Reuters. The common pattern described is that automated instructions not issued by the bank's own application triggered risk flags, and some accounts were refused service. That pushes the agent-permission question out of the application layer and into core financial infrastructure, ahead of any formal rule."
source: "Reuters / Axios"
categories:
  - "ai-tech"
tags:
  - "Artificial Intelligence"
  - "Fintech"
  - "Risk Control"
  - "Banking"
  - "Agents"
---

**[Core Summary]**

Several US banks have begun detecting and blocking unvetted third-party AI agents at the account and payment-instruction layer, according to sources cited by Reuters. The common pattern described is that automated instructions which did not originate from the bank's own application triggered risk flags in behaviour monitoring, and some accounts were refused service outright. This moves the agent-permission question out of the application layer and into core financial infrastructure, ahead of any formal rule.

**[Event Details]**

- **How it surfaced**: According to the reporting, the unusual activity was identified inside the banks' own behaviour monitoring rather than through a regulatory notice or an external security disclosure.
- **Where it was blocked**: The measures sit at the account access and payment-instruction layer, outside the bank's own channels, which amounts to a direct refusal of third-party automated calls.
- **What triggers it**: The feature sources describe as common is the unauthorised origin of the caller, not the content of the instruction itself, which is part of why this activity went unnoticed for as long as it did.
- **A parallel case**: In the same window, reporting showed a large retail platform taking the opposite route and opening a shopping-agent interface to external agents. Two institutions, two directions.
- **What kind of action this is**: These are a bank's own operational risk measures, not a regulatory obligation. The two are legally distinct even when they are hard to tell apart from the customer's side.

**[Wider Perspective]**

Looked at from inside a bank, what is being repriced is not any single feature but the verifiability of an agent's identity. Conventional financial risk control evaluates the account holder: whether the money left the person's own account, whether the device is one they habitually use, whether the pattern matches long-standing behaviour. An agent-driven call introduces a variable the old model cannot attribute, because the instruction originator is not the account owner at all. That is why this activity required banks to adjust their monitoring criteria rather than relying on existing rules to catch it automatically.

What is notable is that the banks chose refusal rather than permission plus limits. The softer approach is easier to build and matches how the payments industry has handled odd transactions for years, because a cap at least bounds the maximum loss. But that logic does not fit agents. Their risk does not live in the size of any single instruction; it lives in the ability to persist across many small, dispersed, individually unremarkable operations. While headroom remains, an agent can operate below every threshold indefinitely, and the account holder may never notice. Blocking outright is therefore an admission that current tooling cannot yet price this class of caller.

There is a second reading worth taking seriously: this may be a policy declaration performed in the language of risk control. Where rules are absent, regulatory arbitrage gets filled in fast. Whichever institution publishes an enforceable standard first effectively draws a temporary baseline. That baseline may never be adopted in rulemaking, and may be so strict it forecloses legitimate uses, but it does shape how developers build in the interim. For product teams this means answering a question that was rarely asked before: not whether they can make the call, but how they will later prove they were authorised to make it.

The episode also exposes a basic gap in the agent ecosystem, namely the absence of an authorisation credential format that multiple parties can accept. Verbal consent and a click-through approval are common today, and neither survives an audit or travels across institutions. A credential that lets a user authorise a specific scope for a specific window is the plausible technical exit. Until one exists, banks and platforms will each improvise their own blocking rules, and the user absorbs the resulting inconsistency from both sides.

**[Multiple Perspectives]**

- **Sources cited**: The reporting emphasises that detection happened inside bank monitoring systems rather than through a regulatory channel, suggesting exposure preceded public discussion.
- **The retail platform side**: The institution that opened an agent interface argues that controlled access expands legitimate use, while outright refusal pushes users toward less regulated alternatives.
- **Risk practitioners**: Practitioners broadly agree that agent calls do not fit the traditional limit-based framework, which is the technical reason for blocking rather than capping.
- **Compliance observers**: A recurring caution is that operational blocks are a bank's own choice rather than a legal duty, yet customers will struggle to tell the two apart.

*Editor: GoodInfo Global News Team*
