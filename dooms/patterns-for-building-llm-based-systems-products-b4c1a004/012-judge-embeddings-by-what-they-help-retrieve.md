---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-011
title: Judge embeddings by what they help retrieve
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — embeddings'
sort_order: 12
language: en
---

An embedding represents text as a fixed-size vector so related items can be retrieved by similarity. Yan stresses downstream usefulness rather than treating proximity in vector space as inherently meaningful.

Embeddings can also connect other modalities or user behaviors. For a **retrieval** product, the relevant question is whether the representation finds the evidence needed for the task, not merely whether it produces elegant-looking vectors.
