---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-013
title: More effort has diminishing returns
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 5.1 Reasoning effort and response length and quality'
sort_order: 13
language: en
---

Higher effort generally produces more tokens and can improve benchmark accuracy. It also increases cost and often **latency**. The article’s examples show that improvements can flatten or become uneven at higher effort settings.

That makes maximum effort a tradeoff rather than a universally efficient default. The right choice depends on how valuable a better answer is for the task and whether the additional work still produces a meaningful improvement on the relevant evaluation.
