---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-015
title: Supervised examples offer another route
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 5.2 Possible effort level implementations'
sort_order: 15
language: en
---

A model can also learn effort control through supervised fine-tuning. Pair each effort instruction with a response that demonstrates the intended amount of reasoning, using human-written or generated-and-filtered targets.

The model learns the relationship between the label and the response style directly from examples. This can be combined with effort-conditioned reinforcement learning. Raschka suspects such combinations may be used in practice, while emphasizing that the relevant OpenAI training details have not been published.
