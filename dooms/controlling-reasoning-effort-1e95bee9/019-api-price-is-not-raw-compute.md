---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-018
title: API price is not raw compute
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 5.4 A short note about inference scaling versus training scaling'
sort_order: 19
language: en
---

A cost-versus-performance chart is useful when choosing a model and effort level, but its horizontal axis matters. The article’s comparison uses API cost, which depends on provider pricing and token usage, not just the physical computation performed.

The best operating point also depends on **latency** and required accuracy. Two settings with similar benchmark scores can impose different waiting times or bills, and a different task suite may change which setting looks attractive.
