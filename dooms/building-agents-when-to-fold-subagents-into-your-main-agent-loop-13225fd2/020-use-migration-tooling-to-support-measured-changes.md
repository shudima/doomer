---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-018
title: Use migration tooling to support measured changes
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Tools to accelerate this work'
sort_order: 20
language: en
---

Anthropic’s migration kit chains tools for building evals, auditing prompts, iterating against evaluations, and profiling costs. It includes a mock-system demo before applying the workflow to a real deployment.

The named skills support different stages: build-eval establishes checks, prompt-audit proposes instruction changes, hillclimb compares improvements, and cost-optimize explores savings one change at a time. Their value depends on keeping the evaluation target meaningful.
