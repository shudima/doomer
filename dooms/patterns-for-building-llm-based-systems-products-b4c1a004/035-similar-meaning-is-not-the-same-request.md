---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-034
title: Similar meaning is not the same request
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Caching — semantic-cache risks'
sort_order: 35
language: en
---

Two requests can sound similar and still need different answers. A semantic cache must check whether the stored response fits the actual request.

Yan uses different film installments to show the risk: a summary of one film cannot answer a question about another. Fast retrieval of a similar response is useful only when reusing that response is correct.
