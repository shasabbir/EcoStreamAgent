# EcoStream-Agent: Decision-Focused Evidence Acquisition for Resource-Efficient Stateful Stream Processing

**Working study title and critical review of 15 papers**  
**Prepared:** 2026-10-13  
**Study status:** Proposed; no EcoStream implementation or experimental results exist yet.  
**Purpose:** Establish the strongest relevant foundations, identify existing capabilities, and sharpen the contribution before implementation.

## 1. Proposed study in brief

EcoStream-Agent will investigate when a stream-processing controller should obtain additional diagnostic evidence before changing a running job. A delayed pipeline might need more processing capacity, a different checkpoint configuration, or no resource change at all. Further investigation can help distinguish these situations, but tool collection, LLM calls, and waiting also have costs. Meanwhile, reconfiguration can interrupt processing and create a backlog while state is restored.

The proposed controller will select evidence according to its expected effect on the intervention decision, rather than collecting everything or pursuing a confident fault label regardless of operational value. Numerical models will estimate action effects and transition costs; the agent will interpret operational evidence; a bounded executor will apply and verify supported actions. We will test whether this combination improves resource use without weakening correctness, latency, or recovery requirements.

The title is provisional. Resource efficiency must eventually be demonstrated, and the agent's contribution must survive comparison with deterministic alternatives. Physical energy and carbon savings are not promised: no suitable energy instrument has been supplied.

**Central research question:** Does decision-focused diagnostic evidence acquisition improve stateful streaming interventions enough to outweigh its collection and delay costs?

## 2. Scope and evidence conventions

The selection contains **15 distinct published papers: 10 journal articles and 5 conference papers**. Eleven have 2025–2026 publication years in the versions recorded below. Four older, directly relevant competitors are retained because excluding them would weaken the novelty assessment.

This is a focused critical review, not an exhaustive systematic review or a completed submission bibliography. Journal quartiles are not assigned here: a Q1 statement requires the ranking database, category, and year. Conference papers do not receive journal quartiles. Relevance to EcoStream is more important than forcing a particular publisher into the list.

Evidence labels used below:

- **FT:** Relevant full-text passages were inspected. This does not mean every supplement, implementation, or result was reproduced.
- **AM:** An author manuscript was inspected and linked to a verified published record. Changes between that manuscript and the final publisher version may remain unresolved.
- **AB:** The review is restricted to a publisher abstract/highlights or their indexed primary-source text. Unavailable methods and evaluation details are not inferred.
- **RP:** An author project repository was inspected as additional operational evidence; its presence does not establish reproducibility.

DOI identity, title, authors, publication type, and dates were checked against Crossref records, with publisher, proceedings, or institutional records where accessible. DOI resolver requests were also attempted for selected records; some publisher pages returned access or automated-client errors. An access failure is not evidence that a DOI is invalid. The retrieved Crossref records exposed no `update-to` notices, but a comprehensive Crossmark/correction/retraction audit remains pending.

All performance statements are **author-reported**, not EcoStream measurements. Critical assessments and proposed extensions are our interpretations, not necessarily limitations stated by the original authors. Author manuscripts are reading sources for published papers; ordinary preprints are not substituted for published bibliography entries.

### Publication-date corrections that matter

- MUDAP/RASK and ORACL have verified **2026 IEEE journal records**; their arXiv dates are not the journal publication dates.
- Ra-Stream has a **2026 FGCS issue record**, although its DOI contains `2025`.
- The Flink energy-aware scheduling paper is in **FGCS, May 2025**, although its DOI contains `2024`.
- The Nature Energy paper appeared online on **5 December 2025** and in the **February 2026 issue**. Both dates are recorded; the issue citation below uses 2026.

## 3. Reading order and role in the study

| No. | Paper / system | Published version | Role for EcoStream |
|---|---|---|---|
| 1 | ORACL | IEEE Transactions on Services Computing, 2026 | Closest joint LLM diagnosis and allocation competitor |
| 2 | RCAgent | ACM CIKM, 2024 | Direct autonomous diagnosis competitor already used for Flink jobs |
| 3 | Demeter | ACM/SPEC ICPE, 2024 | Multi-configuration optimization, selective profiling, and recovery constraints |
| 4 | STREAMLINE | Internet of Things, 2025 | Recent ensemble-wide auto-tuning and state-preserving updates |
| 5 | CAOM | IEEE Transactions on Cloud Computing, 2025 | Cost-aware bottleneck detection and migration timing |
| 6 | MUDAP / RASK | IEEE Transactions on Services Computing, 2026 | Strong sample-efficient numerical adaptation reference |
| 7 | DRRS | IEEE ICDE, 2025 | Efficient stateful scaling execution, distinct from decision selection |
| 8 | Ra-Stream | Future Generation Computer Systems, 2026 | Communication-aware fine-grained scheduling and autoscaling |
| 9 | SAP-DPO | Future Generation Computer Systems, 2026 | Stream-aware partitioning and adaptive update frequency |
| 10 | ESSA / TTCLB-EA | Future Generation Computer Systems, 2025 | Direct Flink efficiency and energy-aware scheduling background |
| 11 | Daedalus | ACM/SPEC ICPE, 2024 | Online capacity modelling and proactive horizontal autoscaling |
| 12 | Phoebe | IEEE ICWS, 2022 | Earlier recovery-aware tuning that must be acknowledged |
| 13 | SciToolAgent | Nature Computational Science, 2025 | Supporting tool-selection and execution design |
| 14 | BioMedAgent | Nature Biomedical Engineering, 2026 | Supporting interactive execution and experience-reuse design |
| 15 | AI data centres as grid-interactive assets | Nature Energy, 2026; online 2025 | Sustainability motivation and physical-measurement discipline |

The first six should receive priority before committing to the main method. Papers 13–15 support particular design or measurement choices; they are not direct streaming-controller baselines.

## 4. Individual paper reviews

### 1. ORACL: Optimized Reasoning for Autoscaling via Chain of Thought With LLMs for Microservices

**Reference:** Haoyu Bai, Muhammed Tawfiqul Islam, Minxian Xu, and Rajkumar Buyya. *IEEE Transactions on Services Computing*, 2026. [DOI: 10.1109/TSC.2026.3707982](https://doi.org/10.1109/TSC.2026.3707982).

**Evidence inspected:** AM; journal identity checked. The accessible manuscript's Sections III–V describe the architecture, reasoning, action generation, and evaluation. The final IEEE text was not accessible for a version-by-version reconciliation.

**What they did:** ORACL turns microservice telemetry and deployment context into a structured prompt. The LLM identifies likely causes, reasons about hypothetical resource changes, and generates executable recommendations. Numerical forecasting is delegated to an external component, and a rule-based interface checks actions. Fine-tuning and reinforcement learning improve the reasoning policy. The authors evaluate diagnosis and service-quality outcomes on microservice workloads. [Inspected manuscript](https://arxiv.org/html/2602.05292v1).

**Critical assessment:** Diagnosis followed by allocation, numerical forecasting outside the LLM, and execution guards are already present. EcoStream cannot claim those as its central novelty. The inspected design does not establish EcoStream's proposed criterion for purchasing another diagnostic observation under stateful recovery costs.

**Use in EcoStream:** A primary novelty counterexample and an agentic-allocation comparator. If adapted without ORACL's training procedure, label the baseline as ORACL-inspired, not an exact reproduction.

### 2. RCAgent: Cloud Root Cause Analysis by Autonomous Agents with Tool-Augmented Large Language Models

**Reference:** Zefan Wang et al. *Proceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM)*, 2024. [DOI: 10.1145/3627673.3680016](https://doi.org/10.1145/3627673.3680016).

**Evidence inspected:** FT/AM; the accessible manuscript explicitly identifies CIKM 2024 and the same DOI. Relevant passages: Sections 3–6 and Tables 1–3.

**What they did:** RCAgent autonomously gathers operational information and uses analytical tools, including specialist LLM agents. It introduces observation snapshot keys to manage lengthy evidence, output repair, error handling, and trajectory self-consistency. The controller can decide when to finalize its diagnosis. Evaluation includes 161 curated anomalous jobs and diagnosis/solution assessments; the system was integrated into Alibaba Cloud's Flink diagnosis workflow. [Method and evaluation](https://arxiv.org/html/2310.16340v2).

**Critical assessment:** Autonomous tool selection, context efficiency, stopping, and Flink diagnosis are not new opportunities by themselves. The reported diagnosis-quality evaluation is different from demonstrating fewer allocated core-seconds after executing controlled streaming interventions.

**Use in EcoStream:** The strongest reference for a conventional diagnostic-agent baseline. Compare stopping *criteria*, not merely whether an agent can stop. Production data access is not assumed available to us.

### 3. Demeter: Resource-Efficient Distributed Stream Processing under Dynamic Loads with Multi-Configuration Optimization

**Reference:** Morgan K. Geldenhuys, Dominik Scheinert, Odej Kao, and Lauritz Thamsen. *Proceedings of the 15th ACM/SPEC International Conference on Performance Engineering (ICPE)*, 2024. [DOI: 10.1145/3629526.3645048](https://doi.org/10.1145/3629526.3645048).

**Evidence inspected:** FT; published PDF, Sections 2 and 3, especially Figure 1 and Sections 3.5.3–3.6.

**What they did:** Demeter combines workload forecasting, multi-objective Bayesian optimization, and parallel profiling to tune workers, CPU, memory, processing slots, and checkpoint interval. It optimizes resources subject to latency and recovery constraints. Profiling is selective, guided by information gain, and can be skipped. Including profiling costs, the authors report CPU reductions of 7% and 3%, and memory reductions of 32% and 35%, across their two benchmark experiments relative to static configurations. [Published paper](https://eprints.gla.ac.uk/322287/1/322287.pdf).

**Critical assessment:** Recovery-aware tuning and selective information acquisition already exist. The remaining candidate distinction concerns operational diagnostic queries about competing bottlenecks, rather than choosing additional configuration-profiling executions.

**Use in EcoStream:** A key numerical baseline and accounting reference. Include profiling overhead and acknowledge that the most resource-efficient policy need not be the same for CPU and memory.

### 4. STREAMLINE: Dynamic and Resource-Efficient Auto-Tuning of Stream Processing Data Pipeline Ensembles

**Reference:** Stefan Pedratscher et al. *Internet of Things*, vol. 34, article 101731, November 2025. [DOI: 10.1016/j.iot.2025.101731](https://doi.org/10.1016/j.iot.2025.101731).

**Evidence inspected:** AB/RP; publisher abstract/highlights and the author repository README. Detailed paper methods and evaluation tables remain to be inspected.

**What they did:** STREAMLINE predicts workloads with transformers, tunes configurations with an evolutionary algorithm, and schedules operators across resources while considering multiple pipelines. Its publisher abstract describes updates that preserve state and reduce downtime, with evaluation on Grid'5000. The authors report improved throughput, latency, utilization, and cost relative to their comparators. [Publisher record](https://www.sciencedirect.com/science/article/pii/S2542660525002458). The repository illustrates NSGA-II-based tuning and shared-resource scheduling. [Author repository](https://github.com/UIBK-DPS-DC/Streamline).

**Critical assessment:** This is a recent, substantial competitor to broad claims about holistic Flink auto-tuning. Abstract-level access cannot establish whether its internal evidence-acquisition policy overlaps with our proposal.

**Use in EcoStream:** Prioritize full-text and source inspection. Evaluate resource contention across pipelines only if the study explicitly adds that scope and can support a fair comparison; a single-job pilot is not an ensemble-wide evaluation.

### 5. A Cost-Aware Operator Migration Approach for Distributed Stream Processing System

**Reference:** Jiawei Tan et al. *IEEE Transactions on Cloud Computing*, vol. 13, no. 1, pp. 441–454, 2025. [DOI: 10.1109/TCC.2025.3538512](https://doi.org/10.1109/TCC.2025.3538512).

**Evidence inspected:** AB; the indexed IEEE abstract was available, but direct full-text access was blocked. Relevant support is limited to that abstract.

**What they did:** CAOM detects bottleneck operators from runtime metrics to avoid repeated migrations caused by hidden dependencies. It accounts for time-varying migration costs and chooses a migration start time to reduce data accumulation during interruptions. The authors implemented the approach in Flink and evaluated WordCount and Nexmark, reporting fewer migrations and lower migration-related latency overhead. [IEEE paper](https://ieeexplore.ieee.org/document/10872811/).

**Critical assessment:** Migration cost, bottleneck-aware interventions, and backlog-sensitive timing already have direct streaming precedents. Adding a restart penalty alone would be an insufficient contribution. Detailed detection accuracy, cost estimation, and comparisons remain unreviewed.

**Use in EcoStream:** Ground the state-transition model in this work and test whether buying another observation changes the preferred action or timing. Do not claim to improve migration execution if EcoStream only chooses configurations.

### 6. Multi-Dimensional Autoscaling of Stream Processing Services on Edge Devices

**Reference:** Boris Sedlak, Philipp Raith, Andrea Morichetta, Víctor Casamayor Pujol, and Schahram Dustdar. *IEEE Transactions on Services Computing*, 2026. [DOI: 10.1109/TSC.2026.3711142](https://doi.org/10.1109/TSC.2026.3711142).

**Evidence inspected:** AM; 2026 journal identity checked. Relevant manuscript passages: Sections III–VI and Algorithm 1. Final journal-version reconciliation remains pending.

**What they did:** MUDAP exposes resource- and service-level elasticity parameters. RASK uses expert-supplied structural relationships, polynomial regression, and numerical optimization to allocate bounded resources across competing services. It includes exploration and solver caching. Experiments cover up to nine service instances and compare with Kubernetes VPA and reinforcement learning; a tested model could be learned in 20 iterations, corresponding to 200 seconds. [Inspected manuscript](https://arxiv.org/html/2510.06882v2).

**Critical assessment:** RASK is a numerical scaling agent, not an LLM diagnostic agent. Some actions trade service quality or model size for performance, whereas EcoStream's exact streaming queries must preserve their semantics. Those action spaces cannot be compared as if equivalent.

**Use in EcoStream:** Learn from its sample-efficient action-effect modelling, constrained solver, and controller-overhead evaluation. A RASK-inspired baseline must use the same permitted actions as EcoStream.

### 7. Towards Fine-Grained Scalability for Stateful Stream Processing Systems

**Reference:** Yunfan Qing and Wenli Zheng. *2025 IEEE 41st International Conference on Data Engineering (ICDE)*, pp. 3835–3848, 2025. [DOI: 10.1109/ICDE65448.2025.00286](https://doi.org/10.1109/ICDE65448.2025.00286).

**Evidence inspected:** AM; published conference identity checked. Relevant manuscript passages: method overview, Section V, and Sections VI–VII.

**What they did:** DRRS reduces the execution overhead of stateful scaling through decoupled scaling signals and re-routing, record reordering, and subdivision of migrating state. Its Flink prototype is evaluated with Nexmark, Twitch-derived events, and a configurable stateful workload, including multi-machine sensitivity tests. The authors report reductions in scaling-related latency and duration. [Inspected manuscript](https://arxiv.org/html/2503.11320v1).

**Critical assessment:** DRRS primarily improves *how* a selected scaling operation executes; EcoStream proposes to improve *whether to investigate and which intervention to choose*. DRRS also shows why it would be wrong to treat every stateful scaling action as a mandatory full restart.

**Use in EcoStream:** Measure the actual transition path of the selected Flink version. Vary state size and report recovery/backlog costs. Engine changes such as DRRS are an optional separate implementation scope, not a required first-stage component.

### 8. A fine-grained task scheduling strategy for resource auto-scaling over fluctuating data streams

**Reference:** Yinuo Fan, Dawei Sun, Minghui Wu, Shang Gao, and Rajkumar Buyya. *Future Generation Computer Systems*, vol. 175, article 108119, 2026. [DOI: 10.1016/j.future.2025.108119](https://doi.org/10.1016/j.future.2025.108119).

**Evidence inspected:** AB plus the indexed first-page text of an author-hosted published PDF. Full method/evaluation tables were not accessible in this review session.

**What they did:** Ra-Stream jointly addresses fluctuating resource needs, application subgraph partitioning, communication dependencies, and fine-grained task placement. It combines a resource-scaling algorithm with heuristic graph partitioning and thread-level deployment. Evaluation in a distributed stream-computing environment reports improvements in latency, throughput, and resource utilization. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0167739X25004133). [Author-hosted paper](https://clouds.cis.unimelb.edu.au/~rbuyya/papers/AutoScale_StreamFGCS.pdf).

**Critical assessment:** Resource shortages are not the only reason for poor streaming performance; communication and placement also matter. Abstract-level findings cannot justify a claim that an LLM would improve Ra-Stream's scheduler.

**Use in EcoStream:** Include topology and communication evidence when applicable. Keep the initial executor bounded; distinguish failures due to resource capacity from failures the available placement/action catalogue cannot remedy.

### 9. Stream-aware and parameter self-adaptive data partitioning algorithm for fluctuating data stream processing

**Reference:** Yifan Ren and Hongjian Li. *Future Generation Computer Systems*, article 108520, 2026. [DOI: 10.1016/j.future.2026.108520](https://doi.org/10.1016/j.future.2026.108520).

**Evidence inspected:** AB and indexed publisher introduction/contributions. Detailed algorithms and evaluation tables remain unavailable.

**What they did:** SAP-DPO improves dynamic partitioning with a stream-load model, an adaptive update-cycle model, and sliding-window parameter adjustment. It responds to fluctuating input rates and task-instance imbalance. The authors compare against Flink's default strategy, St-Stream, Dr-Stream, and LADP, reporting throughput and latency improvements on their tested workloads. [Publisher record](https://www.sciencedirect.com/science/article/abs/pii/S0167739X26001548).

**Critical assessment:** Adaptive monitoring/update frequency is already relevant streaming work, although changing a partitioning cycle differs from selecting diagnostic evidence by intervention value. A novelty claim about adaptive observation frequency alone would be too broad.

**Use in EcoStream:** Use skew as a distinct bottleneck condition. If repartitioning is not a supported action, do not count recognizing skew as successful remediation. Investigate whether a strong deterministic partitioning policy would remove the apparent need for an LLM.

### 10. Energy-aware scheduling and two-tier coordinated load balancing for streaming applications in Apache Flink

**Reference:** Hongjian Li, Junlin Li, Xiaolin Duan, and Jianglin Xia. *Future Generation Computer Systems*, vol. 166, article 107681, May 2025. [DOI: 10.1016/j.future.2024.107681](https://doi.org/10.1016/j.future.2024.107681).

**Evidence inspected:** AB; publisher abstract and highlights. Instrumentation and detailed experimental methods were not available.

**What they did:** The authors design an SLA-based energy-efficiency model and an energy-saving scheduling algorithm, ESSA. TTCLB-EA coordinates load balancing across nodes and within nodes while considering heterogeneous energy efficiency. Their experiments compare with default scheduling, round-robin scheduling, and St-Stream and report improved balancing and reduced energy consumption. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0167739X24006459).

**Critical assessment:** Energy-aware Flink scheduling is established. The abstract does not provide enough evidence to independently assess the measurement boundary or distinguish measured energy from modelling. A single physical host also cannot directly reproduce a heterogeneous multi-node energy-efficiency study.

**Use in EcoStream:** Motivate the resource/performance trade-off, but retain our resource-efficiency endpoint. Do not compare our core-second reductions directly with this paper's energy percentages, and do not reuse its energy claim without inspecting the underlying methods.

### 11. Daedalus: Self-Adaptive Horizontal Autoscaling for Resource Efficiency of Distributed Stream Processing Systems

**Reference:** Benjamin J. J. Pfister, Dominik Scheinert, Morgan K. Geldenhuys, and Odej Kao. *Proceedings of the 15th ACM/SPEC International Conference on Performance Engineering (ICPE)*, pp. 130–141, 2024. [DOI: 10.1145/3629526.3645042](https://doi.org/10.1145/3629526.3645042).

**Evidence inspected:** FT; published proceedings PDF, abstract, capacity-model passages, and Sections 4.7–4.8.

**What they did:** Daedalus learns worker processing capacity from runtime observations and combines that model with workload forecasting for proactive horizontal scaling. Evaluation spans Flink and Kafka Streams. The abstract reports resource reductions of up to 71%; importantly, its Phoebe comparison also shows trade-offs: fewer resources need not mean lower latency, and profiling cost changes the resource comparison. [Published paper](https://research.spec.org/icpe_proceedings/2024/proceedings/p130.pdf).

**Critical assessment:** Simple numerical models can already yield substantial savings. EcoStream must show added operational value beyond capacity prediction, not only outperform an over-provisioned static deployment. Reported maxima are not expected gains for our workloads.

**Use in EcoStream:** Include a strong low-overhead capacity-based controller. Examine resource/latency trade-offs and count development/profiling overhead separately and consistently.

### 12. Phoebe: QoS-Aware Distributed Stream Processing through Anticipating Dynamic Workloads

**Reference:** Morgan K. Geldenhuys, Dominik Scheinert, Odej Kao, and Lauritz Thamsen. *2022 IEEE International Conference on Web Services (ICWS)*, pp. 198–207, 2022. [DOI: 10.1109/ICWS55610.2022.00041](https://doi.org/10.1109/ICWS55610.2022.00041).

**Evidence inspected:** FT/AM; author-hosted paper and a university record identifying a refereed published conference contribution. Relevant passages: abstract, Introduction, and background/recovery discussion.

**What they did:** Phoebe combines parallel profiling, latency and recovery models, workload forecasting, and runtime tuning. It selects resource allocations that preserve service quality and satisfy recovery-time targets. Its motivation explicitly explains that running at full normal-load utilization leaves insufficient spare capacity to clear the backlog after failure. The authors demonstrate reduced over-provisioning with stable service. [Paper](https://lauritzthamsen.org/assets/texts/GeldenhuysScheinertKaoThamsen_2022_PhoebeQoSAwareDistributedStreamProcessingThroughAnticipatingDynamicWorkloads.pdf). [Publication record](https://eprints.gla.ac.uk/272111/).

**Critical assessment:** Recovery-aware autoscaling is not a new 2026 contribution. Resource savings that merely postpone processing or grow the backlog are not meaningful improvements.

**Use in EcoStream:** Justify explicit recovery requirements and accounting through backlog clearance. Retain this older paper for necessary attribution rather than presenting a newer paper as the origin of the idea.

### 13. SciToolAgent: a knowledge-graph-driven scientific agent for multitool integration

**Reference:** Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang, and Huajun Chen. *Nature Computational Science*, vol. 5, pp. 962–972, 2025. [DOI: 10.1038/s43588-025-00849-y](https://doi.org/10.1038/s43588-025-00849-y).

**Evidence inspected:** AB; publisher abstract, figure captions, and availability information. Main-text methods and detailed benchmark results remain to be inspected.

**What they did:** SciToolAgent organizes scientific tools through a knowledge graph and uses graph-based retrieval to support selection and execution. It includes tool-use safety checks and evaluates scientific workflows in biology, chemistry, and materials science. The authors report stronger performance on a curated benchmark and demonstrate several application cases. [Publisher record](https://www.nature.com/articles/s43588-025-00849-y).

**Critical assessment:** This supports structured tool orchestration, not a claim about stream-processing efficiency. With only a small operational tool catalogue, a knowledge graph might add complexity without measurable benefit.

**Use in EcoStream:** Adopt clear tool contracts, dependencies, evidence provenance, and bounded execution. Add retrieval or a tool graph only if catalogue complexity warrants it and an ablation demonstrates value; do not copy the architecture simply because the paper is prestigious.

### 14. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses

**Reference:** Dechao Bu et al. *Nature Biomedical Engineering*, published online 30 March 2026. [DOI: 10.1038/s41551-026-01634-6](https://doi.org/10.1038/s41551-026-01634-6).

**Evidence inspected:** FT; retained PDF pages 1–3 and 7, including Figure 1 and interactive-exploration evaluation. Publication date was checked against Crossref because the retained PDF contains an unresolved online-date placeholder.

**What they did:** BioMedAgent separates planning, coding, and execution and learns to use specialized tools. Interactive exploration repairs unsuccessful workflows, while memory retrieval reuses successful tool choices, workflows, and code. On the authors' BioMed-AQA benchmark of 327 tasks, it achieved a reported 77% success rate, with additional external BixBench evaluation. [Publisher identity](https://www.nature.com/articles/s41551-026-01634-6). Reading source: [retained PDF](../Reference-papers/s41551-026-01634-6.pdf).

**Critical assessment:** Successful biomedical workflow execution does not establish low-latency streaming control or efficient resource allocation. Reusing only successful experiences may also bias our own controller if failure evidence is discarded; that is a design risk to test, not a demonstrated defect of this paper.

**Use in EcoStream:** Use explicit execution feedback and preserve both successes and failures. Reset experience state between independent comparisons, and evaluate online adaptation separately from the frozen main study. Multiple agents are optional, not novelty by themselves.

### 15. AI data centres as grid-interactive assets

**Reference:** Philip Colangelo et al. *Nature Energy*, vol. 11, pp. 254–261, February 2026; first published online 5 December 2025. [DOI: 10.1038/s41560-025-01927-1](https://doi.org/10.1038/s41560-025-01927-1).

**Evidence inspected:** FT; retained PDF, field-trial and architecture passages, workload-flexibility table, and measurement methods. Publisher record confirms both online and issue dates.

**What they did:** The authors coordinate AI workloads through power controls, job pausing, and resource reallocation, using a profiled simulator and grid signals. A Phoenix, Arizona field trial on 256 GPUs achieved a reported 25% power reduction for three hours while meeting the designated workload SLAs. Some workload tiers explicitly permit throughput degradation; strict real-time inference is treated differently. [Publisher record](https://www.nature.com/articles/s41560-025-01927-1). Reading source: [retained PDF](../Reference-papers/s41560-025-01927-1.pdf).

**Critical assessment:** This is a physical power-orchestration demonstration, not an LLM stream-processing controller. Temporary power reduction is not automatically equivalent to total job-energy or carbon savings, and flexible AI-job SLAs differ from preserving exact streaming semantics.

**Use in EcoStream:** Separate allocated capacity, consumed CPU, power, energy, and carbon. Treat sustainability as motivation until a suitable physical measurement boundary is available. GPU-only telemetry would not measure total CPU-based Kafka/Flink energy.

## 5. Comparative synthesis

The literature separates into three connected strands: diagnostic agents gather and interpret evidence; numerical controllers optimize configurations and scheduling; stateful execution mechanisms reduce the disruption of applying those decisions. EcoStream should connect these strands around one testable question, not claim to invent each of them.

| Existing capability | Strong precedent in this review | Consequence for our novelty claim |
|---|---|---|
| LLM diagnosis followed by resource decisions | ORACL | The broad diagnosis–allocation combination is established |
| Autonomous evidence collection and a stopping action for Flink diagnosis | RCAgent | Tool use, Flink diagnosis, and stopping alone are not distinguishing |
| Selective information acquisition through configuration profiling | Demeter | Do not claim that all numerical controllers collect information indiscriminately |
| Multi-parameter and multi-pipeline tuning | Demeter; STREAMLINE | More tuning knobs or pipeline coordination alone is insufficient |
| Sample-efficient action modelling and constrained allocation | MUDAP/RASK | Lightweight numerical alternatives must be tested fairly |
| Recovery constraints and backlog-aware capacity | Phoebe; Demeter | Recovery awareness is inherited, not a standalone new contribution |
| Cost-aware migration timing and lower scaling disruption | CAOM; DRRS | A state-transition penalty or state preservation alone is insufficient |
| Dynamic partitioning/observation-update cycles | SAP-DPO | Adaptive frequency alone is not an unoccupied research area |
| Structured tool execution and experience reuse | SciToolAgent; BioMedAgent | RAG, memory, and extra agents require specific evaluation obligations |

### The defensible candidate distinction

**Proposed, not yet established as novel:** select operational diagnostic observations according to their expected reduction in intervention loss, including the cost of waiting and applying a stateful change. Stop investigating when further evidence is unlikely to justify its operational cost.

For example, more evidence about a fault may be scientifically informative but operationally worthless if every plausible explanation leads to the same feasible action. Conversely, a cheap sink or checkpoint inspection may be valuable if it prevents an expensive, ineffective scale-up. These are motivating examples to test, not observed EcoStream findings.

Value-of-information reasoning is an inherited decision-theoretic principle. This review does not establish priority for that principle or prove that no published system already implements the proposed combination. The contribution would need to be the concrete stateful-streaming formulation, a reproducible implementation, and controlled evidence of useful decisions—not the equation or agent name alone.

### What remains uncertain

1. **Overlap:** Final journal versions and unavailable methods may contain mechanisms not visible in the inspected manuscripts/abstracts, particularly for ORACL, MUDAP, STREAMLINE, and CAOM.
2. **Evidence value:** Query-outcome probabilities and action-effect models must be empirically learned/calibrated; LLM confidence or invented probabilities are insufficient.
3. **Actual cost:** Some metrics may be nearly free to obtain. Do not impose artificial collection delays merely to create a benefit for selective querying.
4. **Agent necessity:** Deterministic processing of the same metrics might match or outperform LLM interpretation. That possibility must be tested.
5. **Actionability:** Diagnosing sink throttling, skew, or a degraded worker is not successful remediation unless the shared action catalogue can address the condition. Include no-change/escalation outcomes where appropriate.

**Novelty gate status:** In progress. The literature supports a focused investigation, but this document is not a final go/no-go approval for an expensive full study.

## 6. Recommended implementation and evaluation direction

### Begin with a small decision-quality pilot

Use two workloads and two incident families with supported actions, three controllers, and three paired repetitions: **2 × 2 × 3 × 3 = 36 runs**, excluding calibration and nominal correctness checks. The three controllers should be:

1. A numerical optimizer with inexpensive telemetry.
2. A deterministic diagnostic controller with the same permitted evidence and interventions.
3. EcoStream with decision-focused evidence acquisition and LLM interpretation.

Before freezing this pilot, map each incident to an executable remedy. CPU pressure and checkpoint pressure are candidate families to characterize, not already validated choices. If retaining worker degradation, first specify a real repair/replacement action; do not secretly remove the injected fault for EcoStream alone.

The main study should additionally include a conventional diagnostic agent, the current Flink autoscaler, and ablations of acquisition criterion and transition-cost modelling. Adapted literature baselines must be named as adaptations and share the same executor, action limits, workload traces, and correctness requirements.

### Measure operational outcomes, not persuasive explanations

Primary outcome: allocated CPU core-seconds per correctly processed input event, under fixed correctness and service-quality requirements. Also record p99 query-valid latency, backlog clearance, recovery time, consumed CPU, allocated memory, ineffective actions, tool calls, API tokens/latency, and controller overhead. Count costs through episode completion and backlog clearance, or a common timeout that retains incomplete runs as failures.

Use paired independent episodes, held-out seeds/conditions, randomized execution order, and uncertainty estimates at the episode level. Events and five-second telemetry rows are not independent experimental repetitions. A favorable anecdote or diagnosis score alone does not establish a resource-efficiency contribution.

### Resource fit

The user reports an **Intel i9 system with 64 GB RAM and an RTX 4090**. It is the preferred candidate for controlled benchmark runs if sufficient access is available; the Ryzen 7 7700/approximately 16 GB PC can support development and smaller tests. Exact i9 generation/core configuration, OS, storage, and reserved runtime remain unknown. The GPU is optional for streaming execution and useful only if we choose a local LLM. Single-machine container experiments do not establish multi-host scalability.

## 7. Operational sources outside the 15-paper count

Two practical competitors must still be inspected, even though they are not counted as research papers:

- **Flink Kubernetes Operator autoscaler:** The documented controller includes backlog catch-up capacity, restart-time accounting, and scaling-effectiveness checks. Compare against relevant enabled features, not a weakened default setup. [Official documentation](https://nightlies.apache.org/flink/flink-kubernetes-operator-docs-stable/docs/managing/autoscaler/).
- **Apache Flink operations-agent demonstration:** The published example supports diagnostic tool use and operational recommendations/repair workflows. Treat it as implementation precedent, not peer-reviewed comparative evidence. [Pinned example source](https://apache.googlesource.com/flink-agents-demos/+/dd82eb7940b17227cd3fdd0e7a78aa2a384adaef/flink-operations-agent-demo/).

These sources further rule out a broad claim that agentic Flink operations or restart-aware scaling is entirely new.

## 8. Search record and outstanding checks

**Search/retrieval date:** 2026-10-13. Sources included IEEE and ACM publication records, ScienceDirect, Nature, Crossref, author manuscripts, institutional repositories, author-hosted PDFs, and project repositories. Retained PDFs were read directly where relevant; the discarded project's authored summary/memory files were not used as evidence.

Search families included:

- ORACL and joint root-cause analysis/autoscaling.
- RCAgent and tool-augmented autonomous cloud diagnosis.
- Stateful stream-processing autoscaling, migration, and recovery costs.
- Multi-configuration optimization, selective profiling, and pipeline ensembles.
- Adaptive partitioning and fluctuating stream workloads.
- Cost-aware diagnostic evidence acquisition and streaming agents.
- DOI/version searches and selected correction/retraction searches.

The query results were screened against primary records. Search coverage is not exhaustive; an absence of a matching result is not proof of novelty. Selected notice searches did not identify a relevant notice, but this is not a completed per-paper notice audit.

**Next literature actions:** Obtain the unavailable published full texts, reconcile manuscript and final versions, inspect closest baseline implementations, and complete a claim-specific reference ledger and correction/retraction checks before a submission-ready bibliography. No ordinary-preprint exception has been invoked for the 15 published records.

**Bottom line:** The study remains technically plausible and has a credible strong-journal direction. The literature demands a narrow contribution: better intervention decisions through justified evidence acquisition, with stateful transition costs and all control overhead accounted for. Q1 suitability will depend on the completed evidence and venue fit, not on the number or prestige of these references.
