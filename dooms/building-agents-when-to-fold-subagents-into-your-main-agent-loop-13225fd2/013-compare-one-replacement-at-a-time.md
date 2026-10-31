---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-012
title: Compare one replacement at a time
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Folding subagents into the main agent via skills and tools'
sort_order: 13
language: en
---

Turn a specialist’s prompts into skills and its API actions into tools, then compare performance with and without that subagent. Keep the version that holds up under evaluation.

Inspect individual tasks that changed outcome, not only the aggregate score. Anthropic describes a faster support workflow that regressed because the main agent answered from order data without obtaining the delivery date from the shipping specialist.
