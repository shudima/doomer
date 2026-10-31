---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-008
title: Long threads need an explicit refresh mechanism
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Reloading skills mid-thread'
sort_order: 9
language: en
---

Deep Agents stores skill metadata in agent state so later turns normally reuse the same library discovered at thread startup. Setting skills_metadata to None invalidates that snapshot.

On the next run, the middleware rescans the sources and discovers additions, edits, or deletions. The application decides when to refresh, avoiding a requirement to discard a long-running thread whenever someone updates a skill.

![Setting skills_metadata to None makes the next run rescan the skill library and pick up a skill added since the last run.](images/source-13.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
