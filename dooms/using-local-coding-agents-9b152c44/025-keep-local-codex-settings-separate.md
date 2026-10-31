---
schema_version: 2
id: using-local-coding-agents-9b152c44-023
title: Keep local Codex settings separate
background_image: images/local-stack.svg
source_url: https://magazine.sebastianraschka.com/p/using-local-coding-agents
source_file: null
source_title: Using Local Coding Agents
source_type: article
source_locator: 'Section: 9. Codex Setup'
sort_order: 25
language: en
---

Raschka keeps a local Codex configuration separate from his usual hosted setup. His example selects `qwen3.6:35b`, the `ollama` provider, high reasoning effort and a pragmatic personality. He launches it with:

```bash
codex --profile ollama
```

The article abbreviates the provider and profile wiring. Treat this as a setup outline, rather than a complete configuration guaranteed to work unchanged in every CLI version.

![Figure 26](images/source-26.webp)

*Source: Sebastian Raschka’s article; paper credits remain in the original diagram. Tap to enlarge; the complete figure is preserved.*
