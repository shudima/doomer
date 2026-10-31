---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-031
title: Narrow the task before choosing the model
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Fine-tuning — model and architecture selection'
sort_order: 32
language: en
---

A small classifier or natural-language-inference model may fit a narrow task better than a large general generator. Yan recommends defining evaluation metrics and the task before selecting the pretrained model.

The architecture may also need adjustment, such as changing a classification head. Parameter-efficient tuning is one option, while more intensive domain adaptation can require a different approach.
