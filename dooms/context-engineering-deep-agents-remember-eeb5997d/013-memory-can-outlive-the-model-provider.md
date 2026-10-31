---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-011
title: Memory can outlive the model provider
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Swap the model, keep the memory'
sort_order: 13
language: en
---

Because the agent’s memory is a plain file in storage controlled by the application, switching models need not discard what the agent learned. A different model can read the same formatting preference from the same backend next week.

Provider-independent storage separates durable knowledge from a particular inference service. The article frames that ownership as a practical requirement for maintaining continuity while changing the model underneath the harness.
