---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-006
title: Measure defects directly when possible
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Key considerations before adopting an LLM-evaluator — classification metrics'
sort_order: 6
language: en
---

**Precision** and recall answer practical questions: how many real defects did the judge catch, and how many of its alarms were justified? Binary evaluator outputs make these measurements straightforward.

Yan prefers this clarity when the task permits it. A high overall agreement or ranking correlation may otherwise conceal weak performance on the bad responses that the product most needs to identify.
