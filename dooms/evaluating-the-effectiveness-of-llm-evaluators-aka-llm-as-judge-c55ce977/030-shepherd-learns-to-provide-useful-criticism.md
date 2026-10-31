---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-028
title: Shepherd learns to provide useful criticism
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Finetuning LLM-evaluator models — Shepherd'
sort_order: 30
language: en
---

Shepherd is a specialized critic trained on community question-answer critiques and human feedback. It aims to identify errors and suggest improvements rather than merely produce a preference label.

Yan reports competitive critique quality in the evaluated settings, including a newer test designed to reduce contamination concerns. This makes specialized training a possible alternative when repeatedly prompting a general model does not provide enough reliability.
