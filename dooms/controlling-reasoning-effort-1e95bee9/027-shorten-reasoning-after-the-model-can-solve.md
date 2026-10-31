---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-025
title: Shorten reasoning after the model can solve
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.3.1 Kimi’s Toggle method'
sort_order: 27
language: en
---

Toggle estimates each problem’s budget from a selected percentile of correct rollout lengths. It activates the budget constraint only after mean accuracy on that problem exceeds a threshold.

This avoids demanding short reasoning before the model can solve the problem reliably. Evaluations on K2 Thinking reported roughly 25–30% fewer generated tokens with little benchmark change, and transfer from math and coding training to GPQA and MMLU-Pro. These are reported experimental results, not guaranteed savings for every task.
