# Doomer reel format, version 2

New collections use **one Markdown file per reel**, with YAML frontmatter for metadata and the actual reader-facing Markdown below it. Styling, code, tables, inline figures and diagrams belong in the body. Do not store a second plain-text body in frontmatter.

```text
dooms/<source-id>/
  001-short-title.md
  002-worked-example.md
  coverage.md
  images/
    background.svg
    source-figure-01.webp
    example-flow.svg
  diagrams/
    example-flow.mmd       # when an editable diagram is created/preserved
  source/
    original.pdf           # unchanged original for PDF inputs
```

Files, including inline figures, use collection-relative paths with `/` separators. Keep all referenced assets inside the collection. Avoid remote image hotlinks, absolute local paths and path traversal. Preserve an original figure's aspect ratio; the separate background should be portrait, preferably 1080×1920.

## Frontmatter

Validate metadata against [reel-markdown.schema.json](reel-markdown.schema.json). The body must be nonempty Markdown.

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer `2` for Markdown reels. |
| `id` | Unique `<source-id>-001` identifier. |
| `title` | Short, plain title for one concept. |
| `background_image` | A real local portrait asset under `images/`; explanatory figures belong inline too. |
| `source_url` | Original supplied URL, unchanged; null for an attachment without a public URL. |
| `source_file` | `source/original.pdf` for a preserved PDF, otherwise null. |
| `source_title` | Title of the full source. |
| `source_type` | `article`, `video` or `pdf`. |
| `source_locator` | Verified section, page or timestamp supporting this reel. |
| `sort_order` | Contiguous integer `1..N`, matching the filename prefix. |
| `language` | Source language, such as `en` or `he`, unless the user requests another. |

## Body and examples

Use ordinary Markdown with useful GFM features: emphasis, lists, code fences and compact tables. Keep raw HTML, CSS and executable content out of the body. The frontmatter title is already the reel title; do not repeat it as an H1.

The example below is fictional and illustrates the format, not an actual source collection:

````markdown
---
schema_version: 2
id: cache-example-a1b2c3d4-002
title: Similar requests can need different answers
background_image: images/background.svg
source_url: https://example.org/caching
source_file: null
source_title: Caching Responses
source_type: article
source_locator: "Section: Cache correctness"
sort_order: 2
language: en
---
Two requests can sound alike and still need **different answers**.

**Illustrative example:** A reader asks for a summary of Film 2. Your cache
finds an answer about Film 3 because the titles are similar. Reusing it is fast,
but wrong.

| Request | Cached answer | Safe to reuse? |
| --- | --- | --- |
| Film 2 | Film 2 | Check freshness |
| Film 2 | Film 3 | No |

![A cache checks the film identifier before reusing an answer.](images/example-flow.svg)

*Added explanatory diagram; toy film titles are not reported study data.*
````

## Source figures and editable diagrams

- Insert figures with `![Meaningful description](images/source-figure-01.webp)`. Use simple filenames without spaces. Include a brief explanation of what to notice and preserve attribution and qualifications where relevant.
- Store actual downloaded or extracted originals. Record origin URL or PDF page/figure, caption, available credit/license details and any modification in a figure table in `coverage.md`. Distinguish original, cropped, redrawn and newly created visuals.
- Keep source code as fenced code and suitable source tables as editable Markdown, not screenshots, when that is clearer. Avoid reproducing large irrelevant tables or articles wholesale.
- Preserve a useful Mermaid diagram in a `mermaid` fence or in `diagrams/*.mmd`. When a reader lacks Mermaid support, include a local SVG/PNG export as the visible figure and keep the editable source. Do not assume Markdown alone makes every diagram renderer available.
- Explanatory images may be wide, square or portrait. Check labels at phone size. Use a dedicated reel or focused crop with context when needed; do not hide a relevant source diagram in a faint background.

## Validation

Run `python .agents/skills/reel-it/scripts/validate_collection.py dooms/<source-id>`. It parses frontmatter and checks schema, order/IDs, consistent source metadata, Markdown image references, asset containment, image decoding and portrait backgrounds. It also checks balanced code fences. It does not prove diagram correctness, readability, source coverage or whether a Markdown renderer supports GFM/Mermaid.

Review the prose and examples against the source separately, and preview the actual formatted text and figures using the available reader. Record missing preview capabilities in `coverage.md` and the delivery.

## Legacy compatibility

Existing version-1 `.yaml` reels remain defined by [reel.schema.json](reel.schema.json), with plain text in `text`. Keep that schema intact because the current application uses it. Do not rewrite existing collections during a skill update or duplicate a reel in both formats.

At this update, `backend/catalog.py` scans `.yaml` files and the React reader renders `text` as plain paragraphs. It does **not** ingest version-2 Markdown files or render their inline assets and Mermaid diagrams. New collections still use the requested Markdown format. Disclose this integration gap until reader support is implemented and verified; publishing files alone is not proof that the app displays them.
