---
title: "Study Finds AI Shopping Assistants Routinely Recommend Fake Retail Sites, with Google Lowest at Four Percent"
title_en: "Study Finds AI Shopping Assistants Routinely Recommend Fake Retail Sites, with Google Lowest at Four Percent"
date: "2026-11-13T04:28:09+08:00"
draft: "false"
tier: "1"
description: "A study conducted by the intellectual property protection firm Podqi and shared exclusively with a technology publication found that as many as fifteen percent of answers from artificial intelligence chatbots contained links to risky websites when shoppers used them to research products. Risky sites include fake websites impersonating real retailers, old brand domains re-registered by someone else, and dead sites that are no longer active but can still be purchased and reactivated. The test covered one hundred fifty-one brands and six thousand seven hundred ninety-five answers."
summary: "The real value of this study lies less in the percentage than in the structural gap it exposes: artificial intelligence assistants are becoming the first stop for shopping research, while the citation pipeline underneath them lacks a verification mechanism to match that role. The risky links are not new; what is new is the efficiency, scale and low level of suspicion with which models now hand them to users."
source: "Compiled wire reports"
categories:
  - "ai-tech"
tags:
  - "AI Assistants"
  - "Cybersecurity"
  - "E-commerce"
  - "Brand Protection"
  - "Search Quality"
---

## Key Facts

- **Method**: Researchers crafted their own shopping prompts and ran them against three leading models, covering one hundred fifty-one brands of varying size across two testing periods in September.
- **Question types**: Included "what are the top websites for buying this brand", "where can I find this brand online" and "does this brand ship internationally and what are its regional websites".
- **Definition of risk**: Fake websites impersonating real retailers, old brand domains re-registered by someone else, and dead sites no longer active but still purchasable and reusable by another party.
- **Results by engine**: Google's Gemini showed risky sites least often, at four percent of answers. A retrieval-led engine performed worst at fifteen percent. A third mainstream model fell in between at eight percent.
- **Warning behaviour**: On how often risky sites were flagged with a warning, one model performed best at twenty-four percent.
- **Brand size effect**: Questions about larger companies produced risky sites at roughly half the rate of questions about smaller brands.
- **Timing**: The findings land just before the holiday shopping season, when more consumers are expected to use artificial intelligence assistants to research and compare products.

## Competing Views

**The researchers argue the risk scales with brand size.** Larger brands surface risky sites at about half the frequency of smaller ones, a gap that maps directly onto the resources those companies spend protecting their own domains. The difference in brand protection capacity ultimately becomes a difference in the probability that a consumer is misdirected, which is the same mechanism that produced the early domain squatting problems on the internet.

**Another reading focuses on the warning mechanism rather than the link count.** All three engines surfaced risky sites, but only one attached a warning. The severity of the problem therefore does not depend on whether links appear, but on whether they are labelled. The meaningful metric is the share of unflagged risky links, not the share of risky links — and under those two definitions the conclusion may point at different models.

**A third view places responsibility on the citation pipeline.** A model's answer is fundamentally a reorganisation of retrieval results. When a search index contains a re-registered old domain, a model that references it without additional verification is behaving predictably. The root of the problem may not lie with the model at all, but with the quality of the citations it depends on and whether any verification step exists before those citations reach the user.

**The consumer side offers a pragmatic instruction.** The study's chief executive stressed that even when a result comes from a chatbot, users should still verify the source before entering personal or payment information. The advice sounds conservative, but it reflects an unresolved reality: there is currently no reliable, low-cost way to verify that a link supplied by a model points to what it claims.

## Panoramic Analysis

The real value of this study lies less in the percentage it reports than in the structural gap it exposes: artificial intelligence assistants are becoming the first stop for shopping research, while the citation pipeline underneath them lacks a verification mechanism to match that role. In the traditional search era, dangerous sites existed too, but users saw them as individual links and the risk was diffuse. Chatbots now aggregate risk into a coherent, authoritative-sounding answer, and what the user faces is no longer a suspicious link but a complete-looking response.

The risk in the underlying links is nothing new. Old brand domains being re-registered and dead domains being bought for reactivation are ordinary features of the domain market, and standing up an imitation retailer is cheap. What is new is the efficiency and scale at which these risks are now handed to users, and how little suspicion the delivery format invites. One hundred fifty-one brands and six thousand seven hundred ninety-five answers indicates the order of magnitude: when consumers begin using models to compare prices, models actively widen their own retrieval, meaning the number of sites considered far exceeds what a user browsing manually would have reached.

The warning-rate data makes the picture subtler. The question shifts from whether a model will surface risky links to whether it will say clearly that a link is problematic. Those are different problems with different remedies. The first needs stricter domain-status validation and shorter index freshness; the second needs one additional judgement step. With the highest warning rate at only twenty-four percent, the industry is effectively in a state of usually saying nothing.

A third observation is easily overlooked: risk frequency runs inversely to brand size. That means the problem is distributed unevenly. Well-resourced names protect themselves through domain monitoring and legal action, while smaller brands — precisely the ones that depend on artificial intelligence assistants for traffic — have neither the capacity to defend nor the incentive to be warned. The information asymmetry between those merchants and their customers is precisely why this gap persists.

Four indicators are worth watching. How the risky-link rate and the warning rate for the three engines move in subsequent versions. Whether model builders introduce checks against domain registration status and historical reputation. The share of shopping questions within the overall query mix. And whether consumer dispute reports cluster during the holiday season. Until such data arrives, links supplied by a model should be treated as leads rather than conclusions, especially where personal or payment details are involved.

*Editor: GoodInfo Global News Team*
