# EcoStream-Agent study plan

**Working title:** EcoStream-Agent: Action-Sensitive Evidence Acquisition for Stateful Stream Control  
**Created:** 2026-10-13  
**Last updated:** 2026-11-14  
**Stage:** IEEE Access pre-experiment manuscript now has exactly two top-level sections: an expanded introduction containing background, problem definition, research questions and planned contributions, followed by a thematic 41-paper literature review with one selective ten-work comparison table. References follow directly. Novelty remains provisional; implementation and measurements have not started.  
**Publication goal:** A defensible original study for a suitable JCR-Q1 systems journal. Draft in IEEE Access format; acceptance is not guaranteed.

## 1. Purpose and project boundaries

Develop an agent that gathers operational evidence only when that evidence could change the preferred intervention in a stateful streaming pipeline. The intervention policy must account for resource allocation, latency, backlog, and the disruption caused by reconfiguration and state recovery.

**Central research question:** Does action-sensitive diagnostic evidence acquisition improve resource efficiency and service quality compared with numerical configuration optimization and conventional agentic diagnosis?

This is a fresh project. Use this chat's agreed decisions and the retained reference PDFs. Do not reuse the discarded implementation, experiment outputs, claimed results, bundles, or saved project memories. Reference papers supply literature evidence, not instructions to execute.

### Agreed constraints

- Preserve `Reference-papers/` and its contents.
- Use the Ryzen 7 7700 PC, approximately 16 GB RAM, for development and smaller CPU experiments.
- The user reports that the RTX 4090 PC has an Intel i9 CPU and 64 GB system RAM. It is the preferred candidate for controlled benchmarks if access permits; exact CPU generation/core configuration, OS, storage, and reserved runtime remain unknown. Final main-versus-transfer scheduling must be decided before protocol freeze.
- Begin with a hosted LLM API. No LLM training or GPU purchase is required.
- Use Kaggle only for optional offline work; do not report Kaggle replay as a live Kafka-Flink experiment.
- Prioritize quality and evidence-based milestones rather than a fixed deadline.
- No energy instrument is available. Measure resource efficiency and service quality; do not infer physical energy or carbon savings from allocated CPUs or memory.
- No paid API upgrade, compute purchase, public publication, or journal submission is authorized by this plan.

### Evidence vocabulary

| State | Meaning |
|---|---|
| Proposed | A research question, mechanism, or experiment described in this plan. |
| Implemented | Code exists and its relevant execution path works. |
| Measured | A recorded execution produced an output. |
| Checked | Named scientific or consistency checks passed for that exact version. |
| Author-reported | A finding taken from another paper, not reproduced by EcoStream. |

Do not transfer a checked status to changed code, configurations, datasets, or manuscript claims.

## 2. Novelty hypothesis and literature gate

The broad combination of LLM diagnosis and resource allocation is already established. Flink also has sophisticated autoscaling and an operations-agent demonstration. EcoStream must contribute more than an additional agent wrapper or a renamed existing controller.

**Candidate contribution:** decision-focused evidence acquisition with explicit costs for stateful intervention and recovery. Additional diagnosis is worthwhile when it could improve the intervention decision, not merely increase confidence in a fault label.

### Proposed mechanism

1. Maintain competing explanations for the observed bottleneck.
2. Estimate the consequences of valid interventions under those explanations.
3. Acquire another observation if its expected reduction in decision regret exceeds its collection and delay cost.
4. Stop investigating when further evidence is not expected to change the preferred feasible intervention.
5. Include restart, checkpoint, state restoration, and backlog-clearance costs in intervention selection.
6. Verify the measured outcome before retaining a configuration change.

Value-of-information and diagnostic stopping principles are inherited concepts. The novelty candidate is their specific adaptation to stateful stream-processing decisions and the empirical evidence supporting that adaptation. Do not claim that EcoStream invents these general principles or is the first such system without sufficient evidence.

### Closest work to inspect, in priority order

| Priority | Work | Identifier / primary pointer | Role |
|---|---|---|---|
| 1 | ORACL: Optimized Reasoning for Autoscaling via Chain of Thought with LLMs for Microservices | Related journal DOI: `10.1109/TSC.2026.3707982`; https://arxiv.org/abs/2602.05292 | Closest overlap in LLM diagnosis and allocation. Verify the journal version and inspect acquisition/stopping behavior. |
| 2 | Demeter: Resource-Efficient Distributed Stream Processing under Dynamic Loads with Multi-Configuration Optimization | `10.1145/3629526.3645048`; https://research.spec.org/icpe_proceedings/2024/proceedings/p142.pdf | Strong numerical stream-optimization competitor. |
| 3 | Multi-Dimensional Autoscaling of Stream Processing Services on Edge Devices | `10.1109/TSC.2026.3711142` | Resource/service adaptation and regression-based optimization. |
| 4 | Energy-aware scheduling and two-tier coordinated load balancing for streaming applications in Apache Flink | `10.1016/j.future.2024.107681` | Direct Flink efficiency and scheduling background. |
| 5 | Stream-aware and parameter self-adaptive data partitioning algorithm for fluctuating data stream processing | `10.1016/j.future.2026.108520` | Fluctuating streams and load-skew adaptation. |
| 6 | SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration | `10.1038/s43588-025-00849-y` | Supporting tool-selection reference; a different application. |
| 7 | Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses | `10.1038/s41551-026-01634-6` | Supporting execution/experience-reuse reference; a different application. |

Operational competitor: https://apache.googlesource.com/flink-agents-demos/+/dd82eb7940b17227cd3fdd0e7a78aa2a384adaef/flink-operations-agent-demo/

These are candidate literature records, not a completed identity/support audit. Inspect full text where available, reconcile versions, and mark unavailable passages explicitly.

### Initial review and newly identified overlap

See [Title and 15-paper review](paper/title-and-15-paper-review.md), prepared 2026-10-13. Published-record DOI metadata were checked for all 15 papers. The review records full-text/author-manuscript versus abstract-level access and does not claim a completed source-version or correction/retraction audit.

Additional high-priority competitors identified during this review:

- RCAgent, CIKM 2024, `10.1145/3627673.3680016`: autonomous evidence gathering and diagnosis already used for Alibaba Cloud Flink jobs; includes a finalize/stopping action.
- STREAMLINE, Internet of Things 2025, `10.1016/j.iot.2025.101731`: multi-layer, multi-pipeline auto-tuning and state-preserving updates.
- CAOM, IEEE Transactions on Cloud Computing 2025, `10.1109/TCC.2025.3538512`: bottleneck-aware migration with timing/cost considerations.
- DRRS, ICDE 2025, `10.1109/ICDE65448.2025.00286`: fine-grained stateful scaling execution; not every scaling action should be modelled as a mandatory full restart.

Demeter already acquires configuration-profiling information selectively. Therefore the proposed distinction must concern decision-focused acquisition of operational diagnostic observations, not selective information acquisition in general. These findings sharpen the title without establishing the novelty gate as passed.

On 2026-10-26, the manuscript was expanded with 15 additional published papers: 14 conventional journal articles and Scarf in the journal-style Proceedings of the VLDB Endowment. No new arXiv/preprint entries or arXiv reading sources were used. See [the additional review](paper/additional-15-paper-review.md) and `research/literature/doi-metadata-additional-20261026.json`. Eleven additions have 2024-2026 issue years; two are surveys. Published venue status is verified separately from any current quartile classification, which remains unclaimed.

Scarf (`10.14778/3801059.3801066`) strengthens the Flink tuning comparison; MMP-SPS (`10.1016/j.future.2026.108461`) strengthens the predictive-adaptation comparison. TAMO (`10.1109/TSC.2025.3629066`), LocaleXpert (`10.1109/TSC.2026.3676262`), and MA-RCA (`10.1007/s40747-025-02096-0`) reinforce overlap with tool-assisted/multimodal diagnosis and runtime hypothesis validation. TAMO's final methods remain inaccessible, so its review is explicitly title-level. These additions do not pass M1: obtain closest final versions, reconcile implementations, and test decision-focused acquisition rather than claiming generic agentic diagnosis as novelty.

### Required literature artifacts and gate

- Record dated searches for active diagnosis, budgeted observability, decision-region determination, agentic autoscaling, and stateful configuration optimization.
- Build a comparison matrix covering observations, interventions, evidence acquisition, stopping rules, transition costs, uncertainty, and evaluation.
- Verify each bibliography entry's DOI, publication year/version, relevant claim support, and available correction/retraction notices.
- Prefer peer-reviewed sources from 2022 onward. Apply the workflow's 2020+ eligibility and documented major-preprint exception; a preprint used for overlap screening need not enter the final bibliography.
- Inspect source implementations where available. Distinguish a reproduced method, an adaptation, and an independently implemented inspired baseline.
- Write a concrete novelty statement and its closest counterexample.

**Go/no-go rule:** proceed to substantial method implementation only when a useful technical distinction remains. If the closest work already implements substantially the same mechanism, record the overlap and return a revised mechanism comparison before the main study. Renaming components or increasing agent count does not satisfy this gate.

## 3. System implementation

### Testbed and software

- Docker Desktop with WSL2, a single-node k3d Kubernetes testbed, and real Flink processes.
- Flink 1.20.5 LTS, Java 17, and Flink Kubernetes Operator 1.16.1 as the initial selected versions.
- A single Kafka broker in KRaft mode.
- Java streaming jobs; a Python controller and experiment runner.
- Prometheus metrics, log excerpts, configuration history, pipeline topology, and container resource records.
- Freeze container digests and dependency versions after compatibility smoke tests.
- Initial Docker memory ceiling: approximately 10 GB, reserving memory for Windows. Up to three TaskManagers, subject to the memory pilot.
- Keep the source generator and sink from becoming accidental host-resource bottlenecks; document their allocation and include them in measurement boundaries.

The first environment milestone must confirm that the testbed fits on this PC. Docker was installed but stopped at planning inspection. Single-host process distribution is not evidence of multi-host scalability; report the actual topology.

### Control flow

`Observe -> form competing explanations -> acquire useful evidence -> choose an intervention -> execute -> verify`

1. Sample inexpensive metrics every five seconds and maintain a one-minute summary window.
2. Trigger investigation on sustained service deterioration, inefficient allocation, or an ineffective previous action. Select thresholds using development/calibration episodes and freeze them before final testing.
3. Let the LLM interpret evidence and propose explanations or observations from a bounded catalogue.
4. Let numerical models estimate intervention outcomes and the usefulness of further diagnosis.
5. Execute only typed, supported configuration changes.
6. Verify correctness, latency, backlog, and resource behavior; retain or revert the change.

The agent is a supervisory control loop, not an LLM invocation for every data event. Begin with a single agent and a deterministic executor; add additional agent roles only if a specific experimental obligation justifies them.

### Mathematical specification

Let `E` be current evidence, `h` a plausible bottleneck explanation, `a` an intervention, `q` an additional diagnostic query, and `z` a possible query result. Let `J(a,h)` be predicted resource cost, including transition/recovery overhead, subject to service constraints.

Choose an intervention by minimizing expected cost over plausible explanations. Define the estimated value of another query as:

```text
V(q | E) = min_a E[J(a,h) | E]
           - E_z[min_a E[J(a,h) | E,z]]
           - C(q)
```

`C(q)` includes collection overhead and the cost of delay in consistent units. Acquire evidence only when its estimated value is positive and the investigation budget remains available.

Fit lightweight query-outcome and action-effect models using development executions. Use separate calibration episodes for uncertainty and feasibility assessment. LLM self-reported confidence is not a calibrated probability. Specify model features, calibration, stopping criteria, missing-data behavior, and pseudocode before implementing the decision layer. Mathematical description does not establish a theoretical guarantee.

### Tools and interventions

Diagnostic tools inspect operator backpressure/skew, sink response times, worker health, checkpoint history, state size, and relevant logs. Tools return measured facts and collection-cost records.

Initial intervention catalogue:

- Operator parallelism.
- TaskManager CPU/memory profiles within the host ceiling.
- Checkpoint interval within a fixed recovery requirement.
- No change.

Enumerate valid candidate settings during development profiling, then freeze the candidate space. Count allocation savings only when resources are released; a parallelism change with unchanged worker allocation is not allocation saving.

All policies preserve query semantics, event arrival traces, and correctness. Do not drop events, change window definitions, weaken recovery requirements, or reduce offered load to manufacture an efficiency improvement.

### Shared interfaces

| Interface | Minimum information |
|---|---|
| Observation | Timestamp, metric window, topology, current configuration, and evidence references. |
| ToolResult | Requested observation, measured facts, duration, and collection cost. |
| Diagnosis | Candidate explanations and supporting/contradicting evidence. |
| ActionProposal | Target settings, predicted effects, transition cost, and preconditions. |
| ActionOutcome | Applied settings, measured effects, correctness, and rollback status. |
| RunManifest | Code/configuration hashes, workload seed, policy, model/version metadata, prompts, hardware, and evidence locations. |

All policies share the executor and verifier. Invalid proposals, stale/missing evidence, and API failures use a documented deterministic fallback. Log fallback events and preserve them in the study's outcome accounting. Do not silently change providers during a comparison.

## 4. Data, scenarios, and evaluation protocol

### Workloads

Use three Nexmark queries spanning joins, aggregation, and stateful/windowed processing. Use Yahoo Streaming Benchmark as a separate external workload family. Verify benchmark version and licensing before redistribution.

Public starting points:

- https://beam.apache.org/documentation/sdks/java/testing/nexmark/
- https://github.com/nexmark/nexmark
- https://github.com/lsds/StreamBench

Synthetic event generation is acceptable benchmark evidence, but describe it as such. Measurements must come from actual executions; replay or simulation results remain separately identified.

### Development, calibration, and final evaluation

- Split by complete episodes and generator seeds, not individual metric rows.
- Fit outcome models on development episodes; calibrate on separate episodes.
- Freeze prompts, settings, thresholds, candidate actions, and selection rules before final evaluation.
- Keep injector labels, schedules, and fault identifiers outside controller access.
- Remove injector-specific naming/messages that expose ground truth, while retaining genuine runtime evidence.
- Reset job, policy, and experience state between independent comparisons.
- Evaluate online adaptation separately from the frozen main comparison.
- Do not tune on the external workload or final hardware-transfer outcomes. Limited nominal setup characterization must be declared and shared by all methods.

### Main scenarios

1. Nominal operation, including opportunities where no diagnosis is useful.
2. Sustained traffic bursts.
3. Skewed load distribution.
4. Sink throttling.
5. Checkpoint/storage pressure.
6. Worker degradation.

Additional tests cover unfamiliar combinations, changed state sizes, incomplete telemetry, and the second PC. Include situations where the available actions cannot satisfy an SLO, and report them as such.

### Main comparison policies

1. Tuned fixed configuration.
2. Flink autoscaler with relevant effectiveness/recovery features enabled.
3. Constrained numerical configuration optimization.
4. Conventional agentic diagnosis followed by optimization, with the same tools/actions.
5. EcoStream with decision-focused evidence acquisition.

Develop a Demeter-informed numerical baseline from the paper's specification. Record every adaptation and omitted feature; an inspired approximation is not an exact Demeter reproduction. Give competitors fair development/tuning access and the same workload, action limits, executor, and measurement code. Do not compare literature-reported scores as if they were controlled reruns.

### Ablations

- Replace LLM evidence processing with deterministic processing under the same decision policy.
- Select evidence by diagnostic uncertainty rather than intervention value.
- Use a fixed diagnostic query budget.
- Remove transition-cost modelling.

These tests attribute effects to the agent, evidence-selection policy, and state-transition accounting. Keep negative and inconclusive ablations; do not impose a monotone improvement pattern.

### Outcomes and measurement boundary

**Primary outcome:** allocated CPU core-seconds per correctly processed event, evaluated with correctness and service-quality requirements.

Secondary outcomes:

- Consumed CPU time and allocated memory GB-seconds.
- p99 query-valid output latency and SLA violations.
- Backlog clearance and recovery time.
- Ineffective reconfigurations and rollback frequency.
- Diagnostic queries, API tokens, call latency, and controller overhead.
- Diagnostic localization/calibration where claimed.

For windowed queries, define latency relative to valid output eligibility; report unavoidable window delay separately. Define output completion/correctness per query before comparing methods. Integrate resource use over the full common episode and backlog clearance or a common timeout. Retain incomplete runs and correctness failures as failures.

Count local collection, profiling, controller, and transition overhead. Report the exact set of instrumented processes/components. Hosted inference compute is outside the local measurement boundary; report token use and API latency separately. Allocated capacity, consumed CPU, monetary cost, and physical energy are different quantities.

### Repetitions and uncertainty

- Pilot at least three paired repetitions to measure variability and runtime.
- Initial main matrix: 3 workloads x 6 scenarios x 5 policies x 5 paired repetitions = 450 runs.
- Increase main repetitions to ten before final testing if development-stage variability indicates inadequate precision. Record the calculation and freeze the repetition decision before final outcomes are inspected.
- Randomize policy execution order within matched experimental blocks.
- Use episode-level paired uncertainty estimates; events and metric samples are not independent experimental repetitions.
- Correct families of inferential comparisons for multiplicity; report effect size and uncertainty, not only p-values.
- Preserve all raw records, crashes, incomplete executions, and reasoned exclusions.

At 30 minutes per episode, the 450-run matrix alone would occupy about 225 execution hours, excluding setup, warm-up, and additional tests. This is an estimate, not a measured budget. Revise it from the pilot before committing to the full matrix.

## 5. Claim-test map and advancement criteria

| Intended claim | Required evidence | What weakens or rejects it |
|---|---|---|
| Decision-focused acquisition improves intervention efficiency | EcoStream versus conventional agent and uncertainty-based acquisition under matched tools/actions. | Similar decisions and costs, or investigation overhead cancels the benefit. |
| LLM interpretation contributes useful information | Full method versus deterministic evidence processing. | Deterministic processing matches or improves outcomes; narrow/drop the agent-benefit claim. |
| State-transition accounting helps | Full method versus removal of transition-cost modelling; vary state size. | No reproducible contribution or inaccurate transition estimates. |
| Improvements transfer | Frozen policies on external workload, unfamiliar combinations, and second hardware. | Benefit disappears or requires undisclosed test-specific tuning. |
| Resource savings preserve service quality | Correctness oracle, common latency/backlog/recovery definitions, allocation and usage records. | Lossy results, shifted semantics, accumulating backlog, or incomplete measurement boundaries. |

**Pilot advancement gate:** correctness survives reconfiguration/recovery; instrumentation matches allocation; leakage checks pass; strong baselines work; and at least one targeted scenario shows a reproducible benefit exceeding investigation overhead.

A pilot gain is a lead, not a final result. If the central mechanism fails, investigate the failure and revise/narrow the contribution before expensive final experiments. Do not fill evidence gaps with expected scores.

## 6. Manuscript and deliverables

`paper/` now contains the official IEEE Access template and an initial pre-experiment manuscript. Its literature review is drafted; methodology, experimental results, and empirical conclusions are explicitly pending. The template is not a generic IEEE conference substitute.

Current artifacts: `paper/main.tex`, `paper/sections/literature-review.tex`, `paper/references.bib`, and `paper/main.pdf`. The bibliography contains 41 published papers with distinct DOI records. The 2026-11-14 revision adds an eligible active-feature-acquisition survey, replaces the two inventory tables with one selective ten-work table, and narrows the title and objective language. The original standalone 15-paper review is preserved. Source-access/version qualifications and incomplete notice checks are recorded in `research/literature/reference-ledger.csv`, `integration-notes.md`, and dated expansion records; compilation does not establish novelty or submission readiness.

Planned manuscript artifacts:

- `paper/main.tex`: evolving manuscript.
- `paper/references.bib`: eligible references with checked identity and claim support.
- `paper/supplement.tex`: full configurations and extended reproduction/evaluation details.
- Editable vector diagrams, data-derived plots/tables, compiled PDFs, and a clean source archive.

Maintain separate research records for literature, methodology specification, protocol, decisions, run provenance, and claim-evidence tracking. These are fresh study artifacts, not reuse of old saved memories.

### Current paper structure

1. Title, abstract, and keywords.
2. Section I, Introduction: background, operational problem, study scope, research questions and one substantive list of planned contributions.
3. Section II, Literature Review: comparative related work, critical gap and evidence-scope limitations.
4. References.

This deliberately restricted two-section draft follows the user's current manuscript scope. Methodology, protocol, results, discussion and conclusion remain research deliverables in the plan and must not be inserted into the paper until requested and supported by implementation or measurements. Finalize empirical claims only after checked measurements exist.

Use `D:\1.msc\Good_paper_instructions` for writing direction and its corrected instruction audit for interpreting the historical assignment examples. Transfer clarity, mathematical depth, comparative reasoning, and vector-figure practices; do not copy domain modules or force duplicated sections.

Treat 40-60 references as a justified coverage target, not a padding quota. Prefer recent peer-reviewed sources with verified DOIs. Do not place unsupported preprints or candidate-only records into a readiness-approved bibliography.

Final validation includes code-method agreement, DOI/support audit, numerical consistency, compilation, rendered-page inspection, and a clean extracted-package build. Disclose actual AI assistance under current venue policy. Do not invent authors, funding, ethics approvals, repository availability, or submission metadata.

IEEE Access is the drafting format, not the strict JCR-Q1 target. Future Generation Computer Systems is the primary venue candidate, subject to current scope/ranking checks and the completed study. Format changes for a selected final venue happen after the evidence and argument are stable.

Official pointers:

- https://ieeeaccess.ieee.org/authors/preparing-your-article/
- https://ieeeaccess.ieee.org/authors/submission-guidelines/
- https://flink.apache.org/downloads/
- https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-stable/docs/managing/autoscaler/

## 7. Required user inputs and resource assumptions

| Input | Required when | Current status |
|---|---|---|
| Dedicated current-PC experiment blocks and Docker Desktop running | Environment/pilot and main experiments. | PC available; dedicated schedule not recorded. |
| Approximately 40 GB initially reserved for dependencies/evidence | Setup; revise storage estimate after pilot. | About 151 GiB free on D: at planning inspection. |
| Gemini API key configured through a local environment variable | First live-agent experiment. | Not supplied/configured or tested. |
| Actual accessible model and account quotas | Before experiment budgeting/protocol freeze. | Not checked for this user's account. |
| DeepSeek granted credit/API access | Optional provider comparison. | User reports possible free access; official API access/credit not checked. |
| 4090-PC specifications and reserved sessions | Controlled benchmarks / hardware-transfer validation. | User reports Intel i9, 64 GB system RAM, and RTX 4090 with 24 GB VRAM. Exact CPU generation/core configuration, OS, storage, and access schedule remain unknown. |
| Author names, affiliations, order, funding facts, availability decisions | Final manuscript/declarations. | Not yet supplied. |

Never put API keys in chat-visible output, manuscript files, run manifests, or committed configuration. Use environment variables/local secret configuration. Do not assume free chatbot access implies free API access. Freeze the tested provider/model configuration and record response/version metadata where available.

The initial study assumes no paid cloud resources. The 4090 GPU and Kaggle GPU hours are optional; the main pipeline is CPU based. The earlier 15-25-hour estimate was for reduced second-PC validation, not the full main experiment matrix. With the reported i9/64 GB specifications, benchmark placement and the required access budget should be revised after a measured pilot; no dedicated schedule has yet been confirmed.

## 8. Milestones and progress tracker

| Milestone | Deliverable / acceptance condition | Status |
|---|---|---|
| M0 - Fresh plan | Save this plan, verify reset, preserve reference papers, record agreed constraints. | Complete: plan written; reset inspection found only Reference-papers before creation. |
| M1 - Novelty audit | Dated search log, verified competitor matrix, precise distinction, claim-test mapping, go/no-go decision. | In progress: review expanded to 41 published papers, one selective ten-work comparison table, dated DOI metadata and access ledger. General cost-aware acquisition is now explicitly treated as prior art. Final-version/access and notice checks, competitor implementation inspection, and go/no-go decision remain pending. |
| M2 - Scaffold and pre-experiment paper | Fresh code/research organization, official IEEE Access template, compilable draft with pending findings. | In progress: official template, two-section manuscript, 41-paper thematic literature review, and rebuilt PDF. Full methods/protocol drafting and code scaffold remain pending. |
| M3 - Instrumented baseline | Real jobs, correctness oracle, telemetry, supported reconfiguration, allocation records, leakage tests. | Not started. |
| M4 - Minimum viable EcoStream | Sink-throttling and worker-degradation pilot against numerical and conventional agentic control. | Not started. |
| M5 - Protocol freeze | Fixed versions, model/prompts, action/tuning budgets, thresholds, measurement definitions, repetition decision, final manifests. | Not started. |
| M6 - Main experiments and ablations | Preserved runs, derived tables/plots, failures, paired uncertainty estimates. | Not started. |
| M7 - External validation | Held-out workload/conditions and reduced second-PC evaluation without test selection. | Not started. |
| M8 - Final paper/package audit | Evidence-backed manuscript, checked bibliography, figures, PDF QA, clean package build, remaining-action report. | Not started. |

### Updating this plan throughout the study

- Update the last-updated date, current stage, milestone status, blockers, and next action after each meaningful work session.
- Record what was actually executed and where its evidence lives. Preparation does not complete a measurement milestone.
- Record changes to the mechanism/protocol as dated deviations with rationale and affected claims/reruns.
- Keep resolved issues distinct from pending user inputs and optional enhancements.
- Reference supporting research/run artifacts rather than duplicating large logs in this file.
- Do not mark the study complete because a manuscript compiles or a favorable pilot exists.

## 9. Current blockers and next actions

**Immediate non-blocked work:** perform M1, establish the literature and mechanism comparison, and prepare the fresh manuscript/scaffold without fabricated results.

**Inputs needed before dependent work:** active Docker environment for real execution; a tested API key/quota for live-agent runs; second-PC specifications/access for hardware validation.

**Next action:** resolve the closest competitors' unavailable full texts and manuscript-to-published-version differences, specify the measurable evidence-acquisition distinction, and finish the M1 gate. The review recommends a 36-run decision-quality pilot before committing to the large main matrix; this is not yet a frozen protocol. Match every injected incident to a supported shared action and include a strong deterministic controller. Do not begin expensive final experiments before M1 and M4 pass.

## 10. Session log

| Date | Work completed | Evidence / consequence |
|---|---|---|
| 2026-10-13 | Agreed the study plan in this chat; inspected project reset, writing instructions, current-PC hardware, and current official documentation. | Only Reference-papers remained; current PC has Ryzen 7 7700 and approximately 16 GB RAM; no measured EcoStream findings exist. |
| 2026-10-13 | Created plan.md with milestones, measurement boundaries, novelty gate, resource needs, and update rules. | M0 complete. All implementation/experimental milestones remain pending. |
| 2026-10-13 | Recorded user-provided i9/64 GB RAM specifications for the RTX 4090 PC. | Hardware feasibility improves, but exact CPU/OS and dedicated experiment access remain unconfirmed. |
| 2026-10-13 | Created paper/title-and-15-paper-review.md; checked 15 published DOI records, inspected available primary evidence, and compared nearest mechanisms. | M1 in progress, not complete. RCAgent, STREAMLINE, CAOM, and DRRS strengthen the competition; the title now emphasizes evidence acquisition. No code, results, final manuscript, or novelty approval was created. |
| 2026-10-13 | Added a thematic literature review to a new official IEEE Access-format manuscript because no main manuscript previously existed; integrated all 15 published references and a comparison table. | paper/main.tex, sections/literature-review.tex, references.bib, and four-page main.pdf created; all 15 cited, DOI links checked, and all pages visually inspected. M2 in progress. Reference readiness remains pending; no implementation or experimental findings exist. |
| 2026-10-26 | Finished delivery verification of the literature integration: fresh-output-directory LaTeX/BibTeX build, all-15 narrative citation check, unique DOI/entry checks, per-reference visible and clickable DOI checks, and visual inspection of all four pages. | research/literature/integration-validation-20261026.md records passing artifact checks and line-wrap false positives in the earlier audit. The requested integration is complete; M1/M2 remain in progress because source checks, full methods/protocol, implementation, and experiments are unfinished. |
| 2026-10-26 | Added 15 further published papers, emphasizing journals and excluding new arXiv sources; integrated all additions into the thematic review, bibliography, comparison table, reading notes, and source ledger; rebuilt and visually checked all six PDF pages. | 30 distinct published references, all cited in prose with visible/clickable DOI links; see research/literature/expansion-validation-20261026.md. Scarf and recent diagnosis work sharpen the novelty comparison. TAMO's final-method access and other source/version/notice checks remain pending. No controller, experiment, or measured gain was created. |
| 2026-10-27 | At the user's request, removed all sections after the literature review except references, including methodology/experimental/results/discussion placeholders and the draft AI disclosure. Updated the source date and rebuilt the PDF. | Literature-review source and bibliography are byte-for-byte unchanged; all 30 references and DOI links remain. All six rendered pages inspected. Prior main source/PDF retained under tmp/manuscript-trim-baseline-20261027 for recovery. Study and source-verification status are unchanged; actual drafting assistance remains recorded in project history. |
| 2026-11-02 | Restructured the manuscript into exactly two top-level sections; expanded the introduction with systems background, the decision problem, four research questions and four planned contributions; added ten published DOI references and integrated them thematically. | The clean IEEE Access build is seven pages with 40 bibliography entries, 40 substantively cited keys, no missing or unused citations, and 40 distinct DOI targets. All pages were rendered and visually inspected. The contribution language remains explicitly pre-experiment; source notice checks and several final-method reconciliations are still pending. |
| 2026-11-14 | Replaced the two 15-paper inventory tables with one selective ten-work positioning table; narrowed the unvalidated title claim; clarified constrained operational objectives; and added a published active-feature-acquisition survey to acknowledge the broader cost-aware acquisition literature. | The manuscript now contains 41 published references and avoids claiming generic evidence acquisition, stopping, or resource efficiency as an established contribution. Source/PDF validation is recorded in the delivery report; implementation and experiments remain pending. |
| 2026-11-14 | Integrated the reviewed humanized abstract, introduction, and literature-review prose into the IEEE Access manuscript, preserving the research-question and contribution structure, citation keys, ten-work table, and bibliography. | Rebuilt paper/main.pdf; this is a prose revision only. The novelty gate, methods, implementation, and experiments remain pending. |
