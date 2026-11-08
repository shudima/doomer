# The components of agent memory

Lance Martin wrote the article for Anthropic Engineering. Anthropic published it on November 6, 2026. Accessed November 8, 2026. Monika Tuchowska created the source figures. [Anthropic article](https://www.anthropic.com/research/components-of-agent-memory)

The English article explains agent memory to technical readers in an approachable research style. It follows knowledge across searchable transcripts, notes, linked wikis, and a small set of context loaded at startup. Background processing, called dreaming, can organize and verify what gets carried forward. The reported evaluations show why note quality, the shape of the task, and maintenance cost matter.

## Coverage map

| Doom | Concept | Article location |
| --- | --- | --- |
| [001](001-save-what-another-session-can-use.md) | Save what another session can use | Memory notes |
| [002](002-give-memory-four-places-to-live.md) | Give memory four places to live | Introduction · Figure 1 |
| [003](003-use-idle-time-to-organize-memory.md) | Use idle time to organize memory | Introduction |
| [004](004-capture-a-clue-while-it-is-fresh.md) | Capture a clue while it is fresh | Memory notes · Figure 2 |
| [005](005-a-memory-rule-makes-a-prediction.md) | A memory rule makes a prediction | Memory can be a prediction about what the future will need |
| [006](006-test-an-explanation-before-saving-it-as-a-rule.md) | Test an explanation before saving it as a rule | Memory can be a prediction about what the future will need |
| [007](007-show-the-next-session-how-you-checked.md) | Show the next session how you checked | Memory can be a prediction about what the future will need |
| [008](008-read-the-notes-to-see-what-the-model-learned.md) | Read the notes to see what the model learned | Memory can be a prediction about what the future will need |
| [009](009-a-memory-folder-helped-models-by-different-amounts.md) | A memory folder helped models by different amounts | Memory can be a prediction about what the future will need · Figure 3 |
| [010](010-a-smaller-notebook-can-carry-more-useful-knowledge.md) | A smaller notebook can carry more useful knowledge | Claude has learned to judge salience · Figure 4 |
| [011](011-save-what-the-screen-cannot-tell-you.md) | Save what the screen cannot tell you | Claude has learned to judge salience |
| [012](012-save-the-tactic-and-how-you-found-it.md) | Save the tactic and how you found it | Claude has learned to judge salience |
| [013](013-a-narrow-rule-can-limit-what-memory-captures.md) | A narrow rule can limit what memory captures | Steering Claude to write memory · Figure 5 |
| [014](014-give-a-model-guidance-where-it-gets-stuck.md) | Give a model guidance where it gets stuck | Steering Claude to write memory |
| [015](015-check-memory-against-the-record.md) | Check memory against the record | Dreaming can correct memory · Figure 6 |
| [016](016-one-wrong-landmark-sent-claude-the-wrong-way.md) | One wrong landmark sent Claude the wrong way | Dreaming can correct memory · Figure 7 |
| [017](017-follow-the-paths-after-the-note-changes.md) | Follow the paths after the note changes | Dreaming can correct memory · Figure 8 |
| [018](018-build-a-map-across-separate-notes.md) | Build a map across separate notes | Dreaming can build new memory representations · Figure 9 |
| [019](019-a-growing-wiki-answered-more-of-the-same-questions.md) | A growing wiki answered more of the same questions | Dreaming can build new memory representations · Figure 10 |
| [020](020-use-the-wiki-to-orient-and-search-to-verify.md) | Use the wiki to orient and search to verify | Dreaming can build new memory representations |
| [021](021-a-wiki-helps-when-the-answer-spans-documents.md) | A wiki helps when the answer spans documents | Dreaming can build new memory representations · Figure 11 |
| [022](022-a-map-can-outgrow-the-territory.md) | A map can outgrow the territory | Dreaming can build new memory representations · Figure 12 |
| [023](023-load-only-the-notes-every-session-needs.md) | Load only the notes every session needs | Dreaming can promote notes up the memory hierarchy · Figure 13 |
| [024](024-use-the-startup-note-as-an-index.md) | Use the startup note as an index | Dreaming can promote notes up the memory hierarchy |
| [025](025-tell-the-memory-builder-what-it-must-preserve.md) | Tell the memory builder what it must preserve | Dreaming can focus memory on a specific goal |
| [026](026-give-each-contract-page-one-writer.md) | Give each contract page one writer | Dreaming can focus memory on a specific goal · Figure 14 |
| [027](027-a-second-pass-can-repair-the-links.md) | A second pass can repair the links | Dreaming can fill in gaps a session leaves behind · Figure 15 |
| [028](028-choose-when-a-note-needs-to-exist.md) | Choose when a note needs to exist | Thinking backward, looking forward |
| [029](029-spend-memory-maintenance-where-it-matters.md) | Spend memory maintenance where it matters | Thinking backward, looking forward |

The article supplies the CL-Bench database setup and scores, the Pokémon runs, the Stainless and merger wiki evaluations, the Harvey LAB examples, and the startup memory index. Those results apply to the reported comparisons. Dooms 001, 007, 024, and 028 add clearly labeled illustrations about a test command, duplicate SQL rows, a support policy index, and an incident handoff.

## Figures

All 15 technical figures are included and credited. The local WebP versions preserve the original dimensions and complete artwork without crops. The credit identifies the figure author. The source page does not identify a separate reuse license for these figures. The portrait background is original decorative artwork for Doomer.

| Figure | Doom | Local image | Original PNG | Dimensions | Original SHA-256 |
| --- | ---: | --- | --- | --- | --- |
| 1 | 002 | `figure-01.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/a0bcfa203214d817d2b4261b7188aba8be6db5b2-3840x1754.png) | 3840 × 1754 | `71a52614d7ec77aaed15978ff19fd9f67b64da45c389f841b9162604ff4e3175` |
| 2 | 004 | `figure-02.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/2ef2bf5c81ea6d578749782782eff10cf3136de4-3840x1754.png) | 3840 × 1754 | `62452337c4fe4a1194908bbef04ca2a70a5c249f9c5a627bd64a960cbaf0af08` |
| 3 | 009 | `figure-03.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/bb0d44c78cc431fb5e84fbf2cb17c4303bc6bd65-3840x2160.png) | 3840 × 2160 | `8fa45d19f8f3f1c66f3f578999e14cc69be918f3723dd85ed647075c398fcc5e` |
| 4 | 010 | `figure-04.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/5e15e10f665773050d90fafc38ab8dd76ae5368b-3840x2545.png) | 3840 × 2545 | `2b46d5123163fc19856b477f071a47fffe877671349ddd54103bf91d8122c050` |
| 5 | 013 | `figure-05.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/da03e864e4eba93a91314fa5f2a5d0e4c14b2a0f-3840x2310.png) | 3840 × 2310 | `b1863eedbd5597967eadc42ccf425b299c36c3801ce9097ce1908be5c90e1633` |
| 6 | 015 | `figure-06.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/55ce85bd12860090704a5543a3da7504334ad9a9-3840x1754.png) | 3840 × 1754 | `8087f771064bcbfb6aa6f7786f17e0252d16bda3d8ee02e018f25dc7cf31482c` |
| 7 | 016 | `figure-07.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/d906d6ed9ac92db36631a624ad517183b07a545d-3840x2101.png) | 3840 × 2101 | `17ace339e07b9b2a46b5e4ac47eadcf828e98ddc5b49c0eab68dcc5b601f0011` |
| 8 | 017 | `figure-08.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/2eb2bfe6d01e9a1fca74a41e952d948c09d42008-3840x2636.png) | 3840 × 2636 | `1559f93f783382b885c6fc99c7929e1f1cc6699ed632b5b7fdbf77bc78f60234` |
| 9 | 018 | `figure-09.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/30923242548d746ee77784c87826cadc46574c34-3840x1754.png) | 3840 × 1754 | `1f195b10c18d03fabc5aa2681c3a09b6d47ccd8c892dfb2067821431bc362daf` |
| 10 | 019 | `figure-10.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/336832b5015f1bfcfd7d786fae8120c533f26ecd-3136x1432.png) | 3136 × 1432 | `abb569202529bac7c5ed7d32e60b371529757b6c5dfc0ef11a982dd690ebc5da` |
| 11 | 021 | `figure-11.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/3677eab5e938466cc41fbac4d47f3118135d0563-3840x3694.png) | 3840 × 3694 | `c8f3a5253171b6d17547907cbe4d589b93580ee71d1606f2bdb27774b64cea50` |
| 12 | 022 | `figure-12.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/ffa35479b1dea63b7948f76995b488d08854e86d-3840x2150.png) | 3840 × 2150 | `8accaa79cff73029704edd79c02db7f67ddaa296434da0e7d8e8313543f7c3bd` |
| 13 | 023 | `figure-13.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/c88bcc04c5d0e77db5828c9dbe72faf1c4421f8f-3840x1754.png) | 3840 × 1754 | `bcf2a3afd4f4179f84fe7a86f64e873955ef52e3dced17cfe73ddf3ed81922b7` |
| 14 | 026 | `figure-14.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/592f604d38e90537553ab7127d1d3115924fda92-3840x1822.png) | 3840 × 1822 | `0d93ccc7cb9d63247063791c1eae898928b67414fbde6a71028d5be145f93ca1` |
| 15 | 027 | `figure-15.webp` | [Source image](https://www-cdn.anthropic.com/images/4zrzovbb/website/f1afeef9a2d986a6155c0789db46b8fa372a20eb-3840x1812.png) | 3840 × 1812 | `ad40204190967fa12d51664e8a8a61b0b74ff9c8f9ec4e2bcf8dcd7e7cf2165f` |

## Source boundaries

The entire article body and all technical figures were available. The decorative hero image, site navigation, related articles, and acknowledgements list are outside the teaching sequence. External cookbooks and references provide further reading. The collection describes memory as knowledge carried across sessions. The article distinguishes that from model training, learning within one conversation, and summaries used to continue a conversation.

## Reader verification

The collection validator passed. The local Doomer API returned all 29 Markdown bodies, including the first text card and the second card’s list and figure reference. Each of the 15 figure routes returned its exact local WebP bytes and valid dimensions. The full figures were visually reviewed in contact sheets. A phone-sized browser preview and in-reader zoom check could not be performed because local browser use is disabled in Work settings.
