---
schema_version: 2
id: public-evals-0ada1934-020
title: Give the grader known-good and known-bad work
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Hot takes: How we’re thinking about evals wrongly'
sort_order: 20
language: en
---

A reference solution helps establish that a task is solvable. A do-nothing run should fail. Adversarial attempts can reveal shortcuts that earn a score without completing the work.

Terminal Bench uses these checks, yet later reviewers still found cheating paths. Keep auditing successful trajectories as well as failures. A grader needs evidence that it accepts valid alternatives and rejects plausible wrong outputs.
