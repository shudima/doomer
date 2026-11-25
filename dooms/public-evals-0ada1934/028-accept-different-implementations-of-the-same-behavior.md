---
schema_version: 2
id: public-evals-0ada1934-028
title: Accept different implementations of the same behavior
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: Diving into the twelve benchmarks — DeepSWE
sort_order: 28
language: en
---

A prompt can allow multiple reasonable designs while a test quietly assumes one. Yan describes DeepSWE failures tied to choices such as nesting a schema differently or adding a new class.

When reviewing a test, ask which behavior the requirement actually promises. Assertions that depend on an unstated internal structure can turn a design preference into a failing grade. This is the acceptance-breadth problem DeepSWE’s review aims to prevent.
