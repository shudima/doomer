---
schema_version: 2
id: components-of-agent-memory-f0247d2b-006
title: Test an explanation before saving it as a rule
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Memory can be a prediction about what the future will need'
sort_order: 6
language: en
---

In Anthropic’s CL-Bench database task, each question began in a fresh session with access to the same memory directory. After answering, Claude received the correct solution. That feedback gave it a chance to learn across questions.

A useful loop is to notice the failure, propose a cause, test that cause, and save the rule with the evidence. A note full of plausible guesses can leave the next session doing the same investigation.
