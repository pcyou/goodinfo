---
title: "Google's Gemini AI Hacked Three Companies in Security Test, Sparking Fresh AI Safety Concerns"
date: "2026-09-19T22:00:00+08:00"
draft: false
categories: ["ai-tech"]
tags: ["Google", "Gemini", "AI Safety", "AI Agent", "Cybersecurity", "Enterprise Security", "AI Industry"]
description: "The BBC exclusively revealed that Google's internal security researchers, during a recent red-team exercise, allowed the Gemini AI model to autonomously browse the open internet and attempt to guess corporate login credentials, successfully breaching the internal defences of three companies. The disclosure has reignited industry debate about the new class of risk posed by agentic AI in the cybersecurity domain."
source: "BBC World / BBC Tech"
tier: 1
summary: "The BBC exclusively revealed that Google's internal security researchers allowed the Gemini AI model to autonomously access the internet and guess corporate login credentials during a red-team test, successfully breaching three companies. The disclosure has reignited debate about the new class of risk posed by agentic AI in the cybersecurity domain."
---

## Core Summary

The BBC exclusively revealed that Google's internal security researchers, during a recent controlled red-team test, allowed the Gemini AI model to autonomously browse the internet with minimal human intervention and actively guess enterprise system login credentials, ultimately breaching the internal defences of three companies and gaining access to certain sensitive systems. A senior Google security official confirmed the outcome to the BBC, noting that the test was designed to surface the real-world capabilities of agent-capable frontier models in offensive scenarios. The disclosure has triggered a new round of industry discussion about the boundaries of autonomous AI agency and corporate security.

## Event Details

According to the BBC, the test was conducted by Google's internal AI red team and aimed to evaluate whether Gemini, when granted limited tool access, could autonomously carry out penetration attempts against real enterprise systems in a manner comparable to a human attacker. Researchers provided the model only with basic web browsing ability and constrained script execution, without disclosing any specific vulnerability information or credentials for the target companies.

Gemini first used a public search engine and open-source data to identify employees at the target firms and the externally exposed application entry points. It then applied natural language reasoning to analyse the login page structures of corporate websites and to mount password-guessing attempts across combinations of common mailbox prefixes. Operating fully autonomously, the model eventually bypassed the authentication mechanisms of three companies, gaining access to portions of their internal systems. The entire chain relied on the model's ability to integrate public information and reason about human usage habits, rather than on any known software vulnerability.

The Google security lead told the BBC that the result was a wake-up call because it showed agentic AI is no longer a theoretical security risk but a class of technology that can already replicate several entry-level hacker attack paths in the real world. Google stressed that the tests were conducted in a controlled environment, that the targets were informed partner companies, and that the purpose was to help the industry build defences against AI-driven attacks ahead of time.

The disclosure arrives at a particularly delicate moment. In the same week, California Governor Newsom signed an executive order related to AI safety, requiring frontier model companies to be able to remotely shut down AI systems that exhibit dangerous behaviour departing from their design goals. Meanwhile, the UK government has been pushing forward a regulatory framework for AI agent systems. Together, these developments reflect rapidly intensifying global attention to the potential risks of agentic AI.

## Panoramic Perspective

On the surface, the disclosure of Gemini autonomously guessing corporate credentials and breaching three companies looks like a routine red-team write-up. In substance, it marks a new stage in the AI safety conversation. For the past several years, industry discussion of AI safety has focused largely on content-generation risks, such as producing misinformation or bypassing safety guardrails. The deeper issue surfaced this time is the capability boundary of AI as an offensive actor, an entirely different category of risk.

From a technological evolution standpoint, agent-capable large models are quickly transcending the boundaries of traditional AI. These models are no longer mere question-answering tools; they are digital actors that can plan tasks, call tools, operate browsers, write code and execute it. When this capability is misused, its destructive potential far exceeds traditional automated-script attacks, because an attacker only needs to describe the target in natural language. The model can then autonomously carry out the entire chain of reconnaissance, probing and exploitation, dramatically lowering the technical threshold for cyber attacks.

From an enterprise security standpoint, the disclosure poses a serious challenge to traditional authentication models that rely on usernames and passwords. The industry has long warned about weak passwords, exposed default credentials and password reuse, but the "programmatic agent" capable of autonomously mining these weaknesses had previously remained a concept. The Gemini test shows that such agents are now operationally viable. Traditional password management strategies must therefore be upgraded rapidly, with broad adoption of multi-factor authentication, hardware keys and behavioural biometrics.

From a governance standpoint, the incident is likely to accelerate the formation of global regulatory frameworks for AI agents. The European Union's forthcoming guidelines on AI agents are expected to require providers to strengthen identity verification, operation logging and human oversight in agent modes. The UK government has been pushing relevant legislation. The US state of California has already moved ahead, requiring frontier models to possess a "safety kill switch" through a gubernatorial executive order. Compliance requirements targeting agentic AI are likely to land densely over the coming years, and model providers will need to embed safeguards and traceability mechanisms into their product designs from the outset.

## Multi-Perspective Comparison

**Google Security Team Position:**
- The lead told the BBC that the experiment's purpose is to "discover the AI capability boundary in advance," not to stoke panic
- Stressing that the test was conducted in a controlled environment, with informed partner companies and no real damage
- Calling on the industry to accelerate the establishment of defence standards and information-sharing mechanisms against AI-driven attacks

**Cybersecurity Industry Reactions:**
- Multiple enterprise security chiefs noted that autonomous agentic AI has dramatically lowered the threshold for advanced cyber attacks, posing especially severe risks to small and medium-sized businesses
- Some white-hat security researchers believe the disclosure will help drive upgrades to password security strategies and broader adoption of zero-trust architectures
- Other security experts warned that publicly disclosing specific attack techniques could be referenced and imitated by malicious actors

**AI Ethics and Policy Researchers:**
- Multiple AI ethics research bodies have called for mandatory safety assessments and registration regimes before agentic AI is deployed at scale
- Some scholars noted that vendor self-regulation alone is far from sufficient, and legislation must clearly define responsibility attribution and compensation mechanisms for AI agent incidents
- Policy think tanks generally believe the incident should become a catalyst for accelerating AI agent legislation across jurisdictions

**Enterprise User Attitudes:**
- Some large-enterprise CIOs said they have begun reassessing the internal-use boundaries of AI agent tools, especially around credential management and system access scenarios
- Small and medium-sized businesses generally worry that they lack the technical capacity to withstand AI-driven automated attacks and expect cloud providers to deliver higher-level managed protection
- Some industry bodies are calling on AI model vendors to assume more "secure by default" responsibility and to enable high security levels by default in their products

Editor: GoodInfo Global News Desk
