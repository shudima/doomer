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
