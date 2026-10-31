---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-013
title: RAG can combine evidence at different levels
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — RAG-Sequence and RAG-Token'
sort_order: 14
language: en
---

The original RAG work combines learned model parameters with an external **retrieval** index. Yan contrasts approaches that mix document-conditioned probabilities across a complete answer or separately for each generated token.

The distinction concerns how retrieved evidence contributes to generation. It illustrates that retrieval augmentation is a family of architectures, not simply one universal instruction to paste search results into a prompt.
