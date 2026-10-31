---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-013
title: Score the conversation, not just each turn
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: How do you evaluate multi-turn conversations?'
sort_order: 14
language: en
---

A user may change the requested date and then add a hotel. Every reply can look reasonable while the final booking ignores one of those changes.

Group traces with a thread ID and evaluate the completed conversation against the accumulated request. For offline testing, store whole conversations or simulate users. The relevant question is whether the final outcome reflects all the turns, including corrections.
