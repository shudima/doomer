---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-034
title: Keep credentials out of context
background_image: images/part-05.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 45-46
sort_order: 38
language: en
---

Use short-lived, narrowly scoped tokens intended for the downstream service. The survey highlights audience binding and MCP's prohibition on passing through tokens meant elsewhere.

The harness holds credentials; tools check scopes and object permissions. The model cannot choose whose identity to use. Audit user and agent, gate sensitive access, and preserve these boundaries across subagents and external handoffs.
