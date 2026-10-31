---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-006
title: Cache, fixtures and timing solve different needs
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — decorator examples'
sort_order: 7
language: en
---

Yan's caching example avoids repeated work when computing Fibonacci values. His fixture examples prepare reusable test data and trained models, while a timing wrapper returns both a prediction and its runtime.

Keep the core job separate from supporting behavior. Shared setup, measurement or reuse behavior can surround the main computation without obscuring what that computation is meant to accomplish.
