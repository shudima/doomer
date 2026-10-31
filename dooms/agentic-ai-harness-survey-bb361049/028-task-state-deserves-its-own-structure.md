---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-025
title: Task state deserves its own structure
background_image: images/part-04.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 38-39
sort_order: 28
language: en
---

Short-term memory includes conversation history, explicit task state and checkpoints. A shortlist, current plan or pending approval should not exist only as something the model must reconstruct from old messages.

Store those items as structured data and render the relevant state into context. This makes long tasks easier to resume and inspect. The model still interprets requests, but the harness maintains a dependable record of what has already happened and what is waiting.
