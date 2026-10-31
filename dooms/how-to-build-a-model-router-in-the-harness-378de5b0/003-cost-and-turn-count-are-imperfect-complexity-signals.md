---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-003
title: Cost and turn count are imperfect complexity signals
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Step 1: understand the tasks'
sort_order: 3
language: en
---

The team used thread cost and invocation counts to explore task difficulty. Feature investigations tended to be longer and more expensive, while testing and release procedures were often shorter.

More invocations can indicate either a hard task or a model needing repeated follow-ups. Treat these observations as evidence for a routing hypothesis, rather than confusing historical effort with an objective measure of inherent difficulty.
