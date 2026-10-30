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
