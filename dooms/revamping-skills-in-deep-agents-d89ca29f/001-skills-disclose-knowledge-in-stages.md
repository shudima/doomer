---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-001
title: Skills disclose knowledge in stages
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: How skills work'
sort_order: 1
language: en
---

Keep a short menu of skill names and descriptions in context. Read a skill’s full instructions only when the task needs it. Load scripts and references after that.

This staged approach lets an agent use a large library without reading all of it on every call. The article adds tools to that pattern: a skill can bring in the capabilities needed to follow its instructions.

![Only a skill's name and description are always in context. The agent reads the instructions on demand, and loads scripts, references, and assets only when needed.](images/source-02.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
