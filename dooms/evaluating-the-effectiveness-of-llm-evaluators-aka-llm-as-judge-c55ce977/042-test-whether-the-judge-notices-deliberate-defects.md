---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-039
title: Test whether the judge notices deliberate defects
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Critiques against and support for LLM-evaluators — Blind Spots'
sort_order: 42
language: en
---

The checklist study creates perturbed answers targeting coherence, factuality, instruction following and reasoning. Even the strongest evaluated model frequently failed to penalize degraded answers.

Yan presents this as a practical diagnostic: a useful judge should respond to meaningful quality changes. More complex rubrics did not consistently outperform simpler judging strategies, so elaborate prompting alone is not evidence of robustness.
