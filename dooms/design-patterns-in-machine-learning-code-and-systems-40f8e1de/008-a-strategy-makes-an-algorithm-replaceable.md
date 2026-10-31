---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-007
title: A strategy makes an algorithm replaceable
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — strategy'
sort_order: 8
language: en
---

A **strategy** lets you replace an algorithm without rewriting the code that uses it. Each replacement follows the same contract.

Yan points to configurable tree-building methods and objective functions in XGBoost. A caller can select a different implementation while keeping the surrounding flow. The replacement still has to accept the expected input and return a usable result.
