---
schema_version: 2
id: coding-with-ai-agents-concepts-40c23e33-015
title: Give experiments a disposable workspace
background_image: images/shield.svg
source_url: https://www.youtube.com/watch?v=hTAWHgQI4xg&list=WL&index=5
source_file: null
source_title: 5 Concepts to Know for Coding with AI Agents
source_type: video
source_locator: 00:08:04–00:08:24; added illustrative example
sort_order: 14
language: en
---

**Illustrative example**

An agent investigating a dependency upgrade needs to install packages and edit files. Put the experiment in a separate checkout with only the credentials it needs.

Run the checks there and review the resulting diff. If the attempt fails, your main work stays usable. Isolation makes recovery easier while the agent still has room to investigate.
