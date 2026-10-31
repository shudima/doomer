# Building agents: When to fold subagents into your main agent loop

- Author: Diane Sarkis
- Original URL: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
- Access date: 2026-10-30
- Language: English
- Tone: practical technical guidance, with product-specific examples and recommendations
- Reels: 19

## Summary

Anthropic describes selectively consolidating enterprise agent systems into one loop with progressively loaded skills and tools, retaining subagents where measured benefits justify them and migrating through task-completion evals.

## Coverage map

| Substantive section | Reel |
| --- | --- |
| Introduction | 1 |
| Introduction | 2 |
| Agent building failure modes for large organizations | 3 |
| Using an agent loop with progressive disclosure | 4 |
| Using an agent loop with progressive disclosure | 5 |
| Using an agent loop with progressive disclosure | 6 |
| How to fold subagents into the main agent loop | 7 |
| How to fold subagents into the main agent loop | 8 |
| Task-completion evals | 9 |
| Combining domain agents | 10 |
| Subagents called as tools | 11 |
| Folding subagents into the main agent via skills and tools | 12 |
| Folding subagents into the main agent via skills and tools | 13 |
| MCP tools | 14 |
| MCP tools | 15 |
| Skills | 16 |
| Knowledge bases | 17 |
| Tools to accelerate this work | 18 |
| Conclusion | 19 |

## Coverage and retrieval limitations

The full public article was retrieved directly from the original URL, with no paywall or pagination gap. Every substantive section is mapped above. Navigation, newsletter forms, unrelated recommendations, and purely promotional resource lists are omitted. No external research was added and no product benchmarks or installations were independently reproduced. Numerical claims and recommendations are attributed to the article or vendor where appropriate.

Article text, captions, and text code blocks were read. Embedded image pixels, animations, and screenshot-only code were not inspected. Reels explain the mechanisms supported by the prose rather than reconstructing uninspected diagrams or promising drop-in code. Any linked guides are references, not additional source material summarized as though read.

## Assets and verification

`images/background.svg` is an original purpose-made 1080×1920 portrait gradient with a faint connected-workflow motif and quiet space for text. It contains no text, active scripts, or third-party assets. No external image credits are required.

YAML schema, unique IDs, contiguous file/order matching, consistent source metadata, contained nonempty images, portrait dimensions and SVG XML are checked. The sequence is compared with the substantive source section map for omissions, redundant ideas, and overstated claims. The first reel was rendered in the running app at a 390×844 phone viewport and visually inspected. Title, paragraphs, controls, and source link fit; the Code Review opening was shortened after the initial preview to preserve the source area. All reels contain 40–90 words.

The consolidation recommendations are observations from enterprise deployments, not a prohibition on subagents. Cases supporting isolated contexts, parallel work, verification, and permission boundaries are retained. Linked migration tools are described without being invoked or treating the article as instructions to modify this project.


## Markdown revision — 2026-10-31

Authorized in-place migration: 19 existing dooms retained their identities; 2 labeled illustrative examples added; 21 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-001` | 1 | Some specialist agents can become skills |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-002` | 2 | Keep subagents when the boundary earns its cost |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-003` | 3 | Team ownership can create architectural sprawl |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-004` | 4 | Shared context can connect related work |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-005` | 5 | Revisit structures built for older models |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-006` | 6 | Own quality centrally and split by context |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-020` | 7 | Separate by useful context |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-007` | 8 | One loop can plan and execute together |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-008` | 9 | Put procedure in skills and hard rules in tools |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-009` | 10 | Build the comparison before the migration |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-010` | 11 | Merge the specialists that already share work |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-011` | 12 | A tool call can preserve the main conversation |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-012` | 13 | Compare one replacement at a time |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-013` | 14 | Repeat tests for important workflow chains |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-014` | 15 | Design tools around user intent |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-015` | 16 | Let tools enforce prerequisites and permissions |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-016` | 17 | Keep ownership while changing the artifact |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-017` | 18 | Retrieve reference facts when they are useful |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-021` | 19 | Retrieve the policy when the task needs it |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-018` | 20 | Use migration tooling to support measured changes |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-019` | 21 | Keep the architecture that survives measurement |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-006` | `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-020` | Separate by useful context |
| `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-017` | `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-021` | Retrieve the policy when the task needs it |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-01.webp` / `building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2-006` | [Original](https://assets.claude.com/cd4b9c4417d5ba31776e8aa79e204966c08c6a43.png) | subagents split by problem | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `0be001f244a09ed7adedeac7cfe7d0e5bb943ec7ece71c93ae241f817c81cf48` |
