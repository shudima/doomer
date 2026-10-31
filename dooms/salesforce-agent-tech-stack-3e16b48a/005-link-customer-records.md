---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-004
title: Link customer records
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: 2. Unified profiles with Data 360'
sort_order: 5
language: en
---

A customer may appear in a website database, a CRM and a warehouse. **Data 360** links those records into one profile.

It reaches the sources, maps fields to a shared shape and applies configurable identity-matching rules. The article shows exact email matching and normalized phone numbers as examples. The unified profile links back to the underlying records; it does not rewrite them just to make the match.

![Data 360 ingests records, harmonizes fields and applies matching rules to build a unified profile.](images/source-13.webp)

*Source: ByteByteGo’s article. Tap to enlarge; the complete figure is preserved.*
