---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-001
title: Choose the model that fits the task
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Introduction'
sort_order: 1
language: en
---

Use a model that is capable enough for the request without paying for more capability than the task needs. A **router** makes that choice.

LangChain describes building one inside its agent harness. It starts with real traffic, defines model tiers and tests whether cheaper routing preserves useful outcomes. Cost savings matter only alongside the quality of completed work.
