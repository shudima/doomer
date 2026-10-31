---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-057
title: Roll out in stages and learn
background_image: images/part-07.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 64-65
sort_order: 62
language: en
---

After offline evaluation, shadow execution can compare a candidate on real inputs without exposing its output to users. A canary then serves a small traffic share before wider rollout.

Compare task outcomes, feedback, guardrail trips, tool errors, approvals, cost and **latency** at each stage. Use feature flags and defined rollback thresholds. Rollback must restore prompts and configuration along with code. Feed new production failures into the suites so release decisions keep learning from reality.
