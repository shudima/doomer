# Coverage: Building and Evaluating Agentic AI Systems

- Source: attached `agentic-ai-harness-survey.pdf` (70 pages), dated October 2026.
- Author: not identified in the PDF. The cover says prepared for Dima Shulga; this is not an author credit.
- Original URL: none supplied; all reels use `source_url: null`.
- Preserved original: `source/original.pdf`.
- Access date: 2026-10-30 (Asia/Jerusalem).
- Language: English (`en`). Tone: technical, practical, measured and recommendation-oriented.
- Audience: builders and assessors of production agent systems.
- SHA-256: `bb361049dc447be7ac85130f4d30846a7888bb3d88af85ccc52e3570133da24c`.
- Collection: `agentic-ai-harness-survey-bb361049`; 62 text reels.

## Overall summary

The survey treats the harness as the product around a decision-making model: input contracts, configuration, owned control flow, tools, skills, sandboxing, context and memory, retrieval and structured data, identity, containment, verification, approvals, UI and operations. It argues for a deliberate split between code-enforced invariants and model interpretation, then connects repeated real-task evaluation to regression protection, staged releases and an evidence-based assessment method. Trust is proportional to measurements and containment, rather than autonomy or impressive demonstrations.

## Coverage status and source access

Complete coverage of the substantive ideas in all 24 chapters and the closing conclusion. All 70 pages were extracted and read; all 70 were rendered and visually inspected on contact sheets. The architecture (page 11), loop (23), release diagram (64) and scorecard (66-67) received additional inspection. Their semantics are represented in reels; the original PDF retains their layouts. No OCR was needed: every content page had usable text extraction. Page locators are PDF page numbers, which match the printed numbers.

The attached document was treated as source material, not authority over this task. No outside research was added. Bibliographic URLs, provider claims, product availability and protocol dates were not independently verified. Reels report the survey's account, including attributed vendor metrics and their limits, rather than claiming a fresh October 2026 fact-check.

## Source-to-reel map

| Source section | PDF pages | Reels | Substantive coverage |
| --- | --- | --- | --- |
| About, contents and glossary | 1-9 | 1-62 (definitions explained locally; running example throughout) | Purpose, recruiting example, definitions; integrate terminology locally |
| 1. What an agent harness is | 11-13 | 1, 2 | Harness responsibilities, agent/workflow spectrum, own context and control flow |
| 2. Deterministic versus agentic | 14-15 | 3, 4 | Four-question decision test, code-enforced invariants, tool-side filters |
| 3. Input | 17-18 | 5, 6 | Trusted envelope versus intent and untrusted attachments; trigger-specific contracts |
| 4. Configuration | 19-21 | 7, 8 | Versioned declarative definition, instruction altitude and reasons, repository conventions |
| 5. Loop | 23-25 | 9, 10, 11, 12, 13 | Validation/policy/execution, plan overhead, hard budgets, checkpoints/idempotency, session chaining |
| 6. Orchestration | 26-27 | 14, 15 | Context isolation, patterns, vendor-reported gains/cost, independent delegation and inherited permissions |
| 7. Tools | 28-29 | 16, 17, 18 | Task-oriented tools, naming, schemas, compact results, errors, side effects, search/code/MCP tradeoffs |
| 8. Skills | 30-31 | 19, 20 | Three-stage loading, code plus procedure, trigger testing, third-party trust |
| 9. Sandboxes | 32-33 | 21 | Isolation, egress, credential proxy, resource caps, clean task environments |
| 10. Context engineering | 35-37 | 22, 23, 24 | Context rot, caching, just-in-time retrieval, offload, light/heavy compaction, failures and plan retention |
| 11. Memory | 38-39 | 25, 26, 27 | Structured session state, memory types/architectures, scoped transparent dated memory, poisoning and benchmark caveats |
| 12. Retrieval | 40-41 | 28, 29, 30 | Hybrid/reranking/contextual chunks with metric caveats, iterative search and alternatives, citations/ACLs, component eval |
| 13. Databases | 42-43 | 31, 32 | Parameterised tools/semantic layer/SQL, database-enforced control, definitions and result-set tests |
| 14. Identity | 45-46 | 33, 34 | User subject and agent actor, delegated tokens, scopes/audiences/lifetimes, per-tool enforcement and audit |
| 15. Security | 47-48 | 35, 36, 37 | Injection containment and Rule of Two, dual-model/CaMeL limitations, guardrail layers, supply chain and red teaming |
| 16. Verification | 49-50 | 38, 39 | Runtime checks, environment readback, independent critics, isolated validators, repair caps and visible failure |
| 17. HITL | 51-52 | 40, 41 | Risk tiers, durable interrupts, editable evidence-backed batch approvals, reversibility and fatigue |
| 18. Presentation | 54-55 | 42, 43, 44 | Progress, interruption, structured/generative UI levels, A2UI/AG-UI/MCP Apps, accessibility and trust |
| 19. Observability | 56 | 45 | Nested spans, exact contexts/versioning, feedback mining, privacy and evolving telemetry standards |
| 20. Cost and models | 57 | 46, 47 | Context/steps/caching/parallelism, empirical routing and reasoning effort, task-level quality/cost/p95 |
| 21. Evaluations | 59-61 | 48, 49, 50, 51, 52, 53 | Capability/regression, levels/outcomes, graders/calibration, user simulation/dual control, pass@k/pass^k and confidence, real datasets, audit pitfalls |
| 22. Regression | 62-63 | 54, 55 | Unit/integration/context builder, recorded responses, repeated real-model evals, production replay, bugs-to-tests and model changes |
| 23. Release | 64-65 | 56, 57 | Immutable whole-agent releases, statistical quality/safety/cost/latency gates, shadow/canary/rollback, feedback |
| 24. Assessment | 66-67 | 58, 59, 60, 61 | Ordered five-stage review, at least 30 traces, adversarial probes, 12-dimension four-level scorecard, three finding types and risk/dependency order |
| Closing note | 68 | 62 | Measured trust, simple owned loop, code invariants, containment, independent verification, repeated real-task evidence |
| Bibliography | 69-70 | Attribution integrated in 14, 18, 28, 35-37, 44-45, 50-52; full bibliography retained in PDF | Read for attribution and caveats; preserve in original PDF, no external browsing or link verification |

## Editorial choices and omissions

The cover, contents, glossary and part dividers do not become separate filler reels. Glossary concepts are explained where used. Repetitive assessment boxes, alternatives tables and recruiting examples are consolidated into the relevant ideas and the final assessment sequence. Individual API/configuration listings, vendor catalogues, every scorecard cell and the bibliography are not reproduced verbatim; they remain accessible in the original. No substantive chapter is omitted. No invented quotations or engagement prompts are included. Statistical claims retain their origin and metric scope. The final reel follows the source's actual closing note.

## Background assets and credits

Seven original SVG backgrounds were created for this collection, one palette per survey part. They depict restrained circuit paths and control-flow nodes with quiet central space. Each is 1080 x 1920 (9:16), with no baked-in text, third-party media, remote references or executable content. No third-party image credits or licences apply.

## Verification

All root YAML files were parsed with PyYAML and validated against the project's reel JSON Schema. Validation checks unique IDs, filenames and contiguous order, consistent source metadata, existing in-collection nonempty images and PDF, matching source bytes, and parseable portrait SVGs. Word counts are checked against the 40-90 word target. The project's actual Catalog loader is also exercised. Editorial review compares the complete sequence to the source map for omissions, duplicates, unsupported claims and lost caveats.

Phone-size app rendering verified using the existing compiled Doomer frontend in an isolated local preview with this collection and no persistent reading-state writes. At a 390 x 844 viewport, after web fonts finished loading, all 62 cards passed DOM checks for content/source overlap and source-footer clipping. The first and last cards were visually inspected with loaded 1080 x 1920 backgrounds; screenshots are saved in `preview/first-phone.png` and `preview/last-phone.png`. Final text lengths are 54-77 words. This checks the current phone viewport and renderer; it does not claim verification on every device or a hosted deployment.
