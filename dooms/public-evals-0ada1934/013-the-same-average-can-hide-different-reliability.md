---
schema_version: 2
id: public-evals-0ada1934-013
title: The same average can hide different reliability
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Hot takes: How we’re thinking about evals wrongly'
sort_order: 13
language: en
---

Imagine two agents that each average 70% success. One always solves the same 70% of tasks. The other succeeds on every kind of task only 70% of the time.

The first has a dependable subset. The second requires checking each attempt. Yan proposes reporting **pass^k**, which gives a task credit only when all `k` repeated attempts succeed. It measures consistency that an average can hide.
