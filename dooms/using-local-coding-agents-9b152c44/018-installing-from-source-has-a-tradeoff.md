---
schema_version: 2
id: using-local-coding-agents-9b152c44-017
title: Installing from source has a tradeoff
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 7. Qwen-Code Setup'
sort_order: 18
language: en
---

Qwen Code offers a standalone installer and an npm package. Those routes assume the published artifacts correspond to the repository you reviewed.

For more direct control, Raschka describes cloning the repository, installing dependencies, building the CLI, and creating a wrapper that points to that checkout. The source route is more manual and still includes dependency installation. Keep the checkout available for the wrapper, then confirm the installation with `qwen --version`.
