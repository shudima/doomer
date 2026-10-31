---
schema_version: 2
id: salesforce-agent-tech-stack-3e16b48a-003
title: Rules become code
background_image: images/network.svg
source_url: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
source_file: null
source_title: A Deep Dive into Salesforce’s Agent Tech Stack
source_type: article
source_locator: 'Section: 1. Deterministic instructions with Agent Script'
sort_order: 3
language: en
---

Agent Script puts predictable steps into code. It compiles into an **Agent Graph**, which the Atlas Reasoning Engine executes.

In the article’s appointment example, a `before_reasoning` block fetches appointments before the model answers. An `after_reasoning` block handles the next step. The lookup runs because it is part of execution, rather than because the model remembered a prompt instruction. Use natural language for the judgment that remains.

![Agent Script compiles into an Agent Graph that combines code steps with model reasoning.](images/source-07.webp)

*Source: ByteByteGo’s article. Tap to enlarge; the complete figure is preserved.*
