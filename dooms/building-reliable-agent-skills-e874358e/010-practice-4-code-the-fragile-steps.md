---
schema_version: 2
id: building-reliable-agent-skills-e874358e-009
title: 'Practice 4: code the fragile steps'
background_image: images/flow.svg
source_url: https://www.youtube.com/watch?v=qYNs80FKIVc&list=WL&index=23
source_file: null
source_title: 5 Best Practices for Building AI Agent Skills
source_type: video
source_locator: 00:08:00–00:08:57
sort_order: 10
language: en
---

A loosely constrained step can allow several successful approaches. A fragile step that must behave consistently deserves a more prescriptive implementation.

The presenters recommend deterministic scripts for those operations. Put the code in the skill’s scripts directory and tell the agent to run it. That keeps the model from reinventing the same delicate logic each time it follows the procedure.
