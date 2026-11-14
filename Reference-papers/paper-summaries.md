# Summaries of the four reference papers

Prepared 6 October 2026 from the four local PDFs in this folder. The summaries use the main articles, methods, and relevant embedded extended-data material. Selected results figures and tables were also inspected visually. External supplementary files and linked software repositories were not downloaded or independently tested. Reported results belong to the authors; critical assessments below are interpretations of the evidence in the PDFs.

Page references are PDF page numbers, starting at 1. This avoids ambiguity where printed journal pagination differs from the PDF.

## 1. Multi-modal learning with incomplete data

**Authors:** Alberto López, John Zobolas, Tanguy Dumontier and Tero Aittokallio.  
**Venue:** Nature Communications, 17, article 10356 (2026).  
**DOI:** https://doi.org/10.1038/s41467-026-77212-w  
**Source:** [s41467-026-77212-w.pdf](D:/1.msc/Big-Data/Reference-papers/s41467-026-77212-w.pdf)

### Purpose and research gap

Multimodal learning combines different kinds of information about the same samples, such as gene expression, protein measurements, images and text. In practice, a sample may lack an entire modality, or individual values within a modality. Many algorithms assume complete inputs, while published methods for incomplete data are scattered across incompatible codebases and programming languages.

Common workarounds are to discard incomplete samples, use only one modality, or fill missing values with simple estimates. These approaches can lose samples, discard complementary information, or introduce noise. The paper addresses the lack of a reusable, standardized software framework for these problems.

### Proposed approach

The authors introduce **iMML**, an open-source Python package bringing together more than 25 methods. Its modules support classification, clustering, retrieval, imputation, feature extraction and selection, missing-data simulation, exploratory analysis, information statistics, and visualization. It uses interfaces compatible with common Python tools, including NumPy, pandas, scikit-learn, PyTorch and Lightning AI.

The package includes established algorithms rather than proposing one universal new learning algorithm. Examples include RAGPT, M3Care and MUSE for classification; multiple incomplete multi-view clustering methods; and MOFA, DFMF and joint non-negative matrix factorization for decomposition or imputation. Many MATLAB/R implementations were translated into Python, with optional wrappers retaining access to the originals.

For evaluation, iMML can deliberately remove modalities from complete data. The supported patterns are missing completely at random, missing not at random, partial missingness with some always-observed modalities, and mutually exclusive missingness where incomplete samples retain only one modality.

### Evaluation and main findings

- **Implementation comparison:** Translated algorithms were compared with their original versions on five datasets, with 50 repetitions. The authors report almost identical clustering results and no detected statistical differences. Table 2 shows substantial average speed gains for several methods, including 9.33-fold for LFIMVC and 8.45-fold for EEIMVC. Gains were not universal: DAIMC's average speed-up factor was 0.97.
- **TCGA pancreatic cancer exploration:** Requiring copy-number alterations and gene expression retained 177 patients, whereas requiring all four omics layers retained only 100. Exploratory information decomposition suggested that gene expression and proteomics provide useful complementary information for an 18-month survival label.
- **Vision-language classification and retrieval:** RAGPT outperformed M3Care in the tested incomplete Food101 settings. Importantly, this experiment used a binary subset of 1,424 samples, not all 101 classes. It used stratified five-fold cross-validation under four missingness patterns and incompleteness rates up to 80%.
- **Text clustering:** On 116 BBCSport articles, incomplete-data methods outperformed their corresponding mean-imputation baselines. IMSR generally performed best, while PIMVC was competitive at high incompleteness. Performance still declined as more samples became incomplete.
- **Imputation:** On the 2,310-instance Statlog image-segmentation dataset, MOFA and DFMF improved downstream classification relative to mean imputation. The authors report a 4-7% average accuracy improvement for MOFA at missing rates of 30-70%.
- **Dimensionality reduction:** On Nutrimouse data from 40 mice, extracted features were more robust than selected features at high missingness. The figure does not show dimensionality reduction beating the all-features baseline; its benefit includes compactness and interpretability.

### Contribution and limitations

The main contribution is reusable infrastructure: common inputs, consistent interfaces, reproducibility controls, and tools for studying missingness across modalities. It makes existing research methods easier to compare and use.

The authors explicitly leave a large, systematic benchmark across domains, missingness mechanisms and computational settings for future work. The small illustrative datasets and simplified Food101 task therefore do not establish universal superiority. Much of the evaluation uses simulated missingness, which may only partially capture real collection processes. The pancreatic-cancer information analysis uses mean imputation, a binarized survival outcome, and excludes some censored patients; it is exploratory rather than a validated clinical survival model. iMML also does not make arbitrary external algorithms missing-data-compatible automatically.

**Takeaway:** This is primarily a software and reproducibility contribution for learning from incomplete multimodal datasets. Its usefulness is broader than any one case study, but its examples are not an exhaustive benchmark of which method works best.

**Evidence locations:** scope and architecture, pp. 2-4; use cases and Table 2, pp. 5-6; discussion and modules, pp. 7-8; evaluation details and availability, pp. 8-9.

## 2. Empowering AI data scientists using a multi-agent LLM framework with self-evolving capabilities for autonomous, tool-aware biomedical data analyses

**Authors:** Dechao Bu, Jingbo Sun, Kun Li and colleagues.  
**Venue:** Nature Biomedical Engineering (2026). The supplied PDF records acceptance on 13 February 2026 but contains a placeholder for the online publication date.  
**DOI:** https://doi.org/10.1038/s41551-026-01634-6  
**Source:** [s41551-026-01634-6.pdf](D:/1.msc/Big-Data/Reference-papers/s41551-026-01634-6.pdf)

### Purpose and research gap

Biomedical analysis often requires chaining specialized programs through several stages: preprocessing, alignment, quantification, statistical analysis, modelling and visualization. General LLMs may write code, but often struggle with tool dependencies, workflow planning and correcting execution errors. Existing agents also tend to focus on narrow tasks and reuse previous analytical experience inefficiently.

The paper proposes **BioMedAgent**, a virtual data scientist that translates a natural-language task and supplied data into an executable biomedical analysis workflow.

### Proposed approach

The framework separates planning, coding and execution across specialist agents, including requirement analysis, tool management, planning, programming and execution. Its three central mechanisms are:

1. **Tool-aware execution:** A Tool Manager interprets documentation and retrieves suitable domain tools. The system combines 67 integrated bioinformatics tools with custom generated code. Docker containers isolate tool dependencies, and a central Python API coordinates execution.
2. **Interactive exploration:** Agents exchange execution feedback, revise plans and repair code when tests fail. Exploration is bounded to three interaction rounds in the planning and coding phases.
3. **Memory retrieval:** Successful tool choices, generalized workflows and code are stored and retrieved by semantic similarity. Continuous memory accumulation retains successful records; iterative memory forgetting retains simpler alternatives for similar problems to reduce memory growth.

Here, self-evolution refers to improving the system's stored experience and its reuse, rather than demonstrated retraining of the underlying LLM's weights.

### Evaluation and main findings

The authors introduce **BioMed-AQA**, containing 327 tasks across omics, precision-medicine support, machine learning, statistics and visualization. It covers 17 analysis types. Of its source datasets, 37.3% are simulated, 15.9% come from tutorials and 46.8% derive from published research. A 172-question multiple-choice subset complements the open tasks.

Success requires satisfying every annotated task milestone. Partial credit contributes to the separate Win score but does not count as full task success. Manual evaluation is primary; the autoscoring agent agreed with manual judgments in 92.3% of evaluations.

- **Ablation results:** Full-task success rose from 28% without interactive exploration to 52% with it, and then to 77% after three memory-learning rounds with GPT-4o-mini.
- **Task differences:** At the reported final configuration, success was 94% for omics, 78% for precision-medicine support, 90% for machine learning, 59% for statistics and 65% for visualization. Statistics remained a weaker area.
- **Comparison:** The paper reports 39% success for GPT Assistants, 33% for its Function Calling configuration with exploration, and 46% for ChatGPT-4o. Tool access and execution environments vary among these comparisons, so the results evaluate configurations as well as agent design.
- **Held-out questions:** Learning on 70% of BioMed-AQA yielded 69% success on unseen questions versus 76% on seen questions. This strengthens the case for transfer beyond direct recall, while also qualifying the headline 77% figure.
- **External evaluation:** On 296 BixBench questions, with GPT-4.1 and no integrated domain tools, success was 49% for open questions, 49% for multiple-choice questions allowing refusal, and 63% without refusal. Corresponding benchmark baselines were 37%, 42% and 55%.
- **Application studies:** The system integrated bulk and single-cell RNA-seq for lung-cancer analysis; reproduced a published cancer-associated thrombosis modelling workflow, with c-indices of 0.73 and 0.74 for liquid-biopsy models versus 0.61 for the Khorana-score model; and combined image resolution enhancement with pathology segmentation, reporting a small overall Dice gain of 0.86%.

### Contribution and limitations

The contribution combines broad biomedical tool orchestration, execution-driven repair, reusable experience and a released benchmark. It shows how natural-language requests can drive real computation across heterogeneous tools.

The 77% figure follows iterative learning on the authors' benchmark and should not be interpreted as first-attempt accuracy on arbitrary new tasks. External open-question performance was 49%. Some benchmark data are synthetic or tutorial-based, and milestone correctness does not by itself establish that every scientific choice is optimal. The authors acknowledge hallucinated intermediate results or conclusions, dependence on tool reliability, and scaling bottlenecks. Memory comparisons span only a limited number of rounds; failures are not yet used as systematically as successes. The application studies demonstrate analytical execution and reproduction, not prospective clinical effectiveness.

**Takeaway:** BioMedAgent shows that specialized tools, collaborative error correction and retrieved experience can improve biomedical analysis automation. Its reliability still depends on task type, prior experience, tool configuration and verification of generated results.

**Evidence locations:** architecture and benchmark, pp. 2-4; comparison table, p. 5; ablations, memory and external evaluation, pp. 6-9; applications and limitations, pp. 9-11; methods and availability, pp. 12-14.

## 3. AI data centres as grid-interactive assets

**Authors:** Philip Colangelo, Ayse K. Coskun and colleagues.  
**Venue:** Nature Energy, 11, 254-261 (February 2026); published online 5 December 2025.  
**DOI:** https://doi.org/10.1038/s41560-025-01927-1  
**Source:** [s41560-025-01927-1.pdf](D:/1.msc/Big-Data/Reference-papers/s41560-025-01927-1.pdf)

### Purpose and research gap

Large AI clusters place substantial loads on electricity grids. During peak demand, fixed data-centre loads can increase infrastructure requirements and delay new connections. Earlier demand-response research often emphasized CPU workloads, simulations or broadly flexible jobs, leaving limited field evidence for GPU-based AI workloads with explicit performance commitments.

The paper asks whether an AI cluster can reduce its power demand when the grid needs relief while respecting individual workload service constraints.

### Proposed approach

The authors develop a software orchestration platform that combines grid signals, workload telemetry and job performance requirements. A simulator predicts each job's relationship between power and throughput using measured workload profiles. The controller chooses a combination of GPU power caps, job pausing, and changing GPU allocations.

Workloads are assigned four flexibility tiers: Flex 0 permits no performance loss; Flex 1, Flex 2 and Flex 3 permit up to 10%, 25% and 50% average throughput reduction, respectively, over the relevant time window. Thus, preserving a service agreement does not require keeping every job at its original speed. Strict real-time workloads are protected, while willing participants absorb slowdowns.

Two policy families are studied. Greedy policies prioritize the most flexible jobs to affect fewer jobs; fair policies distribute slowdown according to the allowed flexibility. Checkpointing preserves training progress when jobs pause or resize.

### Evaluation and main findings

The field trial used an Oracle cloud facility in Phoenix, Arizona, with **256 NVIDIA A100 GPUs**. Four workload ensembles mixed training, fine-tuning, latency-sensitive inference and latency-tolerant inference. Experiments included MPT and LLaMA workloads, MosaicML orchestration, telemetry and grid-demand forecasts.

- **Utility peak events:** On 1 and 3 May 2025, the cluster reduced power by 25% relative to its baseline for three hours. It ramped down and up over 15-minute windows, avoided a substantial immediate rebound, and met workload performance constraints.
- **Emergency re-enactment:** A historical California emergency profile was replayed, requiring a 15% reduction followed by a deeper target of 25% reduction. This was a controlled re-enactment using measured cluster response, not participation in the original 2020 emergency.
- **Broader trials:** Across 33 experiments involving 212 individual jobs, the authors report meeting both power targets and workload constraints with zero service-agreement violations.
- **Prediction accuracy:** Simulator power predictions had a root mean square error of 4.52% relative to average experimental power.
- **Policy trade-offs:** Fair power capping achieved the best average throughput; fair power capping plus pausing balanced throughput and the number of affected jobs. Greedy pausing affected the fewest jobs.

The primary achievement is controllable peak power, measured in kilowatts. A 25% event-time power reduction is not a 25% reduction in the energy needed to complete the workloads. In one SRP example, the authors estimated a 5% energy reduction using job progress and measured power as proxies for the continued schedule.

### Contribution and limitations

The strongest contribution is field evidence that existing AI workloads and GPU controls can provide useful demand response without added batteries, on-site generation or hardware retrofits. It joins computer scheduling with electricity-system requirements.

The trial concerns one GPU cluster, not whole-facility demand including cooling and all support systems. Flexible workload proportions and user willingness to accept slowdown are crucial. Power-performance profiles were measured in advance, which may be difficult for unknown workloads. The paper does not demonstrate long-term, multi-site operation or broad economic outcomes. Faster connections, lower tariffs and large additional grid capacity are implications or findings cited from other work, not outcomes measured in this trial. Financial interests and technology-related pending patents are disclosed by participating companies.

**Takeaway:** AI clusters can help manage grid peaks through workload scheduling and GPU controls, provided sufficient jobs accept bounded slowdown. This is evidence for operational flexibility, with energy savings and large-scale grid benefits requiring separate assessment.

**Evidence locations:** architecture and workload tiers, p. 2; field events and accuracy, pp. 3-5; limitations and algorithms, p. 6; measurement, energy distinction and reproducibility material, p. 7; competing interests, p. 8.

## 4. A multi-agent system for automating scientific discovery

**Authors:** Ali E. Ghareeb, Benjamin Chang and colleagues.  
**Venue:** Nature, 655, 497-504 (9 July 2026); published online 19 May 2026.  
**DOI:** https://doi.org/10.1038/s41586-026-10652-y  
**Source:** [s41586-026-10652-y.pdf](D:/1.msc/Big-Data/Reference-papers/s41586-026-10652-y.pdf)

### Purpose and research gap

Scientific discovery requires linking literature, hypotheses, experiments, analysis and revised hypotheses. Many AI systems support only one part of this cycle. This paper introduces **Robin**, which connects literature-based hypothesis generation with analysis of new laboratory results and uses those results to guide the next round of proposals.

Its demonstration targets dry age-related macular degeneration, using increased retinal pigment epithelium (RPE) phagocytosis as an experimentally testable strategy. Phagocytosis is the uptake and clearance of material by cells; here it is relevant to the RPE's handling of photoreceptor outer segments.

### Proposed approach and human role

Robin coordinates **Crow** for concise literature reviews, **Falcon** for deeper candidate evaluations, and **Finch** for executing data analysis in Jupyter notebooks. Crow and Falcon are based on PaperQA2. Robin's synthesis and hypothesis generation use o4-mini, while Claude 3.7 Sonnet judges candidate pairs. Pairwise judgments feed a Bradley-Terry-Luce ranking model.

Starting from the disease name, Robin proposes mechanisms and assay outlines, ranks them, generates candidate compounds, and evaluates their rationales. Scientists review the shortlist, translate outlines into precise protocols and perform the experiments. Raw flow-cytometry files or processed gene-count data return to Robin. Eight independent Finch analysis trajectories are synthesized into a consensus, which informs follow-up experiments or revised candidates.

This is a semi-autonomous laboratory feedback loop. Humans conducted experiments, supplied expert analysis prompts, made practical assay substitutions and performed RNA-seq read processing. Some figure formatting was also adjusted by humans for publication.

### Evaluation and main findings

- **Initial discovery cycle:** Robin reviewed literature to select an RPE phagocytosis assay and propose 30 initial compounds. The first screen identified the previously studied ROCK inhibitor Y-27632 as a useful lead.
- **Mechanistic follow-up:** Robin proposed RNA-seq, and Finch's analysis identified about threefold upregulation of ABCA1 after Y-27632 treatment. ABCA1 encodes a lipid-efflux transporter. Follow-up experiments also found ABCA1 upregulation with ripasudil in primary RPE-derived cells. This supports a mechanistic hypothesis but does not establish causal mediation.
- **Revised candidates:** Ripasudil increased phagocytosis 1.89-fold relative to control in Finch's ARPE-19 analysis; human analysis estimated 1.75-fold. It was more potent than Y-27632 in the reported dose-response experiments. KL001 was also a hit in primary human RPE-derived cells.
- **Validation scope:** Primary-cell validation used cells from one donor over 60 years old with no known ocular conditions. The ARPE-19 screen used three wells and the primary-cell screen used four technical replicate wells. These are not patient sample sizes or independent donor replication.
- **Architecture checks:** Replacing literature-search agents with a general LLM increased reference hallucination and reduced proposal quality. On the guided discovery tasks, Finch achieved 86% RNA-seq rubric adherence and 100% flow-cytometry rubric adherence over three runs.
- **Broader analysis benchmark:** On 170 selected BixBench questions, Finch achieved 22.8% overall accuracy, comprising 15.3% on bioinformatics and 47.9% on statistics. Strong performance in the guided case study therefore did not generalize to consistently reliable analysis of diverse difficult tasks.
- **Alternative proposal system:** In the reported single-assay comparison, 17 unique candidates suggested by OpenAI Deep Research produced no hits. This narrow comparison does not establish superiority across diseases or research tasks.

### Contribution and limitations

Robin's contribution is the connection between literature-grounded proposals, experimentally generated evidence and revised hypotheses, supported by real in-vitro testing. BioMedAgent primarily executes supplied analytical objectives; Robin extends upstream to choosing scientific hypotheses and uses new experiments to update them.

The study does not demonstrate a treatment for patients, an animal-model benefit, or prevention of vision loss. Increased phagocytosis is a laboratory endpoint, and the single-donor validation limits biological generalization. Expert prompts, human execution and preprocessing remain important. ABCA1 expression changes do not prove that ABCA1 causes the phagocytosis effect.

The reported approximately 200-fold reduction in cognitive labour relies on estimated human times from surveys, not a controlled comparison with scientists performing the same complete project. The estimated US$10.76 per configured run covers the stated Crow/Falcon calls and excludes Finch from the calculation; it is not a total experimental-discovery budget. Moreover, the main text reports a 1.6% no-harness baseline for the broader Finch benchmark, while the Extended Data Fig. 5 legend labels it 1.0%. Finch's own 22.8% figure is consistent, but the baseline discrepancy merits care when quoting that comparison. The base-model control also lacked Finch's data access and execution tools, so it does not isolate orchestration alone.

**Takeaway:** Robin provides a compelling proof of concept for AI-guided scientific discovery through iterative laboratory feedback. Its drug candidates and mechanisms remain research hypotheses requiring broader biological and clinical validation.

**Evidence locations:** architecture and workflow, pp. 2-3; initial experiments and transcriptomics, pp. 4-5; compound validation, Fig. 4, p. 6; system evaluation and clinical boundaries, pp. 7-8; implementation and benchmarking, pp. 10-11; human preprocessing and replication, pp. 11-12; availability, p. 13; extended benchmark figure, p. 18.

## Comparison across the papers

| Paper / system | Main problem | Primary contribution | Evidence type | Main boundary |
|---|---|---|---|---|
| iMML | Missing variables or entire modalities | Unified Python toolkit for incomplete multimodal learning | Software comparisons and six illustrative use cases | No exhaustive cross-domain benchmark or universal winning algorithm |
| BioMedAgent | Complex biomedical analysis workflows | Tool-aware agents, repair and reusable workflow memories | A 327-task benchmark, held-out questions, external benchmark and application studies | Performance depends on experience, tools and task; hallucinations remain |
| Grid-interactive AI data centres | AI power demand during grid peaks | Software orchestration under workload performance constraints | Physical trial on a 256-GPU cluster | Cluster-scale peak-power evidence; broad energy and economic benefits remain separate |
| Robin | Linking hypotheses to experiments and new hypotheses | Literature and analysis agents in an iterative lab feedback loop | In-vitro compound screens, transcriptomics, ablations and analysis benchmarks | Human laboratory work, single-donor validation and no demonstrated clinical benefit |

The papers address four different parts of a data-intensive research ecosystem: usable incomplete data, execution of analyses, control of computational resources, and generation of new scientific hypotheses. Their numerical results use different denominators, endpoints and evaluation conditions. In particular, BioMedAgent's 49% external open-question result and Finch's 22.8% result should not be treated as a direct head-to-head comparison: the evaluated question sets, models, prompting, tools and protocols differ.
