---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-019
title: Keep the architecture that survives measurement
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Conclusion'
sort_order: 21
language: en
---

The article’s final recommendation is incremental: build a small end-to-end evaluation, fold in one subagent, compare results, and retain a separate loop when the consolidated version performs worse.

Models and best practices change, so an architecture should remain revisable. Skills and tools may replace more specialists over time, but measured task quality, cost, and **latency** should decide which boundaries remain useful.
