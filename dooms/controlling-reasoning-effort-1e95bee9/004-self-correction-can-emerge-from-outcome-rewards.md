---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-004
title: Self-correction can emerge from outcome rewards
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 2.2 “Aha” moments'
sort_order: 4
language: en
---

A model trained on final outcomes can learn to generate intermediate explanations, notice mistakes, backtrack, and revise its approach. The article calls these visible self-corrections “aha” moments.

That does not mean a human-like insight has been established. The interesting training result is narrower: the model can acquire useful reasoning-trace behavior without every intermediate step receiving its own explicit correctness reward. Better outcomes can encourage strategies that help produce them.

![Figure 7: An example of an aha moment, where a reasoning model notices an error in its intermediate reasoning and corrects it before producing the final answer.](images/source-06.webp)

*Source: Sebastian Raschka’s article; paper credits remain in the original diagram. Tap to enlarge; the complete figure is preserved.*
