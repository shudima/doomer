---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-004
title: Deferred tools can preserve the cached prefix
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Binding tools to skills'
sort_order: 5
language: en
---

Newer Anthropic and OpenAI models can accept tools disclosed during a conversation. For those models, Deep Agents adds the bound tools after the skill is read without changing the earlier cached prefix.

Other models still receive additions through the request’s tool list, which can invalidate the cache. The caching benefit depends on provider and model support; deferred disclosure is not automatically cache-preserving everywhere.

![Reading call-transcripts unlocks search_calls and get_transcript. They arrive in a new system message, so the cached prefix above it stays unchanged.](images/source-06.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
