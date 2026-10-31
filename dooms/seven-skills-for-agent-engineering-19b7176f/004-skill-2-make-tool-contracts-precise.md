---
schema_version: 2
id: seven-skills-for-agent-engineering-19b7176f-003
title: 'Skill 2: make tool contracts precise'
background_image: images/decision.svg
source_url: https://www.youtube.com/watch?v=mtiOK2QG9Q0&list=WL&index=24
source_file: null
source_title: The 7 Skills You Need to Build AI Agents
source_type: video
source_locator: 00:03:59–00:05:14
sort_order: 4
language: en
---

A tool contract tells the agent which inputs it accepts and what output to expect. Vague contracts leave room for guesses.

The example is a user lookup: saying only that a user ID is a string could invite a name or an arbitrary value. A required field with an explicit pattern and example gives the model a much clearer target. The **precision** belongs in the schema.
