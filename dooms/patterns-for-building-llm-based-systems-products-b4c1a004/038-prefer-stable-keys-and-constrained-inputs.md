---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-036
title: Prefer stable keys and constrained inputs
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Caching — How to apply caching?'
sort_order: 38
language: en
---

Item identifiers, pairs of identifiers and structured options can provide clearer reuse boundaries than unrestricted semantic matching. Yan gives examples such as review summaries and comparisons of known products.

Preparing verified outputs offline can further reduce serving **latency**. These approaches trade some flexibility for more dependable reuse, making cache correctness easier to reason about than a broadly similar natural-language request.
