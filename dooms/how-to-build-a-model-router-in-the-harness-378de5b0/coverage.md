# How to Build a Model Router in the Harness

- Author: Sydney Runkle and Eugene Yurtsev
- Original URL: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
- Access date: 2026-10-30
- Language: English
- Tone: practical technical guidance, with product-specific examples and recommendations
- Reels: 14

## Summary

An Open SWE router uses task-specific harness context and three model tiers; live experiments report substantial cost savings without a measurable merged-PR regression, with clear limits.

## Coverage map

| Substantive section | Reel |
| --- | --- |
| Introduction | 1 |
| Step 1: understand the tasks | 2 |
| Step 1: understand the tasks | 3 |
| Step 2: understand the models | 4 |
| Step 3: build the router in the harness | 5 |
| Step 3: build the router in the harness | 6 |
| Step 4: track task outcomes | 7 |
| The experiment | 8 |
| The experiment | 9 |
| The experiment | 10 |
| The experiment | 11 |
| What's next | 12 |
| What's next | 13 |
| Getting started | 14 |

## Coverage and retrieval limitations

The full public article was retrieved directly from the original URL, with no paywall or pagination gap. Every substantive section is mapped above. Navigation, newsletter forms, unrelated recommendations, and purely promotional resource lists are omitted. No external research was added and no product benchmarks or installations were independently reproduced. Numerical claims and recommendations are attributed to the article or vendor where appropriate.

Article text, captions, and text code blocks were read. Embedded image pixels, animations, and screenshot-only code were not inspected. Reels explain the mechanisms supported by the prose rather than reconstructing uninspected diagrams or promising drop-in code. Any linked guides are references, not additional source material summarized as though read.

## Assets and verification

`images/background.svg` is an original purpose-made 1080×1920 portrait gradient with a faint connected-workflow motif and quiet space for text. It contains no text, active scripts, or third-party assets. No external image credits are required.

YAML schema, unique IDs, contiguous file/order matching, consistent source metadata, contained nonempty images, portrait dimensions and SVG XML are checked. The sequence is compared with the substantive source section map for omissions, redundant ideas, and overstated claims. The first reel was rendered in the running app at a 390×844 phone viewport and visually inspected. Title, paragraphs, controls, and source link fit; the Code Review opening was shortened after the initial preview to preserve the source area. All reels contain 40–90 words.

The benchmark and traffic observations are dated evidence, not current model rankings. The 973-thread A/B test supplies no proof of universal quality equivalence; the fast-only test was stopped before statistical significance. Planned mid-thread and subagent routing remain future work.


## Markdown revision — 2026-10-31

Authorized in-place migration: 14 existing dooms retained their identities; 2 labeled illustrative examples added; 16 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `how-to-build-a-model-router-in-the-harness-378de5b0-001` | 1 | Choose the model that fits the task |
| `how-to-build-a-model-router-in-the-harness-378de5b0-002` | 2 | Start by examining real traffic |
| `how-to-build-a-model-router-in-the-harness-378de5b0-003` | 3 | Cost and turn count are imperfect complexity signals |
| `how-to-build-a-model-router-in-the-harness-378de5b0-004` | 4 | Pick tiers along the cost-quality frontier |
| `how-to-build-a-model-router-in-the-harness-378de5b0-005` | 5 | Give the classifier criteria from your domain |
| `how-to-build-a-model-router-in-the-harness-378de5b0-015` | 6 | Give a router observable criteria |
| `how-to-build-a-model-router-in-the-harness-378de5b0-006` | 7 | The first version makes one choice per thread |
| `how-to-build-a-model-router-in-the-harness-378de5b0-007` | 8 | Define success before optimizing cost |
| `how-to-build-a-model-router-in-the-harness-378de5b0-016` | 9 | Count completed tasks before celebrating savings |
| `how-to-build-a-model-router-in-the-harness-378de5b0-008` | 10 | No measurable regression is not proof of equality |
| `how-to-build-a-model-router-in-the-harness-378de5b0-009` | 11 | The median thread cost fell by 64% |
| `how-to-build-a-model-router-in-the-harness-378de5b0-010` | 12 | Most requests went below the performance tier |
| `how-to-build-a-model-router-in-the-harness-378de5b0-011` | 13 | Always using the fast model did not hold up |
| `how-to-build-a-model-router-in-the-harness-378de5b0-012` | 14 | Rerouting can trade capability for cache cost |
| `how-to-build-a-model-router-in-the-harness-378de5b0-013` | 15 | Subagents and better feedback are further opportunities |
| `how-to-build-a-model-router-in-the-harness-378de5b0-014` | 16 | Treat routing as context engineering |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `how-to-build-a-model-router-in-the-harness-378de5b0-005` | `how-to-build-a-model-router-in-the-harness-378de5b0-015` | Give a router observable criteria |
| `how-to-build-a-model-router-in-the-harness-378de5b0-007` | `how-to-build-a-model-router-in-the-harness-378de5b0-016` | Count completed tasks before celebrating savings |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-05.webp` / `how-to-build-a-model-router-in-the-harness-378de5b0-004` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6abdca4ecb95b9007a8609ea_router-pareto.png) | Intelligence vs. cost per task, with the Pareto frontier, the three models we selected for our router, and a few other models for context. Chart data: Artificial Analysis Intelligence Index , as of Sep 9, 2026. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `423d1fafded2720a23798309b83028b9eb92d3d21016eeeae82bbd55864386db` |
| `images/source-07.webp` / `how-to-build-a-model-router-in-the-harness-378de5b0-009` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6abdca4ecb95b9007a8609e4_exp1-cost-per-thread.png) | LLM cost per thread, Sep 16 to 22 (log scale): always GPT-6 Astra vs. routed, and routed threads split by tier. Tier violin widths scale with thread count. White lines and labels mark the median. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `5cb84823d3c05df43ccd4404a51a768226dc10647dac8e9edce17b417aea19b7` |
