# HIVsim: A New Generation of Interoperable, AI-Native, and Explainable HIV Modeling

**Project and scientific paper vision — Draft v0.1**

*October 2026 | Working concept document for collaborative refinement*

## 1. Executive vision

Mathematical models have become indispensable tools for understanding HIV epidemics, evaluating prevention and treatment strategies, and informing public health policy. Yet despite decades of scientific progress, the HIV modeling ecosystem remains fragmented. Models are commonly developed within distinct computational frameworks, encode different assumptions about transmission and disease progression, require substantial specialist expertise to operate, and are difficult to combine or compare systematically.

These limitations constrain not only the efficiency of HIV modeling, but also its scientific transparency and policy utility.

**We envision HIVsim as the foundation of a new generation of HIV modeling: modular by design, AI-native in operation, and capable of representing and comparing multiple existing modeling approaches within a common computational language.**

Built on Starsim and its emerging epidemiological *lingua franca*, HIVsim aims to transform HIV modeling along three complementary dimensions.

First, it allows HIV to be modeled not as an isolated epidemic, but as one component of a broader, interacting system of infectious diseases, health conditions, transmission networks, and interventions. HIV models can be composed with models of tuberculosis, syphilis, and other conditions without the need to build an entirely new integrated simulation.

Second, HIVsim is conceived as an AI-native modeling environment. A suite of AI agents, skills, plugins, and validated computational tools enables scientists and decision-makers to formulate questions in natural language, translate them into rigorous modeling workflows, execute analyses, and interpret results. Rather than replacing scientific expertise, the system aims to make that expertise more accessible, reproducible, and scalable.

Third, and perhaps most ambitiously, HIVsim provides a potential foundation for a shared computational ecosystem in which existing HIV models can be reconstructed and compared using a common modeling language. This would enable not just the aggregation of projections from multiple models, but systematic investigation of *why those models disagree*: which assumptions, mechanisms, parameterizations, calibration choices, or structural features drive differences in their predictions.

Together, these capabilities suggest a new paradigm for disease modeling: **from standalone models to interoperable scientific infrastructure; from manual analyses to AI-assisted evidence generation; and from opaque disagreement to explainable model diversity.**

HIVsim is both a model and an invitation to reimagine the HIV modeling ecosystem.

## 2. The problem: Powerful models, fragmented science

HIV modeling has a rich methodological history, encompassing deterministic compartmental models, stochastic models, individual-based simulations, and hybrid approaches. These models have played critical roles in projecting epidemic trajectories, estimating intervention impact, and supporting national and global HIV strategies.

Yet the sophistication of individual models has not translated into an equally sophisticated ecosystem for interoperability, reuse, and comparison.

### 2.1 Models are difficult to combine

HIV frequently interacts with other diseases and health conditions. Tuberculosis remains a major cause of morbidity and mortality among people living with HIV, while sexually transmitted infections such as syphilis can interact with HIV transmission dynamics and affect the impact of prevention strategies.

Traditionally, representing these interactions requires bespoke model development, often involving substantial modification to existing codebases. Modules developed independently by different research groups cannot readily be combined, and integrations are frequently difficult to maintain or generalize.

Consequently, modeling research often treats conditions separately even when their biological, behavioral, and programmatic interactions are central to the policy question.

### 2.2 Models remain difficult to operate and translate into decisions

Conducting a high-quality modeling analysis requires expertise in model structure, parameterization, calibration, scenario development, uncertainty analysis, and epidemiological interpretation.

These requirements are appropriate for scientific rigor, but the tools supporting them have generally been designed for specialist users.

Answering a new policy question can involve extensive manual work: interpreting evidence, modifying simulation code, assembling data, calibrating parameters, executing scenarios, producing outputs, and translating findings into policy-relevant insights.

This creates a bottleneck between the emergence of new evidence or policy questions and the generation of actionable model-based guidance.

Recent advances in AI and agent-based scientific computing offer an opportunity to reduce this burden without compromising methodological standards.

### 2.3 Models disagree, but we often cannot explain why

Different HIV models can generate substantially different predictions even when calibrated to similar epidemiological data.

For example, a 2025 comparison of six independently calibrated HIV transmission models—Optima HIV, EMOD, Goals, Thembisa, PopART-IBM, and HIV Synthesis—found considerable variation in estimated HIV transmission patterns across three African countries.

In Malawi, the estimated proportion of new HIV transmissions attributable to undiagnosed people living with HIV in 2024 ranged from **33.3% to 75.3%**.

Such differences matter. Depending on which model is used, policymakers could reach different conclusions about the relative importance of HIV testing, treatment initiation, retention, and re-engagement interventions.

Model comparison exercises help reveal these uncertainties. However, differences in model structure, programming environments, state representations, calibration strategies, and underlying assumptions make it extremely challenging to establish precisely why predictions diverge.

A common modeling language could fundamentally change this.

Instead of simply asking, *What do different models predict?*, we could ask:

**What exactly makes these models produce different answers, and what additional evidence would resolve those differences?**

This is not only a computational challenge. It is an important opportunity for scientific discovery.

## 3. The solution: Three advances in HIV modeling

### Advance 1. Composable epidemiology: From HIV-only models to interacting disease systems

HIVsim is built on Starsim, a modular epidemiological simulation framework designed to represent diseases, populations, networks, interventions, and other health processes through interoperable components.

This architecture creates a fundamentally different development model from traditional disease-specific simulation software.

Rather than building every new co-infection or multimorbidity model from scratch, researchers can compose existing models and specify the interactions between them.

For example:

- **HIV + tuberculosis:** Explore how HIV-associated immunosuppression, ART expansion, TB treatment, and preventive therapy interact to shape disease burden.
- **HIV + syphilis:** Investigate co-transmission, shared sexual networks, interactions in susceptibility, and integrated testing and treatment strategies.
- **HIV + other health conditions:** Extend the framework to additional infections, reproductive health processes, and noncommunicable conditions as appropriate modules become available.

The essential innovation is that models share foundational representations of simulated people, time, demographic processes, interventions, and other modeling constructs.

Disease-specific mechanisms can remain modular, while explicit connectors represent biological or behavioral interactions between diseases.

This architecture aims to enable reusable model components, reduce duplicated development effort, and make increasingly complex multi-disease questions tractable.

**Core scientific proposition:** Composability can make it substantially easier to develop, validate, and maintain integrated HIV models while preserving disease-specific mechanistic detail.

**Proposed proof of concept:** Demonstrate the construction of an HIV-only simulation and at least two integrated simulations—HIV–TB and HIV–syphilis—using shared HIVsim components. Quantify code reuse, integration effort, computational performance, and the epidemiological implications of explicitly representing disease interactions.

Crucially, composability does not imply that combining modules automatically yields a scientifically valid joint model. Interactions, shared population assumptions, calibration, and consistency of interventions must be explicitly specified and tested.

### Advance 2. AI-native epidemiology: From expert-operated models to scientific agents

The second advance is to make HIVsim an AI-native scientific system rather than simply a model with an AI chatbot attached.

An AI-enabled HIVsim environment would expose its modeling capabilities through a collection of structured tools, domain-specific skills, agents, and interfaces, including standardized protocols such as the Model Context Protocol (MCP).

These tools would allow AI agents to interact directly with a well-defined computational environment instead of independently generating and executing arbitrary simulation code.

A researcher might ask:

*"What would be the impact on HIV incidence in Malawi of improving ART retention relative to expanding testing coverage over the next ten years?"*

An AI-enabled workflow could:

1. Interpret the epidemiological question and identify its required population, outcomes, scenarios, and time horizon.
2. Identify an appropriate model configuration, input data, and evidence sources.
3. Construct proposed intervention scenarios and parameter assumptions.
4. Check whether the requested analysis is scientifically and technically valid.
5. Calibrate or load a previously validated model configuration.
6. Execute simulations and uncertainty analyses using deterministic, versioned computational tools.
7. Generate reproducible outputs, including figures, tables, code, and methodological documentation.
8. Explain findings, assumptions, uncertainty, and limitations in language appropriate to the intended audience.

The distinctive ambition is that **scientific rigor becomes a first-class property of the AI workflow**, rather than relying entirely on the knowledge and diligence of an individual user.

Potential scientific safeguards include:

- Explicit assumptions and provenance for input parameters.
- Requirements for calibration and model validation.
- Automated checks of units, parameter ranges, logical consistency, and output plausibility.
- Standardized sensitivity and uncertainty analyses.
- Reproducible execution with versioned configurations and random seeds.
- Traceable records of agent decisions, tool calls, and model modifications.
- Human review and approval for consequential scientific assumptions or policy-facing conclusions.

Such safeguards should be enforced programmatically wherever possible, with AI agents operating inside these constraints.

The relevant conceptual precedent is *Paper2Agent* (Miao et al., Nature, 2026), which demonstrates how scientific publications and associated computational methods can be exposed as interactive AI agents through MCP-based workflows.

HIVsim extends this vision from interactive access to individual research artifacts toward **a persistent, extensible environment for epidemiological inference and decision support**.

**Core scientific proposition:** AI-native workflows can substantially reduce the effort required to move from epidemiological questions to reproducible analyses, while preserving or improving scientific quality.

**Proposed proof of concept:** Evaluate the AI-enabled system on a predefined benchmark of HIV modeling tasks, comparing AI-assisted and conventional workflows on completion time, reproducibility, correctness, calibration quality, methodological compliance, and expert review requirements.

The aim is not fully autonomous policy advice. It is to automate routine and technically intensive components of scientific workflows while maintaining transparent human oversight.

### Advance 3. Explainable model ensembles: From competing black boxes to a shared modeling language

The third advance is arguably the most transformative.

HIVsim would function not only as one HIV model, but also as a foundation for reconstructing and interrogating other HIV models within a common computational representation.

Starsim's emerging epidemiological *lingua franca* aims to provide a standardized language for expressing models across different paradigms, including deterministic compartmental, stochastic, metapopulation, and agent-based approaches.

Within this environment, models with different structures and assumptions could be represented using shared primitives while preserving their distinctive scientific mechanisms.

This would enable a new class of scientific analysis.

**Reconstruction.** Existing models could be translated into the common modeling language, preserving their governing equations, state transitions, stochastic processes, and structural assumptions to the extent supported by the representation.

**Verification.** Reconstructed models could be tested against their original implementations using common inputs, reference outputs, and numerical or statistical equivalence criteria.

**Comparison.** Once represented in a common environment, models could be inspected using standardized tools to identify differences in their structures, parameters, assumptions, and calibration procedures.

**Controlled experimentation.** Individual assumptions or modules could be exchanged or harmonized across models, allowing researchers to investigate which differences drive variation in predictions.

**Ensemble analysis.** Multiple model formulations could be run on common scenarios to characterize structural uncertainty and produce more informative assessments of the robustness of policy conclusions.

The objective is not to eliminate legitimate diversity in epidemiological modeling.

Different model structures often embody meaningful scientific perspectives, alternative representations of incomplete evidence, or distinct assumptions about epidemic dynamics.

Instead, the aim is to make those differences explicit, interrogable, and scientifically useful.

#### A motivating example: Why do HIV models disagree about the source of transmission?

Consider the findings of the 2025 multi-model comparison in Malawi.

Six independently calibrated models generated estimates spanning 33.3% to 75.3% for the proportion of new transmissions attributable to undiagnosed people living with HIV in 2024.

Today, explaining this variation comprehensively could require detailed comparison of independent codebases, documentation, calibration procedures, epidemiological assumptions, and model outputs.

In the envisioned HIVsim ecosystem, researchers could ask:

*"Why do these models disagree so substantially about the contribution of undiagnosed people to HIV transmission?"*

A model-comparison agent, operating on verified reconstructions, could systematically investigate differences in:

- Sexual partnership networks and mixing patterns.
- Heterogeneity in HIV transmission risk.
- HIV testing and diagnosis processes.
- ART initiation, interruption, and re-engagement.
- Viral suppression and infectiousness assumptions.
- Disease progression and survival.
- Historical epidemic trajectories and initialization.
- Calibration targets, priors, data, and uncertainty.
- Definitions and measurement of the reported outcome.

It could then support controlled experiments to determine which combinations of differences explain the divergence.

For example, models could be compared under harmonized testing assumptions, shared calibration targets, or common partnership-network assumptions, where scientifically appropriate.

This might reveal that a substantial fraction of the observed disagreement is attributable to one or two identifiable mechanisms—or, equally importantly, that model differences interact in ways that make the discrepancy irreducible to a single assumption.

The result would be a new kind of model comparison: not simply a distribution of predictions, but **an evidence-based explanation of the sources of disagreement and their implications for policy**.

A critical distinction is that translating models into a common language does not, by itself, explain divergence. Explanation requires faithful reconstructions, carefully designed counterfactual experiments, and methods for attributing differences while accounting for interactions and calibration effects.

**Core scientific proposition:** A shared computational representation can enable systematic structural comparison, controlled model experiments, and more informative characterization of model uncertainty.

**Proposed proof of concept:** Reconstruct two or more distinct HIV models, validate their behavior against original implementations, and demonstrate a structured comparison that identifies and quantifies at least some of the drivers of disagreement in a policy-relevant prediction.

## 4. The unifying concept: A common scientific language

These three advances are not independent features. They are enabled by the same architectural choice: representing epidemiological models through a shared, explicit, machine-interpretable language.

This common foundation supports three forms of interoperability.

**Horizontal interoperability — across diseases.** A shared representation allows HIV to be composed with other disease and health modules.

**Human–machine interoperability — across users and computational systems.** A well-defined modeling language and validated tool interfaces allow AI agents to construct, execute, inspect, and document scientific analyses.

**Vertical interoperability — across modeling paradigms and traditions.** Different HIV models can be represented, compared, and experimentally modified within a shared environment.

The lingua franca therefore plays a role beyond software standardization.

It provides a formal bridge between diverse scientific approaches, supports AI-assisted reasoning about model structure, and creates the basis for reproducible comparisons across previously incompatible systems.

Together, these capabilities could enable a broader ecosystem in which disease models function as reusable, inspectable, interoperable scientific knowledge.

## 5. Scientific demonstration strategy

A high-impact paper should not simply describe the architecture or enumerate its features. It should demonstrate that these capabilities make previously difficult scientific tasks substantially easier, more transparent, or more informative.

We propose organizing the paper around three demonstrations, corresponding to the three contributions.

| Demonstration | Scientific question | Evidence of success |
|---|---|---|
| **A. Composable HIV modeling** | Can HIVsim be integrated with other disease models without bespoke redevelopment? | Working HIV–TB and HIV–syphilis examples, quantified reuse, valid interactions, epidemiological outputs |
| **B. AI-enabled modeling** | Can a natural-language request be transformed into a rigorous, reproducible modeling analysis? | Benchmark performance, task correctness, reproducibility, auditability, time savings, safeguards |
| **C. Explainable model comparison** | Can model disagreement be reproduced, interrogated, and partly explained? | Validated reconstructions, structural differences, controlled experiments, explanation of prediction variance |

### 5.1 A flagship end-to-end demonstration

Beyond these individual demonstrations, the paper could benefit from one integrated example showing how the three capabilities reinforce one another.

For example, a user asks:

*"How should Malawi prioritize expanded HIV testing, ART retention, and integrated HIV–TB services over the next decade, and how robust is that prioritization across plausible HIV model structures?"*

The system would:

1. Translate the question into a structured and reviewable analysis specification.
2. Compose the required HIV and TB components.
3. Define and validate relevant interventions and outcomes.
4. Run multiple independently verified HIV model formulations under comparable scenarios.
5. Evaluate how predictions and intervention rankings vary across models.
6. Identify the assumptions responsible for important differences.
7. Generate a reproducible, uncertainty-aware scientific report.

Such a demonstration would illustrate the larger vision: a single policy question connecting disease integration, AI-assisted scientific workflows, and structural uncertainty analysis.

It should be treated as a stretch demonstration, contingent on the validity of the underlying model components and reconstructions.

## 6. Proposed paper narrative

### Working title

**HIVsim: Towards an Interoperable, AI-Native, and Explainable Ecosystem for HIV Modeling**

Alternative titles:

- **Beyond a Single Model: HIVsim and the Next Generation of Computational HIV Epidemiology**
- **HIVsim: Composable Disease Modeling, AI-Enabled Inference, and Explainable Model Ensembles**
- **From Models to Modeling Ecosystems: A New Paradigm for HIV Simulation**

### Central thesis

*A common computational language can transform HIV modeling from a collection of largely isolated tools into an interoperable scientific ecosystem in which disease models can be composed, analyses can be conducted through rigorous AI-assisted workflows, and alternative model structures can be systematically compared to explain uncertainty and inform policy.*

### Proposed manuscript structure

**Introduction — The limits of the current HIV modeling ecosystem**

Establish the scientific and policy importance of HIV models, the barriers created by fragmentation, and the challenge of explaining model disagreement. Introduce the central hypothesis that a shared modeling language can overcome these limitations.

**Methods — HIVsim architecture and scientific infrastructure**

Describe HIVsim's epidemiological representation, the Starsim foundation, disease composition and connectors, AI-native interfaces and validation architecture, and the common-language approach to reconstructing other models.

**Results 1 — Composable HIV epidemiology**

Demonstrate HIV-only and integrated HIV–TB/HIV–syphilis models, including reusable components and emergent interactions.

**Results 2 — AI-enabled, reproducible modeling**

Demonstrate natural-language-to-analysis workflows, scientific safeguards, and benchmark performance relative to conventional workflows.

**Results 3 — Reconstructing and comparing HIV models**

Demonstrate faithful model reconstruction, structural comparison, controlled assumption changes, and attribution of differences in predictions.

**Discussion — From individual models to scientific ecosystems**

Consider implications for modeling science, transparency, collaboration, uncertainty quantification, reproducibility, and the evidence-to-policy process. Address technical and scientific limitations, governance, and the pathway toward a broader open ecosystem.

## 7. Figures that could define the paper

**Figure 1. From isolated models to a common modeling ecosystem**

A conceptual illustration contrasting today's fragmented HIV modeling landscape with HIVsim's three interconnected capabilities: disease composability, AI-native scientific workflows, and multi-model reconstruction/comparison.

The Starsim lingua franca sits at the center, providing a shared representation.

**Figure 2. Composable HIV modeling**

Demonstrate how HIV-only, HIV–TB, and HIV–syphilis simulations are assembled from reusable population, network, intervention, disease, and connector components. Include a quantitative comparison of component reuse and selected epidemiological results.

**Figure 3. From natural-language questions to reproducible science**

Illustrate an AI-assisted modeling workflow from question formulation through model selection, evidence retrieval, specification, validation, simulation, uncertainty analysis, and scientific reporting. Include measured benchmark performance and safeguards, not just a workflow schematic.

**Figure 4. Explaining disagreement between HIV models**

Potentially the signature figure.

Begin with the observed variation in a policy-relevant output—such as the fraction of transmission attributable to undiagnosed people.

Show how distinct model formulations are reconstructed in a shared language, how structural differences are identified, and how controlled model experiments isolate drivers of disagreement.

An ideal final panel would show how the range of predictions changes as selected assumptions are harmonized, with careful treatment of parameter recalibration and interactions.

**Figure 5 (optional). A policy question answered by a model ensemble**

Illustrate how the combined system produces actionable but uncertainty-aware comparisons of intervention strategies, including which conclusions are robust across models and which depend on contested assumptions.

## 8. Development priorities and minimum viable scientific contribution

The paper's ambition is substantial. It is important to distinguish what must be demonstrated for the publication from what can remain part of a longer-term research program.

### Minimum viable paper

A credible first publication would ideally demonstrate:

1. A clearly documented and scientifically validated HIVsim core model.
2. At least one nontrivial multi-disease integration, preferably two.
3. An operational AI-assisted modeling workflow with measurable scientific quality controls.
4. Reconstruction and verification of at least one existing independent HIV model, preferably two.
5. A demonstrable approach to identifying differences between model formulations, including at least one controlled comparison that explains some observed output divergence.

The paper need not recreate the entire HIV modeling literature or fully automate every stage of scientific inference.

What matters is establishing that the architecture is operational, that the scientific workflows are trustworthy, and that the shared representation creates capabilities unavailable or substantially more difficult in existing practice.

### Longer-term research program

The broader vision would include:

- A growing, openly documented library of HIV model reconstructions.
- Shared benchmark datasets and standardized calibration tasks.
- Model comparison tools for structure, assumptions, outputs, and intervention rankings.
- AI-assisted translation of published mathematical models and codebases into the common language.
- Community-contributed disease models, components, connectors, and agents.
- Versioned ensembles that allow policy analyses to be repeated across multiple model structures.
- New methods for structural sensitivity analysis, uncertainty attribution, and evidence prioritization.
- Reusable interfaces for national programs, researchers, and policy analysts.

Over time, this could evolve into a community-maintained ecosystem that makes HIV modeling more collaborative, accessible, and scientifically cumulative.

## 9. Scientific and technical challenges

The paper will be more persuasive if it acknowledges the most difficult challenges directly.

**Model fidelity.** Translating an existing model into another computational representation may alter its behavior, particularly across different simulation paradigms. Model equivalence needs to be demonstrated rather than assumed.

**Structural versus parameter uncertainty.** Differences in model outputs arise from combinations of structure, calibration, data, initialization, and stochastic variation. Attribution methods must distinguish these factors where possible and avoid overstating causal explanations.

**Non-equivalent outcomes.** Models can use subtly different definitions of incidence, diagnosis, transmission attribution, and other outputs. Standardization must preserve or explicitly document these differences.

**Cross-disease validity.** Software-level interoperability does not ensure epidemiological coherence. Integrated models require appropriate biological interactions, compatible networks and populations, and joint validation.

**AI reliability.** AI agents can introduce incorrect assumptions, fabricate evidence, misuse parameters, or overinterpret results. Their role must be bounded by validated tools, transparent provenance, structured evaluation, and human scientific judgment.

**Scientific governance.** An ecosystem built partly from existing HIV models must respect intellectual contributions, model ownership, licensing, attribution, and the legitimate role of independent scientific perspectives.

**Performance and usability.** A common modeling language must remain practical for real scientific work. Representation fidelity, execution speed, maintainability, and usability are all essential criteria.

The goal is not to claim that one framework can effortlessly replace every existing approach. It is to establish that a common computational foundation can make collaboration and cross-model scientific analysis substantially more feasible.

## 10. Implications for evidence-to-policy translation

The long-term value of HIVsim is not measured solely by improvements in modeling software.

It lies in the possibility of strengthening the relationship between epidemiological evidence, scientific inference, and public health decision-making.

A modular modeling architecture can make it easier to address policy questions spanning multiple diseases and health services.

AI-enabled workflows can reduce the time and technical effort required to evaluate new evidence and intervention scenarios.

Explainable model ensembles can help decision-makers understand when recommendations are robust across different scientific assumptions—and when the evidence remains insufficient to support a confident conclusion.

A particularly important opportunity is to turn disagreement into a guide for future research.

If alternative HIV models disagree because of specific uncertainties in risk heterogeneity, treatment interruption, or transmission dynamics, then model comparison may identify which additional data would be most valuable to collect.

In this way, the system could eventually help connect three activities that have historically been only loosely linked: **model-based policy analysis, uncertainty diagnosis, and evidence generation.**

Rather than producing predictions alone, HIVsim could help reveal what needs to be learned to make better decisions.

## 11. Open questions for refinement

The next phase of development should resolve several central questions.

**Scientific identity.** What distinguishes the HIVsim core epidemiological model from existing implementations? Which biological, behavioral, and programmatic mechanisms are included, and which constitute genuine methodological advances?

**Architecture.** Which capabilities are already implemented in HIVsim and current Starsim, which depend on Starsim v4, and which require new software development?

**AI system.** What specific skills, agents, plugins, validation tools, and scientific guardrails currently exist? Which are essential for an end-to-end demonstration?

**Model reconstruction.** Which existing HIV models are realistic first candidates for reconstruction? What access to source code, documentation, reference outputs, and original-model expertise will be required?

**Comparative science.** What is the smallest scientifically meaningful demonstration of model disagreement attribution? Can it be achieved initially with two contrasting models before attempting a larger ensemble?

**Publication strategy.** Should the first paper demonstrate all three advances equally, or establish a strong HIVsim platform with a flagship example of model comparison and present more extensive AI and multi-model capabilities as companion papers?

These questions should determine the technical sprint plan and the evidence required for publication.

## 12. Conclusion: A new kind of modeling infrastructure

HIVsim begins with an HIV model, but its ambition extends well beyond a single implementation of HIV transmission dynamics.

By building on a shared epidemiological language, it opens the possibility of combining diseases, connecting AI agents to rigorous simulation workflows, and expressing multiple HIV modeling traditions within a common environment.

This creates an opportunity to reconsider what a scientific model can be.

Instead of a standalone computational artifact used by a specialized research team, a model can become part of an interoperable, inspectable, extensible ecosystem—one that makes it easier to reuse established science, examine competing assumptions, reproduce analyses, and generate policy-relevant evidence.

Perhaps most importantly, such an ecosystem would make model disagreement scientifically productive.

**The next generation of HIV modeling should not be defined only by its ability to generate better predictions, but by its ability to explain how those predictions arise, why credible models disagree, and what evidence is needed to improve decisions.**

HIVsim is an opportunity to build that future.

---

## Foundational references

1. Starsim. *A lingua franca for epidemiological modeling.* Design specification, version 1.4, October 20, 2026. https://starsim.org/lingua_franca_design/
2. Miao J, Davis JR, Zhang Y, et al. *Reimagining research papers as interactive and reliable AI agents.* Nature. Published September 16, 2026. https://www.nature.com/articles/s41586-026-11044-y
3. Bansi-Matharu L, et al. *Identifying gaps in the HIV treatment cascade in Africa: a model comparison study.* Lancet Global Health. 2025;13:e1006–e1019. https://pubmed.ncbi.nlm.nih.gov/40412394/
4. Starsim documentation. https://docs.starsim.org/
5. STIsim and HIVsim documentation. https://stisim.org/
6. Starsim AI tools. https://ai.starsim.org/
