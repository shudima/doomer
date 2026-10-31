---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-017
title: Model choice and effort are separate knobs
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 5.4 A short note about inference scaling versus training scaling'
sort_order: 17
language: en
---

Choosing a model selects an already trained checkpoint. Raising its effort level changes the work spent **during inference**; it does not train a new model.

The article shows that a smaller model at higher effort can sometimes approach a larger one at lower effort. That overlap is benchmark-specific. Compare answer quality, cost and latency on your task instead of assuming one combination always wins.
