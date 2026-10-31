---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-003
title: Reference overlap measures only part of quality
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Evals — BLEU and ROUGE'
sort_order: 3
language: en
---

BLEU emphasizes matching generated word sequences against references, with a penalty discouraging excessively short outputs. ROUGE emphasizes coverage of reference content, including variants based on subsequences or skip-bigrams.

Yan explains why these inexpensive metrics remain useful in suitable tasks, while warning that lexical overlap is not the same as usefulness, fluency or factual support in a more open-ended response.
