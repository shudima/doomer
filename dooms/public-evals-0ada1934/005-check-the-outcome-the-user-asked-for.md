---
schema_version: 2
id: public-evals-0ada1934-005
title: Check the outcome the user asked for
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Principles: That shape grading and task selection'
sort_order: 5
language: en
---

Many benchmarks inspect the final workspace or deliverable and let the agent choose its own method. Terminal Bench checks container state. AutomationBench checks application state.

**Illustrative example.** A request asks for a spreadsheet sorted by date. A valid grader checks the saved rows and dates. Requiring one particular sequence of clicks would reject other ways to produce the same correct file.
