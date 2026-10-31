---
schema_version: 2
id: revamping-skills-in-deep-agents-d89ca29f-010
title: Scale knowledge without loading everything at once
background_image: images/background.svg
source_url: https://www.langchain.com/blog/revamping-skills-in-deep-agents
source_file: null
source_title: Revamping Skills in Deep Agents
source_type: article
source_locator: 'Section: Get started'
sort_order: 12
language: en
---

The revamped design addresses three different needs: bind capabilities to their instructions, preload procedures explicitly selected by the user, and refresh a library without restarting the conversation.

The article presents these as extensions of **progressive disclosure**, not a reason to load all enterprise knowledge up front. Skills remain portable instruction packages, while the harness decides how their tools, activation, and lifecycle work during a run.
