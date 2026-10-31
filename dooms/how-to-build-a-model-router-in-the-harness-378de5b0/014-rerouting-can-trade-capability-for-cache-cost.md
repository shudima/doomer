---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-012
title: Rerouting can trade capability for cache cost
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: What''s next'
sort_order: 14
language: en
---

A thread that changes complexity may justify a different model. Switching also discards the existing model’s prompt cache, forcing the next model to read history at full price.

The article notes that this penalty may matter less for asynchronous threads whose caches have already expired between human turns. Mid-thread routing needs both a capability signal and an accounting of the transition cost.
