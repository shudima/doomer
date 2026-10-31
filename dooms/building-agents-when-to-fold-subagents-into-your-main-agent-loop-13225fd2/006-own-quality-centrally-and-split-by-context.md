---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-006
title: Own quality centrally and split by context
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Using an agent loop with progressive disclosure'
sort_order: 6
language: en
---

The article recommends a small central team owning the system prompt and end-to-end quality, with new tools and evaluations vetted before release. Domain teams can still contribute specialized knowledge.

Where multiple agents remain, choose simple boundaries with little shared context and compact outputs, such as independent research or black-box **verification**. Splitting tightly related work by problem label can create a repeated telephone game of degraded detail.

![subagents split by problem](images/source-01.webp)

*Source: Anthropic’s article. Tap to enlarge; the complete figure is preserved.*
