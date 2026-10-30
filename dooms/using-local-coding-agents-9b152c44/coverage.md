# Using Local Coding Agents

- Author: Sebastian Raschka, PhD
- Original URL: https://magazine.sebastianraschka.com/p/using-local-coding-agents
- Access date: 2026-10-30
- Language: English
- Tone: conversational, technical, exploratory; practical enthusiasm tempered by small-sample caveats.
- Collection: using-local-coding-agents-9b152c44
- Reels: 34

## Summary

The tutorial separates local model serving from the coding-agent harness, compares suitable desktop-scale models, and evaluates long-context speed, tool reasoning, and complete agent tasks. It audits the harness's permissions and outbound behavior, configures Qwen Code, explores Codex and Claude Code, and connects a Mac harness to a DGX server over SSH. Its conclusion favors evaluating the complete stack on representative work over assuming a model's native harness is best.

## Source map

| Substantive source section | Reels |
| --- | --- |
| Opening stack overview and 1. Intro: motivations and hosted-tool context | 1–2 |
| 2. Coding Agent Harness Overview: native-harness rationale, evidence limits, model options | 3–4 |
| 3. Local LLM Setup: serving layer, Ollama, hardware-specific downloads, cloud distinction | 5–6 |
| 4. Simple Speed Performance Assessment: procedure, memory caveats, speed and quantization comparisons | 7–9 |
| 5. Simple Benchmark Performance Assessment: relative benchmarks, five-task tool-reasoning results and limits | 10–12 |
| 6. Agent Code Base Audit: audit scope, findings, privacy settings, updates and injection | 13–15 |
| 7. Qwen-Code Setup: isolation, installation choices, provider setup, model switching and maintenance | 16–19 |
| 8. Agent Capability Assessment: representative tasks and complete-agent results | 20–21 |
| 9. Codex Setup: CLI route, separate configuration, unexpected harness comparison | 22–24 |
| 10. Claude Code Setup: Ollama integration, closed-source concern, results, tokens, input history, quality caveat | 25–28 |
| 11. Mac <-> DGX: split-machine workflow, SSH forwarding, verification, launcher endpoint | 29–31 |
| 12. What about OpenClaw and Hermes?: broader agents versus coding baseline | 32 |
| 13. Conclusion: stack literacy, hosted/local tradeoffs and empirical harness choice | 33–34 |
| Further Resources: evaluation repository | 34 |

## Coverage and retrieval limitations

The entire public article body was retrieved directly from the supplied URL without a paywall or pagination gap. All substantive numbered sections are represented. Navigation, related-story embeds, book promotion, and subscription appeals are omitted. Installation scripts and configuration blocks are condensed into explanations rather than copied in full. This collection summarizes the tutorial; it does not execute or independently reproduce its installations, audits, timings, or benchmarks. No outside research was added.

Figure captions and the author's surrounding explanations were read. Embedded figure pixels were not inspected, and numerical results in the reels come only from the article's prose and code output, not inferred table cells. This limits verification of figure-only detail without leaving a numbered prose section uncovered.

The source contains inconsistent prose about Gemma 4 in Claude Code: it first says the model does reasonably well, then says it fails almost all tasks. Reels avoid assigning it an exact Claude success rate. The source also abbreviates Codex profile/provider wiring and alternates between `~/.qwen/settings.json` and `~/qwen/settings.json`; no complete version-independent setup is promised. Reel 23 flags the configuration omission. For model addition, reel 19 refers generically to the settings file rather than choosing an unverified path.

The source frames a 50% token reduction as twice the speed. Reel 28 preserves the efficiency argument but qualifies wall-clock implications because input processing, output generation, and tool time differ; this is an editorial qualification, not a new measured result.

## Assets and verification

`images/local-stack.svg` is an original purpose-made 1080×1920 background with a quiet dark text area and connected terminal motifs. No third-party image assets or licenses are involved. The background is shared across the collection; reel text is not embedded in it.

Every YAML is parsed and validated against the project schema; IDs, source metadata, file order, image containment, nonempty files, portrait dimensions, and SVG XML are checked. Content is mapped against all numbered source sections and reviewed for duplicate ideas and unsupported certainty. The first reel was rendered in the running Doomer app at a 390×844 phone viewport and its screenshot was visually inspected. The title, paragraphs, source link, and controls were readable without clipping. All reel texts contain 59–78 words. The app catalog loads the new collection (15 total topics, 283 total reels).
