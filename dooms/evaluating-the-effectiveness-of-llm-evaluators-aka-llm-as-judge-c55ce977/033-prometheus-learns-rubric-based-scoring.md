---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-031
title: Prometheus learns rubric-based scoring
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Finetuning LLM-evaluator models — Prometheus'
sort_order: 33
language: en
---

Prometheus takes an instruction, scoring rubric, candidate response and reference answer, then generates feedback and a score. Its training data uses model-generated rubrics, responses and critiques.

Yan reports strong results on some evaluated data but weaker results elsewhere. The model illustrates the promise of specialized judges while also showing why evaluation must test more than a benchmark closely related to the training setup.
