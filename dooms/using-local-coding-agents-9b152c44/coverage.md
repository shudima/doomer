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


## Markdown revision — 2026-10-31

Authorized in-place migration: 34 existing dooms retained their identities; 2 labeled illustrative examples added; 36 Markdown dooms now. All original source files are unchanged. `sort_order` is display position, not identity. Earlier coverage references use original doom identities, which remain stable. The table below maps those identities to the new positions.

Every body was checked for paragraph length, exact numeric evidence and meaningful Markdown. Direct rewrites simplify dense explanations; lightly edited cards retain their evidence, qualifications and source examples. Added scenarios are teaching aids, not measured results or real company reports. Composite scenarios in the exceptional-IC source remain identified as composites.

| Doom identity | Current position | Title |
| --- | ---: | --- |
| `using-local-coding-agents-9b152c44-001` | 1 | The model is only half the agent |
| `using-local-coding-agents-9b152c44-002` | 2 | Why keep a coding stack local? |
| `using-local-coding-agents-9b152c44-003` | 3 | Try the native harness, then compare |
| `using-local-coding-agents-9b152c44-004` | 4 | A model that fits a capable desktop |
| `using-local-coding-agents-9b152c44-005` | 5 | Serve the model before adding tools |
| `using-local-coding-agents-9b152c44-006` | 6 | Choose the right model variant |
| `using-local-coding-agents-9b152c44-007` | 7 | Short chats hide long-context costs |
| `using-local-coding-agents-9b152c44-008` | 8 | Benchmark the machine you will use |
| `using-local-coding-agents-9b152c44-009` | 9 | Read speed numbers with their caveats |
| `using-local-coding-agents-9b152c44-010` | 10 | Use benchmarks as relative evidence |
| `using-local-coding-agents-9b152c44-011` | 11 | Correct reasoning includes the next action |
| `using-local-coding-agents-9b152c44-012` | 12 | A fast model can still be a poor agent |
| `using-local-coding-agents-9b152c44-013` | 13 | Audit the tool that can act |
| `using-local-coding-agents-9b152c44-014` | 14 | Local inference does not stop telemetry |
| `using-local-coding-agents-9b152c44-035` | 15 | Separate local inference from network activity |
| `using-local-coding-agents-9b152c44-015` | 16 | Make privacy settings explicit |
| `using-local-coding-agents-9b152c44-016` | 17 | Separate the experiment from your main files |
| `using-local-coding-agents-9b152c44-017` | 18 | Installing from source has a tradeoff |
| `using-local-coding-agents-9b152c44-018` | 19 | Connect Qwen Code to Ollama |
| `using-local-coding-agents-9b152c44-019` | 20 | Thinking and model switching |
| `using-local-coding-agents-9b152c44-020` | 21 | Test the complete agent on real work |
| `using-local-coding-agents-9b152c44-036` | 22 | Compare complete stacks on the same task |
| `using-local-coding-agents-9b152c44-021` | 23 | The harness changes the outcome |
| `using-local-coding-agents-9b152c44-022` | 24 | Codex can host a local model workflow |
| `using-local-coding-agents-9b152c44-023` | 25 | Keep local Codex settings separate |
| `using-local-coding-agents-9b152c44-024` | 26 | Native is not automatically best |
| `using-local-coding-agents-9b152c44-025` | 27 | Claude Code can connect through Ollama |
| `using-local-coding-agents-9b152c44-026` | 28 | Count tokens as well as solved tasks |
| `using-local-coding-agents-9b152c44-027` | 29 | Long history can dominate the bill |
| `using-local-coding-agents-9b152c44-028` | 30 | Passing tests leaves quality unmeasured |
| `using-local-coding-agents-9b152c44-029` | 31 | Keep the harness near your files |
| `using-local-coding-agents-9b152c44-030` | 32 | Forward the Ollama port over SSH |
| `using-local-coding-agents-9b152c44-031` | 33 | Point the launcher at the tunnel |
| `using-local-coding-agents-9b152c44-032` | 34 | Start with a coding-focused harness |
| `using-local-coding-agents-9b152c44-033` | 35 | Understand the stack, then judge the work |
| `using-local-coding-agents-9b152c44-034` | 36 | Your familiar harness is worth a trial |

### Added examples

| Follows original identity | New identity | Concept |
| --- | --- | --- |
| `using-local-coding-agents-9b152c44-014` | `using-local-coding-agents-9b152c44-035` | Separate local inference from network activity |
| `using-local-coding-agents-9b152c44-020` | `using-local-coding-agents-9b152c44-036` | Compare complete stacks on the same task |

### Source figure provenance

Accessed 2026-10-31 from the complete article. Source captions, on-image credits and the article remain the authority for reported results. Reproduction here does not imply a new license; no separate reuse license was identified in the fetched figure metadata.

| Local file / original identity | Origin | Original caption or context | Export |
| --- | --- | --- | --- |
| `images/source-00.webp` / `using-local-coding-agents-9b152c44-001` | [Original](https://substackcdn.com/image/fetch/$s_!w1ai!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98ebec9f-115a-4896-926d-5461220de62a_10126x2817.png) | Figure 1: Overview of the local stack, that is, a coding agent harness that uses a local model hosted through an inference engine / runtime server. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `6f3e6bad214377fb26477f473dde26916b3e25385f1173ea35a2062c50ae3947` |
| `images/source-02.webp` / `using-local-coding-agents-9b152c44-003` | [Original](https://substackcdn.com/image/fetch/$s_!vjT6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F54573a7d-c74a-47d5-8e89-f7be21458de8_3085x1566.png) | Figure 2: Qwen model performance in different coding harnesses via Polar: Agentic RL on Any Harness at Scale ( https://arxiv.org/abs/2605.24220 ) | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `b9d30a14dcba1e760986abdc1dc4f86cea3629b3dcec013d582986383632a827` |
| `images/source-18.webp` / `using-local-coding-agents-9b152c44-018` | [Original](https://substackcdn.com/image/fetch/$s_!xSSj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24752ae3-df6e-49b2-a788-e09c80de4ab9_6048x4272.png) | Figure 18: Configure Qwen Code to use Ollama’s local OpenAI-compatible endpoint, http://127.0.0.1:11434/v1 . | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `7cffeaaeb43cb1dd96d0684cecb2caed47c7cb0a50a20d81f63c3420a0ff6064` |
| `images/source-26.webp` / `using-local-coding-agents-9b152c44-023` | [Original](https://substackcdn.com/image/fetch/$s_!BtrE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc617934-d2c5-4aba-948a-fcf69c2740a4_6972x2665.png) | Figure 26: Set up a separate Ollama profile for Codex for convenience. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `abd7b461b698cf15582a12d674e8f4b79c0a9c7c20d779d920d7e018b5955d95` |
| `images/source-29.webp` / `using-local-coding-agents-9b152c44-025` | [Original](https://substackcdn.com/image/fetch/$s_!un9p!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F70cdf586-90c1-41c4-a867-710b3ada7922_4436x2889.png) | Figure 29: Claude Code with a local Qwen3.6 model through Ollama. | Complete first frame, resized only if above 2400×6000; WebP export. No crop. Download SHA-256 `3a846cc3c7b00d13b5f48e5b58d67f1e0ed179f25ab5eae869f643d9ab0dc032` |
