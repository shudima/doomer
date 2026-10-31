---
schema_version: 2
id: agentic-ai-harness-survey-bb361049-028
title: Search beyond similarity
background_image: images/part-04.svg
source_url: null
source_file: source/original.pdf
source_title: Building and Evaluating Agentic AI Systems
source_type: pdf
source_locator: Pages 40-41
sort_order: 31
language: en
---

Embedding search can miss exact names and codes. The survey recommends combining keyword and embedding search, merged rankings and a reranker for prose.

Contextual descriptions preserve a chunk's place in its document. Anthropic reported 49 percent fewer top-20 **retrieval** failures with contextual embeddings plus BM25, and 67 percent with reranking added. These figures concern specific datasets and metrics, not guaranteed gains.
