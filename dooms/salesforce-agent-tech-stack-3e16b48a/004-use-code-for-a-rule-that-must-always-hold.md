---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-010
title: Use code for a rule that must always hold
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: 1. Deterministic instructions with Agent Script; added illustrative example'
sort_order: 4
language: en
---

**Illustrative example**

A hypothetical support agent must confirm an order’s owner before changing it. Put that check in the execution path, before the update runs.

The model can decide which relevant order to discuss and explain the result. It cannot bypass ownership validation by forgetting a prompt instruction. This illustrates the article’s separation of deterministic steps and reasoning.
