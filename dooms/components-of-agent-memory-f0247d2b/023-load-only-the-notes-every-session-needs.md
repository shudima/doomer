---
schema_version: 2
id: components-of-agent-memory-f0247d2b-023
title: Load only the notes every session needs
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Dreaming can promote notes up the memory hierarchy · Figure
  13'
sort_order: 23
language: en
---

Some information is important before an agent knows to look for it. The harness can load selected notes at the start of every session. This is **context injection**.

Those notes consume tokens every time, and a mistaken entry can steer every new session. Long instructions can also be harder to follow. Keep the startup layer small and move details into files that the agent can open when needed.

![Selected notes and transcript findings move into a small layer that the harness loads at session start.](images/figure-13.webp)

*Figure 13 from Anthropic. Illustration by Monika Tuchowska.*
