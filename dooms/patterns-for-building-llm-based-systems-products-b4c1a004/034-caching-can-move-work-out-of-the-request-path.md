---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-033
title: Caching can move work out of the request path
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Caching — Why caching?'
sort_order: 34
language: en
---

Reusing a previously computed response can reduce generation cost and replace seconds of inference with a faster lookup. Some experiences may require precomputation to meet their **latency** needs at all.

Yan describes both on-demand caching and preparing likely outputs ahead of time. The engineering question is whether the reused answer remains correct for the request being served.

![Overview of GPTCache](images/source-22.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
