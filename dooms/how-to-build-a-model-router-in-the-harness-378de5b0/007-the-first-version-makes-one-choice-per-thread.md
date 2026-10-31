---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-006
title: The first version makes one choice per thread
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Step 3: build the router in the harness'
sort_order: 7
language: en
---

Open SWE’s router selects a model from the first human message and uses it for the whole thread. This keeps the implementation simple but cannot adapt when an initial question evolves into a more demanding change.

The article treats mid-thread rerouting as future work. A successful first implementation does not establish that task complexity stays fixed or that one initial classification is always sufficient.
