---
schema_version: 2
id: using-local-coding-agents-9b152c44-025
title: Claude Code can connect through Ollama
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 10. Claude Code Setup'
sort_order: 27
language: en
---

Ollama provides a Claude Code integration through `ollama launch claude`. The article also notes `ollama launch codex`, although Raschka prefers a separate Codex profile for visibility and control.

Claude Code is his least favored local option because its proprietary codebase limits inspection of data logging. Using a local model changes the inference endpoint; it does not make the surrounding proprietary harness open source or establish that all of its activity stays local.

![Figure 29](images/source-29.webp)

*Source: Sebastian Raschka’s article; paper credits remain in the original diagram. Tap to enlarge; the complete figure is preserved.*
