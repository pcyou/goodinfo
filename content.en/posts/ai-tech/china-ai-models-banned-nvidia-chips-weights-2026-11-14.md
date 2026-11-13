---
title: "Model Weight Fingerprints Show China's Top Open Models Were Trained on Export-Banned Nvidia Chips"
title_en: "Model Weight Fingerprints Show China's Top Open Models Were Trained on Export-Banned Nvidia Chips"
date: "2026-11-14T05:39:23+08:00"
draft: "false"
tier: "1"
description: "A nonprofit research group analysed the publicly released weights of models from DeepSeek, Moonshot AI, MiniMax and Ant Group and matched them to fingerprints of a restricted generation of Nvidia accelerators. The researchers argue that the internal structure of a model's weights preserves the configuration of the chips used to train it. The route by which restricted chips reach Chinese labs through offshore data centres, and the compliance scrutiny triggered by Nvidia chief executive Jensen Huang's departure, are unfolding at the same time."
summary: "The distinctive value of this disclosure lies in method. Comparable allegations in the past rested on intelligence briefings and anonymous sourcing, neither of which can be verified in public or accepted by the other side in diplomatic settings. Weight analysis offers a method anyone can reproduce. Once the trace of a restricted chip can be independently reproduced, the burden of proving that controls failed shifts from the regulator to the regulated."
source: "TechCrunch"
categories:
  - "ai-tech"
tags:
  - "Nvidia"
  - "Export Controls"
  - "AI Compute"
  - "Model Weights"
  - "Chip Restrictions"
---

## Key Facts

- **Who did the work**: The research was led by a former OpenAI researcher working at a nonprofit organisation called Unemployment Labs.
- **How it was verified**: The team analysed the publicly released weights of large language models directly, rather than relying on supply-chain intelligence or anonymous sourcing.
- **Which models**: The study named openly released weights from DeepSeek, Moonshot AI, MiniMax and Ant Group.
- **Core evidence**: The structure of a model's weights preserves the configuration of the chips used to train it; Moonshot's Kimi K3 releases and DeepSeek's V4 models were identified as carrying fingerprints consistent with training on Nvidia's newest accelerator generation.
- **Prior corroboration**: A White House technology adviser cited US intelligence sources earlier in the year when saying Moonshot had used export-banned Nvidia chips.
- **Scale estimate**: Epoch AI estimates that roughly two million advanced chips entered China during 2024 and 2025 through schemes designed to conceal their final destination.
- **The detour**: The research notes that the chips may sit in offshore data centres; Epoch AI's data shows 275,000 Nvidia accelerators were imported to Malaysia across the same two years.
- **Inventory in Hong Kong**: Roughly 600,000 H200 chips are reportedly stockpiled in Hong Kong awaiting shipment into China.
- **Enforcement context**: Megaspeed and its subsidiary Speedmatrix are under investigation in both the United States and Singapore, and Bloomberg reported this week that a company linked to Alice Huang was involved in moving restricted chips to a data centre in Shanghai.
- **Short-seller framing**: In May, Culper published a report arguing that Nvidia has a China problem, with a significant share of revenue driven by Chinese demand, whether through remote data centres or through unlawful transshipment.

## Event Details

The method deserves as much attention as the conclusion. Model weights are the unique numerical structure that emerges from training, and the hardware that performed the training leaves traces in that structure. Comparing the fingerprints in an openly published model against the signatures of particular accelerator configurations is, in effect, reading a shipping manifest written into the parameters themselves.

That approach sidesteps the hardest part of export-control enforcement. Tracking where a chip ended up requires watching layers of transshipment, offshore hosting arrangements and contract manufacturing chains, none of which leave a clean record. Reading the evidence out of a publicly downloaded file does not.

The research also draws a line that matters. Its authors note that this does not mean the models were trained entirely on Nvidia hardware, nor that export-control law was necessarily violated, since the chips could have been deployed in an offshore data centre. The claim is narrower and stronger for being narrow: the fingerprints point one way.

## Competing Views

**One reading treats the weight analysis as an upgrade in enforcement methodology.** Evidence about restricted chip use has historically come from intelligence briefings and anonymous sourcing. That kind of evidence is hard to verify in public and harder still for the other side to accept in a diplomatic setting. Weight analysis changes the structure of proof: anyone can download the public model, rerun the comparison and check the result. Once the trace of a restricted chip can be reproduced independently, the burden of showing that controls failed shifts to the side being controlled, which now has to demonstrate otherwise.

**A second reading identifies a structural gap between the goal of controls and the actual routes.** A researcher at Georgetown's Center for Security and Emerging Technology frames the question bluntly: if the technology lead matters, it makes little sense to bar Chinese firms from obtaining chips on the mainland or in Hong Kong and Macau, while effectively permitting them to do whatever they like once the work moves to Malaysia. The Malaysia detour appears repeatedly in the research, and the 600,000 H200 chips still awaiting clearance in Hong Kong suggest that the authorities enforcing the rules are themselves caught between objectives.

**A third reading insists on the limitation the researchers themselves stated.** The weights indicate where the hardware came from, not that the models were trained entirely on Nvidia silicon, and certainly not that the law was broken, since the chips could have lived in an offshore data centre. Strip that qualification away and the conclusion slides into a much stronger claim that the controls have been comprehensively broken through, which the evidence does not support.

**The fourth reading comes from the short seller's own logic.** When Culper published its China-problem report in May, the bet was not driven by an expectation of an American crackdown. It was a wager that Beijing would respond to the bans by recommitting to its domestic chip industry, and that the response would cost Nvidia its Chinese demand. The evidence published this week is better read as measuring how far that response still has to travel.

## Panoramic Analysis

The real weight of this disclosure is not that it adds another list of allegations. It is that it supplies a form of verification that did not previously exist.

The first layer is how proof is produced. The enforcement difficulty in export control has always been the same: the object being regulated is the final destination of a chip, and destinations become extremely hard to track after several layers of resale, offshore data centres and contract manufacturing. Where border and customs records cannot cover every path, a technical trace becomes the substitute. The significance of weight analysis lies precisely here, because what it measures is not where a chip went but what the chip left behind while training. Reading model parameters as a record of chip usage is an idea, and once the idea spreads, the auditability of the controls improves with it.

The second layer is that the inconsistency of the policy itself now has numbers attached. Two million advanced chips entering China over two years, 275,000 Nvidia accelerators routed into Malaysia, and 600,000 H200 units held in Hong Kong point respectively to inflow, detour and detention. What they jointly show is that the operative strength of a control is determined by how many links in the chain agree to enforce it, not by how strict the written rule looks.

The third layer is a corrective for the domestic-substitution narrative in both directions. A Stanford scholar focused on United States-China technology policy does not believe that withholding chips drives domestic production, because demand is simply too large. But the flip side deserves stating just as plainly: the dependency revealed by weight analysis is not a scorecard for the domestic route either. It measures how much traffic is still being served by Nvidia hardware, not how much the alternative has already absorbed.

The fourth layer is timing. Nvidia's chief executive left the company this week, the board is searching for a successor, and the company's exposure on export-control compliance has entered open scrutiny. Evidence that is both current and independently reproducible puts pressure on the regulator and on corporate governance at the same moment.

Four indicators are worth tracking. Whether the research team extends the weight-analysis method to additional closed and open models. Whether Malaysia and comparable third jurisdictions tighten their review of accelerator transshipment. How a new chief executive at Nvidia speaks publicly about export compliance. And whether export-control rules move from tracking the end user toward tracking the final location of computation.
---

*Editor: GoodInfo Global News Team*
