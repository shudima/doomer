---
schema_version: 2
id: public-evals-0ada1934-012
title: Two digits do not prove an email is correct
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Gaps: Failing correct work and passing wrong work'
sort_order: 12
language: en
---

An AutomationBench task asks for an email with counts of ready and not-ready audit items. Its check only looks for a `3` and a `4`.

An email that swaps the two counts still contains both digits. A date or identifier could contain them too. Check each value together with what it describes. A substring match alone cannot establish that the message communicates the right result.
