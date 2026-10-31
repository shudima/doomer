---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-004
title: Offload large tool results before they enter
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Offloading: keeping it out the context window'
sort_order: 4
language: en
---

A large tool result can fill the context window before the agent has used it. Save the full result to a file and return a short preview with its path.

The agent can read the relevant part later. This is **offloading**: the evidence stays available without appearing in every following model call. The article applies this before oversized results enter the conversation.
