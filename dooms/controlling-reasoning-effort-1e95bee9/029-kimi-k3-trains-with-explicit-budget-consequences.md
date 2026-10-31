---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-027
title: Kimi K3 trains with explicit budget consequences
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.3.3 Kimi K3 (Update)'
sort_order: 29
language: en
---

The article’s Kimi K3 update describes low, high, and max effort. For simple verifiable tasks, a response that exceeds its training budget receives a negative reward instead of the usual correctness reward.

Training starts with a generous-budget max-effort specialist, then lowers the budget for high- and low-effort specialists. The exact reward treatment differs for non-verifiable and agentic tasks, where learned rewards and pairwise comparisons also enter the pipeline.
