---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-014
title: Recommendation widgets need page-level coordination
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in systems — mediator example; conclusion'
sort_order: 16
language: en
---

Separate recommendation widgets may each look sensible while producing a poor page together. Yan's mediator example ranks widgets, checks minimum content and removes duplicate items across placements.

The closing point is: naming the pattern helps explain why coordination belongs in that component. Choosing an appropriate pattern communicates intended use as well as organizing the implementation.

![Using a mediator to allocate widgets to placements on the home page](images/source-04.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
