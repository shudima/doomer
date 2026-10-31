---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-016
title: Swap the scoring rule
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — strategy; added illustrative example'
sort_order: 9
language: en
---

**Illustrative example**

A recommender calls `score(user, item)`. One strategy scores popularity; another scores recent user interest.

Both return the same kind of score, so the surrounding ranking flow stays the same. Compare the strategies through that shared contract. If one returns a different shape, it is no longer a drop-in replacement.
