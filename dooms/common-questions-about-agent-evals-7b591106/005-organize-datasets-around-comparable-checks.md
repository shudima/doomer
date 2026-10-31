---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-005
title: Organize datasets around comparable checks
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: What''s the difference between offline and online evals?'
sort_order: 5
language: en
---

A dataset can begin with manually written examples, traces, reviewed annotation queues, uploaded CSV or JSONL, or synthetic variations. Keep examples together when they test the same behavior with the same evaluators.

Separate datasets when the input shape, scoring logic, or purpose changes—for example, full conversations versus single requests, or a small pull-request gate versus a larger release suite. Splits can select subsets within one dataset.
