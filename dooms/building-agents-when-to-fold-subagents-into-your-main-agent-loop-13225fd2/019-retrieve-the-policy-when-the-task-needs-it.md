---
schema_version: 2
id: building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-021
title: Retrieve the policy when the task needs it
background_image: images/background.svg
source_url: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
source_file: null
source_title: 'Building agents: When to fold subagents into your main agent loop'
source_type: article
source_locator: 'Section: Knowledge bases; added illustrative example'
sort_order: 19
language: en
---

**Illustrative example**

An assistant needs the current refund deadline for one customer request. It searches the policy reference, reads the relevant section and applies it.

The policy does not need to sit in every prompt for every task. Keep a discoverable pointer and fetch the facts when useful. The tool still enforces any permissions around issuing the refund.
