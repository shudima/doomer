# Markdown catalog migration — 2026-10-31

All 673 existing dooms across 31 topics were converted to version-2 Markdown. The revision adds 73 explicitly labeled illustrative examples, producing 746 dooms, with 46 locally packaged figures from the original articles. There are three added explanatory diagrams with editable Mermaid and portable SVG overviews. Writing and Markdown clarity edits affect more than 200 existing bodies, including over 100 direct rewrites. Clear existing prose is retained elsewhere. A final fidelity pass restores source-specific setup instructions, caveats and technical distinctions while expanding terse Salesforce and Uber summaries. Each collection’s coverage document records its identity-to-position mapping, added examples and figure origins.

All original collection IDs and doom IDs are preserved. New example IDs are allocated above the original maximum and inserted using display order. No database schema change is required. A regression test saves progress and a reaction on YAML, finishes another topic, converts the first to Markdown, inserts a card before the saved doom and verifies the original state after restart.

Original PDF attachments are unchanged. Article figures were visually inspected in contact sheets and exported without cropping to WebP; unusually large images are resized to at most 2400×6000, and image credits remain visible. Per-file origin URLs, export details and downloaded-byte hashes appear in coverage.md. The PDF sources have editable text/vector tables rather than embedded raster illustrations; concise comparisons use Markdown. Existing video transcript-only limitations remain recorded: no new source video frames were recovered.

The API accepts legacy YAML and Markdown, validates local asset containment, decodes figures and reports width/height for stable layout. Only referenced assets are exposed, through profile-scoped routes. Raw HTML is omitted by the React renderer; Mermaid uses strict security mode and renders into image blobs. GFM tables and code scroll horizontally without triggering topic changes.

Verification includes all collection validators, backend migration/asset tests, frontend Markdown tests, a production build and phone-sized browser checks. See the appended verification record for the exact checks performed. Desktop viewport emulation does not substitute for testing Safari on a physical iPhone.

| Topic | Previous | Current | Added examples | Source figures |
| --- | ---: | ---: | ---: | ---: |
| advice-for-new-principal-tech-ics-i-e-notes-to-myself-b808666e | 21 | 23 | 2 | 0 |
| agent-frameworks-by-system-type-767b05d7 | 11 | 13 | 2 | 0 |
| agentic-ai-harness-survey-bb361049 | 62 | 67 | 5 | 0 |
| agentic-engineering-beyond-vibe-coding-4871572b | 11 | 13 | 2 | 0 |
| ai-era-sdlc-survey-6223bf11 | 44 | 48 | 4 | 0 |
| building-agents-when-to-fold-subagents-into-your-main-agent-loop-13225fd2 | 19 | 21 | 2 | 1 |
| building-reliable-agent-skills-e874358e | 15 | 17 | 2 | 0 |
| code-review-is-now-generally-available-67e0e2ca | 4 | 5 | 1 | 0 |
| coding-with-ai-agents-concepts-40c23e33 | 13 | 15 | 2 | 0 |
| common-questions-about-agent-evals-7b591106 | 17 | 19 | 2 | 4 |
| context-engineering-deep-agents-remember-eeb5997d | 12 | 14 | 2 | 4 |
| context-engineering-failure-modes-88666974 | 12 | 14 | 2 | 0 |
| controlling-reasoning-effort-1e95bee9 | 35 | 37 | 2 | 3 |
| design-patterns-in-machine-learning-code-and-systems-40f8e1de | 14 | 17 | 3 | 4 |
| did-the-ai-bubble-just-pop-8236b1f5 | 11 | 13 | 2 | 0 |
| evaluating-the-effectiveness-of-llm-evaluators-aka-llm-as-judge-c55ce977 | 43 | 46 | 3 | 3 |
| exceptional-leadership-some-qualities-behaviors-and-styles-2591e3a5 | 9 | 11 | 2 | 0 |
| how-to-build-a-model-router-in-the-harness-378de5b0 | 14 | 16 | 2 | 2 |
| how-to-interview-and-hire-ml-ai-engineers-63f4110a | 24 | 26 | 2 | 0 |
| how-to-work-and-compound-with-ai-d9423452 | 20 | 22 | 2 | 0 |
| jev-automation-and-specialized-models-235a11a9 | 11 | 13 | 2 | 0 |
| jev-decisions-without-text-0dd53b3f | 16 | 18 | 2 | 0 |
| jev-trust-observability-bef2a4f9 | 13 | 15 | 2 | 0 |
| patterns-for-building-llm-based-systems-products-b4c1a004 | 52 | 55 | 3 | 10 |
| product-evals-in-three-simple-steps-e1d32e24 | 14 | 16 | 2 | 0 |
| revamping-skills-in-deep-agents-d89ca29f | 10 | 12 | 2 | 3 |
| salesforce-agent-tech-stack-3e16b48a | 9 | 11 | 2 | 4 |
| seven-skills-for-agent-engineering-19b7176f | 13 | 15 | 2 | 0 |
| the-exceptional-individual-contributor-50d9f41e | 82 | 88 | 6 | 0 |
| uber-mcp-gateway-31398518 | 8 | 10 | 2 | 3 |
| using-local-coding-agents-9b152c44 | 34 | 36 | 2 | 5 |
