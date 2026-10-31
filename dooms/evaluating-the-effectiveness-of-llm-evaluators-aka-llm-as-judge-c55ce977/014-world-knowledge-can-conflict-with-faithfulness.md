---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-014
title: World knowledge can conflict with faithfulness
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Use cases for LM-evaluators — HaluEval'
sort_order: 14
language: en
---

HaluEval deliberately includes plausible hallucinations that differ from correct answers in important factual spans. The evaluators Yan discusses struggled with these subtle differences.

Some errors involved statements that were true in the world but unsupported by the supplied context. A judge must distinguish those standards: knowing a fact is plausible does not establish that a response faithfully represents the evidence it was given.
