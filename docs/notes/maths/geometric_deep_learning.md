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

??? question "What the basic idea of geometric deep learning [](){.fbutton .ok}[](){.fbutton .nok}"
    Applying deep learning to surfaces or manifolds while respecting and preserving their underlying geometry
    ##### id: ae47ec, box: 3, score: 2/2, next: 17/10/2023, last: 11/10/2023

??? question "`Geodesic` [](){.fbutton .ok}[](){.fbutton .nok}"
    It is a generalization of the notion of a "straight line". Curve representing in some sense the shortest path (arc) between two points in a surface, or more generally in a Riemannian manifold.
    ##### id: d1187b, box: 2, score: 1/1, next: 12/10/2023, last: 11/10/2023

??? question "Relation between convolution and shift-invariant linear operator [](){.fbutton .ok}[](){.fbutton .nok}"
    Convolutions are linear shift-equivariant operations, and any shift-equivariant linear operator is a convolution.
    ##### id: 352c61, box: 1, score: 0/0, next: 07/10/2023, last: 07/10/2023
