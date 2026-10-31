---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-014
title: Fusion-in-Decoder combines separately encoded passages
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — Fusion-in-Decoder'
sort_order: 15
language: en
---

FiD pairs each retrieved passage with the question and encodes those pairs separately. Its decoder then attends across the encoded material to generate an answer.

Yan highlights the scaling benefit of avoiding joint encoder self-attention across every passage at once. Separating encoding from final evidence combination lets the system use many passages while retaining a way to integrate information during decoding.

![Overview of Fusion-in-Decoder](images/source-07.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
