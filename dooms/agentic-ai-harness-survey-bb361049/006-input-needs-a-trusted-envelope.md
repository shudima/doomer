---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-005
title: Input needs a trusted envelope
background_image: images/part-02.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 17-18
sort_order: 6
language: en
---

An enterprise agent receives more than a message: identity, tenant, session, channel, application context, attachments and saved task state all shape the work.

Keep these layers explicit. Authentication supplies identity; a user's message supplies intent, not permissions. Pass object references when possible, label attachment provenance, and treat document contents as data. Credentials remain with the harness, outside the model's context, where they can be attached to tool calls safely.
