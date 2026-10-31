# Coverage audit

- **Source:** Design Patterns in Machine Learning Code and Systems
- **Author:** Eugene Yan (Ziyou Yan)
- **Original URL:** https://eugeneyan.com/writing/design-patterns/
- **Accessed:** 2026-10-30
- **Language:** English
- **Tone:** Practical, explanatory and experience-based; preserve the author's qualifications and distinguish reviewed research from recommendations.
- **Coverage:** Complete at the level of substantive article ideas, examples and qualifications. This is an independently paraphrased reading sequence, not a transcript or reproduction of the article.
- **Dooms:** 14

## Overall summary

A guided explanation of factory, adapter, decorator, strategy, iterator and pipeline patterns in ML code, followed by proxy and mediator patterns in systems.

## Source map and editorial plan

The original body was read through its conclusion before drafting. The plan follows its progression; related details are consolidated into one central idea per doom. Original section headings: Design patterns in libraries and code; Design patterns in systems; References.

| Source section or numbered advice | Dooms |
| --- | --- |
| Introduction | 1 |
| Design patterns in libraries and code — factory | 2 |
| Design patterns in libraries and code — factory examples | 3 |
| Design patterns in libraries and code — adapter | 4 |
| Design patterns in libraries and code — decorator | 5 |
| Design patterns in libraries and code — decorator examples | 6 |
| Design patterns in libraries and code — strategy | 7 |
| Design patterns in libraries and code — iterator | 8 |
| Design patterns in libraries and code — pipeline | 9 |
| Design patterns in libraries and code — pipeline examples | 10 |
| Design patterns in systems — proxy | 11 |
| Design patterns in systems — reverse proxy | 12 |
| Design patterns in systems — mediator | 13 |
| Design patterns in systems — mediator example; conclusion | 14 |

## Limits and deliberate omissions

The complete original article body, inline examples and figure explanations were retrieved successfully. Navigation, sharing links, promotional offers, bibliography entries and acknowledgments are omitted. Code listings are explained conceptually rather than reproduced. Embedded research diagrams and tables are not reprinted cell by cell; the sequence preserves their substantive findings and qualifications as discussed in the article. Linked papers and external resources were not independently treated as additional sources. Model rankings, tool examples and benchmark findings are historical claims from this article, not independently updated recommendations.

## Background asset

`images/background.svg` is an original, purpose-made 1080×1920 vector gradient with quiet abstract shapes. It contains no reel text and uses no third-party image assets. The same background is intentionally shared across the collection.

## Verification

Every YAML is parsed and checked against the project's JSON Schema. Filenames, unique IDs, ordering, source metadata, word lengths and local asset references are checked. The SVG parses and has a portrait 9:16 canvas. Source-to-doom mapping was checked for substantive section coverage, omitted caveats and duplicate ideas. App preview results are recorded after the representative phone-size checks.

Phone-size preview: the first doom was opened in the actual local Doomer reader at 393×730. Topic title, doom total, original source link, background and full text were inspected; no clipping was observed. This was a desktop browser viewport check, not a physical iPhone test.


## Markdown revision — 2026-10-31

Authorized in-place migration: 14 existing dooms retained their identities; 3 labeled illustrative examples added; 17 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-001` | 1 | A pattern communicates intent |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-002` | 2 | A factory hides creation details |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-003` | 3 | Dataset interfaces standardize customization |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-004` | 4 | Adapters turn different formats into one interface |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-015` | 5 | One table, two file formats |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-005` | 6 | A decorator adds behavior around existing code |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-006` | 7 | Cache, fixtures and timing solve different needs |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-007` | 8 | A strategy makes an algorithm replaceable |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-016` | 9 | Swap the scoring rule |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-008` | 10 | Iteration separates traversal from storage |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-009` | 11 | A pipeline makes transformations composable |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-010` | 12 | Pipelines can package a whole modeling flow |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-011` | 13 | A cache proxy can avoid repeated inference |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-012` | 14 | A reverse proxy provides one public entrance |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-013` | 15 | A mediator coordinates services through shared rules |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-014` | 16 | Recommendation widgets need page-level coordination |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-017` | 17 | Remove duplicates across the whole page |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-004` | `design-patterns-in-machine-learning-code-and-systems-40f8e1de-015` | One table, two file formats |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-007` | `design-patterns-in-machine-learning-code-and-systems-40f8e1de-016` | Swap the scoring rule |
| `design-patterns-in-machine-learning-code-and-systems-40f8e1de-014` | `design-patterns-in-machine-learning-code-and-systems-40f8e1de-017` | Remove duplicates across the whole page |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-00.webp` / `design-patterns-in-machine-learning-code-and-systems-40f8e1de-004` | [Original](https://eugeneyan.com/assets/pandas_read.webp) | Non-exhaustive list of adapters to read different file storage formats in Pandas | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `5ba61425462ba79c41915eac9170efdc9d27b0b88f71bc839a967906465e7b7f` |
| `images/source-02.webp` / `design-patterns-in-machine-learning-code-and-systems-40f8e1de-011` | [Original](https://eugeneyan.com/assets/proxy.webp) | Using a cache proxy to serve common requests and reduce compute cost from real-time inference | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `2b47177f61d6a18175b0966f83009d55f301e52c511539138219f1174ac942f8` |
| `images/source-03.webp` / `design-patterns-in-machine-learning-code-and-systems-40f8e1de-012` | [Original](https://eugeneyan.com/assets/load-balancer.gif) | Using a reverse proxy to distribute incoming requests to multiple backend servers | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `f993c6b3c20e7abac31c1d6530b28c6a99f1628a5b87cc2a376c42fd79465f5f` |
| `images/source-04.webp` / `design-patterns-in-machine-learning-code-and-systems-40f8e1de-014` | [Original](https://eugeneyan.com/assets/mediator.webp) | Using a mediator to allocate widgets to placements on the home page | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `17618d292e6d9f4f04755ca8d0341acb7eab9110bf36a4af29bd8b86a0d435f9` |
