# Coverage audit

- **Source:** Patterns for Building LLM-based Systems & Products
- **Author:** Eugene Yan (Ziyou Yan)
- **Original URL:** https://eugeneyan.com/writing/llm-patterns/
- **Accessed:** 2026-10-30
- **Language:** English
- **Tone:** Practical, explanatory and experience-based; preserve the author's qualifications and distinguish reviewed research from recommendations.
- **Coverage:** Complete at the level of substantive article ideas, examples and qualifications. This is an independently paraphrased reading sequence, not a transcript or reproduction of the article.
- **Dooms:** 52

## Overall summary

A production-oriented survey of evaluation, retrieval, adaptation, caching, guardrails, defensive UX and feedback, including research mechanisms and operational trade-offs.

## Source map and editorial plan

The original body was read through its conclusion before drafting. The plan follows its progression; related details are consolidated into one central idea per doom. Original section headings: Evals: To measure performance; Why evals?; More about evals; How to apply evals?; Retrieval-Augmented Generation: To add knowledge; Why RAG?; More about RAG; How to apply RAG; Fine-tuning: To get better at specific tasks; Why fine-tuning?; More about fine-tuning; How to apply fine-tuning?; Caching: To reduce latency and cost; Why caching?; More about caching; How to apply caching?; Guardrails: To ensure output quality; Why guardrails?; More about guardrails; How to apply guardrails?; Defensive UX: To anticipate & handle errors gracefully; Why defensive UX?; More about defensive UX; How to apply defensive UX?; Collect user feedback: To build our data flywheel; Why collect user feedback; How to collect user feedback; Other patterns common in machine learning; Conclusion; References.

| Source section or numbered advice | Dooms |
| --- | --- |
| Introduction | 1 |
| Evals — Why evals? | 2 |
| Evals — BLEU and ROUGE | 3 |
| Evals — BERTScore and MoverScore | 4 |
| Evals — metric pitfalls and MMLU | 5 |
| Evals — G-Eval, Vicuna and QLoRA | 6 |
| Evals — How to apply evals? | 7 |
| Evals — judge biases | 8 |
| Evals — human evaluation | 9 |
| Retrieval-Augmented Generation — Why RAG? | 10 |
| Retrieval-Augmented Generation — embeddings | 11 |
| Retrieval-Augmented Generation — Dense Passage Retrieval | 12 |
| Retrieval-Augmented Generation — RAG-Sequence and RAG-Token | 13 |
| Retrieval-Augmented Generation — Fusion-in-Decoder | 14 |
| Retrieval-Augmented Generation — RETRO | 15 |
| Retrieval-Augmented Generation — internet-augmented models and CodeT5+ | 16 |
| Retrieval-Augmented Generation — HyDE | 17 |
| Retrieval-Augmented Generation — How to apply RAG | 18 |
| Retrieval-Augmented Generation — embedding models | 19 |
| Retrieval-Augmented Generation — ANN indexes | 20 |
| Retrieval-Augmented Generation — ANN trade-offs | 21 |
| Fine-tuning — definitions | 22 |
| Fine-tuning — Why fine-tuning? | 23 |
| Fine-tuning — demonstration data and regressions | 24 |
| Fine-tuning — ULMFiT, BERT and GPT | 25 |
| Fine-tuning — T5 and InstructGPT | 26 |
| Fine-tuning — soft prompt and prefix tuning | 27 |
| Fine-tuning — adapters and LoRA | 28 |
| Fine-tuning — QLoRA | 29 |
| Fine-tuning — How to apply fine-tuning? | 30 |
| Fine-tuning — model and architecture selection | 31 |
| Fine-tuning — hyperparameters | 32 |
| Caching — Why caching? | 33 |
| Caching — semantic-cache risks | 34 |
| Caching — cache hit rate | 35 |
| Caching — How to apply caching? | 36 |
| Guardrails — purpose | 37 |
| Guardrails — prompts and validators | 38 |
| Guardrails — NeMo and self-consistency | 39 |
| Guardrails — Guidance and token healing | 40 |
| Guardrails — How to apply guardrails? | 41 |
| Defensive UX — purpose | 42 |
| Defensive UX — Microsoft guidelines | 43 |
| Defensive UX — Google and Apple guidelines | 44 |
| Defensive UX — expectations, dismissal and attribution | 45 |
| Defensive UX — familiarity and chat | 46 |
| Collect user feedback — Why collect user feedback | 47 |
| Collect user feedback — explicit feedback | 48 |
| Collect user feedback — implicit feedback | 49 |
| Other patterns common in machine learning — flywheel and cascade | 50 |
| Other patterns common in machine learning — monitoring and practitioner additions | 51 |
| Conclusion | 52 |

## Limits and deliberate omissions

The complete original article body, inline examples and figure explanations were retrieved successfully. Navigation, sharing links, promotional offers, bibliography entries and acknowledgments are omitted. Code listings are explained conceptually rather than reproduced. Embedded research diagrams and tables are not reprinted cell by cell; the sequence preserves their substantive findings and qualifications as discussed in the article. Linked papers and external resources were not independently treated as additional sources. Model rankings, tool examples and benchmark findings are historical claims from this article, not independently updated recommendations.

## Background asset

`images/background.svg` is an original, purpose-made 1080×1920 vector gradient with quiet abstract shapes. It contains no reel text and uses no third-party image assets. The same background is intentionally shared across the collection.

## Verification

Every YAML is parsed and checked against the project's JSON Schema. Filenames, unique IDs, ordering, source metadata, word lengths and local asset references are checked. The SVG parses and has a portrait 9:16 canvas. Source-to-doom mapping was checked for substantive section coverage, omitted caveats and duplicate ideas. App preview results are recorded after the representative phone-size checks.

Phone-size preview: the first doom was opened in the actual local Doomer reader at 393×730. Topic title, doom total, original source link, background and full text were inspected; no clipping was observed. This was a desktop browser viewport check, not a physical iPhone test.


## Markdown revision — 2026-10-31

Authorized in-place migration: 52 existing dooms retained their identities; 3 labeled illustrative examples added; 55 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `patterns-for-building-llm-based-systems-products-b4c1a004-001` | 1 | A demo is only the beginning |
| `patterns-for-building-llm-based-systems-products-b4c1a004-002` | 2 | Measure the system, not just the base model |
| `patterns-for-building-llm-based-systems-products-b4c1a004-003` | 3 | Reference overlap measures only part of quality |
| `patterns-for-building-llm-based-systems-products-b4c1a004-004` | 4 | Embedding metrics allow different wording |
| `patterns-for-building-llm-based-systems-products-b4c1a004-005` | 5 | Benchmarks can hide measurement differences |
| `patterns-for-building-llm-based-systems-products-b4c1a004-006` | 6 | A language model can judge, but not without bias |
| `patterns-for-building-llm-based-systems-products-b4c1a004-007` | 7 | Build evaluations around your actual task |
| `patterns-for-building-llm-based-systems-products-b4c1a004-008` | 8 | Control order, length and self-preference |
| `patterns-for-building-llm-based-systems-products-b4c1a004-009` | 9 | Keep room for direct human inspection |
| `patterns-for-building-llm-based-systems-products-b4c1a004-010` | 10 | Retrieval supplies knowledge outside the weights |
| `patterns-for-building-llm-based-systems-products-b4c1a004-053` | 11 | Find evidence before answering |
| `patterns-for-building-llm-based-systems-products-b4c1a004-011` | 12 | Judge embeddings by what they help retrieve |
| `patterns-for-building-llm-based-systems-products-b4c1a004-012` | 13 | Better retrieval can improve the final answer |
| `patterns-for-building-llm-based-systems-products-b4c1a004-013` | 14 | RAG can combine evidence at different levels |
| `patterns-for-building-llm-based-systems-products-b4c1a004-014` | 15 | Fusion-in-Decoder combines separately encoded passages |
| `patterns-for-building-llm-based-systems-products-b4c1a004-015` | 16 | RETRO builds retrieval into language modeling |
| `patterns-for-building-llm-based-systems-products-b4c1a004-016` | 17 | Search and code examples can support generation |
| `patterns-for-building-llm-based-systems-products-b4c1a004-017` | 18 | HyDE searches with a hypothetical document |
| `patterns-for-building-llm-based-systems-products-b4c1a004-018` | 19 | Combine lexical and semantic retrieval |
| `patterns-for-building-llm-based-systems-products-b4c1a004-019` | 20 | Embedding choices include task instructions |
| `patterns-for-building-llm-based-systems-products-b4c1a004-020` | 21 | Approximate search exchanges exactness for speed |
| `patterns-for-building-llm-based-systems-products-b4c1a004-021` | 22 | Benchmark the index against operational needs |
| `patterns-for-building-llm-based-systems-products-b4c1a004-022` | 23 | Fine-tuning names several different processes |
| `patterns-for-building-llm-based-systems-products-b4c1a004-023` | 24 | Specialization can improve control and reduce dependency |
| `patterns-for-building-llm-based-systems-products-b4c1a004-024` | 25 | Improvements can carry an alignment tax |
| `patterns-for-building-llm-based-systems-products-b4c1a004-025` | 26 | Transfer learning made reuse a standard workflow |
| `patterns-for-building-llm-based-systems-products-b4c1a004-026` | 27 | T5 and InstructGPT broadened the task interface |
| `patterns-for-building-llm-based-systems-products-b4c1a004-027` | 28 | Soft prompts and prefixes update a small addition |
| `patterns-for-building-llm-based-systems-products-b4c1a004-028` | 29 | Adapters and LoRA constrain what is learned |
| `patterns-for-building-llm-based-systems-products-b4c1a004-029` | 30 | QLoRA reduces the memory burden of adaptation |
| `patterns-for-building-llm-based-systems-products-b4c1a004-030` | 31 | Training examples need both quality and usable rights |
| `patterns-for-building-llm-based-systems-products-b4c1a004-031` | 32 | Narrow the task before choosing the model |
| `patterns-for-building-llm-based-systems-products-b4c1a004-032` | 33 | Tune the training process, not only the model name |
| `patterns-for-building-llm-based-systems-products-b4c1a004-033` | 34 | Caching can move work out of the request path |
| `patterns-for-building-llm-based-systems-products-b4c1a004-034` | 35 | Similar meaning is not the same request |
| `patterns-for-building-llm-based-systems-products-b4c1a004-054` | 36 | Check the film identifier before a cache hit |
| `patterns-for-building-llm-based-systems-products-b4c1a004-035` | 37 | Measure whether requests actually repeat |
| `patterns-for-building-llm-based-systems-products-b4c1a004-036` | 38 | Prefer stable keys and constrained inputs |
| `patterns-for-building-llm-based-systems-products-b4c1a004-037` | 39 | Guardrails check more than whether text sounds good |
| `patterns-for-building-llm-based-systems-products-b4c1a004-038` | 40 | Prompting and validation play different roles |
| `patterns-for-building-llm-based-systems-products-b4c1a004-039` | 41 | Model-based checks have their own uncertainty |
| `patterns-for-building-llm-based-systems-products-b4c1a004-040` | 42 | Constrain structure during generation |
| `patterns-for-building-llm-based-systems-products-b4c1a004-041` | 43 | Layer checks around the actual requirement |
| `patterns-for-building-llm-based-systems-products-b4c1a004-055` | 44 | Layer checks around a refund |
| `patterns-for-building-llm-based-systems-products-b4c1a004-042` | 45 | Design for errors before users encounter them |
| `patterns-for-building-llm-based-systems-products-b4c1a004-043` | 46 | Explain capability and support correction |
| `patterns-for-building-llm-based-systems-products-b4c1a004-044` | 47 | Work backward from the human experience |
| `patterns-for-building-llm-based-systems-products-b4c1a004-045` | 48 | Be honest, dismissible and attributable |
| `patterns-for-building-llm-based-systems-products-b4c1a004-046` | 49 | Chat is not automatically the easiest interface |
| `patterns-for-building-llm-based-systems-products-b4c1a004-047` | 50 | Feedback supplies evidence of actual usefulness |
| `patterns-for-building-llm-based-systems-products-b4c1a004-048` | 51 | Useful actions can carry preference information |
| `patterns-for-building-llm-based-systems-products-b4c1a004-049` | 52 | Behavior needs interpretation, not blind counting |
| `patterns-for-building-llm-based-systems-products-b4c1a004-050` | 53 | Combine the patterns into an improvement loop |
| `patterns-for-building-llm-based-systems-products-b4c1a004-051` | 54 | Keep monitoring, access and security in view |
| `patterns-for-building-llm-based-systems-products-b4c1a004-052` | 55 | Choose patterns by the problem they solve |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `patterns-for-building-llm-based-systems-products-b4c1a004-010` | `patterns-for-building-llm-based-systems-products-b4c1a004-053` | Find evidence before answering |
| `patterns-for-building-llm-based-systems-products-b4c1a004-034` | `patterns-for-building-llm-based-systems-products-b4c1a004-054` | Check the film identifier before a cache hit |
| `patterns-for-building-llm-based-systems-products-b4c1a004-041` | `patterns-for-building-llm-based-systems-products-b4c1a004-055` | Layer checks around a refund |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-00.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-001` | [Original](https://eugeneyan.com/assets/llm-patterns-og.webp) | Image | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `66e9ccba6e36547902e9d33e9afbd4a54ab96df87ccf7e194cd382bf8a372810` |
| `images/source-06.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-010` | [Original](https://eugeneyan.com/assets/rag.webp) | Overview of Retrieval Augmented Generation | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `2492333660052c36f625102332bb81396b424865639b5c391346d1679348617f` |
| `images/source-07.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-014` | [Original](https://eugeneyan.com/assets/fid.webp) | Overview of Fusion-in-Decoder | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `e56aa14afbd07ea89eaa37489aeaea7288ff17c38105861d66a7d01a448eb0a7` |
| `images/source-12.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-017` | [Original](https://eugeneyan.com/assets/hyde.webp) | Overview of HyDE | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `52ac72237f22da48317f0899ded6bebec49d6edf269b246e2a3ce731f1d39cff` |
| `images/source-20.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-028` | [Original](https://eugeneyan.com/assets/lora.webp) | Overview of LoRA | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `56646d58dd9901d11ebfb516d2da40619aaddafa1d711e1f1a24e1545b199a7f` |
| `images/source-21.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-029` | [Original](https://eugeneyan.com/assets/qlora.webp) | Overview of QLoRA | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `0dc2f719630abd067299e6dc591f5858bdfbc680c62a48e895c9bf2c0b290405` |
| `images/source-22.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-033` | [Original](https://eugeneyan.com/assets/gptcache.webp) | Overview of GPTCache | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `2e954618df91fc5bdaa7f7bf0b2786016fef7cf40918d07b6bc36f632d2a920e` |
| `images/source-25.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-042` | [Original](https://eugeneyan.com/assets/ms-guidelines.webp) | Guidelines for Human-AI interaction across the user journey | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `48c268ada588a24a13d8602104f0a75593cc21dad19688319ecfe879a41db008` |
| `images/source-28.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-048` | [Original](https://eugeneyan.com/assets/midjourney.webp) | >Example of collecting user feedback as part of the UX | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `6cfdd9a3fd1857c936bff82e537d39d3371e9c45c39d1840ddb66a02125422ca` |
| `images/source-29.webp` / `patterns-for-building-llm-based-systems-products-b4c1a004-050` | [Original](https://eugeneyan.com/assets/llm-patterns.webp) | LLM patterns across the axis of data to user, and defensive to offensive. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `d6b3876c69d42110ebb742655dfa47843bf663cc1ec380b7ab0e3dd64471c543` |

Added diagram: Check a cache candidate. Authored for the labeled illustrative example, not reproduced from the source. Editable Mermaid and a portable SVG are included. The SVG is a linear overview; the live Mermaid also shows decision branches.
