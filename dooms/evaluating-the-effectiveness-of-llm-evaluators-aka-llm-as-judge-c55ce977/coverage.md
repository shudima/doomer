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


## Markdown revision — 2026-10-31

Authorized in-place migration: 43 existing dooms retained their identities; 3 labeled illustrative examples added; 46 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-001` | 1 | A judge is another model to evaluate |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-002` | 2 | Choose the baseline before judging success |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-003` | 3 | Direct scoring checks an individual answer |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-004` | 4 | Pairwise judgments suit relative preferences |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-005` | 5 | A reference changes the evaluation problem |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-006` | 6 | Measure defects directly when possible |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-007` | 7 | Match agreement metrics to the labels |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-008` | 8 | Critique can become training feedback |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-009` | 9 | More capable critics still need a task-specific test |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-010` | 10 | Summaries can be checked in several ways |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-011` | 11 | Better than overlap metrics is not expert-level |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-012` | 12 | A consistency judge can miss the bad summaries |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-013` | 13 | Prompt sensitivity complicates calibration |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-014` | 14 | World knowledge can conflict with faithfulness |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-015` | 15 | Correctness and support are separate criteria |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-044` | 16 | A true statement can fail faithfulness |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-016` | 17 | Cross-examination trades calls for evidence |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-017` | 18 | G-Eval structures the judgment process |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-018` | 19 | Self-consistency is a signal, not external evidence |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-019` | 20 | Pairwise gains depend on the criterion |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-020` | 21 | Equivalent prompts can produce different preferences |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-021` | 22 | Inspect the confusion matrix behind a correlation |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-045` | 23 | Read precision and recall from ten flags |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-022` | 24 | A diverse panel can beat one expensive judge |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-023` | 25 | More reasoning can be the wrong behavior |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-024` | 26 | Refine the criterion as well as the prompt |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-025` | 27 | Structure and semantics need different controls |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-026` | 28 | Looking at outputs changes what quality means |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-027` | 29 | Human-guided validation can beat automated assertions |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-028` | 30 | Shepherd learns to provide useful criticism |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-029` | 31 | Evaluating critics creates another judgment problem |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-030` | 32 | Ranking candidates is not rejecting defects |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-031` | 33 | Prometheus learns rubric-based scoring |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-032` | 34 | A gold answer can do much of the work |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-033` | 35 | CriticGPT can augment human code review |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-034` | 36 | More detected bugs can bring more false complaints |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-035` | 37 | Human agreement depends on the measurement |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-036` | 38 | Position and length can distort preference |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-046` | 39 | Swap the answers before trusting the winner |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-037` | 40 | A judge can prefer its own style |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-038` | 41 | Fine-tuned judges can fail outside their scheme |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-039` | 42 | Test whether the judge notices deliberate defects |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-040` | 43 | Expert agreement may be harder than crowd agreement |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-041` | 44 | Keep simple matching baselines |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-042` | 45 | Choose the method from the requirement |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-043` | 46 | Development judges and production gates have different budgets |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-015` | `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-044` | A true statement can fail faithfulness |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-021` | `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-045` | Read precision and recall from ten flags |
| `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-036` | `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-046` | Swap the answers before trusting the winner |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-00.webp` / `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-001` | [Original](https://eugeneyan.com/assets/llm-eval-tree.webp) | Image | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `30b48c9ceef74c128b1473fb0e38d2c89ff2741db6cb7cca997eebbe17040582` |
| `images/source-01.webp` / `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-021` | [Original](https://eugeneyan.com/assets/post-ft.webp) | Diagnostic plots for classification tasks | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `16b147c3d381045079efe7fc66c6310229c9cb7f4feec50d6e71c40860924813` |
| `images/source-18.webp` / `evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977-017` | [Original](https://eugeneyan.com/assets/geval.webp) | Overview of G-Eval | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `e6fe1d41f2434e1728ebcf4d41684f8d61ee8bf61336f7c3909ac8044f554ea4` |
