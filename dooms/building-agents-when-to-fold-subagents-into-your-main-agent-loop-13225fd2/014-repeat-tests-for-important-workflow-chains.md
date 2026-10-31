---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-013
title: Repeat tests for important workflow chains
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Folding subagents into the main agent via skills and tools'
sort_order: 14
language: en
---

Before each migration step, include examples for production chains of cooperating agents and rules the system must not break. Run those examples more than once.

In the article’s support example, a regression appeared in only one of two runs. A single successful attempt could therefore hide a changed failure rate. Reducing **latency** is not sufficient evidence that consolidation preserved the procedure users depend on.
