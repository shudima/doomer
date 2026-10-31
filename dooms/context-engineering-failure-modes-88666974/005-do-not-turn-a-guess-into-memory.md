---
schema_version: 2
id: context-engineering-failure-modes-88666974-013
title: Do not turn a guess into memory
background_image: images/shield.svg
source_url: https://www.youtube.com/watch?v=BwXremQ-i6I&list=WL&index=4
source_file: null
source_title: 'Context Engineering for AI Agents: 4 Failure Modes to Avoid'
source_type: video
source_locator: 00:04:34–00:05:17; added illustrative example
sort_order: 5
language: en
---

**Illustrative example**

An agent guesses that a service uses port 9000 and saves the guess as a project fact. Later runs keep trying the wrong port.

Check the configuration before saving the note. If the answer remains uncertain, record that uncertainty and a way to verify it. Persistent memory should improve the next run rather than preserve the first mistake.
