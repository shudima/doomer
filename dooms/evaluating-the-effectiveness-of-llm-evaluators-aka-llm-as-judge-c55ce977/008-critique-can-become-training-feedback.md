---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-008
title: Critique can become training feedback
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Use cases for LM-evaluators — Constitutional AI'
sort_order: 8
language: en
---

The Constitutional AI work reviewed by Yan uses a model to identify harmful aspects of an answer and guide a revised version. Revised responses can then support instruction tuning.

It also uses model preferences between responses for preference training. This demonstrates a judge participating in an improvement loop, where its assessment changes what the next model learns rather than merely generating a dashboard score.
