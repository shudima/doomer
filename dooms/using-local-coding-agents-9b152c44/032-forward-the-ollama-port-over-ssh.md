---
schema_version: 2
id: using-local-coding-agents-9b152c44-030
title: Forward the Ollama port over SSH
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 11. Mac <-> DGX'
sort_order: 32
language: en
---

First stop the Mac’s Ollama service, or choose a different local port to avoid a collision. The article forwards port 11434 with `ssh -N -L 11434:127.0.0.1:11434 rasbt@DGX-Spark`, replacing the account and hostname for your machines.

Keep that terminal open while using the agent; an idle-looking session is expected. Check `http://127.0.0.1:11434/v1/models` before and after connecting. Once it lists the remote models, the familiar local endpoint reaches the remote server.
