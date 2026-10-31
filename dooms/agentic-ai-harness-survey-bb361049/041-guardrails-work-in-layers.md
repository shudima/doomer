---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-037
title: Guardrails work in layers
background_image: images/part-05.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 47-48
sort_order: 41
language: en
---

Agent controls can inspect input, proposed tool calls, returned data, final output and runtime behaviour. Deterministic policy before tool execution is the core; classifiers add signals around it.

Budgets, anomaly alerts and a kill switch limit runaway activity. Review and pin external servers, plugins and skills, since descriptions and scripts are part of the attack surface. Probe every content channel with injected instructions. A successful detector in one channel does not establish containment across the system.
