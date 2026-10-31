---
schema_version: 2
id: using-local-coding-agents-9b152c44-006
title: Choose the right model variant
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 3. Local LLM Setup'
sort_order: 6
language: en
---

After installing Ollama, download the model before connecting an agent. On Apple silicon, the article recommends `ollama pull qwen3.6:35b-mlx` to use the optimized MLX variant. On Linux, it uses `ollama pull qwen3.6:35b`.

Test the model in Ollama’s interface or terminal first. Exit an interactive session with `/bye`. A successful chat confirms basic serving works, though it does not yet establish reliable coding or tool use.
