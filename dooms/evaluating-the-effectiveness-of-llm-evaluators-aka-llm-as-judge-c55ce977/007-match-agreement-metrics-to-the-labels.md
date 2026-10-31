---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-007
title: Match agreement metrics to the labels
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Key considerations before adopting an LLM-evaluator — agreement and correlation'
sort_order: 7
language: en
---

Cohen's kappa measures categorical agreement while accounting for agreement expected by chance. Rank correlations such as Spearman's rho and Kendall's tau address ordering rather than the same categorical decision.

Yan warns against treating their numerical values as interchangeable evidence. Pick a metric suited to the labels, then examine what it says about the judge's actual behavior and production-relevant errors.
