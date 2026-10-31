---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-011
title: Stop honestly when a budget ends
background_image: images/part-03.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 24-25
sort_order: 13
language: en
---

The loop needs hard limits on steps, tokens or money, elapsed time and repeated calls. Code must enforce those limits even if the model ignores them.

When a limit is reached, return an honest partial result. A recruiter needs to know that only 40 of 120 applicants were reviewed before judging the shortlist. Showing the remaining budget can help the model allocate effort, but the harness remains responsible for stopping execution.
