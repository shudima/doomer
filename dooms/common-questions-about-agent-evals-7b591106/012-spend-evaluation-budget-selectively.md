---
schema_version: 2
id: common-questions-about-agent-evals-7b591106-011
title: Spend evaluation budget selectively
background_image: images/background.svg
source_url: https://www.langchain.com/blog/common-questions-about-agent-evals
source_file: null
source_title: The Most Common Questions About Agent Evals, Answered
source_type: article
source_locator: 'Section: How can you evaluate production traffic without high costs?'
sort_order: 12
language: en
---

Scoring every production trace with an expensive judge can make evaluation costs rise with traffic. Sample a percentage, filter for signals such as negative feedback, and use code checks wherever the question is deterministic.

A cheaper judge is another option. LangChain reports one experiment where Jev matched all human pass/fail labels for $0.34 versus $28.17 for Sonnet 4.6; that result belongs to that experiment, not every rubric.
