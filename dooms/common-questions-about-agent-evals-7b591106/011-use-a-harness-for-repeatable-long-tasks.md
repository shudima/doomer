---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-010
title: Use a harness for repeatable long tasks
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: Are evals the same as benchmarks?'
sort_order: 11
language: en
---

Harbor provides scaffolding for environment-based tasks and powers Terminal-Bench. Its LangSmith integration logs a run as an experiment with scores and traces.

The article describes turning observed failures into tasks, defining success with code checks or judges, and comparing changes against the score. LangChain used this pattern for Deep Agents and IssueBench. An automated edit-and-rerun loop still depends on a useful rubric.
