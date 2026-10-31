---
schema_version: 2
id: ai-era-sdlc-survey-6223bf11-048
title: Test a fault that could really happen
background_image: images/quality.svg
source_url: null
source_file: source/original.pdf
source_title: The Software Development Life Cycle in the AI Era
source_type: pdf
source_locator: 'Pages 4-5: Mutation glossary; pages 6 and 18: Meta ACH; added illustrative example'
sort_order: 32
language: en
---

**Illustrative example**

An export test checks that a CSV file exists. A broken implementation writes only the header, and the test still passes.

Add a record with a comma in its name and check the parsed rows and values. Now the test protects useful behavior. A plausible bad implementation should fail, rather than receive credit for producing any file.
