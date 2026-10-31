---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-002
title: Platform layers
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: How Agentforce is built'
sort_order: 2
language: en
---

Salesforce separates the platform into four layers:

- **Surfaces:** interfaces such as Slack and Claude.
- **Agentforce:** where agents are defined and run.
- **Customer 360:** business applications and actions.
- **Data 360:** a consistent view of company records.

Each layer has a different job. The model can reason over prepared context while other systems handle data, actions and enforceable rules.

![Salesforce’s surface, agent, application and data layers connect user interfaces to business actions and records.](images/source-05.webp)

*Source: ByteByteGo’s article. Tap to enlarge; the complete figure is preserved.*
