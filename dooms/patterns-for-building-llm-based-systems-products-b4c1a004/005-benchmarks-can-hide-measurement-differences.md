---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-005
title: Benchmarks can hide measurement differences
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Evals — metric pitfalls and MMLU'
sort_order: 5
language: en
---

Yan highlights weak human correlation, poor transfer between tasks and reproducibility problems in familiar metrics. Even implementations carrying the same benchmark name may use different prompts or answer-scoring rules.

His MMLU example contrasts scoring an answer letter, the next generated token or the full answer sequence. A model ranking is difficult to interpret if those details change between comparisons.
