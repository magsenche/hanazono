# Organization

## Topographic organization categories in brain

> A third feature of brain architecture that is manifested in the VTC is the **superimposition of multiple functional maps and fine-scale clusters within the same cortical expanse**. Superimposition of functional representations may be a necessary **consequence of projecting a high-dimensional representational space onto the two-dimensional cortical sheet**. The dimensionality of representations in the **VTC is estimated between 35 to 50 dimensions**.

Visual categorization occuring in Ventral Temporal Cortex **VTC**. After V1-4 in the human visual stream.
It contains information about:

- color
- eccentricity bias
- visual field maps
- specific domains
- expertise
- object categories
- concepts
- semantics
- real world object size

They propose that a nested sptial hierarchy enables efficient categorization. It enables flexible access to category information through multiple sclaes of abstraction.

Marr approach for understanding information processing systems involves 3 levels:

1. **Computation**: what does the system do?
2. **Representation**: how does it achieve its goal?
3. **Neural implementation**: how is it implemented in the brain?

### Computation

To achieve generalization while keeping robust and accurate categorization and specitifity among examples, need to overcome 3 forms of variability:

1. Type of visual information (motion, luminance, texture)
2. Viewing conditions
3. Appearance

Need

- linear operations to build new features, specificity
- non-linear operations to discriminate and generalize well across transformations
- processing herarchy to increase tolerance to transformations and build mort complex features

With separable representation its faster to categorize. Disantagle tangled representations coming from V1 may be the role of the VTC.

VTC should allow flexible accesss to category information, depending on the context or the task

### Representation

Evidences showing VTC representations are
- primarily driven by shape and content
- more tolrant to position, size and mirror rotation transformations
- linearly separable in contrast with V1-hV4 representations

VTC responses represent perceived similarity more than physical similarity

### Implementation

- neurons with similar properties are clustered together
- topological orgaization of functional representation
- multiple functional representation superimposed on the same cortical expanse

Multiple levels and scales of clustering:
- columns (1 mm) — which are thought to reflect the basic computational unit of the brain
- patches (5 mm)
- regions (10 mm)
- maps
  - within a region (for example, a retinotopic map)
  - across regions (>10 mm; for example, an eccentricity band, which can span several visual areas)

> Consistent topology of functional representations relative to anatomical landmarks and to each other is meaningful: it reveals that particular axes of representational spaces are physically implemented as axes in anatomical space and, furthermore, that anatomical constraints might determine the topology of functional representations

> The finding that representational spaces are systematically mapped across the cortical sheet suggests that a particular type of information is arranged in the cortex in a way that is easy to read out. For example, both V1 and middle temporal area MT contain neurons that selectively respond to motion in particular directions (direction-selective neurons), but only MT contains direction-selective columns that are systematically arranged across the cortical sheet. This cortical topology potentially enables MT (but not V1) to represent motion direction information in an explicit manner.

Divergence vs convergence. They are both beneficial:
- speed up processing, generalize
- build hierarchical representations, accelerate neural communication, reduce wiring cost

> The organization of VTC representations along the cortical sheet indicates that different kinds of information manifest at different spatial scales


> Increases in brain size are accompanied by a relative decrease in connectivity (macaques vs mouse)

> Evolutionarily preserved features, however, often are expected to manifest themselves as organizational principles tied to biophysical constraint


## Topographic Deep Artificial Neural Network

[A Unifying Principle for the Functional Organization of Visual Cortex](https://www.biorxiv.org/content/10.1101/2023.05.18.541361v1.full.pdf) & [code](https://github.com/neuroailab/TDANN)

`TDANN`
:  unified model that predict functional organization in cortical areas of the primate visual system by achieving a self-supervised task-general sensory representation and maximizing the  smoothness of responses across the cortical sheet according to a metric that scales relative to cortical surface area (the network’s inter-layer wiring length: the brain balances performance with metabolic costs.)

#### Constraints

- support ecologically-relevant behaviors $\Rightarrow$ produce useful neural representations
- biophysically efficient manner, using as few ressources as possible $\Rightarrow$ minimize of neuronal wiring length

TDANN reproduces the functional organization of the ventral stream:

- smooth orientation, maps with pinwheels in an earlier model layer
- category-selective patches in a later layer that match the number, size, and relative geometry of patches in human VTC.

#### Overview of Training

In summary, models are trained in 6 steps:

1. ResNet-18 is trained on the task loss only.
2. Positions in each layer are initialized to preserve coarse retinotopy (Stage 1).
3. Positions are further pre-optimized in an iterative process that preserves retinotopy while bringing together
units with correlated responses to sine gratings images (Stage 2).
1. Positions are frozen and never again modified.
2. All network weights are randomly re-initialized.
3. The network is trained to minimize a weighted combination of the spatial and task loss components.

Pretraining using sine grating images to pre-correlate nearby neurons (orientation,color,spatial frequency)

## Ressources

- [Modeling Category-Selective Cortical Regions with
opographic Variational Autoencoders](https://arxiv.org/pdf/2110.13911.pdf)
- [Principles governing the topological organization of object
selectivities in ventral temporal cortex](https://www.biorxiv.org/content/10.1101/2021.09.15.460220v1.full.pdf)
- [The functional architecture of the ventral temporal cortex and its
role in categorization](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4143420/pdf/nihms612516.pdf)
- [Spatial Embedding and Wiring Cost Constrain the Functional Layout of the Cortical Network of Rodents and Primates](https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.1002512&type=printable)

## Flashcards

??? question "What is a prominent feature of brain architecture seen in the VTC?"
    Superimposition of multiple functional maps and fine-scale clusters within the same cortical expanse.

??? question "Where does visual categorization occur after V1-4 in the human visual stream?"
    In the Ventral Temporal Cortex (VTC).

??? question "Name three types of information contained in the VTC"
    - color
    - eccentricity bias
    - visual field maps

??? question "List all 3 levels of Marr's approach for understanding information processing systems"
    - computation
    - representation
    - neural implementation

??? question "What is the role of the VTC in visual information processing?"
    To disentangle tangled representations coming from V1 and allow flexible access to category information based on context or task

??? question "How do VTC responses differ from V1-hV4 responses?"
    VTC responses represent perceived similarity more than physical similarity and are primarily driven by shape and content

??? question "Describe the levels of clustering in VTC"
    Columns (1 mm), patches (5 mm), regions (10 mm), and maps (within and across regions)

??? question "What is the primary objective of the TDANN model?"
    To predict functional organization in cortical areas of the primate visual system in a biophysically efficient manner

??? question "Name the two main constraints of TDANN"
    - support ecologically-relevant behaviors
    - minimize neuronal wiring length
