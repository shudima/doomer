---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-014
title: Train the reward around the requested effort
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 5.2 Possible effort level implementations'
sort_order: 14
language: en
---

One possible implementation adds effort labels during reinforcement learning and changes the cost of producing tokens. Low effort receives a stronger length penalty; high effort receives a smaller penalty or none.

The model learns how to balance solving the task against spending tokens under each instruction. This is an implementation pattern proposed in the article, not a disclosed account of OpenAI’s proprietary training pipeline. An effort label alone would not create that learned tradeoff.
