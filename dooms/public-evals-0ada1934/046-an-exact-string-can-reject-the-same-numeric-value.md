---
schema_version: 2
id: public-evals-0ada1934-046
title: An exact string can reject the same numeric value
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — AutomationBench
sort_order: 46
language: en
---

One review of AutomationBench found valid work rejected for representing the same amount as `150,000` and `150000.0`. The public assertions also often use substring matching, which can accept an unrelated number in a message.

A numeric requirement needs a check of numeric meaning and its role in the record. A required verbatim phrase needs a different kind of check. Pick the comparison from the task’s actual contract.
