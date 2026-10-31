---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-002
title: Two ways to spend more compute
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 2. A brief overview of training and inference scaling reasoning models'
sort_order: 2
language: en
---

You can spend more compute at two different times:

- **Training:** improve the model before anyone asks a question.
- **Inference:** let it spend more work answering a particular question.

The article compares these ways of improving results. More inference-time work can help some tasks, but its value depends on the model, task and method. It also adds latency and cost.

![Figure 4: Training and inference-scaling are two ways to improve LLM and reasoning model problem-solving capabilities. Plot based on Learning to reason with LLMs](images/source-03.webp)

*Source: Sebastian Raschka’s article; paper credits remain in the original diagram. Tap to enlarge; the complete figure is preserved.*
