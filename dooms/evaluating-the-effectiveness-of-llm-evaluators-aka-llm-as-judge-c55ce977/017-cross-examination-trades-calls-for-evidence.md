---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-016
title: Cross-examination trades calls for evidence
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Techniques for prompting LLM-evaluators — LM vs LM'
sort_order: 17
language: en
---

One model can question another about a claim, asking follow-ups designed to reveal inconsistencies before making a verdict. The reviewed LM-vs-LM experiments also repeat examinations and combine the decisions.

Yan reports promising **precision** and recall around this approach, but emphasizes its operational cost. Multiple conversational turns and repeated runs increase both latency and the number of paid model calls.
