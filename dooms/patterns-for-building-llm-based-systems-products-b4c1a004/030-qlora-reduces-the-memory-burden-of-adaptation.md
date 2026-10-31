---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-029
title: QLoRA reduces the memory burden of adaptation
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Fine-tuning — QLoRA'
sort_order: 30
language: en
---

QLoRA combines low-rank adaptation with a quantized base model. The article describes its quantization techniques and paged optimizers as ways to make larger-model fine-tuning more practical within limited accelerator memory.

The important distinction is between adapting a compact set of parameters and storing every base weight at full **precision**. The reported savings are research results for specific setups, not a universal hardware guarantee.

![Overview of QLoRA](images/source-21.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
