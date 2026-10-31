---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-009
title: Benchmarks give tasks their own environments
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: Are evals the same as benchmarks?'
sort_order: 10
language: en
---

A benchmark is an offline evaluation built from tasks. For action-taking agents, a task can include instructions, an isolated container, and a test script that inspects the resulting state.

The agent may edit files or make dozens of tool calls. Scoring then checks the outcome—such as passing tests or updated reservations—rather than trusting the agent’s description of what it accomplished.
