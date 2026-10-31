---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-064
title: Follow one checked tool call
background_image: images/part-03.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 23-25; added illustrative example
sort_order: 11
language: en
---

**Illustrative example**

A support agent wants to look up an order. The harness checks that the order belongs to the user, runs the lookup and returns its result.

The model then decides whether it has enough information to answer. A failed lookup returns an error it can handle, rather than silently turning into an invented delivery date.

```mermaid
flowchart TD
  A[Assemble context] --> B[Model proposes action]
  B --> C{Allowed and valid?}
  C -->|Yes| D[Run tool]
  C -->|No| E[Return useful error]
  D --> F[Observe and save state]
  E --> F
  F --> B
```

*Added explanatory diagram.* [Editable diagram](diagrams/example-64.mmd) · [Portable image](images/example-64.svg)
