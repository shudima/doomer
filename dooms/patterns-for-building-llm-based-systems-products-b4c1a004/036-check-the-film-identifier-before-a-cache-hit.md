---
schema_version: 2
id: patterns-for-building-llm-based-systems-products-b4c1a004-054
title: Check the film identifier before a cache hit
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/llm-patterns/
source_file: null
source_title: Patterns for Building LLM-based Systems & Products
source_type: article
source_locator: 'Section: Caching — semantic-cache risks; added illustrative example'
sort_order: 36
language: en
---

**Illustrative example**

A reader asks for the plot of Film 2. The cache finds a similar request about Film 3.

| Requested film | Cached film | Reuse? |
| --- | --- | --- |
| Film 2 | Film 2 | Check freshness and other inputs |
| Film 2 | Film 3 | No |

Semantic similarity helps find a candidate. The exact film identity decides whether that answer can fit.

```mermaid
flowchart TD
  A[Request for Film 2] --> B[Find similar cached request]
  B --> C{Same film and valid inputs?}
  C -->|Yes| D[Check freshness and reuse]
  C -->|No| E[Generate a new answer]
```

*Added explanatory diagram.* [Editable diagram](diagrams/example-54.mmd) · [Portable image](images/example-54.svg)
