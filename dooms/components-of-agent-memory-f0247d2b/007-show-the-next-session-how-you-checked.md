---
schema_version: 2
id: components-of-agent-memory-f0247d2b-007
title: Show the next session how you checked
background_image: images/background.svg
source_url: https://www.anthropic.com/research/components-of-agent-memory
source_file: null
source_title: The components of agent memory
source_type: article
source_locator: 'Section: Memory can be a prediction about what the future will need'
sort_order: 7
language: en
---

**Illustrative example.** A database query counts customers twice after joining their orders. The agent checks a customer with two orders and confirms the join creates two rows.

A useful memory records the rule and the test together. Count distinct customer IDs after this join when the question is about people. The two-order case showed why counting rows gave the wrong answer.
