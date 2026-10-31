# How Uber Built A Gateway For AI Agents To Access Tools

- Author: ByteByteGo
- Original: https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents
- Published: 2026-10-28
- Accessed: 2026-10-30 (Asia/Jerusalem)
- Language: English
- Tone: explanatory, technical, practical.
- Summary: Existing services become governed agent capabilities.

## Coverage audit

Coverage status: complete main-section coverage in abridged concept form; supporting examples are condensed as documented below.

The entire accessible article body was read, including its ending. All substantive headings are mapped below. These are concise concept reels: examples and supporting detail are abridged, rather than reproduced at article length. Figures were not separately analyzed; the prose supplied the information used here. There was no paywall or missing text. Sponsored material, site navigation, reader comments, and recommendations are excluded. No outside research or invented quotations were added. Company and demonstration claims retain source attribution in the relevant cards.

| Source location | Reels |
| --- | --- |
| Why AI Agents Need Tools; The Role of MCP at Uber | 001 |
| How the Uber MCP Gateway is Designed | 002 |
| How Tools Are Discovered | 003 |
| Discovering Tools vs Permission to Use Them | 004 |
| How Uber’s MCP Gateway Works | 005 |
| How the Gateway Takes Care of Access | 006 |
| How the Uber MCP Gateway Deals With A Huge Catalog | 007 |
| Conclusion | 008 |

The opening is covered by 001. Discovery covers both contract-derived tools and native servers. Detailed schema examples, listTools mechanics, and individual token-exchange hops are condensed. The conclusion is 008.

## Assets and checks

`images/network.svg` is original purpose-made vector artwork created for this collection. No third-party imagery or image-generation service was used. It is 1080 × 1920 (9:16), contains no reel text, and leaves the central area quiet.

All reel files were parsed with PyYAML and validated with JSON Schema; IDs, order, source metadata, contained nonempty assets, and SVG dimensions were checked. Editorial audit: each card maps to supporting prose; examples are condensed as listed above. The first reel was rendered and visually inspected in the existing Doomer app at a 420 × 912 browser viewport. The title, prose, source credit, and background were readable without overlap. Screenshot: [preview/001-phone.jpg](preview/001-phone.jpg). This is desktop browser emulation, not a physical-device test.


## Markdown revision — 2026-10-31

Authorized in-place migration: 8 existing dooms retained their identities; 2 labeled illustrative examples added; 10 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `uber-mcp-gateway-31398518-001` | 1 | Tools reach systems |
| `uber-mcp-gateway-31398518-002` | 2 | Two planes |
| `uber-mcp-gateway-31398518-003` | 3 | Automate discovery |
| `uber-mcp-gateway-31398518-004` | 4 | Owners enable access |
| `uber-mcp-gateway-31398518-005` | 5 | Translate every call |
| `uber-mcp-gateway-31398518-009` | 6 | Follow a call through the gateway |
| `uber-mcp-gateway-31398518-006` | 7 | Check the caller |
| `uber-mcp-gateway-31398518-007` | 8 | Keep context small |
| `uber-mcp-gateway-31398518-010` | 9 | Discover a small toolset for one task |
| `uber-mcp-gateway-31398518-008` | 10 | Reuse existing APIs |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `uber-mcp-gateway-31398518-005` | `uber-mcp-gateway-31398518-009` | Follow a call through the gateway |
| `uber-mcp-gateway-31398518-007` | `uber-mcp-gateway-31398518-010` | Discover a small toolset for one task |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-03.webp` / `uber-mcp-gateway-31398518-002` | [Original](https://substackcdn.com/image/fetch/$s_!n_le!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F95275c8e-ba05-4377-9ee4-9610e42e8e0a_3304x1878.png) | Source: Uber Engineering Blog | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `5dbbd421dd1980f54e5f50442fbceb5b4b9ac00c202a2a178645919acfb530ff` |
| `images/source-05.webp` / `uber-mcp-gateway-31398518-005` | [Original](https://substackcdn.com/image/fetch/$s_!9gky!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F608cc4f1-c016-41af-8208-7f2ddeb83f8e_4384x2568.png) | To understand things in a better way, it’s good to follow the path of a request through the gateway. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `f338f071fa9a61e8f0f1f1ebb9659a1347ed52f3308093011c316ff56f866956` |
| `images/source-06.webp` / `uber-mcp-gateway-31398518-007` | [Original](https://substackcdn.com/image/fetch/$s_!saqB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa381b984-1306-4e56-890e-ea73e295209d_3802x2030.png) | Source: Uber Engineering Blog | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `a80feb20c0ab0a1c28d6005cd54927fe7dac749d5bbfbf2e619f75972796172e` |
