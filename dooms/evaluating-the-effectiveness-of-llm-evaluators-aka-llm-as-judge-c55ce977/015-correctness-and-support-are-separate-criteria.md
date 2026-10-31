---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-015
title: Correctness and support are separate criteria
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Use cases for LM-evaluators — Correctness and Faithfulness in QA'
sort_order: 15
language: en
---

An answer can be factually correct and still unsupported by the supplied source. These are separate checks:

- **Correctness:** is the claim true?
- **Faithfulness:** does the provided material support it?

A judge using its own world knowledge may pass a claim that a source-grounded task should reject. Tell it which criterion matters and test that distinction with examples.
