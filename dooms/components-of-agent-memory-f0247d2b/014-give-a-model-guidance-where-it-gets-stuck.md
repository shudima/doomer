---
schema_version: 2
id: components-of-agent-memory-f0247d2b-014
title: Give a model guidance where it gets stuck
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Steering Claude to write memory'
sort_order: 14
language: en
---

Sonnet 4.6 often skipped its memory files or saved theories it had never tested. On Anthropic’s database task, explicit guidance to read the notes and test its theories raised mean reward from **0.364 to 0.641** with memory.

Sonnet 5 read memory before answering about nine times in ten on its own. Anthropic describes lighter guidance for its stronger models, such as saving what the user asks for and what clearly matters.
