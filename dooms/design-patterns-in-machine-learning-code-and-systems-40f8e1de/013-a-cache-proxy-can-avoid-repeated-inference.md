---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-011
title: A cache proxy can avoid repeated inference
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in systems — proxy'
sort_order: 13
language: en
---

When a small set of search queries accounts for many requests, a service can check cached results before invoking the production inference path. A hit returns immediately; a miss proceeds to computation.

Yan describes this as a proxy acting on behalf of another service. Reusing common query results can reduce real-time compute for suggestions, classification, **retrieval** or ranking.

![Using a cache proxy to serve common requests and reduce compute cost from real-time inference](images/source-02.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
