---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-065
title: Retry without sending twice
background_image: images/part-03.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 24-25; added illustrative example
sort_order: 15
language: en
---

**Illustrative example**

A reminder tool sends a message, then the worker crashes before saving completion. On restart, the same step runs again.

Give the send operation a stable key such as `run-42:reminder-1`. The tool records that key with the send and returns the earlier result on a retry. Recovery resumes the task without producing a duplicate reminder.
