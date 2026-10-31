---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-017
title: HyDE searches with a hypothetical document
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Retrieval-Augmented Generation — HyDE'
sort_order: 18
language: en
---

**HyDE** searches using a hypothetical document. The model first drafts what a relevant answer or passage might look like, then embeds that text to retrieve real documents.

The draft is a search aid, not verified evidence. Ground the final answer in the retrieved material. The article presents this as one way to bridge the wording gap between a user’s short question and useful source passages.

![Overview of HyDE](images/source-12.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
