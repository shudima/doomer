---
schema_version: 2
id: public-evals-0ada1934-023
title: Ask whether the task is specific, solvable, and honest
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — Terminal Bench
sort_order: 23
language: en
---

Terminal Bench combines human review with three automated checks.

1. **Specificity** checks alignment between the prompt and tests.
2. **Solvability** confirms the reference works and doing nothing fails.
3. **Integrity** looks for ways to cheat, such as reading future repository commits.

The checks examine different risks. A task can have a working reference while still rejecting another valid solution or exposing a shortcut.
