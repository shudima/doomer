# Revamping Skills in Deep Agents

- Author: Sydney Runkle
- Original URL: https://www.langchain.com/blog/revamping-skills-in-deep-agents
- Access date: 2026-10-30
- Language: English
- Tone: practical technical guidance, with product-specific examples and recommendations
- Reels: 10

## Summary

Deep Agents extends progressive skill loading with bound tools, runtime pinning, and controlled reloading, while preserving prompt caching where supported.

## Coverage map

| Substantive section | Reel |
| --- | --- |
| How skills work | 1 |
| Binding tools to skills | 2 |
| Binding tools to skills | 3 |
| Binding tools to skills | 4 |
| Binding tools to skills | 5 |
| Pinned skills | 6 |
| Pinned skills | 7 |
| Reloading skills mid-thread | 8 |
| Reloading skills mid-thread | 9 |
| Get started | 10 |

## Coverage and retrieval limitations

The full public article was retrieved directly from the original URL, with no paywall or pagination gap. Every substantive section is mapped above. Navigation, newsletter forms, unrelated recommendations, and purely promotional resource lists are omitted. No external research was added and no product benchmarks or installations were independently reproduced. Numerical claims and recommendations are attributed to the article or vendor where appropriate.

Article text, captions, and text code blocks were read. Embedded image pixels, animations, and screenshot-only code were not inspected. Reels explain the mechanisms supported by the prose rather than reconstructing uninspected diagrams or promising drop-in code. Any linked guides are references, not additional source material summarized as though read.

## Assets and verification

`images/background.svg` is an original purpose-made 1080×1920 portrait gradient with a faint connected-workflow motif and quiet space for text. It contains no text, active scripts, or third-party assets. No external image credits are required.

YAML schema, unique IDs, contiguous file/order matching, consistent source metadata, contained nonempty images, portrait dimensions and SVG XML are checked. The sequence is compared with the substantive source section map for omissions, redundant ideas, and overstated claims. The first reel was rendered in the running app at a 390×844 phone viewport and visually inspected. Title, paragraphs, controls, and source link fit; the Code Review opening was shortened after the initial preview to preserve the source area. All reels contain 40–90 words.


## Markdown revision — 2026-10-31

Authorized in-place migration: 10 existing dooms retained their identities; 2 labeled illustrative examples added; 12 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `revamping-skills-in-deep-agents-d89ca29f-001` | 1 | Skills disclose knowledge in stages |
| `revamping-skills-in-deep-agents-d89ca29f-002` | 2 | Load a tool with the instructions for using it |
| `revamping-skills-in-deep-agents-d89ca29f-011` | 3 | Load the tool with its procedure |
| `revamping-skills-in-deep-agents-d89ca29f-003` | 4 | Declare the tools in the skill metadata |
| `revamping-skills-in-deep-agents-d89ca29f-004` | 5 | Deferred tools can preserve the cached prefix |
| `revamping-skills-in-deep-agents-d89ca29f-005` | 6 | Resolve tool groups using runtime permissions |
| `revamping-skills-in-deep-agents-d89ca29f-006` | 7 | Explicit requests can skip the discovery round trip |
| `revamping-skills-in-deep-agents-d89ca29f-007` | 8 | Pinning brings instructions and bound tools together |
| `revamping-skills-in-deep-agents-d89ca29f-008` | 9 | Long threads need an explicit refresh mechanism |
| `revamping-skills-in-deep-agents-d89ca29f-012` | 10 | Refresh a skill list at a clear boundary |
| `revamping-skills-in-deep-agents-d89ca29f-009` | 11 | Refresh deliberately because discovery affects caching |
| `revamping-skills-in-deep-agents-d89ca29f-010` | 12 | Scale knowledge without loading everything at once |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `revamping-skills-in-deep-agents-d89ca29f-002` | `revamping-skills-in-deep-agents-d89ca29f-011` | Load the tool with its procedure |
| `revamping-skills-in-deep-agents-d89ca29f-008` | `revamping-skills-in-deep-agents-d89ca29f-012` | Refresh a skill list at a clear boundary |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-02.webp` / `revamping-skills-in-deep-agents-d89ca29f-001` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac683627460955a72092e8a_skill-anatomy.png) | Only a skill's name and description are always in context. The agent reads the instructions on demand, and loads scripts, references, and assets only when needed. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `44cab9f79f0efad166179d5398f8e2ef01428089d036dec24faa87ea7e4a656f` |
| `images/source-06.webp` / `revamping-skills-in-deep-agents-d89ca29f-004` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac683627460955a72092e90_skill-tools.png) | Reading call-transcripts unlocks search_calls and get_transcript. They arrive in a new system message, so the cached prefix above it stays unchanged. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `f52bbc295522998cb6680ad8f09a7a4d63fde4327bf3a6753bce02e695b139e5` |
| `images/source-13.webp` / `revamping-skills-in-deep-agents-d89ca29f-008` | [Original](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6ac683627460955a72092e96_skill-reload.png) | Setting skills_metadata to None makes the next run rescan the skill library and pick up a skill added since the last run. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `b91fba6b4d13f46fecebe5eb0cc44392648253d4d03426fa44c4e3e3ac339af1` |
