---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-050
title: Combine the patterns into an improvement loop
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Other patterns common in machine learning — flywheel and cascade'
sort_order: 53
language: en
---

Better data can improve a model, a better experience can increase use, and use can supply further evidence for evaluation and training. Yan describes this as a data flywheel.

He also highlights task decomposition: conventional **retrieval** or specialized components can handle work that a language model need not perform internally, reserving generation for the parts where it adds value.

![LLM patterns across the axis of data to user, and defensive to offensive.](images/source-29.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
