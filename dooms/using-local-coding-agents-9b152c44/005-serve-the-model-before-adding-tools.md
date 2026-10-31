---
schema_version: 2
id: using-local-coding-agents-9b152c44-005
title: Serve the model before adding tools
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 3. Local LLM Setup'
sort_order: 5
language: en
---

Every harness in this tutorial first needs a running model server. Ollama provides that layer, with a command-line workflow across macOS, Linux, and Windows.

Other options include LM Studio, vLLM, SGLang, and MLX. Raschka chooses Ollama for convenient, optimized inference rather than training or fine-tuning. Its optional cloud models are a separate, paid route for models too large for consumer hardware; choosing them changes the fully local premise.
