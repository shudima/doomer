---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-020
title: Separate by useful context
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Using an agent loop with progressive disclosure; added illustrative example'
sort_order: 7
language: en
---

**Illustrative example**

A coding agent knows why it changed a function. Let it write the matching tests while that reasoning is available.

A separate verifier can run the suite and report failures without needing every design detail. The boundary has a clear purpose: independent execution evidence. Splitting feature writing and test writing into isolated specialists could instead force the same context to be explained twice.
