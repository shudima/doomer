---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-011
title: Soft instructions versus a hard prefix
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 4. Reasoning mode on and off switches'
sort_order: 11
language: en
---

Qwen3 supports `/think` and `/no_think` instructions as soft mode requests. Its `enable_thinking=False` chat-template setting takes a more direct route: it prefills an empty `<think></think>` block at the start of the assistant response.

The model then continues after the closed reasoning section. The tokenizer is not simply adding `/no_think` to the user’s question. It changes the response prefix to select a behavior that the model has already learned.
