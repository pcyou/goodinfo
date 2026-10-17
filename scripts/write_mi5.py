#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate MI5 state threats article (Tier 1 bilingual)."""
import sys, os
sys.path.insert(0, '/root/goodinfo-site')
from scripts.generate import yaml_field, write_article, sanitize_text, filter_tags

NOW_BJT_STR = "2026-10-14T02:21:00+08:00"

title_cn = "英国军情五处警告：国家威胁密度已超过冷战时期"
title_en = "MI5 Warns State Threat Density Has Surpassed Cold War Levels"

description_cn = "英国军情五处处长10月14日在公开演讲中警告，英国正面临来自俄罗斯、伊朗等国的国家威胁，其规模与复杂度已超过冷战时期。"

summary_cn = "英国军情五处处长10月14日在公开演讲中警告，英国正面临来自俄罗斯、伊朗等国的国家威胁，其规模与复杂度已超过冷战时期。英国情报机构正同时应对间谍活动、破坏行动与网络攻击等多类威胁，情报工作量达到历史峰值。"

source = "BBC / The Guardian / NBC News / Reuters"

body_cn = """**[核心摘要]**

英国军情五处处长10月14日在公开演讲中发出警告，称英国当前面临的国家级安全威胁数量与复杂度已超过冷战时期，英国情报机构正同时应对间谍活动、破坏行动与网络攻击等多类威胁。

**[事件详情]**

- **核心表态**：军情五处处长在伦敦公开演讲中表示，英国正进入"国家安全新纪元"，来自俄罗斯、伊朗等国的国家行为体在英领土从事间谍活动、破坏行动与网络攻击的频率与复杂度持续上升。
- **威胁维度**：情报机构披露，目前正在处理的调查与行动数量是冷战结束以来的最高水平，涉及破坏关键基础设施、窃取知识产权与政治干预等多个领域。
- **重点方向**：英国情报官员指出，伊朗相关网络正将目标转向军事基地与情报机构等"高价值目标"，并协调针对英国海外基地的破坏图谋。
- **政策响应**：英国政府正在扩充情报与安全机构预算，加强关键基础设施保护，并推动新的国家安全立法以应对快速演变的威胁环境。

**[全景透视]**

军情五处的最新表态标志着英国国家安全认知的显著升级。在俄乌冲突延宕、中东局势动荡以及大国竞争加剧的多重背景下，传统间谍活动与新型网络攻击和破坏行动的边界日益模糊，国家行为体越来越多地采用混合战术。英国情报机构承担的工作量呈结构性上升，这对预算编制、人才培养与跨机构协作提出更高要求。从长期看，英国可能进一步扩大与五眼联盟及欧洲伙伴的情报共享，并通过立法赋予执法部门更广泛的调查权力。然而，隐私保护与国家安全之间的平衡、以及针对外国代理人的法律工具是否足够，将成为公共政策辩论的焦点。

**[多方观点对比]**

- **情报界警示**：军情五处处长强调当前威胁具有"持续性、多样性与隐蔽性"，呼吁公众与私营部门提高警惕。
- **政府承诺**：英国首相表示将加大对情报机构的投入，并加快相关立法进程以填补法律漏洞。
- **公民自由担忧**：部分议员与公民社会组织指出，扩大监控与调查权力可能侵蚀公民自由，应建立更强有力的监督机制。

*编辑：GoodInfo全球资讯组*
"""

meta = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_cn,
    "summary": summary_cn,
    "source": source,
    "categories": ["world"],
    "tags": ["英国", "军情五处", "国家安全", "国际动态", "欧洲政治", "情报机构", "俄罗斯", "伊朗"],
}

path_cn = "/root/goodinfo-site/content/posts/world/uk-mi5-state-threat-cold-war-levels-2026-10-14.md"
write_article(path_cn, meta, body_cn)
print(f"CN written: {path_cn}")

title_en_full = title_en
summary_en = "The head of MI5 warned on October 14 that the volume and complexity of state threats facing the UK have surpassed Cold War levels, with British intelligence simultaneously tackling espionage, sabotage, and cyberattacks from actors including Russia and Iran."
description_en = "The head of MI5 warned that the volume and complexity of state threats facing the UK have surpassed Cold War levels, with British intelligence facing record-high caseloads."

body_en = """**[Core Summary]**

The head of MI5 warned in a public speech on October 14 that the UK is facing a volume and complexity of state-level threats that exceeds Cold War levels, with British intelligence simultaneously tackling espionage, sabotage operations, and cyberattacks.

**[Event Details]**

- **Core Statement**: The Director General of MI5 stated in a London speech that the UK has entered a "new era of national security," with state actors from Russia, Iran, and other countries conducting espionage, sabotage, and cyberattacks on UK soil at increasing frequency and complexity.
- **Threat Dimensions**: British intelligence disclosed that the number of investigations and operations currently being handled is the highest since the end of the Cold War, spanning critical infrastructure sabotage, intellectual property theft, and political interference.
- **Key Focus**: UK intelligence officials noted that Iran-linked networks are shifting their focus to "harder targets" such as military bases and intelligence agencies, and are coordinating sabotage plots against British overseas bases.
- **Policy Response**: The UK government is expanding intelligence and security agency budgets, strengthening critical infrastructure protection, and pushing new national security legislation to address the rapidly evolving threat landscape.

**[Panorama]**

MI5's latest warning marks a significant upgrade in UK national security awareness. Against the backdrop of the prolonged Russia-Ukraine conflict, turmoil in the Middle East, and intensifying great power competition, the boundary between traditional espionage and new forms of cyberattacks and sabotage is increasingly blurred, with state actors adopting hybrid tactics with growing frequency. The workload of British intelligence agencies is rising structurally, placing higher demands on budgeting, talent development, and inter-agency coordination. In the long run, the UK may further expand intelligence sharing with the Five Eyes alliance and European partners, and grant law enforcement broader investigative powers through legislation. However, the balance between privacy protection and national security, as well as whether legal tools against foreign agents are sufficient, will become focal points of public policy debate.

**[Multiple Perspectives]**

- **Intelligence Community Warning**: The MI5 chief emphasized that current threats are characterized by "persistence, diversity, and stealth," calling on the public and private sector to raise vigilance.
- **Government Commitment**: The UK Prime Minister stated that investment in intelligence agencies will be increased and the legislative process accelerated to close legal loopholes.
- **Civil Liberties Concerns**: Some MPs and civil society organizations noted that expanded surveillance and investigative powers may erode civil liberties and that stronger oversight mechanisms are needed.

*Editor: GoodInfo Global News Desk*
"""

meta_en = {
    "title": title_en_full,
    "title_en": title_en_full,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_en,
    "summary": summary_en,
    "source": source,
    "categories": ["world"],
    "tags": ["UK", "MI5", "National Security", "International", "European Politics", "Intelligence", "Russia", "Iran"],
}

path_en = "/root/goodinfo-site/content.en/posts/world/uk-mi5-state-threat-cold-war-levels-2026-10-14.md"
write_article(path_en, meta_en, body_en)
print(f"EN written: {path_en}")
