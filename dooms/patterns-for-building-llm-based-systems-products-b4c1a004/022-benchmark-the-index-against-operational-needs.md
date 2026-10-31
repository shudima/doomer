---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-021
title: Benchmark the index against operational needs
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — ANN trade-offs'
sort_order: 22
language: en
---

An index should be compared on **recall** against exact neighbors, latency, throughput, memory requirements and the cost of adding new material. A fast query benchmark alone does not determine the right deployment choice.

Yan recommends defining requirements first. A system with frequent updates may value a different trade-off from a mostly static corpus, even when both use similar embedding models.
