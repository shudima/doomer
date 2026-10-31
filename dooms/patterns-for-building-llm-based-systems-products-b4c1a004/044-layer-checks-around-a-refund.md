---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-055
title: Layer checks around a refund
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Guardrails — How to apply guardrails?; added illustrative example'
sort_order: 44
language: en
---

**Illustrative example**

For a hypothetical refund assistant, parse the model’s request into a fixed schema, check the order owner, enforce the refund limit and verify the saved transaction.

Each layer checks a different requirement. A polite answer cannot replace ownership validation, and a valid JSON object cannot prove that the refund was applied correctly.
