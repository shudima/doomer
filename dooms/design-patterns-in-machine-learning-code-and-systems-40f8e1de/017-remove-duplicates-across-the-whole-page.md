---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-017
title: Remove duplicates across the whole page
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in systems — mediator example; conclusion; added illustrative example'
sort_order: 17
language: en
---

**Illustrative example**

A “Popular” widget and a “New releases” widget both select the same film. Each widget looks reasonable on its own.

A mediator receives both candidate lists, ranks the placements and removes the repeated film. It solves a page-level problem that neither widget can see independently.
