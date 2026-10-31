---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-023
title: Practice answering after an interrupted trace
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.2.2 Reasoning budget-aware training in Nemotron'
sort_order: 25
language: en
---

To prepare Nemotron for hard budgets, its training data include reasoning traces cut at randomly selected token limits while retaining the original final answers. The externally inserted closing tag is masked from the supervised loss.

The model therefore practices continuing to an answer from an incomplete trace once the reasoning block is closed. This budget preparation complements the separately learned medium-effort behavior; shortening a trace and learning a more efficient reasoning policy are related but distinct interventions.
