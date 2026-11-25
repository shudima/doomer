---
schema_version: 2
id: public-evals-0ada1934-043
title: AutomationBench makes the agent discover business APIs
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — AutomationBench
sort_order: 43
language: en
---

AutomationBench includes 600 public workflows across six business domains and 47 simulated apps. A separate, harder private set drives the leaderboard.

Models get two tools. **Search** finds API schemas. **Execute** calls an endpoint. A run ends when the model stops or reaches 50 steps. All-pass checks inspect final records and messages, including negative checks for actions that should never have happened.

![The agent searches API schemas, executes calls, and changes simulated application state. Deterministic assertions grade the final state.](images/source-04.webp)

*Source figure reproduced in Eugene Yan’s article. Credits and original captions are preserved.*
