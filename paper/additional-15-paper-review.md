# EcoStream-Agent: 15 additional published papers

**Added:** 2026-10-26. These are additions 16-30 to the original reading list, not manuscript citation numbers.

The integrated manuscript now covers **30 distinct published papers**. This expansion contains **14 conventional journal articles and one PVLDB journal-style proceedings article**, with no arXiv/preprint bibliography entries or newly used arXiv reading sources. Eleven additions have 2024-2026 issue years; four older journal papers supply directly relevant foundations. Two are surveys and thirteen are method-oriented studies. Published status does not certify a journal's current Q1 classification.

Each entry distinguishes inspected contributions from our proposed use. These are not reproduced findings. Abstract-only access and inaccessible final methods are qualified below. The original `title-and-15-paper-review.md` and PDF remain unchanged.

## 16. Scarf: Self-Adaptive Tuning via Multi-Objective Reinforcement Learning for Apache Flink

**Liu Liu et al. | Proceedings of the VLDB Endowment, 19(7), 1516-1529, 2026.** [Published DOI](https://doi.org/10.14778/3801059.3801066)

- **What they did / verified scope:** Combines sensitivity-based knob selection, multi-objective RL and transferable graph models for Flink tuning.
- **Relevance to EcoStream:** Strong recent tuning comparator. Match available knobs, workload access and training budget; learning resource/performance trade-offs is not EcoStream's novelty.
- **Evidence inspected:** PVLDB journal-style proceedings; publisher-deposited abstract; final PDF not retrieved. [Primary support](https://api.crossref.org/works/10.14778%2F3801059.3801066).

## 17. A Multi-Model predictive framework for adaptive resource management in stream processing systems

**Daniel Wladdimiro et al. | Future Generation Computer Systems, 182, article 108461, 2026.** [Published DOI](https://doi.org/10.1016/j.future.2026.108461)

- **What they did / verified scope:** MMP-SPS separates monitoring, predictor selection and adaptation across multiple windows, using RMSE-based or bandit-based model selection in Storm.
- **Relevance to EcoStream:** Test whether better forecasting already explains gains. Include prediction/control overhead and service degradation alongside resource savings.
- **Evidence inspected:** Publisher full-text HTML; Abstract and Sections 3.3, 5.3-5.4. [Primary support](https://www.sciencedirect.com/science/article/pii/S0167739X26000956).

## 18. A Hierarchical Near-Source Grouping Strategy for Elastic Stream Computing Systems

**Minghui Wu et al. | IEEE Transactions on Services Computing, 18(6), 3378-3391, 2025.** [Published DOI](https://doi.org/10.1109/tsc.2025.3611995)

- **What they did / verified scope:** Ns-Stream dynamically favors near-source processing through data grouping; the published implementation uses Storm.
- **Relevance to EcoStream:** Communication pressure and compute pressure can require different repairs. Do not assume this grouping mechanism is available in our Flink executor.
- **Evidence inspected:** Author-hosted published PDF; indexed abstract and Section VI, p. 3384; full download timed out. [Primary support](https://buyya.com/papers/NearSource_Stream-TSC.pdf).

## 19. Straggler mitigation via hierarchical scheduling in elastic stream computing systems

**Minghui Wu et al. | Future Generation Computer Systems, 166, article 107673, 2025.** [Published DOI](https://doi.org/10.1016/j.future.2024.107673)

- **What they did / verified scope:** Ms-Stream coordinates data grouping, task partitioning and placement to mitigate task- and node-level stragglers.
- **Relevance to EcoStream:** Incident identification is useful only when an effective shared intervention exists. This informs incident/action matching.
- **Evidence inspected:** Author-hosted published PDF; Abstract and Introduction, p. 1. [Primary support](https://clouds.cis.unimelb.edu.au/~rbuyya/papers/StragglerStreamComp-FGCS.pdf).

## 20. Federated reinforcement learning-based adaptive stream applications scheduling in edge and cloud computing

**Sabeur Lajili et al. | Future Generation Computer Systems, 177, article 108235, 2026.** [Published DOI](https://doi.org/10.1016/j.future.2025.108235)

- **What they did / verified scope:** ProOSStream combines offline optimization, federated RL for online scheduling and LSTM workload forecasting in edge-cloud settings.
- **Relevance to EcoStream:** Proactive decentralized scheduling is established. A single-host experiment cannot substantiate comparable distributed-deployment claims. A deposited coauthor-name spelling needs final-article reconciliation.
- **Evidence inspected:** Publisher full-text HTML; Abstract and Introduction. [Primary support](https://www.sciencedirect.com/science/article/pii/S0167739X25005291).

## 21. Hierarchical Auto-scaling Policies for Data Stream Processing on Heterogeneous Resources

**Gabriele Russo Russo et al. | ACM Transactions on Autonomous and Adaptive Systems, 18(4), 1-44, 2023.** [Published DOI](https://doi.org/10.1145/3597435)

- **What they did / verified scope:** Uses application- and operator-level controllers, Bayesian optimization and RL to choose replica counts and heterogeneous resource types.
- **Relevance to EcoStream:** Numerical methods already address uncertainty and interacting control levels. Retained despite its older date because it strengthens the numerical comparison.
- **Evidence inspected:** Publisher-deposited abstract and institutional record; full text restricted. [Primary support](https://art.torvergata.it/handle/2108/345524).

## 22. Adaptive Scheduling Framework of Streaming Applications based on Resource Demand Prediction with Hybrid Algorithms

**Hongjian Li et al. | Journal of Grid Computing, 22(1), article 39, 2024.** [Published DOI](https://doi.org/10.1007/s10723-024-09756-4)

- **What they did / verified scope:** CEBFD combines a cost model, SSA/XGBoost demand prediction and executor placement for heterogeneous Spark Streaming clusters.
- **Relevance to EcoStream:** Separates demand forecasting from placement decisions. Micro-batch execution differs from Flink, so this is a design precedent, not a plug-in baseline.
- **Evidence inspected:** Publisher abstract; methods/paywalled full text not inspected. [Primary support](https://link.springer.com/article/10.1007/s10723-024-09756-4).

## 23. Local recovery and partial snapshot in distributed stateful stream processing

**Takdir et al. | Knowledge and Information Systems, 67(10), 9407-9435, 2025.** [Published DOI](https://doi.org/10.1007/s10115-025-02509-z)

- **What they did / verified scope:** Implements partial snapshots and local recovery in Flink, restoring selected operators rather than necessarily the entire job.
- **Relevance to EcoStream:** The transition model must reflect the deployed recovery path. Do not impose a mandatory global restart on every stateful intervention.
- **Evidence inspected:** Publisher full text; Abstract and Section 1. [Primary support](https://link.springer.com/article/10.1007/s10115-025-02509-z).

## 24. Adaptive Fragment-Based Parallel State Recovery for Stream Processing Systems

**Hailu Xu et al. | IEEE Transactions on Parallel and Distributed Systems, 34(8), 2464-2478, 2023.** [Published DOI](https://doi.org/10.1109/tpds.2023.3251997)

- **What they did / verified scope:** A-FP4S distributes state fragments over a peer-to-peer overlay and reconstructs state in parallel, adapting to hardware heterogeneity.
- **Relevance to EcoStream:** Recovery has independent systems mechanisms. EcoStream would select supported actions, not claim this recovery machinery as its invention.
- **Evidence inspected:** Author-hosted published PDF; Abstract, p. 2464. [Primary support](https://people.ucsc.edu/~lhu82/Biobibnet/Journal/23TPDS_AFP4S.pdf).

## 25. TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent With Multi-Modality Observation Data in Cloud-Native Systems

**Xiao Zhang et al. | IEEE Transactions on Services Computing, 18(6), 4221-4233, 2025.** [Published DOI](https://doi.org/10.1109/tsc.2025.3629066)

- **What they did / verified scope:** The published title establishes tool-assisted LLM root-cause analysis with multimodal observations. Detailed mechanism and performance claims are withheld.
- **Relevance to EcoStream:** Close overlap with a generic agent-plus-telemetry proposal. Final-method access is a priority; this is not a completed full-paper review. No arXiv substitute was used.
- **Evidence inspected:** Published title/DOI metadata only; IEEE challenge blocked abstract/full text; no preprint substituted. [Primary support](https://ieeexplore.ieee.org/document/11229957/).

## 26. LLM-Enhanced Failure Localization in Microservices: Integrating Multi-Modal Data and Expert Interpretation

**Zhenyu Zhong et al. | IEEE Transactions on Services Computing, 19(3), 2275-2288, 2026.** [Published DOI](https://doi.org/10.1109/tsc.2026.3676262)

- **What they did / verified scope:** LocaleXpert converts heterogeneous telemetry to text and coordinates specialist agents for failure localization and interpretation.
- **Relevance to EcoStream:** Multimodal inputs and specialist agents alone are insufficient novelty. Final-version reconciliation is pending; the manuscript's first-author spelling is inconsistent, so the bibliography follows the deposited journal identity.
- **Evidence inspected:** Author-hosted manuscript; Abstract and Introduction; final-version reconciliation pending. [Primary support](https://nkcs.iops.ai/wp-content/uploads/2026/03/LocaleXpert.pdf).

## 27. Leveraging multi-agent framework for root cause analysis

**Feng Fu et al. | Complex & Intelligent Systems, 12(1), article 4, 2026.** [Published DOI](https://doi.org/10.1007/s40747-025-02096-0)

- **What they did / verified scope:** MA-RCA assigns specialist diagnostic roles and combines retrieval grounding with runtime hypothesis testing.
- **Relevance to EcoStream:** Evidence grounding and validation are established. EcoStream must show when further investigation changes an intervention enough to justify waiting.
- **Evidence inspected:** Publisher full text; Abstract and Introduction. [Primary support](https://link.springer.com/article/10.1007/s40747-025-02096-0).

## 28. CausalRCA: Causal inference based precise fine-grained root cause localization for microservice applications

**Ruyue Xin et al. | Journal of Systems and Software, 203, article 111724, 2023.** [Published DOI](https://doi.org/10.1016/j.jss.2023.111724)

- **What they did / verified scope:** Learns a weighted causal graph from metrics and ranks fine-grained candidate root causes.
- **Relevance to EcoStream:** A non-LLM diagnosis alternative. Observational causal ranking does not itself prove repair success or remove causal-model assumptions.
- **Evidence inspected:** Institutional final published PDF; article Abstract, PDF p. 2. [Primary support](https://pure.uva.nl/ws/files/166189852/CausalRCA.pdf).

## 29. A survey on the evolution of stream processing systems

**Marios Fragkoulis et al. | The VLDB Journal, 33(2), 507-541, 2024.** [Published DOI](https://doi.org/10.1007/s00778-023-00819-8)

- **What they did / verified scope:** Surveys stream-processing evolution across ordering, state, fault tolerance, load management, elasticity and reconfiguration.
- **Relevance to EcoStream:** Defines systems and semantic constraints. It is a survey, not an implementation baseline. Online publication was 2023; the publisher's issue citation is 2024.
- **Evidence inspected:** Publisher full text; Abstract and Introduction; 2024 issue / 2023 online. [Primary support](https://link.springer.com/article/10.1007/s00778-023-00819-8).

## 30. Runtime Adaptation of Data Stream Processing Systems: The State of the Art

**Valeria Cardellini et al. | ACM Computing Surveys, 54(11s), 1-36, 2022.** [Published DOI](https://doi.org/10.1145/3514496)

- **What they did / verified scope:** Provides a taxonomy of runtime stream-processing adaptation strategies and identifies open challenges.
- **Relevance to EcoStream:** Foundational comparison framework, not a recent experimental controller. Full-text inspection and article-number refinement remain pending.
- **Evidence inspected:** Publisher-deposited abstract and institutional bibliography; full text not inspected. [Primary support](https://api.crossref.org/works/10.1145%2F3514496).

## Implications for our study

1. Keep the proposed contribution narrow: decision-focused acquisition of operational observations, accounting for collection cost, investigation delay and stateful intervention consequences.
2. Strengthen numerical controls with recent tuning/prediction work and deterministic processing of the same evidence. An adapted baseline must not be labelled an exact reproduction.
3. Match incidents to implemented shared actions. Do not assume grouping changes, local recovery or successful skew repair are available.
4. Evaluate action selection and actual recovery, not only diagnosis accuracy or explanation quality. Resource allocation, service violations, evidence cost and backlog clearance remain intended endpoints.
5. Keep the novelty gate open. Final versions, notice checks, code inspection and the decision-quality pilot remain pending. No experiment or Q1 acceptance is established by this review.

The manuscript contains the thematic integration and two comparison tables. The ledger and dated metadata snapshot in `research/literature/` preserve DOI identities and access limitations. MA-RCA uses the publisher's 2026 issue year despite online publication in 2025; other DOI-year/issue-year differences are retained explicitly.

