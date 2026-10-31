---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-009
title: A pipeline makes transformations composable
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — pipeline'
sort_order: 11
language: en
---

A machine-learning pipeline chains preparation, feature transformations and an estimator. Each step needs a compatible input/output contract and the methods expected by the framework.

Yan treats preprocessing choices as tunable parts of the model-building process too. Changing scaling, imputation or text features can be compared alongside estimator settings instead of being hidden in disconnected preparation scripts.
