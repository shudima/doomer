---
schema_version: 2
id: the-exceptional-individual-contributor-50d9f41e-059
title: Keep side effects safe and revisit the design
background_image: images/background.svg
source_url: null
source_file: source/original.pdf
source_title: The Exceptional Individual Contributor
source_type: pdf
source_locator: 'Page 37: Agent architecture — recommended practice'
sort_order: 64
language: en
---

Probabilistic judgments and deterministic state changes serve different purposes. The survey recommends separating them and making tools that change state safe to retry.

Architecture should also remain revisable. A workflow that once required several calls may become simpler as models improve, while a real need for dynamic investigation may justify adding autonomy. Measurements, rather than architectural fashion, should trigger those changes.
