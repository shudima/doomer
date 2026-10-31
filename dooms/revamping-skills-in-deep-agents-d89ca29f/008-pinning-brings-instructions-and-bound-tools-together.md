---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-007
title: Pinning brings instructions and bound tools together
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Pinned skills'
sort_order: 8
language: en
---

Pinned instructions are added once as a tagged message, with their bound tools available too. The agent can start the requested workflow on its first model call rather than spending one call loading instructions.

Earlier messages remain unchanged, helping preserve the prompt cache. A chat interface can display a compact skill label instead of its full instructions while the model receives the procedure it needs.
