---
schema_version: 2
id: product-evals-in-three-simple-steps-e1d32e24-006
title: Hold out examples while aligning the judge
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/product-evals/
source_file: null
source_title: Product Evals in Three Simple Steps
source_type: article
source_locator: 'Section: Then, align our LLM-evaluator'
sort_order: 6
language: en
---

An evaluator prompt is a model component that can overfit. Yan recommends treating its development like a conventional machine-learning problem.

One example split uses 75% of labeled cases for prompt iteration and 25% for testing. The held-out portion checks whether the evaluator can apply the criterion to unfamiliar cases, rather than merely improving on the examples that shaped its prompt.
