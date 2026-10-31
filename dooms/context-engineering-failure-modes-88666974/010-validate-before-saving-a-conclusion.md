---
schema_version: 2
id: context-engineering-failure-modes-88666974-008
title: Validate before saving a conclusion
background_image: images/measure.svg
source_url: https://www.youtube.com/watch?v=BwXremQ-i6I&list=WL&index=4
source_file: null
source_title: 'Context Engineering for AI Agents: 4 Failure Modes to Avoid'
source_type: video
source_locator: 00:07:28–00:07:53
sort_order: 10
language: en
---

For context poisoning, the proposed fix is validation. Before recording a conclusion as a fact, check it against something real.

In the migration example, a quick connection test could have shown whether the new driver actually retried. That check would have stopped a mistaken interpretation from becoming persistent context and driving repeated edits through the rest of the codebase.
