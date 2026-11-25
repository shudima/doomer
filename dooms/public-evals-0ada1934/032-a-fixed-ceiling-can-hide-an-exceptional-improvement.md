---
schema_version: 2
id: public-evals-0ada1934-032
title: A fixed ceiling can hide an exceptional improvement
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — FrontierSWE
sort_order: 32
language: en
---

Once a FrontierSWE task reaches its full-credit target, improving further earns the same score. Yan proposes measuring the fraction of baseline work saved for performance tasks.

His example uses `1 - 1/speedup`. Halving the instruction count gives a speedup of two and a score of **0.5**. Cutting the count by 99% gives **0.99**. This is a proposed scoring approach, rather than the benchmark’s existing rule.
