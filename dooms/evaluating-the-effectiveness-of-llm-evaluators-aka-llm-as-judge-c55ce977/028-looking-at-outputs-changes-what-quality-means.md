---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-026
title: Looking at outputs changes what quality means
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Aligning LLM-evaluators to our criteria — EvalGen'
sort_order: 28
language: en
---

EvalGen lets builders inspect outputs, revise criteria and choose code assertions or model-based checks. The study observes that people often discover their actual standards only after grading examples.

Yan describes this as an inner alignment loop inside product evaluation. Criteria cannot always be completely specified upfront; the tooling should support revisiting earlier judgments when newly observed failures clarify the requirement.
