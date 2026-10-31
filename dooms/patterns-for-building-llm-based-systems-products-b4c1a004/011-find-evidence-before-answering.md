---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-053
title: Find evidence before answering
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — Why RAG?; added illustrative example'
sort_order: 11
language: en
---

**Illustrative example**

A user asks whether a purchased ticket can be refunded. Retrieve the policy for that ticket type, then answer from the relevant clause.

A model’s general knowledge may describe a different policy. Retrieval supplies the missing local evidence, while a grounding check tests whether the final answer actually follows it.
