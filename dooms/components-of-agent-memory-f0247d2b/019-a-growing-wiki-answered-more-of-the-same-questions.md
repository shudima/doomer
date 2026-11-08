---
schema_version: 2
id: components-of-agent-memory-f0247d2b-019
title: A growing wiki answered more of the same questions
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Dreaming can build new memory representations · Figure 10'
sort_order: 19
language: en
---

Anthropic gave Opus 5 about **350,000 Stainless files**, roughly **420 million tokens**, and graded answers to 25 questions. The agents built a linked wiki across repeated background sessions.

Using the wiki alone, Claude met **13% of graded criteria after two build sessions** and **48% after 128**. The chart’s horizontal axis uses a budget of one million tokens per session. It shows allocated budget, with actual spending left unmeasured there.

![A chart shows wiki-only scores rising from 13% to 48% as the wiki grows. The adjacent graphs show the linked pages after 2 and 128 sessions.](images/figure-10.webp)

*Figure 10 from Anthropic. Illustration by Monika Tuchowska.*
