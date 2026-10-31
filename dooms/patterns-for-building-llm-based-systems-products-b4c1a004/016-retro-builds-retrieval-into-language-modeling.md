---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-015
title: RETRO builds retrieval into language modeling
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — RETRO'
sort_order: 16
language: en
---

RETRO retrieves neighboring text chunks during model training and generation, using chunk-level attention to incorporate external context. This goes beyond adding documents only at the end of an existing inference pipeline.

Yan also reviews adapting pretrained models with **retrieval**-related components while freezing most weights. The work illustrates how external memory and learned generation can be combined at different depths of the architecture.
