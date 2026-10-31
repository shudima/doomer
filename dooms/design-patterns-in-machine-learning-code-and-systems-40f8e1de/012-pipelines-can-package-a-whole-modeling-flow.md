---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-010
title: Pipelines can package a whole modeling flow
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — pipeline examples'
sort_order: 12
language: en
---

Yan illustrates a scikit-learn chain containing imputation, scaling and a classifier, and a Spark chain containing tokenization, feature hashing and logistic regression.

The examples show how a consistent abstraction can represent several stages as a trainable object. A fitted pipeline can then be evaluated or persisted as a coherent flow rather than managed as unrelated transformations.
