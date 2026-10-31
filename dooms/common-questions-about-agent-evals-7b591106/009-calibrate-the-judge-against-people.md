---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-008
title: Calibrate the judge against people
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: Can you trust an LLM judge?'
sort_order: 9
language: en
---

A model judge can assess whether an answer is supported by retrieved evidence, but its decisions may drift from the team’s judgment. Have people score sample runs, inspect disagreements, and refine the rubric or examples.

Ask narrow questions and use descriptive categories or pass/fail. A vague one-to-ten quality score makes distinctions such as six versus seven difficult to reproduce consistently.

![Contrasting an evaluator with 1-10 scoring (non-descriptive and susceptible to high variability) and a set of binary evaluators.](images/source-05.webp)

*Source: LangChain’s article. Tap to enlarge; the complete figure is preserved.*
