---
schema_version: 2
id: public-evals-0ada1934-026
title: DeepSWE builds fresh software tasks
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — DeepSWE
sort_order: 26
language: en
---

DeepSWE’s engineers wrote 113 long-horizon tasks from scratch across 91 open-source repositories, rather than mining completed pull requests. Review checked realism, clean environments, clear instructions, and acceptance of reasonable implementations.

Every model uses mini-swe-agent with the same bash tool and system prompt. Tests check outputs, APIs, and regressions. Version 1.1 moved grading into a fresh container. The headline result is single-attempt all-pass performance.

At its May 2026 launch, the top score on v1 was 70%.
