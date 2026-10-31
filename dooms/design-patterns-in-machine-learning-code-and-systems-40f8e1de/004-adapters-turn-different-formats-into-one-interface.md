---
schema_version: 2
id: design-patterns-in-machine-learning-code-and-systems-40f8e1de-004
title: Adapters turn different formats into one interface
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/design-patterns/
source_file: null
source_title: Design Patterns in Machine Learning Code and Systems
source_type: article
source_locator: 'Section: Design patterns in libraries and code — adapter'
sort_order: 4
language: en
---

An **adapter** translates one representation into the interface another component expects.

A data pipeline may read CSV, JSON and Parquet, then pass them to the same processing code. Pandas and Spark readers illustrate this idea; Arrow provides a shared columnar representation. Fewer format-specific assumptions need to spread through the rest of the pipeline.

![Non-exhaustive list of adapters to read different file storage formats in Pandas](images/source-00.webp)

*Source: Eugene Yan’s article; underlying paper credits remain in the figure and linked source. Tap to enlarge; the complete figure is preserved.*
