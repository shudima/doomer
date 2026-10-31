---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-019
title: Remember the constraint across turns
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: How do you evaluate multi-turn conversations?; added illustrative example'
sort_order: 15
language: en
---

**Illustrative example**

A traveler first says “no overnight layovers,” then asks to change the departure city.

Evaluate the whole conversation. The final booking should still respect the layover constraint even though the last message does not repeat it. A test that scores only the last turn can miss the lost requirement.
