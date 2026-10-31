---
schema_version: 2
id: using-local-coding-agents-9b152c44-035
title: Separate local inference from network activity
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 6. Agent Code Base Audit; added illustrative example'
sort_order: 15
language: en
---

**Illustrative example**

A model runs on your laptop, but the coding harness still sends telemetry or calls a remote service. The model’s location alone does not make the entire workflow offline.

Inspect the harness settings and observe the network behavior needed for your task. Make privacy expectations explicit before choosing the complete stack.
