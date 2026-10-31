---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-033
title: The agent acts for a specific user
background_image: images/part-05.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 45-46
sort_order: 37
language: en
---

A shared service account makes every request as powerful as the account itself. That creates a confused-deputy risk and obscures who initiated an action.

Give the agent its own identity and delegate narrower user-scoped access. Token exchange can represent the user as the subject and the agent as the actor. Downstream services can then enforce both the person's permissions and additional restrictions on what the agent may do on that person's behalf.
