---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-003
title: Declare the tools in the skill metadata
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Binding tools to skills'
sort_order: 4
language: en
---

The article uses metadata.include_tools in the skill frontmatter to identify bound tools, then passes those tools to SkillsMiddleware rather than directly exposing them on the agent.

In its sales example, reading the call-transcripts skill unlocks call search and transcript **retrieval** together. The instructions and capabilities become available as one unit, instead of relying on the model to discover their relationship independently.
