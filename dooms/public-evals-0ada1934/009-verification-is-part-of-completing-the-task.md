---
schema_version: 2
id: public-evals-0ada1934-009
title: Verification is part of completing the task
background_image: images/background.svg
source_url: https://eugeneyan.com/writing/public-evals
source_file: null
source_title: 'Lessons from 12 Evals: Where They Break and What to Measure Instead'
source_type: article
source_locator: 'Failures: Skipped verification and dropped reqs'
sort_order: 9
language: en
---

Several error analyses found agents stopping without checking the result. Some processed only part of a list and then reported the whole job as complete. Others dropped requirements that were plainly stated.

Check the final artifact or state against the request before declaring success. A completion message is useful when it follows that check and accurately describes what was finished.
