---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-005
title: A reference changes the evaluation problem
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Key considerations before adopting an LLM-evaluator — reference-based evaluation'
sort_order: 5
language: en
---

Providing a gold answer lets a judge compare the generated response against expected information. This can resemble sophisticated fuzzy matching rather than independent assessment of truth.

Yan emphasizes that reference-based results should not be mistaken for reference-free capability. A method that works well when supplied the correct answer may not work as a production guardrail where that answer is unavailable.
