---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-008
title: Put procedure in skills and hard rules in tools
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: How to fold subagents into the main agent loop'
sort_order: 9
language: en
---

Put the procedure in a skill and the non-negotiable rules in tools.

A skill can explain how to prepare an analysis or when to call a tool. The tool should enforce required fields, permissions and prerequisites. This lets the model adapt its approach while the system keeps exact requirements reliable. Moving instructions into one agent does not remove the need for those controls.
