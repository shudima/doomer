---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-013
title: Keep the large report within reach
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Offloading: keeping it out the context window; added illustrative example'
sort_order: 5
language: en
---

**Illustrative example**

A search returns a long report. Save it to `research/report.md` and return a short summary plus the path.

When the writer needs the exact benchmark conditions, it reads that section. The full report remains available without being repeated in every model call. Offloading saves working space while preserving a route back to the evidence.
