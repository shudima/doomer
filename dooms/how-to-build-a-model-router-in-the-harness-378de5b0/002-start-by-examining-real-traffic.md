---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-002
title: Start by examining real traffic
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Step 1: understand the tasks'
sort_order: 2
language: en
---

Before building Open SWE’s router, the team examined a week of interactive threads using LangSmith traces and an LLM task classifier. New features accounted for 22%, bug fixes 17%, and test or no-op runs 16%.

These categories were heuristic labels based on titles and metadata. They revealed varied workloads rather than proving that one type of request always needs a particular model.
