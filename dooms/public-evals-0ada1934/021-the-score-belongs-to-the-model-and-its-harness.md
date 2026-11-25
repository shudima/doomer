---
schema_version: 2
id: public-evals-0ada1934-021
title: The score belongs to the model and its harness
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Hot takes: How we’re thinking about evals wrongly'
sort_order: 21
language: en
---

The harness supplies the prompt, tools, context management, and retry budget. Changing it can change the same model’s score.

On Terminal Bench 2.0, one cited comparison gave a model **57.8%** in Terminus 2 and **52.1%** in its provider’s harness. Another comparison had a larger gap. Use public results to choose candidates, then test them inside the harness your application will actually use.
