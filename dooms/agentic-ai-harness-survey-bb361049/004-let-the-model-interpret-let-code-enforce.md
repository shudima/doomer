---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-063
title: Let the model interpret; let code enforce
background_image: images/part-01.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 14-15; added illustrative example
sort_order: 4
language: en
---

**Illustrative example**

A recruiting assistant receives “find senior data engineers with Spark experience.” The model interprets the request.

The search tool applies the signed-in user’s permissions before returning any candidates. It also excludes withdrawn applications. Those rules hold even if the model asks for every record.

The model decides which permitted profiles look relevant; it never receives records it has no right to read.
