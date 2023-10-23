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
??? question "What is the primary way mammals organize knowledge?"
    By constructing models of the world that make use of the regularities of the world to reduce memory and computational cost

??? question "What are the two component of a world model?"
    General and specific knowledge

??? question "What does Modality-agnostic mapping machine means?"
    The ability of the brain to creates maps that are not specific to any type (vision, sound) of sensory input

??? question "Where are the grid cells?"
    - in the entorhinal cortex
    - they are context-independent and code path integration

??? question "Where are the place cells? What they do?"
    - in the hippocampus
    - they are context-dependant and code for current loaction

??? question "What are boundary cells for?"
    They code for boundaries in both entorhinal cortex and hippocampus

??? question "`Path integration`"
    A navigational process where an organism calculates its position using internal cues about distances and directions traveled, rather than external landmarks.
