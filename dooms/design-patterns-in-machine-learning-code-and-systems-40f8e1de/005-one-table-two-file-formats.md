---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-015
title: One table, two file formats
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — adapter; added illustrative example'
sort_order: 5
language: en
---

**Illustrative example**

A daily job receives CSV from one team and JSON from another. Give each format an adapter that returns the same table columns.

The validation and modeling steps can then use one interface. When a third team sends Parquet, add an adapter rather than teaching every downstream function about another file format.
