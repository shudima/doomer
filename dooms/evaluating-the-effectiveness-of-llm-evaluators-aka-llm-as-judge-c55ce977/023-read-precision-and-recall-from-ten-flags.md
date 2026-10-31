---
schema_version: 2
id: evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-045
title: Read precision and recall from ten flags
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-evaluators/
source_file: null
source_title: Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
source_type: article
source_locator: 'Section: Techniques for prompting LLM-evaluators — UMbrela; added illustrative example'
sort_order: 23
language: en
---

**Illustrative example**

Suppose a judge flags ten answers. Eight really fail, so precision is 8/10, or 80%. The dataset contains twenty real failures, so recall is 8/20, or 40%.

| Result | Count |
| --- | ---: |
| Real failures caught | 8 |
| Acceptable answers flagged | 2 |
| Real failures missed | 12 |

The judge’s flags are often right, but it misses most defects. These are toy numbers.
