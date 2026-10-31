---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-015
title: Give a router observable criteria
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: Step 3: build the router in the harness; added illustrative example'
sort_order: 6
language: en
---

**Illustrative example**

Route a request to “rename a button” differently from “diagnose an intermittent data-loss bug.” Define features the classifier can recognize, such as scope, ambiguity and required investigation.

Use examples from real traffic to calibrate those criteria. The labels fast and performance need concrete meaning in your domain before the router can apply them consistently.
