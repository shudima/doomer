---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-023
title: More reasoning can be the wrong behavior
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Techniques for prompting LLM-evaluators — PoLL ablation'
sort_order: 25
language: en
---

In the panel study, the larger baseline sometimes injected background knowledge into what should have been a comparison against a reference answer. Even simple string matching could outperform it on one dataset.

An instruction discouraging overthinking improved the model's result. Yan uses this to highlight that a judge should perform the required operation, not substitute an impressive but inappropriate reasoning task.
