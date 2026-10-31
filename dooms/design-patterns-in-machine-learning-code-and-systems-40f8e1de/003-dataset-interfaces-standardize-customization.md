---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-003
title: Dataset interfaces standardize customization
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — factory examples'
sort_order: 3
language: en
---

In Yan's examples, a custom PyTorch dataset implements length and indexed access, while a Gensim corpus implements how documents become token sequences. Hugging Face's dataset interface offers loading and transformation without requiring the same subclassing approach.

These examples illustrate different ways to expose convenient data construction and access. The article's code is explanatory, not a promise that every library version retains identical APIs.
