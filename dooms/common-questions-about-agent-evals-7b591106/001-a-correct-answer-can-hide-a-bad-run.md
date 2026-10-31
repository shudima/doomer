---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-001
title: A correct answer can hide a bad run
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: Introduction'
sort_order: 1
language: en
---

An agent can finish with a plausible answer after taking the wrong action. Evaluate the run as well as its final message.

The article’s travel example books a flight on the wrong date, even though the price looks acceptable. A trace shows where the error happened. Checking only whether the final response sounds helpful would miss the failure that matters to the traveler.

![The price is accurate, but the agent searched the wrong day. This trace would become a new example in our dataset.](images/source-02.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
