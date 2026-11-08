---
schema_version: 2
id: components-of-agent-memory-f0247d2b-018
title: Build a map across separate notes
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Dreaming can build new memory representations · Figure 9'
sort_order: 18
language: en
---

A wiki gathers related details into pages and links those pages to one another. An agent can start from a subject it recognizes and follow the links to adjacent facts, decisions, or evidence.

Anthropic used successive sessions to add pages, merge duplicates, prune old material, and check claims against source files. A shared log let each session pick up where the previous one stopped.

![A background pass combines transcripts and notes into linked pages that future sessions can navigate.](images/figure-09.webp)

*Figure 9 from Anthropic. Illustration by Monika Tuchowska.*
