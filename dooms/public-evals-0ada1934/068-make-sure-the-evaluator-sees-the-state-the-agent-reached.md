---
schema_version: 2
id: public-evals-0ada1934-068
title: Make sure the evaluator sees the state the agent reached
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — OSWorld 2.0
sort_order: 68
language: en
---

OSWorld’s behavioral analysis flagged possible state mismatches in **31% to 43%** of 108 trajectories. Resets, stale sessions, or unavailable files can make the grader observe something different from the agent’s final state.

These were possible mismatches, rather than confirmed defects in every flagged run. They still identify an important audit target. Check the environment’s reliability before attributing the full score gap to agent capability.
