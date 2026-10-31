---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-017
title: Retrieve reference facts when they are useful
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Knowledge bases'
sort_order: 18
language: en
---

Keep reference facts available to retrieve when they are useful. Policies, metric definitions and product specifications can live in knowledge bases or skill reference files.

The agent can fetch the relevant detail for the current task. Pasting every reference into every prompt wastes attention. Separate instructions about **how to work** from facts needed for one particular step.
