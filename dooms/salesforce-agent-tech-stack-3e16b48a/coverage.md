# A Deep Dive into Salesforce’s Agent Tech Stack

- Author: ByteByteGo
- Original: https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent
- Published: 2026-10-26
- Accessed: 2026-10-30 (Asia/Jerusalem)
- Language: English
- Tone: explanatory, technical, practical.
- Summary: Dedicated systems support reliable agent reasoning.

## Coverage audit

Coverage status: complete main-section coverage in abridged concept form; supporting examples are condensed as documented below.

The entire accessible article body was read, including its ending. All substantive headings are mapped below. These are concise concept reels: examples and supporting detail are abridged, rather than reproduced at article length. Figures were not separately analyzed; the prose supplied the information used here. There was no paywall or missing text. Sponsored material, site navigation, reader comments, and recommendations are excluded. No outside research or invented quotations were added. Company and demonstration claims retain source attribution in the relevant cards.

| Source location | Reels |
| --- | --- |
| The naive design: one large prompt | 001 |
| How Agentforce is built | 002 |
| 1. Deterministic instructions with Agent Script | 003 |
| 2. Unified profiles with Data 360 | 004 |
| 3. Relevant context with Agent Context Engine | 005, 006 |
| 4. Permission management with Agent Identity | 007 |
| Where the agent runs | 008 |
| What’s next | 009 |

The opening motivation is covered by 001. The appointment example, detailed matching-rule examples, secondary token comparisons, usage totals, benchmark figures, and the opportunity-search walkthrough are condensed. The eight-instruction observation is Salesforce’s report, not a general model limit. The 124,000-to-9,000 comparison is a demonstration, not an independently verified universal result. The harness is presented as proposed work.

## Assets and checks

`images/network.svg` is original purpose-made vector artwork created for this collection. No third-party imagery or image-generation service was used. It is 1080 × 1920 (9:16), contains no reel text, and leaves the central area quiet.

All reel files were parsed with PyYAML and validated with JSON Schema; IDs, order, source metadata, contained nonempty assets, and SVG dimensions were checked. Editorial audit: each card maps to supporting prose; examples are condensed as listed above. The first reel was rendered and visually inspected in the existing Doomer app at a 420 × 912 browser viewport. The title, prose, source credit, and background were readable without overlap. Screenshot: [preview/001-phone.jpg](preview/001-phone.jpg). This is desktop browser emulation, not a physical-device test.


## Markdown revision — 2026-10-31

Authorized in-place migration: 9 existing dooms retained their identities; 2 labeled illustrative examples added; 11 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `salesforce-agent-tech-stack-3e16b48a-001` | 1 | Prompt limits |
| `salesforce-agent-tech-stack-3e16b48a-002` | 2 | Platform layers |
| `salesforce-agent-tech-stack-3e16b48a-003` | 3 | Rules become code |
| `salesforce-agent-tech-stack-3e16b48a-010` | 4 | Use code for a rule that must always hold |
| `salesforce-agent-tech-stack-3e16b48a-004` | 5 | Link customer records |
| `salesforce-agent-tech-stack-3e16b48a-005` | 6 | Choose context |
| `salesforce-agent-tech-stack-3e16b48a-006` | 7 | Memory needs confirmation |
| `salesforce-agent-tech-stack-3e16b48a-011` | 8 | A possible move is not a confirmed address |
| `salesforce-agent-tech-stack-3e16b48a-007` | 9 | Separate agent permissions |
| `salesforce-agent-tech-stack-3e16b48a-008` | 10 | Discover before dispatch |
| `salesforce-agent-tech-stack-3e16b48a-009` | 11 | A shared harness |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `salesforce-agent-tech-stack-3e16b48a-003` | `salesforce-agent-tech-stack-3e16b48a-010` | Use code for a rule that must always hold |
| `salesforce-agent-tech-stack-3e16b48a-006` | `salesforce-agent-tech-stack-3e16b48a-011` | A possible move is not a confirmed address |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-05.webp` / `salesforce-agent-tech-stack-3e16b48a-002` | [Original](https://substackcdn.com/image/fetch/$s_!X5dE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F369f1a8b-272d-4ae3-a2be-2df43c632b89_2048x1942.png) | Surface layer: The places where a person talks to the agent, such as a Claude chat or Slack. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `e72e568e075f836939cb43671f3f8b12d07148142571eb0b15b5532c95237bb0` |
| `images/source-07.webp` / `salesforce-agent-tech-stack-3e16b48a-003` | [Original](https://substackcdn.com/image/fetch/$s_!1V2V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6ef82f6-8652-41dd-9724-4b7f15abdf36_2048x650.png) | How does it work? You just write the agent’s behavior in an Agent Script file. That file is compiled into a structured specification called the Agent Graph, and the Agent Graph is executed by the Atlas Reasoning Engine, the runtime behind Agentforce. The engine runs the code parts and calls the model when reasoning is needed. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `0304193d3c71a1bc8dac872ed0d76d5f65c901c5b16dabaef4ab9ddc18184ad8` |
| `images/source-13.webp` / `salesforce-agent-tech-stack-3e16b48a-004` | [Original](https://substackcdn.com/image/fetch/$s_!cYru!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21c1405b-957d-48c4-92cc-4af9578a8a6d_2048x784.png) | Step 3: Resolve identities. This step handles situations where records from different sources describe the same person. In Data 360, this is done by match rules that an admin can configure. A rule can be an exact match (such as the same email address), a fuzzy rule that allows small differences, or a normalized rule, which cleans up a field before comparing it. This way, two phone numbers written in different formats will match. Note that the sou | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `bfd26ae6444ed477b6b71fc2e0407b3b16ff3e0d843118c764d11034a1659d31` |
| `images/source-19.webp` / `salesforce-agent-tech-stack-3e16b48a-007` | [Original](https://substackcdn.com/image/fetch/$s_!HZ9g!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F458aef94-804f-4f1f-beb9-63ccf888b883_2048x791.png) | With Agent Identity, when an agent authenticates, there are two tokens, one for the agent and one for the user it is acting for. Before an operation runs, Salesforce checks the user’s permissions, the agent’s permissions, and the data policies. The operation runs only if none of them deny it. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `37db4f2662bc9d4bab5bb89d61abe7d881127bb89f2804bbba4c0888062ebadf` |
