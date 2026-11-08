---
schema_version: 2
id: components-of-agent-memory-f0247d2b-013
title: A narrow rule can limit what memory captures
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Steering Claude to write memory · Figure 5'
sort_order: 13
language: en
---

On the database task, telling Opus 5 and Opus 4.7 that a memory folder was available helped them. Telling them to save only failures reduced much of that benefit. Opus 5’s memory gain dropped by **0.234** and Opus 4.7’s by **0.150** mean reward.

Rules about what to keep shape what future sessions can learn. A successful method or a verified fact can deserve a note too.

![The right panel shows the drop in memory gains under a failure-only rule. The left panel shows how more specific guidance helped Sonnet 4.6.](images/figure-05.webp)

*Figure 5 from Anthropic. Illustration by Monika Tuchowska.*
