# Coverage audit

- **Source:** Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)
- **Author:** Eugene Yan (Ziyou Yan)
- **Original URL:** https://eugeneyan.com/writing/llm-evaluators/
- **Accessed:** 2026-10-30
- **Language:** English
- **Tone:** Practical, explanatory and experience-based; preserve the author's qualifications and distinguish reviewed research from recommendations.
- **Coverage:** Complete at the level of substantive article ideas, examples and qualifications. This is an independently paraphrased reading sequence, not a transcript or reproduction of the article.
- **Dooms:** 43

## Overall summary

A research survey of model-based judging, distinguishing scoring schemes, metrics, prompting, alignment, specialized critics and evidence of important blind spots.

## Source map and editorial plan

The original body was read through its conclusion before drafting. The plan follows its progression; related details are consolidated into one central idea per doom. Original section headings: Key considerations before adopting an LLM-evaluator; Use cases for LM-evaluators; Techniques for prompting LLM-evaluators; Aligning LLM-evaluators to our criteria; Finetuning LLM-evaluator models; Critiques against and support for LLM-evaluators; References.

| Source section or numbered advice | Dooms |
| --- | --- |
| Introduction | 1 |
| Key considerations before adopting an LLM-evaluator | 2 |
| Key considerations before adopting an LLM-evaluator — direct scoring | 3 |
| Key considerations before adopting an LLM-evaluator — pairwise comparison | 4 |
| Key considerations before adopting an LLM-evaluator — reference-based evaluation | 5 |
| Key considerations before adopting an LLM-evaluator — classification metrics | 6 |
| Key considerations before adopting an LLM-evaluator — agreement and correlation | 7 |
| Use cases for LM-evaluators — Constitutional AI | 8 |
| Use cases for LM-evaluators — Constitutional AI results | 9 |
| Use cases for LM-evaluators — Human-like Summarization Evaluation | 10 |
| Use cases for LM-evaluators — summarization results | 11 |
| Use cases for LM-evaluators — Factual Inconsistency Evaluator | 12, 13 |
| Use cases for LM-evaluators — HaluEval | 14 |
| Use cases for LM-evaluators — Correctness and Faithfulness in QA | 15 |
| Techniques for prompting LLM-evaluators — LM vs LM | 16 |
| Techniques for prompting LLM-evaluators — G-Eval | 17 |
| Techniques for prompting LLM-evaluators — SelfCheckGPT | 18 |
| Techniques for prompting LLM-evaluators — Pairwise Preference | 19 |
| Techniques for prompting LLM-evaluators — Fairer Preferences | 20 |
| Techniques for prompting LLM-evaluators — UMbrela | 21 |
| Techniques for prompting LLM-evaluators — PoLL | 22 |
| Techniques for prompting LLM-evaluators — PoLL ablation | 23 |
| Aligning LLM-evaluators to our criteria — EvalLM | 24 |
| Aligning LLM-evaluators to our criteria — Structured Output | 25 |
| Aligning LLM-evaluators to our criteria — EvalGen | 26 |
| Aligning LLM-evaluators to our criteria — EvalGen results | 27 |
| Finetuning LLM-evaluator models — Shepherd | 28 |
| Finetuning LLM-evaluator models — Shepherd evaluation | 29 |
| Finetuning LLM-evaluator models — Cappy | 30 |
| Finetuning LLM-evaluator models — Prometheus | 31 |
| Finetuning LLM-evaluator models — Prometheus ablation | 32 |
| Finetuning LLM-evaluator models — CriticGPT | 33 |
| Finetuning LLM-evaluator models — CriticGPT caveats | 34 |
| Critiques against and support for LLM-evaluators — MT-Bench and Chatbot Arena | 35 |
| Critiques against and support for LLM-evaluators — position and verbosity biases | 36 |
| Critiques against and support for LLM-evaluators — self-enhancement bias | 37 |
| Critiques against and support for LLM-evaluators — Limitations of Fine-tuned Judges | 38 |
| Critiques against and support for LLM-evaluators — Blind Spots | 39 |
| Critiques against and support for LLM-evaluators — Twenty NLP Tasks | 40 |
| Critiques against and support for LLM-evaluators — Judging the Judges | 41 |
| Conclusion — scoring and metrics | 42 |
| Conclusion — deployment | 43 |

## Limits and deliberate omissions

The complete original article body, inline examples and figure explanations were retrieved successfully. Navigation, sharing links, promotional offers, bibliography entries and acknowledgments are omitted. Code listings are explained conceptually rather than reproduced. Embedded research diagrams and tables are not reprinted cell by cell; the sequence preserves their substantive findings and qualifications as discussed in the article. Linked papers and external resources were not independently treated as additional sources. Model rankings, tool examples and benchmark findings are historical claims from this article, not independently updated recommendations.

## Background asset

`images/background.svg` is an original, purpose-made 1080×1920 vector gradient with quiet abstract shapes. It contains no reel text and uses no third-party image assets. The same background is intentionally shared across the collection.

## Verification

Every YAML is parsed and checked against the project's JSON Schema. Filenames, unique IDs, ordering, source metadata, word lengths and local asset references are checked. The SVG parses and has a portrait 9:16 canvas. Source-to-doom mapping was checked for substantive section coverage, omitted caveats and duplicate ideas. App preview results are recorded after the representative phone-size checks.

Phone-size preview: the first doom was opened in the actual local Doomer reader at 393×730. Topic title, doom total, original source link, background and full text were inspected; no clipping was observed. This was a desktop browser viewport check, not a physical iPhone test.
