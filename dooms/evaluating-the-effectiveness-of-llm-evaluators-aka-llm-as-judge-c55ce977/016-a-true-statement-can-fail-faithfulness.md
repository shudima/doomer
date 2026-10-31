---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-044
title: A true statement can fail faithfulness
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Use cases for LM-evaluators — Correctness and Faithfulness in QA; added illustrative example'
sort_order: 16
language: en
---

**Illustrative example**

The supplied passage says only that a company opened a Paris office. The answer adds that Paris is the capital of France.

That extra claim is true, but the passage did not support it. If the task requires using only the supplied text, the answer fails the grounding rule. Test correctness and faithfulness as separate criteria.
