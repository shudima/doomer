---
schema_version: 2
id: ai-era-sdlc-survey-6223bf11-032
title: Make evals part of release and operation
background_image: images/quality.svg
source_url: null
source_file: source/original.pdf
source_title: The Software Development Life Cycle in the AI Era
source_type: pdf
source_locator: 'Page 20: Evaluations, release gates and pitfalls'
sort_order: 36
language: en
---

The survey recommends blocking releases on evaluation regressions and using the same evaluators in production to detect drift. Incidents and negative feedback should create new cases, closing the learning loop.

Version prompts, models, tools and datasets together so experiments can be reproduced against a baseline. Watch for overfitting and saturated test sets. Audit the harness for incomplete runs, bad metrics and judge parsing failures before trusting its numbers. Evaluations need operational consequences, not just a report.
