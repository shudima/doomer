---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-027
title: Soft prompts and prefixes update a small addition
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Fine-tuning — soft prompt and prefix tuning'
sort_order: 28
language: en
---

Soft prompt tuning learns input-embedding parameters instead of relying only on discrete words. Prefix tuning adds learned parameters to transformer hidden states while leaving the original model weights frozen.

Yan describes these as parameter-efficient alternatives to updating the entire model. Some reviewed experiments obtain competitive performance with far fewer trainable parameters, including settings where limiting adaptation helps reduce overfitting.
