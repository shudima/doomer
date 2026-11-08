---
schema_version: 2
id: components-of-agent-memory-f0247d2b-002
title: Give memory four places to live
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Introduction · Figure 1'
sort_order: 2
language: en
---

Each layer answers a different question.

- **Transcripts** record what happened and can be searched later.
- **Notes** save observations that seem useful.
- **Linked pages** organize knowledge around topics.
- **Injected context** loads a small set of information at the start of every session.

The lower layers can hold more detail. The top layer takes up space in every new session.

![Four layers sit between sessions. A background pass can organize the transcript, notes, linked representations, and context loaded up front.](images/figure-01.webp)

*Figure 1 from Anthropic. Illustration by Monika Tuchowska.*
