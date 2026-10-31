---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-013
title: A mediator coordinates services through shared rules
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in systems — mediator'
sort_order: 15
language: en
---

A **mediator** coordinates components through shared rules. Each component talks to the mediator instead of learning every other component’s interface.

A machine-learning service might need to meet the mediator’s request format, latency budget and rate limits. The model is one part of that larger system. Its output becomes useful when it fits the coordination rules around it.
