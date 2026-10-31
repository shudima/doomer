---
schema_version: 2
id: context-engineering-deep-agents-remember-eeb5997d-006
title: Summarize the gradual climb
background_image: images/background.svg
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
source_file: null
source_title: 'Context Engineering: How Deep Agents Remember'
source_type: article
source_locator: 'Section: Summarization: compacting what''s already there'
sort_order: 7
language: en
---

Offloading handles large individual results. Small messages can still accumulate into a long conversation.

The article uses summarization to reduce that gradual growth when context approaches a threshold. Keep the task, decisions and important references in the summary. Saving the earlier conversation makes it possible to recover details that the summary leaves out.

![Offloading stops the small spikes, while summarization “resets” the overall climb](images/source-04.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
