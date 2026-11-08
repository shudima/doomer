---
schema_version: 2
id: components-of-agent-memory-f0247d2b-009
title: A memory folder helped models by different amounts
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Memory can be a prediction about what the future will need
  · Figure 3'
sort_order: 9
language: en
---

On Anthropic’s CL-Bench database task, Opus 5 went from **0.564 to 0.828** mean reward with memory. Sonnet 4.6 went from **0.330 to 0.364**. Opus 5.5 and Sonnet 5.5 started higher and finished close to Opus 5 with memory.

These scores describe this task. The comparison shows why giving a model a folder and checking how it uses the folder are separate steps.

![The left bars compare mean database-task reward with and without memory. The right plot tracks the running mean across 30 questions.](images/figure-03.webp)

*Figure 3 from Anthropic. Illustration by Monika Tuchowska.*
