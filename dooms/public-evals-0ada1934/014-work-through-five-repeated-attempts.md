---
schema_version: 2
id: public-evals-0ada1934-014
title: Work through five repeated attempts
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Hot takes: How we’re thinking about evals wrongly'
sort_order: 14
language: en
---

**Worked example from the article.** Suppose each attempt succeeds independently with probability `0.7`. The chance that five attempts all succeed is `0.7^5`, about **17%**.

| Agent behavior | Average success | Pass all five |
| --- | --- | --- |
| Always solves the same 70% | 70% | 70% |
| Independent 70% chance per attempt | 70% | About 17% |

The independence assumption belongs to this example. Real repeated runs need to be measured.
