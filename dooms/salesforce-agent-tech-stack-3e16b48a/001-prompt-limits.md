---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-001
title: Prompt limits
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: The naive design: one large prompt'
sort_order: 1
language: en
---

Putting every rule in one prompt leaves the model responsible for remembering and following all of them. Salesforce reported that its early Agentforce setup began dropping instructions beyond about eight.

That is the team’s reported observation, not a universal model limit. The architectural lesson is clearer: move rules that must hold into systems that can enforce them. Keep the model for the parts that need interpretation.
