# Context Engineering: How Deep Agents Remember

- Author: Jess Weng
- Original URL: https://www.langchain.com/blog/context-engineering-deep-agents-remember
- Access date: 2026-10-30
- Language: English
- Tone: practical technical guidance, with product-specific examples and recommendations
- Reels: 12

## Summary

Deep Agents manages active context through recoverable offloading, summarization, skills, isolated work, and plain-file memory that survives provider changes.

## Coverage map

| Substantive section | Reel |
| --- | --- |
| Understanding context engineering techniques | 1 |
| Applying context engineering to common use cases | 2 |
| How to implement these techniques: middleware | 3 |
| Offloading: keeping it out the context window | 4 |
| Offloading: keeping it out the context window | 5 |
| Summarization: compacting what's already there | 6 |
| Summarization: compacting what's already there | 7 |
| Skills: load information only when it's needed | 8 |
| Subagents: isolate the noisy work | 9 |
| Long-term memory: persist across conversations | 10 |
| Swap the model, keep the memory | 11 |
| Context engineering strategies to keep in mind; Try it | 12 |

## Coverage and retrieval limitations

The full public article was retrieved directly from the original URL, with no paywall or pagination gap. Every substantive section is mapped above. Navigation, newsletter forms, unrelated recommendations, and purely promotional resource lists are omitted. No external research was added and no product benchmarks or installations were independently reproduced. Numerical claims and recommendations are attributed to the article or vendor where appropriate.

Article text, captions, and text code blocks were read. Embedded image pixels, animations, and screenshot-only code were not inspected. Reels explain the mechanisms supported by the prose rather than reconstructing uninspected diagrams or promising drop-in code. Any linked guides are references, not additional source material summarized as though read.

## Assets and verification

`images/background.svg` is an original purpose-made 1080×1920 portrait gradient with a faint connected-workflow motif and quiet space for text. It contains no text, active scripts, or third-party assets. No external image credits are required.

YAML schema, unique IDs, contiguous file/order matching, consistent source metadata, contained nonempty images, portrait dimensions and SVG XML are checked. The sequence is compared with the substantive source section map for omissions, redundant ideas, and overstated claims. The first reel was rendered in the running app at a 390×844 phone viewport and visually inspected. Title, paragraphs, controls, and source link fit; the Code Review opening was shortened after the initial preview to preserve the source area. All reels contain 40–90 words.


## Markdown revision — 2026-10-31

Authorized in-place migration: 12 existing dooms retained their identities; 2 labeled illustrative examples added; 14 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `context-engineering-deep-agents-remember-eeb5997d-001` | 1 | More history can make an agent less accurate |
| `context-engineering-deep-agents-remember-eeb5997d-002` | 2 | Research creates context the final draft no longer needs |
| `context-engineering-deep-agents-remember-eeb5997d-003` | 3 | Middleware changes context at the right moment |
| `context-engineering-deep-agents-remember-eeb5997d-004` | 4 | Offload large tool results before they enter |
| `context-engineering-deep-agents-remember-eeb5997d-013` | 5 | Keep the large report within reach |
| `context-engineering-deep-agents-remember-eeb5997d-005` | 6 | Large user messages can be offloaded too |
| `context-engineering-deep-agents-remember-eeb5997d-006` | 7 | Summarize the gradual climb |
| `context-engineering-deep-agents-remember-eeb5997d-007` | 8 | Make compaction recoverable and repeatable |
| `context-engineering-deep-agents-remember-eeb5997d-014` | 9 | Make a summary useful for recovery |
| `context-engineering-deep-agents-remember-eeb5997d-008` | 10 | Keep procedures in a menu until needed |
| `context-engineering-deep-agents-remember-eeb5997d-009` | 11 | Return the result instead of the research trail |
| `context-engineering-deep-agents-remember-eeb5997d-010` | 12 | Save durable preferences as files |
| `context-engineering-deep-agents-remember-eeb5997d-011` | 13 | Memory can outlive the model provider |
| `context-engineering-deep-agents-remember-eeb5997d-012` | 14 | Keep the evidence reachable, not always visible |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `context-engineering-deep-agents-remember-eeb5997d-004` | `context-engineering-deep-agents-remember-eeb5997d-013` | Keep the large report within reach |
| `context-engineering-deep-agents-remember-eeb5997d-007` | `context-engineering-deep-agents-remember-eeb5997d-014` | Make a summary useful for recovery |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-02.webp` / `context-engineering-deep-agents-remember-eeb5997d-003` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac7d0681e478429d6f14812_agent-harness-light.png) | Harness = surrounds the model (LLM) | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `594a6f7b3ffdd7f58ea9707cc07471575b557ab1559c57515d2983c2b754689a` |
| `images/source-04.webp` / `context-engineering-deep-agents-remember-eeb5997d-006` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac7d1ec1e9634285e74f7ec_context-management-light-1.png) | Offloading stops the small spikes, while summarization “resets” the overall climb | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `1116eb1ef08a77dbdafb7c2ca7401732a480c3eb74ff0077e3e7bfbdda4e69a1` |
| `images/source-06.webp` / `context-engineering-deep-agents-remember-eeb5997d-008` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac7d428941b180be1e389ce_skill-anatomy-light.png) | Anatomy of a skill folder | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `53d0cb8598b2bfd67be6391e8b3d6f3d84823084cd5c22eea7ad1997fec2b881` |
| `images/source-08.webp` / `context-engineering-deep-agents-remember-eeb5997d-009` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac7d4926b0fa2c1f904c517_subagents-light-still.png) | Offloading effectively combats oversized results, but subagents are a good design choice for work you already know will be noisy (like researching a company across dozens of searches and pages). The subagent does that work in its own context window and returns only the final result so that the main agent never sees the “noise”. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `507ea117dd11b63b1641514195fd70e106829f192eead8d0f764afbaafea6271` |
