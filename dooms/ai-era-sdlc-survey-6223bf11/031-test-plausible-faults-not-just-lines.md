---
schema_version: 2
id: ai-era-sdlc-survey-6223bf11-028
title: Test plausible faults, not just lines
background_image: images/quality.svg
source_url: null
source_file: source/original.pdf
source_title: The Software Development Life Cycle in the AI Era
source_type: pdf
source_locator: 'Pages 4-5: Mutation glossary; pages 6 and 18: Meta ACH'
sort_order: 31
language: en
---

Mutation testing injects small faults to see whether tests detect them. An equivalent mutant leaves behavior unchanged, so no test can catch it. The survey describes Meta's ACH using models to generate realistic faults, write tests and filter equivalent mutants.

Its reported equivalent-mutant detection reached 0.95 **precision** and 0.96 recall with preprocessing. Across 10,795 classes, 73% of tests were accepted. Crucially, 277 of 571 accepted tests would have been rejected by a coverage-only criterion. Coverage can miss valuable protection.
