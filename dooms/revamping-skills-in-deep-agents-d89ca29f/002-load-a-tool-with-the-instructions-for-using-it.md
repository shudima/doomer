---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-002
title: Load a tool with the instructions for using it
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Binding tools to skills'
sort_order: 2
language: en
---

Previously, skill instructions and tool discovery were separate: an agent might find a tool without reading its procedure, or read a skill and still need another search. Deep Agents now binds tools to skills.

A bound tool remains unavailable until the agent reads the associated skill. This keeps schemas out of context and ensures the procedure is present before that tool becomes callable.
