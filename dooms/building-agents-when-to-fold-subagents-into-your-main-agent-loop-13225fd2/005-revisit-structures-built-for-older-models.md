---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-005
title: Revisit structures built for older models
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Using an agent loop with progressive disclosure'
sort_order: 5
language: en
---

Some rigid classifiers and fixed pipelines were added because earlier models needed more scaffolding. Anthropic argues that newer models can manage more planning and tool work within one loop, making some structures redundant.

It reports cutting Claude Code’s system prompt by over 80%, including reductions tied to **progressive disclosure**. That example motivates auditing accumulated instructions; it does not guarantee that removing the same fraction elsewhere preserves quality.
