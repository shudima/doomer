---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-040
title: Constrain structure during generation
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Guardrails — Guidance and token healing'
sort_order: 42
language: en
---

Rather than hoping a model generates the right delimiters and format, a constrained-generation approach can directly control structural tokens. Yan describes Guidance as an example of coordinating generation with a prescribed output structure.

He also discusses token healing, which handles awkward boundaries between a supplied prompt and generated continuation. These mechanisms address generation mechanics; they do not independently verify the truth of the resulting content.
