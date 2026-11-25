---
schema_version: 2
id: public-evals-0ada1934-002
title: An evaluation task has four parts
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Patterns: How eval tasks are built and maintained'
sort_order: 2
language: en
---

To understand one task, identify its components.

- **Instruction** explains the requested work.
- **Environment** supplies files, tools, and services.
- **Grader** decides whether the result passes.
- **Reference**, when provided, supplies an expert solution or baseline.

A failure can come from a mismatch between these parts. A fair grader needs to accept the valid outcomes the instruction allows.

![An instruction sends the agent into a workspace. A grader checks its output or final state, with an optional expert reference.](images/source-01.webp)

*Source figure reproduced in Eugene Yan’s article. Credits and original captions are preserved.*
