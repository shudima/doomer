---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-032
title: Continuous control still needs training
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.6 Inkling conditions RL on a continuous effort value'
sort_order: 34
language: en
---

Inkling’s report places most post-training work after a relatively small initial supervised stage, using asynchronous reinforcement learning with more than 30 million rollouts. The desired effort enters the system message, and the associated token penalty changes during training.

This is why a numeric effort value can influence output at inference. The number selects an established cost-quality behavior; it is not a universal token-budget formula that can be transplanted unchanged to other models.
