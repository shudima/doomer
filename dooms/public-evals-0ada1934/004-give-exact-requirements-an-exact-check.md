---
schema_version: 2
id: public-evals-0ada1934-004
title: Give exact requirements an exact check
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Principles: That shape grading and task selection'
sort_order: 4
language: en
---

Code can check whether a file exists, a saved value matches a target, or a transaction changed the right record. Repeating the same check keeps its meaning stable.

A language-model judge helps when a requirement needs interpretation. Several benchmarks keep that job narrow, asking a yes-or-no question for each rubric item. Record the judge version too, because changing it can change model rankings.
