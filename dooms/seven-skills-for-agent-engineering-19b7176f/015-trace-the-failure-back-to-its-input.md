---
schema_version: 2
id: seven-skills-for-agent-engineering-19b7176f-015
title: Trace the failure back to its input
background_image: images/flow.svg
source_url: https://www.youtube.com/watch?v=mtiOK2QG9Q0&list=WL&index=24
source_file: null
source_title: The 7 Skills You Need to Build AI Agents
source_type: video
source_locator: 00:13:33–00:14:24; added illustrative example
sort_order: 15
language: en
---

**Illustrative example**

A search answer cites the wrong customer. Follow the run backward: final response, selected record, tool arguments and original request.

The tool may have accepted an ambiguous name without requiring a stable ID. Fixing that contract can prevent the same error across many prompts. A trace helps locate the cause rather than merely rewriting the last answer.
