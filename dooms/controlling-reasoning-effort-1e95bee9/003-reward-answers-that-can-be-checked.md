---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-003
title: Reward answers that can be checked
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 2.1 Training reasoning models'
sort_order: 3
language: en
---

Reinforcement learning with verifiable rewards, or RLVR, trains on tasks whose answers can be checked. Math can use symbolic checkers; code can use tests or compilation. A simple correctness signal gives one reward for success and another for failure.

In the DeepSeek-R1 recipe discussed here, the reasoning steps were not individually graded for correctness. Final-answer and formatting rewards guided learning. Rewarding intermediate steps directly remains a separate research direction.
