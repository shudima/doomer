---
schema_version: 2
id: public-evals-0ada1934-034
title: Inspect the verifier before blaming a low science score
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — Terminal Bench Science
sort_order: 34
language: en
---

The article reports task-fix issues across much of Terminal Bench Science. Examples included a verifier rejecting correct predictions because their rows were reordered and a reference labeling two samples incorrectly.

Those reports give concrete reasons to inspect an apparent failure. A deliberately hard task and a defective check can both produce zero. They require different responses when improving the agent or interpreting its capability.
