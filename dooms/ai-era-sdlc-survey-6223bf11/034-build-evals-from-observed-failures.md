---
schema_version: 2
id: ai-era-sdlc-survey-6223bf11-030
title: Build evals from observed failures
background_image: images/quality.svg
source_url: null
source_file: source/original.pdf
source_title: The Software Development Life Cycle in the AI Era
source_type: pdf
source_locator: 'Pages 4-5: Eval glossary; page 20: Evaluations'
sort_order: 34
language: en
---

An evaluation is a repeatable check of an AI system's output quality. For an LLM feature, the survey recommends starting with real execution traces: inspect inputs, outputs and tool calls, label failures and build a taxonomy before choosing evaluators.

Use code assertions for properties such as schema, tool choice, **latency** and cost. Semantic qualities may need a model judge or human assessment. A curated, versioned dataset becomes a baseline, and the evaluation suite becomes an executable specification for the feature.
