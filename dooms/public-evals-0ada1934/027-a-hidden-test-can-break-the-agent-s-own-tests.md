---
schema_version: 2
id: public-evals-0ada1934-027
title: A hidden test can break the agent’s own tests
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — DeepSWE
sort_order: 27
language: en
---

DeepSWE’s grader swaps in hidden test files. Those files can clash with tests the agent added, causing compilation errors even when its implementation is valid.

Yan cites an Epoch AI review identifying this particular problem in **18 of 113 tasks** in v1.1. The mechanism matters because agents that add verification can be penalized by the grader’s integration step. Inspect how grading files combine with the submitted repository.
