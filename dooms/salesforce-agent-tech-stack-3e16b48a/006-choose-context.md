---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-005
title: Choose context
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: 3. Relevant context with Agent Context Engine'
sort_order: 6
language: en
---

An agent usually needs only part of a customer’s information for one question. Agent Context Engine selects that part before the model reasons.

The article describes stages for resolving the request, planning, reconciling evidence, applying governance, compiling context and learning from the interaction. In its demonstration, the context for one question fell from 124,000 tokens to 9,000. That is a reported demonstration, rather than a guaranteed saving for every request.
