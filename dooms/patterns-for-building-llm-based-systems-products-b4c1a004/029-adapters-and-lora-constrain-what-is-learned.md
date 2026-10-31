---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-028
title: Adapters and LoRA constrain what is learned
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Fine-tuning — adapters and LoRA'
sort_order: 29
language: en
---

Fine-tuning every weight can be expensive. **LoRA** keeps the original weights fixed and learns a smaller set of low-rank updates.

These updates adapt the model while reducing the amount that must be trained. The article also discusses adapters, which add small trainable modules. Both approaches limit what changes, though they do so in different ways.

![Overview of LoRA](images/source-20.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
