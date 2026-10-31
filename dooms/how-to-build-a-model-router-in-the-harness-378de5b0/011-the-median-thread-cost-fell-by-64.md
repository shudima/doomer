---
schema_version: 2
id: how-to-build-a-model-router-in-the-harness-378de5b0-009
title: The median thread cost fell by 64%
background_image: images/background.svg
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
source_file: null
source_title: How to Build a Model Router in the Harness
source_type: article
source_locator: 'Section: The experiment'
sort_order: 11
language: en
---

Against always using GPT-6 Astra, the routed median cost was $0.94 versus $2.61. Mean cost fell 42% and the ninetieth percentile fell 37%, suggesting savings beyond a handful of tiny requests.

These are results from Open SWE’s traffic and selected models. They demonstrate the potential of routing in that setting, rather than promising the same percentage for a different agent or pricing schedule.

![LLM cost per thread: always GPT-6 Astra vs. routed, and routed threads split by tier](images/source-07.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
