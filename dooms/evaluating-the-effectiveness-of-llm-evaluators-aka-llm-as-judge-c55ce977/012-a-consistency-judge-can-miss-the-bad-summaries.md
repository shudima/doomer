---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-012
title: A consistency judge can miss the bad summaries
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Use cases for LM-evaluators — Factual Inconsistency Evaluator'
sort_order: 12
language: en
---

The factual-inconsistency study Yan reviews found strong recognition of supported summaries but much weaker recognition of unsupported ones. Depending on the dataset, the judge identified only about 30–60% of inconsistent summaries.

This is why overall performance can mislead. A guardrail's usefulness depends especially on catching the defects it exists to block, not simply approving the many acceptable examples.
