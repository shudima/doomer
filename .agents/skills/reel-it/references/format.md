# Doomer reel format, version 1

The unit displayed by the future app is one YAML file. Scan only `*.yaml` at the root of each collection folder; sort by the integer `sort_order`. Paths in a reel are relative to its collection folder, use `/`, and must stay inside that folder. JSON Schema: [reel.schema.json](reel.schema.json).

```text
/home/dima/projects/doomer/dooms/<source-id>/
  001-short-title.yaml
  002-next-idea.yaml
  coverage.md
  images/
    001.svg
    002.webp
  source/
    original.pdf        # only when the source is a PDF attachment
```

## Fields

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer `1`. |
| `id` | Unique reel ID, `<source-id>-001`, etc. |
| `title` | Short reader-facing title. |
| `text` | Final reader-facing prose. Prefer a YAML literal block using the pipe character followed by a minus sign. |
| `background_image` | Actual local image, e.g. `images/001.svg`; no external image URLs or prompts. |
| `source_url` | Original supplied HTTP(S) URL, unchanged, including a video URL or PDF URL. Null when the source is only a local attachment. Do not invent a public URL. |
| `source_file` | `source/original.pdf` for a copied PDF attachment; null for URL-only sources. If a PDF has both a URL and a local copy, populate both fields. |
| `source_title` | Title of the whole source; use a clearly descriptive title if untitled. |
| `source_type` | `article`, `video`, or `pdf`. |
| `source_locator` | Human-readable supporting location, e.g. `Pages 3–5`, `00:02:10–00:03:04`, or `Section: Why memory fails`. Never invent page numbers or timestamps. |
| `sort_order` | Integer `1..N`, contiguous within a collection, matching the filename's number. |
| `language` | Language code such as `en`, `he`, or `pt-BR`; preserve the source language by default. |

Required keys are intentionally flat so the future app can read each file independently. Do not add implementation notes to `text`. Keep all reel metadata consistent for one source.

The app can show `title` and `text` over `background_image`, with a dark scrim chosen to keep text legible, wrapping at a comfortable phone width and respecting right-to-left languages. Do not design around tiny font sizes. These are presentation expectations for the later app, not an instruction to build it now.

## Example of an article reel

This is a fictional format example, not output from a real source. On an actual run, supply the real original URL and create the referenced image.

```yaml
schema_version: 1
id: "memory-example-a1b2c3d4-001"
title: "Remembering takes attention"
text: |-
  You can look straight at something and still fail to remember it.
  In this account, attention is the first step: it helps determine
  which details get a chance to become a lasting memory.

  That does not make attention a guarantee. The point is narrower:
  before asking why a memory faded, consider whether you noticed
  the detail clearly in the first place.
background_image: "images/001.svg"
source_url: "https://example.org/memory-and-attention"
source_file: null
source_title: "Memory and Attention"
source_type: "article"
source_locator: "Section: Attention comes first"
sort_order: 1
language: "en"
```

For a PDF attachment, use `source_type: "pdf"`, `source_url: null`, `source_file: "source/original.pdf"`, and a verified page locator. That gives the future app a durable local source to open even though the attachment has no original web link.
