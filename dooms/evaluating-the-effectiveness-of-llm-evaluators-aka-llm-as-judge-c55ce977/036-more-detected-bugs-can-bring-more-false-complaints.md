---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-034
title: More detected bugs can bring more false complaints
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Finetuning LLM-evaluator models — CriticGPT caveats'
sort_order: 36
language: en
---

The CriticGPT findings also include nitpicks and hallucinated problems. Yan notes a trade-off between catching more defects and maintaining **precision** in the resulting critiques.

The inserted bugs were not drawn from the natural distribution of model mistakes, which also limits generalization. A code critic should be tested on realistic errors and unnecessary alarms, not celebrated solely for finding adversarially planted bugs.
