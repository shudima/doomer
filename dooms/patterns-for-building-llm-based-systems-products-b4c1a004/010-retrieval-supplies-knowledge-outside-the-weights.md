---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-010
title: Retrieval supplies knowledge outside the weights
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — Why RAG?'
sort_order: 10
language: en
---

**Retrieval-augmented generation**, or RAG, gives the model relevant material from outside its weights. Search first, then use the retrieved material while generating the answer.

This can supply current or specialized knowledge. The result still depends on finding the right evidence and using it correctly. Evaluate retrieval and the final answer together, rather than assuming that adding a search step guarantees accuracy.

![Overview of Retrieval Augmented Generation](images/source-06.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
