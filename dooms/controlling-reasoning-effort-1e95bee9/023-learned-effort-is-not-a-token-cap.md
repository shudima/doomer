---
schema_version: 2
id: controlling-reasoning-effort-1e95bee9-022
title: Learned effort is not a token cap
background_image: images/effort.svg
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
source_file: null
source_title: Controlling Reasoning Effort in LLMs
source_type: article
source_locator: 'Section: 6.2.1 Using Nemotron reasoning budgets during inference'
sort_order: 23
language: en
---

Nemotron selects its learned modes through the chat template. Regular opens a reasoning block; medium-effort also adds an efficiency instruction. Reasoning-off prefills an empty block so the model proceeds to its answer.

A separate reasoning budget can constrain either reasoning mode. Near the limit, the client requests an end to reasoning; if necessary, it closes the block externally. The mode guides how the model spends tokens, while the budget limits how long that spending can continue.
