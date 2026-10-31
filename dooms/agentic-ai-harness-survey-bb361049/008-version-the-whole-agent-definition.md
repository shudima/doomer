---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-007
title: Version the whole agent definition
background_image: images/part-02.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 19-21
sort_order: 8
language: en
---

An agent's behaviour depends on its prompt, tools, skills, model, parameters, policies and budgets. Scattering those settings makes a production failure hard to reproduce.

Keep a declarative definition under version control, with instructions in separate files. Record the configuration version on every trace and evaluate changes as a unit. Tenant customisation should use bounded settings, such as tone or enabled tools, so the range of behaviours remains reviewable and testable.
