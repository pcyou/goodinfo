#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tier 2 briefs for 2026-10-19 BJT hourly batch: Egypt-Saudi-Yemen, Mastercard stablecoin security."""
import sys
sys.path.insert(0, '/root/goodinfo-site')
from scripts.generate import yaml_field, article_header, write_article

NOW_BJT_STR = "2026-10-20T00:10:00+08:00"

# ============================================================
# Brief 1: Egypt / Saudi / Yemen conflict
# ============================================================
slug1 = "egypt-saudi-yemen-conflict-military-involvement-2026-10-20"

title_cn = "[快讯] 埃及或介入沙特与也门冲突 中东地缘博弈再升温"
title_en = "[Brief] Egypt Edges Toward Possible Military Involvement in Saudi-Yemen Conflict"

description_cn = "多方报道指出，埃及正在评估是否军事介入沙特与也门之间的冲突，中东地区地缘博弈再度升温。"
summary_cn = "10月19日，多家媒体报道指出，埃及正在评估是否对沙特与也门之间的冲突进行军事介入。这一动向引发中东地区广泛关注，区域国家正就潜在升级进行密集外交协调。"

source_cn = "Reuters"
source_en = "Reuters"

body_cn = """**[核心摘要]**

10月19日，多家媒体报道指出，埃及正在评估是否对沙特与也门之间的冲突进行军事介入，相关讨论已延伸至区域安全协调层面。这一动向引发中东地区广泛关注，海湾国家与西方外交官正就潜在升级进行密集磋商。

**[事件详情]**

- **背景**：沙特与也门之间的武装冲突已持续多年，区域安全格局复杂。
- **埃及立场**：开罗方面未正式确认将介入，但军方与外交部门均进入评估状态。
- **外交斡旋**：多个区域国家正在推动外交解决方案，避免冲突进一步扩大。

*编辑：GoodInfo全球资讯组*
"""

body_en = """**[Key Facts]**

Multiple outlets reported on October 19, 2026 that Egypt is weighing whether to intervene militarily in the long-running conflict between Saudi Arabia and Yemen. The potential shift has triggered active diplomatic coordination among Gulf states and Western envoys seeking to prevent further escalation.

**[Event Details]**

- **Context**: The Saudi-Yemen conflict has been running for years and continues to shape regional security dynamics.
- **Egyptian posture**: Cairo has not confirmed any deployment, but military and diplomatic channels are understood to be in active assessment mode.
- **Diplomacy**: Several regional states are pushing for a negotiated settlement to head off a wider escalation.

*Editor: GoodInfo Global News Team*
"""

meta_cn = {
    "title": title_cn,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_cn,
    "summary": summary_cn,
    "source": source_cn,
    "categories": ["world"],
    "tags": ["中东", "埃及", "沙特", "也门", "地缘政治", "安全局势"],
}
path_cn = f"/root/goodinfo-site/content/posts/world/{slug1}.md"
write_article(path_cn, meta_cn, body_cn)

description_en = "Reports indicate Egypt is weighing possible military intervention in the Saudi-Yemen conflict, triggering a fresh round of regional diplomacy."
summary_en = "Multiple outlets reported on October 19, 2026 that Egypt is weighing whether to intervene militarily in the long-running Saudi-Yemen conflict. The potential shift has triggered active diplomatic coordination among Gulf states and Western envoys seeking to prevent further escalation."

meta_en = {
    "title": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_en,
    "summary": summary_en,
    "source": source_en,
    "categories": ["world"],
    "tags": ["Middle East", "Egypt", "Saudi Arabia", "Yemen", "Geopolitics", "Regional Security"],
}
path_en = f"/root/goodinfo-site/content.en/posts/world/{slug1}.md"
write_article(path_en, meta_en, body_en)
print(f"Brief 1: {path_cn}\n         {path_en}")

# ============================================================
# Brief 2: Mastercard Stablecoin Security tool
# ============================================================
slug2 = "mastercard-stablecoin-security-fraud-sanctions-2026-10-20"

title_cn = "[快讯] 万事达卡推出稳定币安全工具 加强欺诈与制裁风险筛查"
title_en = "[Brief] Mastercard Unveils Stablecoin Security Tool to Screen Payments for Fraud and Sanctions Risks"

description_cn = "支付巨头万事达卡推出针对稳定币交易的安全筛查工具，应对加密支付领域的欺诈与制裁风险。"
summary_cn = "10月19日，万事达卡宣布推出稳定币交易安全工具，用于在支付环节筛查欺诈与制裁风险。该工具面向金融机构与商户，反映传统支付巨头正加速布局加密资产合规基础设施。"

source_cn = "The Block"
source_en = "The Block"

body_cn = """**[核心摘要]**

10月19日，万事达卡宣布推出稳定币交易安全工具，用于在支付环节筛查欺诈与制裁风险。该工具面向金融机构与商户，反映传统支付巨头正加速布局加密资产合规基础设施。

**[事件详情]**

- **产品定位**：新工具针对稳定币交易流程，提供实时筛查能力。
- **应用场景**：可用于识别可疑资金流向与受制裁主体相关的地址。
- **行业意义**：传统支付公司加快在加密合规领域的产品化布局。

*编辑：GoodInfo全球资讯组*
"""

body_en = """**[Key Facts]**

Mastercard announced on October 19, 2026 a new security tool aimed at screening stablecoin transactions for fraud and sanctions-related risks. The product is targeted at banks, payment firms and merchants, and underscores how traditional payment giants are moving deeper into crypto-compliance infrastructure.

**[Event Details]**

- **Product scope**: Real-time screening layer designed to slot into existing stablecoin transaction flows.
- **Use cases**: Identifying suspicious counterparties and addresses linked to sanctioned entities.
- **Industry signal**: Major card networks are accelerating the productisation of compliance tooling for digital assets.

*Editor: GoodInfo Global News Team*
"""

meta_cn = {
    "title": title_cn,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_cn,
    "summary": summary_cn,
    "source": source_cn,
    "categories": ["crypto"],
    "tags": ["万事达卡", "稳定币", "合规", "支付", "加密货币", "金融科技"],
}
path_cn = f"/root/goodinfo-site/content/posts/crypto/{slug2}.md"
write_article(path_cn, meta_cn, body_cn)

description_en = "Mastercard has rolled out a security tool designed to screen stablecoin payments for fraud and sanctions risks, signalling deeper traditional-finance engagement with crypto compliance."
summary_en = "Mastercard announced on October 19, 2026 a new security tool aimed at screening stablecoin transactions for fraud and sanctions-related risks. The product is targeted at banks, payment firms and merchants, and underscores how traditional payment giants are moving deeper into crypto-compliance infrastructure."

meta_en = {
    "title": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "2",
    "description": description_en,
    "summary": summary_en,
    "source": source_en,
    "categories": ["crypto"],
    "tags": ["Mastercard", "Stablecoin", "Compliance", "Payments", "Crypto", "Fintech"],
}
path_en = f"/root/goodinfo-site/content.en/posts/crypto/{slug2}.md"
write_article(path_en, meta_en, body_en)
print(f"Brief 2: {path_cn}\n         {path_en}")