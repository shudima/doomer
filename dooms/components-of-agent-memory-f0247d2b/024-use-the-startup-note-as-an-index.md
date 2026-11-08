---
schema_version: 2
id: components-of-agent-memory-f0247d2b-024
title: Use the startup note as an index
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Dreaming can promote notes up the memory hierarchy'
sort_order: 24
language: en
---

The article describes Claude Code’s auto memory loading the first **200 lines or 25 KB** of `MEMORY.md`. Claude maintains that file during the session. Its opening acts as an index to other notes.

**Illustrative example.** A support agent’s startup note can point to the current refund policy and tell the agent when to open it. The full policy can live in a separate file, ready for requests that actually need it.
