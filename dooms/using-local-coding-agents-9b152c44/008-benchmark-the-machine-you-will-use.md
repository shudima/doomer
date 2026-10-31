---
schema_version: 2
id: using-local-coding-agents-9b152c44-008
title: Benchmark the machine you will use
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 4. Simple Speed Performance Assessment'
sort_order: 8
language: en
---

The article’s benchmark command is `uv run speed-memory-benchmark/ollama_speed_memory_bench.py --model qwen3.6:35b`, run from the downloaded evaluation repository. Use the `-mlx` model name on an Apple silicon Mac.

The model must already be downloaded. Machines with less than 30 GB of RAM may need a smaller model such as Gemma 4 E2B, which the article reports can use around 8 GB at long contexts. Fitting in memory does not guarantee useful agent behavior.
