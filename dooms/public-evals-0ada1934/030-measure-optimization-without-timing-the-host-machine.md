---
schema_version: 2
id: public-evals-0ada1934-030
title: Measure optimization without timing the host machine
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — FrontierSWE
sort_order: 30
language: en
---

A speed result can vary because the host machine changes. FrontierSWE v2 grades performance work using weighted instruction counts to make measurement deterministic across machines.

It also grades in a fresh container, limits the agent’s access, mutates public tests to catch hardcoded answers, and reviews trajectories for cheating. These choices aim to make the observed gain come from the submitted work.
