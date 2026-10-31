---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-005
title: Give the classifier criteria from your domain
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Step 3: build the router in the harness'
sort_order: 5
language: en
---

The Open SWE router combines a base instruction, plain-language criteria for each tier, and a classifier. It reads the initial request and selects the least expensive tier likely to succeed.

The criteria come from observed tasks and model guidance, not only a general leaderboard. Middleware swaps the chosen model while leaving the rest of the agent intact. The classifier later moved to Jev, which the team reports made classification almost fifty times faster.
