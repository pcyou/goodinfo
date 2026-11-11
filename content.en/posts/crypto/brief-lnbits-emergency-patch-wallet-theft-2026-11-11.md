---
title: "[Brief] LNbits Rushes Emergency Patch After Reported Bitcoin Wallet Thefts"
title_en: "[Brief] LNbits Rushes Emergency Patch After Reported Bitcoin Wallet Thefts"
date: "2026-11-11T20:59:08+08:00"
draft: "false"
tier: "2"
description: "LNbits, a custodial dashboard for Bitcoin Lightning Network nodes, published an emergency patch on Wednesday in response to reports of Bitcoin wallet thefts. The project warned that installations running older versions were vulnerable and urged operators to replace potentially exposed credentials even after upgrading."
summary: "The line most easily skipped in the advisory is the instruction to replace credentials even after upgrading: here the vulnerability is the credential exposure itself, so patching the code leaves the attacker's copy valid unless it is actively rotated — exactly the step between finding a flaw and stopping the loss."
source: "Cointelegraph"
categories:
  - "crypto"
tags:
  - "Blockchain Security"
  - "Bitcoin"
  - "Lightning Network"
  - "Credential Exposure"
---

## Key Facts

LNbits, a custodial dashboard for Bitcoin Lightning Network nodes, published an emergency patch on Wednesday in response to reports of Bitcoin wallet thefts. The project warned that installations running older versions were vulnerable, and urged operators to replace potentially exposed credentials even after upgrading. Multiple community reports described losses from wallets managed through affected instances.

## Wider Perspective

The line most easily skipped in that advisory is the instruction to replace credentials even after upgrading. For most software vulnerabilities the reminder is redundant: patch the code and the flaw is fixed. Here it is different, because the vulnerability is the exposure of the credentials themselves. Once credentials have leaked, patching the code leaves the attacker's copy valid unless it is actively rotated, and that is precisely the step between finding a flaw and actually stopping the loss.

The dashboard's position in the chain matters more than it first appears. Ordinary Lightning Network users rarely operate nodes directly; they hand funds to a service running a dashboard, and once the dashboard's login credentials land in an attacker's hands, real on-chain assets are what gets moved. The cluster of theft reports through dashboards has pushed this category of service into plain view.

For operators, what this exposed is as much an operational habit as a technical gap: how often dashboard credentials are rotated, whether they are separated from the primary account, whether withdrawal permissions are restricted. All of these may have looked like unnecessary caution until now. The patch closes the entry point; rotating the keys disposes of the copy already in circulation. Both have to happen.

---

Editor: GoodInfo Global News Team
