---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-002
title: A factory hides creation details
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — factory'
sort_order: 2
language: en
---

A **factory** hides the details of creating an object behind a useful interface. Callers describe what they need; the factory handles construction.

Yan uses dataset libraries as examples. A standard contract lets the surrounding library work with different data sources without knowing every source’s internal details. The important part is the reliable interface, rather than the pattern’s name.
