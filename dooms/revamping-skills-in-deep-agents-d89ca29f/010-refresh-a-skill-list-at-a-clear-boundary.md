---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-012
title: Refresh a skill list at a clear boundary
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Reloading skills mid-thread; added illustrative example'
sort_order: 10
language: en
---

**Illustrative example**

A new skill is added while a long thread is idle. The agent’s existing skill list still reflects the earlier scan.

Refresh that metadata before the next relevant run so the new procedure can be discovered. Do it deliberately: rescanning every turn can add overhead and disturb caching without helping the current task.
