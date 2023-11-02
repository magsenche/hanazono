# Geometric Deep Learning

## [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/pdf/2104.13478.pdf)

## Problem-Dependent Structure

The choice of the appropriate level of structure depends on the problem.

For example, when segmenting histopathology slide images, consider flipped versions of images as equivalent. In contrast, for road sign classification, only consider orientation-preserving transformations as symmetries.

## Quantifying Transformations

Measure the difference between a transformation and the symmetry subgroup using a complexity measure denoted as $c(\tau)$:

$\lVert f(\rho(\tau)x)-f(x)\lVert \leq Cc(\tau)\lVert x \lVert$

## Signal vs. Domain Deformations

Understand the geometry of the input domain. Utilize:

- local equivariant maps
- global invariant maps
- coarsening operators.

## Shifts and Convolutions

Convolutions are linear shift-equivariant operations, and any shift-equivariant linear operator is a convolution.

## Invariances in Manifolds

Manifolds exhibit invariance in transformations that preserve metric structure and local reference frame changes.

## Advantages of Manifold Models

- compact representation of 3D objects, allowing the elimination of memory allocation for empty space
- enable ignoring the internal structure of objects and are suitable for modeling non-rigid deformations, such as those found in the human body

## Geodesics

Among all the curves connecting points $u$ and $v$ on a manifold, we seek $\gamma$ that minimizes the length functional.

`Geodesic`
:  It is a generalization of the notion of a "straight line". Curve representing in some sense the shortest path (arc) between two points in a surface, or more generally in a Riemannian manifold.

## Flashcards

??? question "What the basic idea of geometric deep learning"
    Applying deep learning to surfaces or manifolds while respecting and preserving their underlying geometry

??? question "Relation between convolution and shift-invariant linear operator"
    Convolutions are linear shift-equivariant operations, and any shift-equivariant linear operator is a convolution.
