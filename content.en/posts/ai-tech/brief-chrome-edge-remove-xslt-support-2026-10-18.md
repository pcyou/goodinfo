---
title: "[Brief] Chrome and Edge are removing XSLT support"
title_en: "[Brief] Chrome and Edge are removing XSLT support"
date: "2026-10-18T04:00:00+08:00"
draft: "false"
tier: "2"
description: "According to a Hacker News item on Oct. 17, Chrome and Edge are planning to remove support for XSLT 1.0, a decision that has sparked wide discussion across the enterprise and developer communities, with some internal systems that rely on XSLT for document display needing adjustment."
summary: "According to a Hacker News item on Oct. 17, Chrome and Edge are planning to remove support for XSLT 1.0, a decision that has sparked wide discussion across the enterprise and developer communities. XSLT is a traditional Web technology used to transform XML documents into other formats (such as HTML), and has been used by many enterprises and government agencies for internal systems, data publishing and document display. The reports note that removing XSLT support is part of browser-engine modernization, but some legacy systems and public-document pages that depend on XSLT may face display anomalies or need to migrate to new rendering schemes."
source: "Hacker News / browser-engineering blog posts"
categories:
  - "ai-tech"
tags:
  - "Chrome"
  - "Edge"
  - "XSLT"
  - "Browsers"
  - "Web Standards"
  - "Developer Community"
---

**[Core Summary]**

According to a Hacker News item on Oct. 17, Chrome and Edge are planning to remove support for XSLT 1.0, a decision that has sparked wide discussion across the enterprise and developer communities.

**[Event Details]**

- **Change**: The browser engines will no longer support XSLT 1.0 APIs and parsing paths, meaning pages that rely on XSLT to display XML directly in the browser will no longer render as before.
- **Background**: XSLT was once used by many enterprises, government agencies and data-publishing platforms for XML document transformation and display, but its usage has declined significantly over the past decade as modern frameworks and JSON data formats have become mainstream.
- **Impact**: Some legacy internal systems, government open-data portals and historical document sites may need to assess the impact and develop migration plans.
- **Developer Reaction**: The developer community has discussed the trade-off between compatibility and modernization, with some voices calling for a longer transition period or retaining a toggleable compatibility option.
- **Alternatives**: The industry advises affected projects to migrate to server-side XSLT processing or client-side JavaScript rendering to avoid relying on the browser's native XSLT.

**[Panoramic Perspective]**

Chrome and Edge's decision to remove XSLT reflects the long-running Web platform path of "streamlining legacy technology and focusing on modern standards." XSLT, in its heyday, was a key tool for processing structured documents and cross-platform data display, but as Web application architecture has shifted toward SPA, PWA and API-driven models, the use cases for XSLT have shrunk dramatically. In the short term, some enterprises and public agencies need to invest resources in migrating legacy systems — a typical "technical-debt concentrated repayment" task. In the long run, as browser engines continue to shed historical baggage, they also need to provide clearer migration guidance and transition tools for key legacy scenarios, balancing the pace of innovation with ecosystem stability.

*Editor: GoodInfo Global News Desk*