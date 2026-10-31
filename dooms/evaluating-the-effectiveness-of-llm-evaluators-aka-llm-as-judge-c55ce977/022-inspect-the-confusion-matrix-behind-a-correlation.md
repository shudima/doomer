---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-021
title: Inspect the confusion matrix behind a correlation
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Techniques for prompting LLM-evaluators — UMbrela'
sort_order: 22
language: en
---

A strong overall correlation can hide failures you care about. Inspect which examples the judge passes and rejects.

A **confusion matrix** separates real failures it catches, failures it misses, acceptable answers it rejects, and acceptable answers it passes. These groups reveal whether a judge is useful for the intended decision. Ranking answers and blocking defects require different evidence.

![Classification diagnostic plots: ROC, precision-recall, threshold trade-offs and a score distribution.](images/source-01.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
