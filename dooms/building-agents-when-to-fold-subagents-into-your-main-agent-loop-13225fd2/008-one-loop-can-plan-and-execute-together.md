---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-007
title: One loop can plan and execute together
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: How to fold subagents into the main agent loop'
sort_order: 8
language: en
---

The proposed design uses one model and **context window** with an open-ended tool loop. The model plans, calls tools, reads raw results, and revises its approach rather than handing a fixed plan to separate specialists.

The harness still enforces turn and cost budgets and write gates. Independent tool calls can run in parallel, while the same model decides whether to continue, ask the user, or answer.
