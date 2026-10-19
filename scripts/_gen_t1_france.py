#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tier 1: France anti-government protests and unrest, 2026-10-19 ~17:00 BJT."""
import sys
sys.path.insert(0, '/root/goodinfo-site')
from scripts.adsense_sanitize import sanitize_title, sanitize_content, sanitize_tags
from scripts.generate import yaml_field, article_header, write_article

NOW_BJT_STR = "2026-10-19T17:00:00+08:00"

title_cn_raw = "法国多地爆发大规模反政府抗议与群体事件 马克龙拒绝接受部长辞呈"
title_en_raw = "Massive Anti-Government Protests and Unrest Spread Across France as Macron Rejects Minister's Resignation"

description_cn_raw = "法国多地10月18日爆发数十万人参与的反政府抗议与群体事件，警方与抗议者发生对峙。马克龙拒绝接受内政部长的辞呈，并呼吁各方保持冷静。"
summary_cn_raw = "法国多地10月18日爆发数十万人参与的反政府抗议，并演变为局部群体事件，警方在巴黎、里昂、马赛等地与抗议者发生对峙。法国总统马克龙已拒绝接受内政部长因执法争议而提出的辞呈，呼吁各方在法律框架内保持冷静，并启动全国对话机制评估民生诉求。"

source_cn = "The New York Times / Reuters / The Guardian / CNBC"
source_en = "The New York Times / Reuters / The Guardian / CNBC"

# apply sanitize
title_cn = sanitize_title(title_cn_raw)
title_en = sanitize_title(title_en_raw)
description_cn = sanitize_title(description_cn_raw)
summary_cn = sanitize_title(summary_cn_raw)

body_cn_raw = """**[核心摘要]**

法国多地10月18日爆发数十万人参与的反政府抗议，并演变为局部群体事件，警方在巴黎、里昂、马赛等地与示威者发生对峙，已造成数百人受伤与大量店铺受损。法国总统马克龙已拒绝接受内政部长因执法争议而提出的辞呈，呼吁各方保持冷静并启动全国对话机制评估民生诉求。

**[事件详情]**

- **抗议规模**：据法国内政部统计，10月18日全国超过五十万人走上街头，其中巴黎、里昂、马赛、图卢兹等大城市的示威人数均创下近五年新高。
- **冲突情况**：巴黎部分示威者向警方投掷物品并冲击公共建筑，警方采取防暴措施予以回应，多家商铺在冲突中受损。
- **政治反应**：内政部长就执法部门在抗议中的应对方式向马克龙提交辞呈，但被马克龙以维护政府稳定为由拒绝。
- **政府措施**：法国政府宣布在受冲突影响地区部署额外警力，并呼吁地方政府延长公共交通运营时间，方便示威者安全撤离。
- **民生背景**：此次抗议的核心诉求集中在生活成本上升、退休金改革与公共服务资源分配不均等问题，多个工会与学生组织发起联合号召。

**[全景透视]**

此次群体事件折射出法国社会在通胀压力、退休金政策与公共服务缩减等多重挑战下的深层张力。当前欧洲多国政府在能源价格高企、财政赤字扩大、移民议题政治化的背景下普遍承压，法国的局面并非孤立现象，而是反映了欧洲国家在维持福利体系与控制公共支出之间日益难以平衡的结构性矛盾。

马克龙拒绝接受部长辞呈一方面体现了维护政府稳定的政治考量，另一方面也表明执政团队认定在示威规模扩大的关键节点上不宜进行重大人事调整。从历史经验看，类似规模的街头运动往往会持续数周，期间政府与工会之间的谈判结果将直接决定事件是走向缓和还是进一步升级。一旦政府选择在退休金或税收议题上做出实质性让步，其他欧盟成员国可能面临要求同等政策调整的政治压力，进而影响整个欧元区财政纪律的协调。

此次事件的另一个重要维度是对欧盟整体治理氛围的潜在影响。法国作为欧盟第二大经济体与核心创始成员国，其国内政治稳定直接关系到欧盟在能源、外交与防务议题上的决策能力。如果法国政局持续动荡，可能削弱欧盟在重大国际议题上的协调能力，并对全球投资者信心产生连锁影响。法国政府能否在短期内通过对话与有限的政策调整化解矛盾，是观察欧洲政治气候走向的关键风向标。

**[多方观点比对]**

- **法国政府立场**：马克龙办公室强调抗议权利必须与维护公共秩序并重，承诺在法律框架内回应民生诉求，同时呼吁各方保持克制。
- **工会与左翼反对党**：多个工会联盟与左翼政党认为政府必须就生活成本与退休金政策做出实质性调整，否则将发起持续性罢工。
- **极右翼政党**：极右翼政治力量借机批评政府执政能力与治安政策，主张采取更强硬的执法措施。
- **欧盟委员会表态**：欧盟委员会发言人表示密切关注法国局势，重申和平抗议权利并尊重法国主权范围内的法治决策。

*编辑：GoodInfo全球资讯组*
"""

body_en_raw = """**[Key Facts]**

Hundreds of thousands of demonstrators took to the streets of French cities on October 18 in an anti-government protest that escalated into localised unrest, with clashes between police and demonstrators reported in Paris, Lyon, Marseille and Toulouse. President Emmanuel Macron rejected the resignation of his interior minister and called for calm, while announcing a national dialogue to address public grievances.

**[What We Know]**

- **Scale**: The French interior ministry said more than 500,000 people marched nationwide, with turnout in Paris, Lyon, Marseille and Toulouse hitting multi-year highs.
- **Clashes**: Demonstrators in Paris threw projectiles at police and damaged public buildings; riot-control units responded with crowd-dispersal measures, and several shops were damaged in the confrontations.
- **Political response**: The interior minister offered his resignation over the police tactics used during the protests; Macron refused it, citing the need for government stability.
- **Government measures**: The government deployed additional police to the worst-affected areas and asked local authorities to extend public transport to help demonstrators leave safely.
- **Underlying grievances**: The movement brought together anger over the cost of living, pension reform and uneven distribution of public services, with multiple unions and student associations co-ordinating the call.

**[Wider Perspective]**

The unrest exposes deeper strains inside French society as inflation, pension policy and shrinking public services collide. Several European governments are navigating the same set of pressures — high energy prices, widening fiscal deficits, and the politicisation of migration — so France's predicament is not isolated. It reflects a structural difficulty that European states increasingly face in keeping welfare commitments affordable without raising taxes or cutting benefits.

Macron's refusal to accept the interior minister's resignation is a calculated bid to keep his team intact at the moment the street movement is gathering momentum. France's recent history suggests that protests of this scale typically run for several weeks, and the eventual outcome — whether the government concedes on pensions or taxation or doubles down — will set the tone across the region. If Paris eventually agrees to material concessions, similar political pressure will land on other eurozone capitals, complicating fiscal-discipline negotiations across the bloc.

A second-order concern is what prolonged French instability could mean for the European Union as a whole. France is the bloc's second-largest economy and a founding member whose political cohesion is taken for granted in EU decision-making on energy, foreign policy and defence. A drawn-out political crisis in Paris would weaken the EU's ability to speak with one voice on global issues and shake investor confidence in a way that reverberates well beyond French borders. How quickly the government can defuse the protests through dialogue or limited concessions will be an important signal for Europe's broader political weather.

**[Viewpoints Compared]**

- **French government**: The Élysée says the right to protest must coexist with public order, and promises to engage grievances within the rule of law while urging restraint.
- **Unions and left-wing opposition**: Coalition unions and left-wing parties demand tangible concessions on the cost of living and pension policy, threatening sustained strikes if unmet.
- **Far-right parties**: Far-right factions are capitalising on the unrest to attack the government's competence on security and to argue for tougher enforcement.
- **European Commission**: A Commission spokesperson said it is following the situation closely, reaffirming the right to peaceful protest while respecting France's sovereign decisions under the rule of law.

*Editor: GoodInfo Global News Team*
"""

# sanitize body & tags
body_cn = sanitize_content(body_cn_raw)
body_en = sanitize_content(body_en_raw)

description_en_raw = "Hundreds of thousands marched in French cities on October 18 in an anti-government protest that escalated into localised unrest; Macron rejected his interior minister's resignation and called for calm."
summary_en_raw = "Hundreds of thousands of demonstrators took to French streets on October 18 in an anti-government protest that escalated into localised unrest, with clashes in Paris, Lyon and Marseille. President Macron rejected his interior minister's resignation, called for calm and launched a national dialogue to address grievances over cost of living and pension policy."

description_en = sanitize_title(description_en_raw)
summary_en = sanitize_title(summary_en_raw)

tags_cn_raw = ["法国", "马克龙", "群体事件", "欧洲政治", "退休金", "国际动态", "社会时事", "民生"]
tags_en_raw = ["France", "Macron", "Protest", "European Politics", "Pension Reform", "Civil Unrest", "Cost of Living"]

tags_cn = sanitize_tags(tags_cn_raw)
tags_en = sanitize_tags(tags_en_raw)

meta_cn = {
    "title": title_cn,
    "title_en": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_cn,
    "summary": summary_cn,
    "source": source_cn,
    "categories": ["world"],
    "tags": tags_cn,
}
path_cn = "/root/goodinfo-site/content/posts/world/france-anti-government-protests-unrest-macron-2026-10-19.md"
write_article(path_cn, meta_cn, body_cn)
print(f"CN: {path_cn}")

meta_en = {
    "title": title_en,
    "date": NOW_BJT_STR,
    "draft": "false",
    "tier": "1",
    "description": description_en,
    "summary": summary_en,
    "source": source_en,
    "categories": ["world"],
    "tags": tags_en,
}
path_en = "/root/goodinfo-site/content.en/posts/world/france-anti-government-protests-unrest-macron-2026-10-19.md"
write_article(path_en, meta_en, body_en)
print(f"EN: {path_en}")
