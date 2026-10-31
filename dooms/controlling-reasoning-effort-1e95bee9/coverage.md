# Controlling Reasoning Effort in LLMs

- Author: Sebastian Raschka, PhD
- Source URL: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
- Access date: 2026-10-30
- Language: English
- Tone: conversational technical explanation, with explicit uncertainty about undisclosed implementations.
- Collection: controlling-reasoning-effort-1e95bee9
- Reel count: 35

## Summary

Reasoning-effort controls select learned behaviors and/or apply external budgets. The article explains RLVR, inference scaling, thinking delimiters and hybrid modes, then distinguishes documented open-model mechanisms from hypotheses about proprietary systems. It compares DeepSeek V4, Nemotron 3 Ultra, Kimi K2.5 and the Kimi K3 update, GLM-5, Qwen3 and Inkling, ending with the cost-quality tradeoff and the prospect of automatic routing.

## Source map

| Section | Reels |
| --- | --- |
| Introduction; 1. A brief definition of reasoning models | 1 |
| 2. A brief overview of training and inference scaling reasoning models | 2 |
| 2.1 Training reasoning models | 3 |
| 2.2 “Aha” moments | 4 |
| 2.2 “Aha” moments | 5 |
| 2.3 Inference scaling in a nutshell | 6 |
| 3. Think tokens | 7 |
| 3. Think tokens | 8 |
| 4. Reasoning mode on and off switches | 9 |
| 4. Reasoning mode on and off switches | 10 |
| 4. Reasoning mode on and off switches | 11 |
| 5.1 Reasoning effort and response length and quality | 12 |
| 5.1 Reasoning effort and response length and quality | 13 |
| 5.2 Possible effort level implementations | 14 |
| 5.2 Possible effort level implementations | 15 |
| 5.3 Inkling case study | 16 |
| 5.4 A short note about inference scaling versus training scaling | 17 |
| 5.4 A short note about inference scaling versus training scaling | 18 |
| 6.1 DeepSeek V4 trains separate effort specialists | 19 |
| 6.1 DeepSeek V4 trains separate effort specialists | 20 |
| 6.2 Nemotron 3 Ultra combines learned modes with hard budgets | 21 |
| 6.2.1 Using Nemotron reasoning budgets during inference | 22 |
| 6.2.2 Reasoning budget-aware training in Nemotron | 23 |
| 6.3.1 Kimi’s Toggle method | 24 |
| 6.3.1 Kimi’s Toggle method | 25 |
| 6.3.2 What Toggle changes at inference | 26 |
| 6.3.3 Kimi K3 (Update) | 27 |
| 6.3.3 Kimi K3 (Update) | 28 |
| 6.4 GLM-5 introduces turn-level and interleaved thinking through SFT | 29 |
| 6.4 GLM-5 introduces turn-level and interleaved thinking through SFT | 30 |
| 6.5 Qwen3 uses mode fusion and inference-time truncation | 31 |
| 6.6 Inkling conditions RL on a continuous effort value | 32 |
| 6.7 Overview of the known recipes | 33 |
| 7. Conclusion | 34 |
| 7. Conclusion | 35 |

## Coverage and limitations

Complete coverage of the substantive public prose, including all numbered subsections and the later Kimi K3 update. Retrieved the original URL directly with no paywall or pagination gap. Figure captions were read; embedded figure pixels were not inspected. No exact numerical benchmark results were inferred from figure-only tables. The prose and captions fully support the claims selected for these reels. Promotional book material, related-story embeds, and subscription appeals are omitted. No external research or independent reproduction of training and benchmark results was performed.

Proprietary GPT implementation ideas remain explicitly hypotheses. Inkling's reward description remains conceptual, without invented coefficients. The Kimi K2.5 discussion preserves the difference between Toggle training and the separate inference switch; the later K3 report update supersedes the earlier lack of K3 training details. The historical comments about GPT Auto being removed are not independently verified or generalized as current interface facts. The conclusion retains automatic routing as an aspiration.

## Assets and checks

`images/effort.svg` is an original 1080×1920 portrait background showing faint compute levels and an abstract diminishing-returns curve, with quiet space for text. No third-party images or licenses are involved. It is decorative, not a numerical chart; no reel text is baked into it.

Each reel is parsed and validated against the project JSON Schema, checked for unique IDs, contiguous order, matching filenames, consistent metadata, image containment, valid nonempty portrait SVG, and suitable text length. The sequence was checked against the complete section map for omissions and unsupported certainty. The first reel was rendered in the running app at 390×844 and its screenshot visually inspected: title, complete body, source link, and controls fit legibly. Reel text lengths are 65–79 words.


## Markdown revision — 2026-10-31

Authorized in-place migration: 35 existing dooms retained their identities; 2 labeled illustrative examples added; 37 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `controlling-reasoning-effort-1e95bee9-001` | 1 | What reasoning effort actually controls |
| `controlling-reasoning-effort-1e95bee9-002` | 2 | Two ways to spend more compute |
| `controlling-reasoning-effort-1e95bee9-003` | 3 | Reward answers that can be checked |
| `controlling-reasoning-effort-1e95bee9-004` | 4 | Self-correction can emerge from outcome rewards |
| `controlling-reasoning-effort-1e95bee9-005` | 5 | R1-Zero was the proof of concept |
| `controlling-reasoning-effort-1e95bee9-006` | 6 | Longer traces are only one strategy |
| `controlling-reasoning-effort-1e95bee9-007` | 7 | Think tags mark a boundary |
| `controlling-reasoning-effort-1e95bee9-008` | 8 | Formatting is a separate reward |
| `controlling-reasoning-effort-1e95bee9-009` | 9 | Why an off switch matters |
| `controlling-reasoning-effort-1e95bee9-010` | 10 | Teach both response styles |
| `controlling-reasoning-effort-1e95bee9-011` | 11 | Soft instructions versus a hard prefix |
| `controlling-reasoning-effort-1e95bee9-012` | 12 | An effort label can be ordinary text |
| `controlling-reasoning-effort-1e95bee9-013` | 13 | More effort has diminishing returns |
| `controlling-reasoning-effort-1e95bee9-014` | 14 | Train the reward around the requested effort |
| `controlling-reasoning-effort-1e95bee9-015` | 15 | Supervised examples offer another route |
| `controlling-reasoning-effort-1e95bee9-016` | 16 | Inkling uses a continuous effort value |
| `controlling-reasoning-effort-1e95bee9-017` | 17 | Model choice and effort are separate knobs |
| `controlling-reasoning-effort-1e95bee9-036` | 18 | Compare model and effort together |
| `controlling-reasoning-effort-1e95bee9-018` | 19 | API price is not raw compute |
| `controlling-reasoning-effort-1e95bee9-019` | 20 | DeepSeek V4 learns three behaviors |
| `controlling-reasoning-effort-1e95bee9-020` | 21 | Distill specialists into one checkpoint |
| `controlling-reasoning-effort-1e95bee9-021` | 22 | Nemotron separates efficient from regular reasoning |
| `controlling-reasoning-effort-1e95bee9-022` | 23 | Learned effort is not a token cap |
| `controlling-reasoning-effort-1e95bee9-037` | 24 | A token ceiling is not a learned plan |
| `controlling-reasoning-effort-1e95bee9-023` | 25 | Practice answering after an interrupted trace |
| `controlling-reasoning-effort-1e95bee9-024` | 26 | A fixed budget can teach the wrong habit |
| `controlling-reasoning-effort-1e95bee9-025` | 27 | Shorten reasoning after the model can solve |
| `controlling-reasoning-effort-1e95bee9-026` | 28 | Toggle does not create a runtime toggle |
| `controlling-reasoning-effort-1e95bee9-027` | 29 | Kimi K3 trains with explicit budget consequences |
| `controlling-reasoning-effort-1e95bee9-028` | 30 | Nine specialists, one Kimi model |
| `controlling-reasoning-effort-1e95bee9-029` | 31 | Three thinking behaviors are not three effort levels |
| `controlling-reasoning-effort-1e95bee9-030` | 32 | GLM’s template selects the response path |
| `controlling-reasoning-effort-1e95bee9-031` | 33 | Qwen’s hard budget was not explicitly trained |
| `controlling-reasoning-effort-1e95bee9-032` | 34 | Continuous control still needs training |
| `controlling-reasoning-effort-1e95bee9-033` | 35 | The same menu can hide different machinery |
| `controlling-reasoning-effort-1e95bee9-034` | 36 | There is no controlled winner yet |
| `controlling-reasoning-effort-1e95bee9-035` | 37 | Automatic effort is the next practical goal |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `controlling-reasoning-effort-1e95bee9-017` | `controlling-reasoning-effort-1e95bee9-036` | Compare model and effort together |
| `controlling-reasoning-effort-1e95bee9-022` | `controlling-reasoning-effort-1e95bee9-037` | A token ceiling is not a learned plan |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-03.webp` / `controlling-reasoning-effort-1e95bee9-002` | [Original](https://substackcdn.com/image/fetch/$s_!Uf-n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4efb291d-6cd3-4fba-ab3a-bac088cb2601_1999x961.png) | Figure 4: Training and inference-scaling are two ways to improve LLM and reasoning model problem-solving capabilities. Plot based on Learning to reason with LLMs | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `4d2a8497fd155835785733d3c9e3c8a265d09d1060458d5bb221f9f294ac3a18` |
| `images/source-06.webp` / `controlling-reasoning-effort-1e95bee9-004` | [Original](https://substackcdn.com/image/fetch/$s_!Vm06!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe934cf9d-40a0-4907-9505-275bbbbb4864_1999x1413.png) | Figure 7: An example of an aha moment, where a reasoning model notices an error in its intermediate reasoning and corrects it before producing the final answer. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `b021db89c650babab06252010fe32a360b4b00b49d749ed077037e35cb060524` |
| `images/source-08.webp` / `controlling-reasoning-effort-1e95bee9-005` | [Original](https://substackcdn.com/image/fetch/$s_!_0KN!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918b28a0-01aa-45b0-91ec-21f2624276d6_1999x1508.png) | Figure 9: More detailed reasoning model training pipeline. This one depicts the various DeepSeek-R1 models. For more details, see my other article: Understanding Reasoning LLMs | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `6c231ae48d219d358c32eb09565a637076c7bd8495d4a775885a1eed1d4102b8` |
