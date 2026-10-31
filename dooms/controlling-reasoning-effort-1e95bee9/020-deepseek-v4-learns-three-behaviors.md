---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-019
title: DeepSeek V4 learns three behaviors
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.1 DeepSeek V4 trains separate effort specialists'
sort_order: 20
language: en
---

DeepSeek V4 supports Non-think, Think High, and Think Max. Non-think gives a direct response. The other modes produce reasoning traces, with Think Max receiving an additional strong effort instruction.

The instruction is backed by post-training differences. Think Max gets a longer **context window** and a smaller length penalty than Think High. Copying its wording into an arbitrary model would not reproduce the behavior created by those training conditions.
