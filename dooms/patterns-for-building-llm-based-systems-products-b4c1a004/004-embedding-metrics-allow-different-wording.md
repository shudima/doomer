---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-004
title: Embedding metrics allow different wording
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Evals — BERTScore and MoverScore'
sort_order: 4
language: en
---

BERTScore compares contextual token representations, allowing semantic matches that exact word overlap misses. MoverScore also uses embeddings, modeling the effort of aligning the two texts with a more flexible matching scheme.

Yan presents them as alternatives when paraphrases and synonyms matter. They still compare against reference text, so their applicability depends on whether that comparison captures what the task actually requires.
