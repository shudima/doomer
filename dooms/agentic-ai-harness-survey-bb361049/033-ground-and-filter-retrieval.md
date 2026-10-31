---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-030
title: Ground and filter retrieval
background_image: images/part-04.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 40-41
sort_order: 33
language: en
---

Retrieval should return passages with source identifiers and enforce permissions before content reaches the model. Citations let users check specific claims.

Measure retrieval **recall** separately from answer quality on labelled questions. Probe answers hidden from the test user's permissions and questions unanswered anywhere in the corpus. The agent should disclose missing evidence without exposing forbidden material or inventing a confident answer.
