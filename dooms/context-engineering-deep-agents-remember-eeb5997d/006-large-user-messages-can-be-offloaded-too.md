---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-005
title: Large user messages can be offloaded too
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Offloading: keeping it out the context window'
sort_order: 6
language: en
---

A pasted transcript can overwhelm context just as a verbose tool result can. Deep Agents applies a higher threshold—50,000 tokens in the article—to oversized human messages, storing them under /conversation_history/.

The distinction is between offloading and truncation. Offloading moves material out of the active window while preserving a way to read it later; truncation simply discards content that may become important.
