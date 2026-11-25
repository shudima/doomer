---
schema_version: 2
id: public-evals-0ada1934-022
title: Terminal Bench grades a working container
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — Terminal Bench
sort_order: 22
language: en
---

Terminal Bench evaluates command-line work across software, science, operations, and other domains. The article distinguishes its **2.0 paper dataset** from **4.1**, the November 2026 release with 66 tasks.

Agents work in containers with internet access. The neutral Terminus 2 harness offers a terminal. After the agent stops, grading tests inspect the final container state. Every test must pass for the task to earn credit.

![A Terminal Bench task supplies an instruction and container. After the agent runs, hidden tests are copied in and executed.](images/source-02.webp)

*Source figure reproduced in Eugene Yan’s article. Credits and original captions are preserved.*
