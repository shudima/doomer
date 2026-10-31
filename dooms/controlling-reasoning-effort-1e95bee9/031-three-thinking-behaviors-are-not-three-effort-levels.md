---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-029
title: Three thinking behaviors are not three effort levels
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.4 GLM-5 introduces turn-level and interleaved thinking through SFT'
sort_order: 31
language: en
---

GLM-5 describes interleaved, preserved, and turn-level thinking. Interleaved thinking places reasoning before responses and tool calls. Preserved thinking retains earlier reasoning blocks for later turns. Turn-level thinking enables or disables reasoning for each request.

These are different controls over when reasoning occurs and what history is kept, rather than a low-medium-high effort scale. The report introduces them through multi-task supervised fine-tuning and an updated chat template.
