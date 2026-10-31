---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-007
title: Separate agent permissions
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: 4. Permission management with Agent Identity'
sort_order: 9
language: en
---

Give the agent its own identity and permissions, alongside the user’s identity. An operation must fit both sets of permissions and the applicable policies.

The article describes checks using separate user and agent tokens. This makes it possible to allow a person to perform an action while withholding the same action from an agent acting for them. The model’s instructions do not grant access.

![An operation checks the user token, agent token and policies before permitting an update.](images/source-19.webp)

*Source: ByteByteGo’s article. Tap to enlarge; the complete figure is preserved.*
