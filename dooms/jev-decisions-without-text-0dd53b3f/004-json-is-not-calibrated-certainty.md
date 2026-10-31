---
schema_version: 2
id: jev-decisions-without-text-0dd53b3f-004
title: JSON is not calibrated certainty
background_image: images/decision.svg
source_url: https://www.youtube.com/watch?v=YGgNBcIgI4s&list=WL&index=9&t=13s
source_file: null
source_title: What Is Jev? The AI Model That Doesn't Generate Text
source_type: video
source_locator: 00:03:17–00:04:04
sort_order: 4
language: en
---

Well-formed JSON tells you that an answer follows a structure. It does not show that a confidence number is trustworthy.

A model can output `{"confidence": 0.9}` without being correct about 90% of comparable cases. The conversation distinguishes this from a model trained and evaluated to produce calibrated probabilities. Test the probability’s behavior, rather than trusting its appearance.
