---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-010
title: Save durable preferences as files
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Long-term memory: persist across conversations'
sort_order: 12
language: en
---

A preference such as using bullets in report summaries should not require repeating every week. Deep Agents represents long-term memory as a Markdown file read at startup and injected into model calls.

When the agent learns something worth retaining, it updates that file. This differs from retaining every conversation detail: the durable memory holds selected knowledge useful across future runs.
