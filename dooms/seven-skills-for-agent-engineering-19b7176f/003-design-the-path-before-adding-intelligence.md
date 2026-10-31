---
schema_version: 2
id: seven-skills-for-agent-engineering-19b7176f-014
title: Design the path before adding intelligence
background_image: images/layers.svg
source_url: https://www.youtube.com/watch?v=mtiOK2QG9Q0&list=WL&index=24
source_file: null
source_title: The 7 Skills You Need to Build AI Agents
source_type: video
source_locator: 00:02:39–00:03:59; added illustrative example
sort_order: 3
language: en
---

**Illustrative example**

A support agent reads the request, retrieves policy, proposes an action and checks whether approval is needed. Draw those steps and their failure paths first.

Now decide where a model adds useful interpretation. A visible structure makes missing permissions, recovery and evidence easier to notice than one large prompt that asks the model to handle everything.

```mermaid
flowchart TD
  A[Read request] --> B[Retrieve policy]
  B --> C[Propose action]
  C --> D{Approval required?}
  D -->|Yes| E{User approves?}
  D -->|No| F[Execute and verify]
  E -->|Yes| F
  E -->|No| G[Stop or revise]
```

*Added explanatory diagram.* [Editable diagram](diagrams/example-14.mmd) · [Portable image](images/example-14.svg)
