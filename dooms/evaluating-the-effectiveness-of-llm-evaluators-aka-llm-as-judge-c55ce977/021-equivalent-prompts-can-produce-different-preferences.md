---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-020
title: Equivalent prompts can produce different preferences
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Techniques for prompting LLM-evaluators — Fairer Preferences'
sort_order: 21
language: en
---

Rephrasing an evaluation instruction without changing its meaning can still change which response a judge prefers. The fairer-preferences study tries to reduce that asymmetry through prompt optimization.

Yan reports improved average human correlation but mixed results on important individual dimensions. A gain on an aggregate should not hide regressions in the specific qualities the product needs to measure reliably.
