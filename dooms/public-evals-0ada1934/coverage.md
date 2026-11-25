# Lessons from 12 Evals: Where They Break and What to Measure Instead

Written by Eugene (Ziyou) Yan. Published November 2026. Accessed November 25, 2026. [Original article](https://eugeneyan.com/writing/public-evals)

The English article is an accessible technical teardown of twelve public agent evaluations. It reviews task design, grading, benchmark maintenance, failure analysis, and measurement proposals. This collection follows its cross-benchmark lessons, then all twelve benchmark discussions, and ends with the recommendation to test candidate systems inside the application’s own harness.

## Coverage map

| Doom | Concept | Source location |
| --- | --- | --- |
| [001](001-ask-what-a-benchmark-pass-actually-means.md) | Ask what a benchmark pass actually means | Introduction |
| [002](002-an-evaluation-task-has-four-parts.md) | An evaluation task has four parts | Patterns: How eval tasks are built and maintained |
| [003](003-treat-the-benchmark-version-like-a-software-version.md) | Treat the benchmark version like a software version | Patterns: How eval tasks are built and maintained |
| [004](004-give-exact-requirements-an-exact-check.md) | Give exact requirements an exact check | Principles: That shape grading and task selection |
| [005](005-check-the-outcome-the-user-asked-for.md) | Check the outcome the user asked for | Principles: That shape grading and task selection |
| [006](006-all-pass-scoring-makes-every-check-decisive.md) | All-pass scoring makes every check decisive | Principles: That shape grading and task selection |
| [007](007-partial-credit-shows-how-far-the-work-got.md) | Partial credit shows how far the work got | Principles: That shape grading and task selection |
| [008](008-hard-task-selection-changes-what-a-low-score-means.md) | Hard task selection changes what a low score means | Principles: That shape grading and task selection |
| [009](009-verification-is-part-of-completing-the-task.md) | Verification is part of completing the task | Failures: Skipped verification and dropped reqs |
| [010](010-a-failed-check-can-reject-correct-work.md) | A failed check can reject correct work | Gaps: Failing correct work and passing wrong work |
| [011](011-a-passing-rubric-can-miss-a-serious-error.md) | A passing rubric can miss a serious error | Gaps: Failing correct work and passing wrong work |
| [012](012-two-digits-do-not-prove-an-email-is-correct.md) | Two digits do not prove an email is correct | Gaps: Failing correct work and passing wrong work |
| [013](013-the-same-average-can-hide-different-reliability.md) | The same average can hide different reliability | Hot takes: How we’re thinking about evals wrongly |
| [014](014-work-through-five-repeated-attempts.md) | Work through five repeated attempts | Hot takes: How we’re thinking about evals wrongly |
| [015](015-include-the-human-work-left-behind.md) | Include the human work left behind | Hot takes: How we’re thinking about evals wrongly |
| [016](016-a-cheap-failure-can-cost-more-overall.md) | A cheap failure can cost more overall | Hot takes: How we’re thinking about evals wrongly · added illustrative example |
| [017](017-a-detailed-specification-changes-the-skill-being-tested.md) | A detailed specification changes the skill being tested | Hot takes: How we’re thinking about evals wrongly |
| [018](018-test-requirements-that-arrive-during-the-work.md) | Test requirements that arrive during the work | Hot takes: How we’re thinking about evals wrongly |
| [019](019-a-late-requirement-may-change-an-earlier-decision.md) | A late requirement may change an earlier decision | Hot takes: How we’re thinking about evals wrongly · added illustrative example |
| [020](020-give-the-grader-known-good-and-known-bad-work.md) | Give the grader known-good and known-bad work | Hot takes: How we’re thinking about evals wrongly |
| [021](021-the-score-belongs-to-the-model-and-its-harness.md) | The score belongs to the model and its harness | Hot takes: How we’re thinking about evals wrongly |
| [022](022-terminal-bench-grades-a-working-container.md) | Terminal Bench grades a working container | Diving into the twelve benchmarks — Terminal Bench |
| [023](023-ask-whether-the-task-is-specific-solvable-and-honest.md) | Ask whether the task is specific, solvable, and honest | Diving into the twelve benchmarks — Terminal Bench |
| [024](024-a-hidden-requirement-can-dominate-the-result.md) | A hidden requirement can dominate the result | Diving into the twelve benchmarks — Terminal Bench |
| [025](025-keep-a-fixed-yardstick-beside-the-changing-exam.md) | Keep a fixed yardstick beside the changing exam | Diving into the twelve benchmarks — Terminal Bench |
| [026](026-deepswe-builds-fresh-software-tasks.md) | DeepSWE builds fresh software tasks | Diving into the twelve benchmarks — DeepSWE |
| [027](027-a-hidden-test-can-break-the-agent-s-own-tests.md) | A hidden test can break the agent’s own tests | Diving into the twelve benchmarks — DeepSWE |
| [028](028-accept-different-implementations-of-the-same-behavior.md) | Accept different implementations of the same behavior | Diving into the twelve benchmarks — DeepSWE |
| [029](029-frontierswe-follows-work-across-a-full-day.md) | FrontierSWE follows work across a full day | Diving into the twelve benchmarks — FrontierSWE |
| [030](030-measure-optimization-without-timing-the-host-machine.md) | Measure optimization without timing the host machine | Diving into the twelve benchmarks — FrontierSWE |
| [031](031-a-long-budget-still-needs-a-finished-submission.md) | A long budget still needs a finished submission | Diving into the twelve benchmarks — FrontierSWE |
| [032](032-a-fixed-ceiling-can-hide-an-exceptional-improvement.md) | A fixed ceiling can hide an exceptional improvement | Diving into the twelve benchmarks — FrontierSWE |
| [033](033-terminal-bench-science-selects-difficult-research-workflows.md) | Terminal Bench Science selects difficult research workflows | Diving into the twelve benchmarks — Terminal Bench Science |
| [034](034-inspect-the-verifier-before-blaming-a-low-science-score.md) | Inspect the verifier before blaming a low science score | Diving into the twelve benchmarks — Terminal Bench Science |
| [035](035-ninety-nine-correct-stars-can-still-score-zero.md) | Ninety-nine correct stars can still score zero | Diving into the twelve benchmarks — Terminal Bench Science |
| [036](036-gdpval-compares-work-with-an-expert-s-deliverable.md) | GDPval compares work with an expert’s deliverable | Diving into the twelve benchmarks — GDPval |
| [037](037-professional-judgment-adds-disagreement-to-the-score.md) | Professional judgment adds disagreement to the score | Diving into the twelve benchmarks — GDPval |
| [038](038-check-whether-the-rubric-rewards-professional-judgment.md) | Check whether the rubric rewards professional judgment | Diving into the twelve benchmarks — GDPval |
| [039](039-agents-last-exam-turns-expert-projects-into-runnable-tasks.md) | Agents’ Last Exam turns expert projects into runnable tasks | Diving into the twelve benchmarks — Agents’ Last Exam |
| [040](040-match-the-comparison-method-to-the-artifact.md) | Match the comparison method to the artifact | Diving into the twelve benchmarks — Agents’ Last Exam |
| [041](041-locate-the-failure-before-choosing-the-fix.md) | Locate the failure before choosing the fix | Diving into the twelve benchmarks — Agents’ Last Exam |
| [042](042-a-checkable-project-can-become-an-academic-exercise.md) | A checkable project can become an academic exercise | Diving into the twelve benchmarks — Agents’ Last Exam |
| [043](043-automationbench-makes-the-agent-discover-business-apis.md) | AutomationBench makes the agent discover business APIs | Diving into the twelve benchmarks — AutomationBench |
| [044](044-difficulty-can-come-from-distractions-around-the-workflow.md) | Difficulty can come from distractions around the workflow | Diving into the twelve benchmarks — AutomationBench |
| [045](045-a-success-message-can-conceal-unfinished-list-work.md) | A success message can conceal unfinished list work | Diving into the twelve benchmarks — AutomationBench |
| [046](046-an-exact-string-can-reject-the-same-numeric-value.md) | An exact string can reject the same numeric value | Diving into the twelve benchmarks — AutomationBench |
| [047](047-harvey-lab-starts-from-a-legal-matter.md) | Harvey LAB starts from a legal matter | Diving into the twelve benchmarks — Harvey LAB |
| [048](048-know-what-the-legal-judge-can-see.md) | Know what the legal judge can see | Diving into the twelve benchmarks — Harvey LAB |
| [049](049-reading-and-revision-tracked-better-legal-results.md) | Reading and revision tracked better legal results | Diving into the twelve benchmarks — Harvey LAB |
| [050](050-an-impossible-criterion-can-punish-a-faithful-answer.md) | An impossible criterion can punish a faithful answer | Diving into the twelve benchmarks — Harvey LAB |
| [051](051-check-the-whole-legal-document-against-its-sources.md) | Check the whole legal document against its sources | Diving into the twelve benchmarks — Harvey LAB |
| [052](052-finance-agent-follows-evidence-across-filings.md) | Finance Agent follows evidence across filings | Diving into the twelve benchmarks — Finance Agent |
| [053](053-a-dealbreaker-can-erase-partial-credit.md) | A dealbreaker can erase partial credit | Diving into the twelve benchmarks — Finance Agent |
| [054](054-more-searches-do-not-guarantee-a-resolved-analysis.md) | More searches do not guarantee a resolved analysis | Diving into the twelve benchmarks — Finance Agent |
| [055](055-an-unstated-ratio-can-become-a-hidden-dealbreaker.md) | An unstated ratio can become a hidden dealbreaker | Diving into the twelve benchmarks — Finance Agent |
| [056](056-healthbench-pro-begins-with-clinician-conversations.md) | HealthBench Pro begins with clinician conversations | Diving into the twelve benchmarks — HealthBench Professional |
| [057](057-a-clinical-score-combines-content-and-length-rules.md) | A clinical score combines content and length rules | Diving into the twelve benchmarks — HealthBench Professional |
| [058](058-a-thin-rubric-can-leave-most-of-a-response-unchecked.md) | A thin rubric can leave most of a response unchecked | Diving into the twelve benchmarks — HealthBench Professional |
| [059](059-a-fixed-length-target-fits-some-tasks-better-than-others.md) | A fixed length target fits some tasks better than others | Diving into the twelve benchmarks — HealthBench Professional |
| [060](060-browsecomp-builds-questions-backward-from-an-answer.md) | BrowseComp builds questions backward from an answer | Diving into the twelve benchmarks — BrowseComp |
| [061](061-the-browsing-runner-supplies-part-of-the-system.md) | The browsing runner supplies part of the system | Diving into the twelve benchmarks — BrowseComp |
| [062](062-an-answer-key-can-be-wrong-or-ambiguous.md) | An answer key can be wrong or ambiguous | Diving into the twelve benchmarks — BrowseComp |
| [063](063-osworld-stretches-desktop-work-over-longer-tasks.md) | OSWorld stretches desktop work over longer tasks | Diving into the twelve benchmarks — OSWorld 2.0 |
| [064](064-let-the-benchmark-user-answer-and-change-their-mind.md) | Let the benchmark user answer and change their mind | Diving into the twelve benchmarks — OSWorld 2.0 |
| [065](065-read-desktop-completion-beside-partial-progress.md) | Read desktop completion beside partial progress | Diving into the twelve benchmarks — OSWorld 2.0 |
| [066](066-remember-the-constraints-through-the-final-desktop-action.md) | Remember the constraints through the final desktop action | Diving into the twelve benchmarks — OSWorld 2.0 |
| [067](067-copying-the-displayed-name-can-still-fail-the-grader.md) | Copying the displayed name can still fail the grader | Diving into the twelve benchmarks — OSWorld 2.0 |
| [068](068-make-sure-the-evaluator-sees-the-state-the-agent-reached.md) | Make sure the evaluator sees the state the agent reached | Diving into the twelve benchmarks — OSWorld 2.0 |
| [069](069-use-public-scores-to-choose-your-own-experiments.md) | Use public scores to choose your own experiments | Conclusion |

## Examples, evidence, and qualifications

The source supplies the swapped audit counts, repeated-run 70% example, hidden-test collisions, the 99-of-100 stars run, mismatched numeric formatting, legal rubric omissions, unstated financial ratios, and desktop name/state mismatches. These are described within their original benchmark contexts. The independent-attempt assumption is explicit in the worked reliability example. Two additional labeled illustrations explain the human-time cost of cheap failures and a changing customer-export request. The spreadsheet sorting illustration is also clearly labeled.

All numerical results are snapshots reported in the article, with relevant versions, launch dates, or task subsets. They are not newly reproduced benchmark experiments. Observational associations, reviewer issue reports, possible state mismatches, and confirmed defects retain their different evidentiary status. Proposals such as reporting repeated-run reliability, fixed-subset scores, savings-based performance credit, or task-specific length adjustment are presented as proposals.

The article summarizes DeepSWE grading problems using different counts in different passages. The collection uses the detail section’s 18-of-113 count specifically for hidden-test clashes, without treating it as a total for every grading problem. Likewise, it avoids combining the article’s differing 55% and 57% substring-check summaries into a single statistic.

## Figure provenance

All nine explanatory figures embedded in the article were downloaded at the largest advertised dimensions, decoded, and visually inspected in contact sheets. The local files preserve the downloaded WebP bytes, the complete images, captions, and aspect ratios. No figures were cropped or redrawn. The decorative portrait background is original SVG artwork.

The article is the source for these reproductions. Underlying paper captions and credits remain visible. No separate reuse license was identified in the fetched figure metadata.

| Local image | Doom | Article image / attribution | Download origin | Dimensions | SHA-256 |
| --- | ---: | --- | --- | --- | --- |
| `images/source-01.webp` | 002 | The four basic components of an eval task | [Original](https://eugeneyan.com/img/fig-task-anatomy_hu_ac5dc8695b0257a.webp) | 1600 × 701 | `f24c5f81336f29ca95065811373bbb4562adc290ddb5620f738290ce3459b0ba` |
| `images/source-02.webp` | 022 | Terminal Bench Figure 2 | [Original](https://eugeneyan.com/img/tbench-fig2_hu_88131e9d10f1c174.webp) | 1600 × 664 | `2bf8cfa4ae30e4d823127b769db90d943cb7992e72eb8ab719c81c1391780690` |
| `images/source-03.webp` | 036 | GDPval Figure 4 | [Original](https://eugeneyan.com/img/gdpval-fig4_hu_29526e8ec2c4c677.webp) | 1600 × 885 | `c96e5fb9a10405d318287b4740664dc803f09b22dbd73dd4f80e2379ba84173b` |
| `images/source-04.webp` | 043 | AutomationBench Figure 1 | [Original](https://eugeneyan.com/img/automationbench-fig1_hu_a47b2b7545956933.webp) | 1600 × 1163 | `08091023f4832ca4337736b45f96e0c4638ef9922947eaae7bd58c826e292209` |
| `images/source-05.webp` | 047 | How LAB encodes a law firm’s workflow as an agent task | [Original](https://eugeneyan.com/img/harvey-fig_hu_1a7b9fa7fc4dd67d.webp) | 1600 × 643 | `750dfe6d9d5398f3efffc9ccdd5856c53c392f6aa8b1a9e3c59242751728724d` |
| `images/source-06.webp` | 052 | Finance Agent Figure 3 | [Original](https://eugeneyan.com/img/financeagent-fig3_hu_e74f15be86705002.webp) | 1600 × 758 | `35e38435c43d653b620524977e81e534a962d052f568efac5101fa55c9150af0` |
| `images/source-07.webp` | 056 | HealthBench Professional Figure 1 | [Original](https://eugeneyan.com/img/healthbenchpro-fig1_hu_3dd6b2ce53ce4de6.webp) | 1600 × 1274 | `3449b496987b36cb6b63d725b509297f8935ef17503523b6430a3f29c69428b4` |
| `images/source-08.webp` | 060 | BrowseComp example questions | [Original](https://eugeneyan.com/img/browsecomp-qns_hu_9ce0f6cac3897323.webp) | 1600 × 605 | `3f99ad5066f73eaf66895405bb90bb87ce21355a3dec668ed54a1d257df60724` |
| `images/source-09.webp` | 063 | OSWorld 2.0 Figures 3 and 4 | [Original](https://eugeneyan.com/img/osworld-fig3_hu_40f868cc29075fde.webp) | 1600 × 890 | `e6b517b5b018e1ac0afe10a22b8de195c74fa94ecadc9b05c64cdf81236f367b` |

The Finance Agent picture comes from the v1 paper and shows four tools. The accompanying doom explicitly distinguishes that figure from the six-tool v2.1 setup. The HealthBench image contains a clinical response as part of its benchmark-design illustration. The teaching text discusses how evaluation is constructed and graded.

## Access and scope

The complete article body, benchmark sections, conclusion, and all nine images were available. The collection summarizes Yan’s review and the findings he cites. Linked papers, repositories, issue reports, and live leaderboards were not separately reproduced or comprehensively audited. Site navigation, repeated contents lists, subscription prompts, related posts, and the full bibliography are outside the reading sequence. The original article retains all supporting links.

## Verification

The collection validator passed for all 69 Markdown files and their assets. The isolated local Doomer API loaded the complete topic in order, including the first text reel, the second reel’s list and inline figure, the repeated-attempt table, and the labeled illustrative examples. All 9 source-figure routes returned the exact local WebP bytes and valid dimensions. The source figures were visually inspected in contact sheets.

A phone-sized browser preview and in-reader image zoom check could not be performed because local browser access is unavailable in this chat. The reader’s serving paths were verified through the API, while visual rendering of this collection remains unverified.
