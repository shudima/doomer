---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-032
title: A gold answer can do much of the work
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Finetuning LLM-evaluator models — Prometheus ablation'
sort_order: 34
language: en
---

Removing the reference answer caused the largest performance decline in the Prometheus ablation discussed by Yan. Removing other ingredients had smaller effects.

That makes the reference an important condition of the result. A judge may be learning a sophisticated comparison against a supplied answer; its success should not be presented as equivalent evidence of independent, reference-free evaluation.
