# Cognitive maps

## World model

**General knowledge $\times$ Specific knowledge $\Rightarrow$ [world model](../ai/world_model.md)**

### Regularities
Mammals organize knowledge by constructing models of the world: make us of **regularities** of the world to reduce memory and computational cost

### Factorized representation
For the brain, a situation is broke down:

**structural knowledge (coordinates) $\times$ sensory cues = situation**

General knowledge lies on the existence of a **factorized representation** (probabilities are independant 2D = 1D x 1D)
We can use graph formalism to unify these differents modalities. Each modality has differents graphs:

- vision: 2D grid graphs
- sound: 1D graph
- family members: tree
### Modality-agnostic mapping machine
Information is organized as selective maps. First discovered for spatial mapping, but also non-spatial mapping (e.g. sound).

Use **[path integration](path_integration.md)** can be generalized to to navigate in any graph.

## Cells
### [Entorhinal cortex](../brain/neuroanatomy.md#entorhinal-cortex)

General coordinate system

 - Grid cells: contex independant, hexagonal grids
 - Object vector cells: activates if at a certain distance direction of any object
 - Sound grid cells

### Hippocampus

Specific code

  - Place cells: context dependant, code for current location
  - Landmark cells: same as ovc, but for specific objects
  - Sound place cells

### In both regions

- Boundary cells: code for boundaries
- Head direction cells: direction the anoi!al is facing

## Ressources
### [Spatial Computing enables flexible working memory](https://picower.mit.edu/news/spatial-computing-enables-flexible-working-memory)
> Study shows that the brain creates distinct spaces in the cortex for each general rule and controls those patches with brain rhythms
> Your brain can do this because it represents the rules and the contents at different physical scales

## Flashcards
??? question "What is the primary way mammals organize knowledge? [](){.fbutton .ok}[](){.fbutton .nok}"
    By constructing models of the world that make use of the regularities of the world to reduce memory and computational cost
    ##### id: ecbf75, box: 1, score: 0/1, next: 11/10/2023, last: 11/10/2023

??? question "What are the two component of a world model? [](){.fbutton .ok}[](){.fbutton .nok}"
    General and specific knowledge
    ##### id: 7f8747, box: 1, score: 0/1, next: 11/10/2023, last: 11/10/2023

??? question "What does "Modality-agnostic mapping machine" means? [](){.fbutton .ok}[](){.fbutton .nok}"
    The ability of the brain to creates maps that are not specific to any type (vision, sound) of sensory input
    ##### id: 6bf0b4, box: 3, score: 2/2, next: 17/10/2023, last: 11/10/2023

??? question "Where are the grid cells? [](){.fbutton .ok}[](){.fbutton .nok}"
    - in the entorhinal cortex
    - they are context-independent and code path integration
    ##### id: ed444c, box: 2, score: 2/3, next: 13/10/2023, last: 12/10/2023

??? question "Where are the place cells? What they do? [](){.fbutton .ok}[](){.fbutton .nok}"
    - in the hippocampus
    - they are context-dependant and code for current loaction
    ##### id: be677f, box: 1, score: 0/0, next: 09/10/2023, last: 09/10/2023

??? question "What are boundary cells for? [](){.fbutton .ok}[](){.fbutton .nok}"
    They code for boundaries in both entorhinal cortex and hippocampus
    ##### id: 7e38a7, box: 2, score: 1/2, next: 12/10/2023, last: 11/10/2023

??? question "How does the brain use graph formalisme in cognitive mapping? [](){.fbutton .ok}[](){.fbutton .nok}"
    To unify different modalities, with each modality having different graphs, like vision using 2D grid graphs and sound using 1D graphs
    ##### id: 1c9b99, box: 1, score: 0/0, next: 09/10/2023, last: 09/10/2023

??? question "`Path integration` [](){.fbutton .ok}[](){.fbutton .nok}"
    A navigational process where an organism calculates its position using internal cues about distances and directions traveled, rather than external landmarks.
    ##### id: e9575e, box: 3, score: 2/2, next: 19/10/2023, last: 13/10/2023
