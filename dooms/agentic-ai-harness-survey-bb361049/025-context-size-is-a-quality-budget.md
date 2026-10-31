---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-022
title: Context size is a quality budget
background_image: images/part-04.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 35-37
sort_order: 25
language: en
---

A large **context window** does not guarantee that the model can use everything inside it. The survey describes context rot: accuracy can deteriorate well before the hard limit.

Keep high-signal material and measure quality as context grows. Stable instructions and tool definitions at the beginning help prompt caching; volatile timestamps and changing serialisation can break that reuse. Track cache hit rate and context size per step, rather than treating a larger window as the whole solution.
