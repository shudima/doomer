---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-039
title: Keep verification independent
background_image: images/part-05.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 49-50
sort_order: 43
language: en
---

A separate critic can assess faithfulness, completeness and tone using the output and evidence in its own context. Keep tests, verifier instructions and logs beyond the producing agent's control.

Test verifiers with known-bad outputs. Return specific failures for repair, cap retries and disclose unresolved problems. Silently dropping failed items can leave the user believing an incomplete result is complete.
