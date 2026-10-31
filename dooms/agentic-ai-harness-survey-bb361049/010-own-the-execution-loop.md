---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-009
title: Own the execution loop
background_image: images/part-03.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 23-25
sort_order: 10
language: en
---

The harness runs the agent’s loop:

1. Assemble the information the model needs.
2. Ask the model what to do next.
3. Check requested tools, arguments and permissions.
4. Run allowed actions and return their results.
5. Save progress and check the remaining budget.

Repeat until the task is done or a limit is reached. A final-looking answer still needs verification before it is ready for the user.
