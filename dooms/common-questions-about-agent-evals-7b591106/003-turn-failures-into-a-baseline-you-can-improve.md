---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-003
title: Turn failures into a baseline you can improve
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: Where should we start?'
sort_order: 3
language: en
---

Run the current agent on your initial dataset and save its results and evaluator scores as an experiment. That becomes the baseline for later versions.

When testing or production reveals a failure, add it as another example, improve the agent, and rerun. A travel assistant searching the wrong date belongs in the dataset even if its quoted ticket price was accurate.
