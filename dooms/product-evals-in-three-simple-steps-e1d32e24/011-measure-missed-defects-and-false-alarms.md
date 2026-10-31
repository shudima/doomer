---
schema_version: 2
id: product-evals-in-three-simple-steps-e1d32e24-009
title: Measure missed defects and false alarms
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/product-evals/
source_file: null
source_title: Product Evals in Three Simple Steps
source_type: article
source_locator: 'Section: Then, align our LLM-evaluator'
sort_order: 11
language: en
---

Check two things about a failure detector:

- **Precision:** among the answers it flags, how many really fail?
- **Recall:** among all real failures, how many does it catch?

High recall catches more defects. High precision avoids wasting time on false alarms. Compare the judge with human labels on the cases that matter to the product.
