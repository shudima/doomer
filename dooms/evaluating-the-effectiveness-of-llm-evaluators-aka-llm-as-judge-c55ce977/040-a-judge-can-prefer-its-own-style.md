---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-037
title: A judge can prefer its own style
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Critiques against and support for LLM-evaluators — self-enhancement bias'
sort_order: 40
language: en
---

Models may favor responses produced by themselves. Yan reports examples in which model-based win rates were more favorable to the judge's own outputs than human evaluations were.

This matters when comparing models or optimizing against a judge. A system may learn the evaluator's stylistic preferences while appearing to improve, so evaluator selection and human checks should account for this potential source of bias.
