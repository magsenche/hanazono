# Calculus

## Einstein summation

>**Upper** indices go **up** to down; **lower** indices go **left** to right.

>**Co**variant tensors are **row** vectors that have indices that are **below** **(co-row-below)**

### Inner product
-  $u_j v^j$
-  $\mathbf{u} \cdot \mathbf{v}$

### Outer product
-  $u^i v_j$
-  $\mathbf{u} \otimes \mathbf{v}$

### Matrix vector multiplication
- $u^i = {A^i}_j v^j$
- $\mathbf{u}_{i} = (\mathbf{A} \mathbf{v})_{i}  =\sum_{j=1}^N A_{ij} v_{j}$

### Matrix multiplication
- ${C^i}_k = {A^i}_j {B^j}_k$
- $\mathbf{C}_{ik} = (\mathbf{A} \mathbf{B})_{ik}  =\sum_{j=1}^N A_{ij} B_{jk}$


## Matrix

- row vs column

### Derivatives



$\frac{\partial \bold{y}}{\partial \bold{x}}=(\frac{\partial y_j}{\partial x_i}) = \begin{pmatrix}\frac{\partial y_1}{\partial x_1} & \frac{\partial y_2}{\partial x_1} & \dots & \frac{\partial y_m}{\partial x_1} \\ \vdots & \vdots & \dots & \vdots \\ \frac{\partial y_1}{\partial x_n} & \frac{\partial y_2}{\partial x_n} & \dots & \frac{\partial y_m}{\partial x_n} \end{pmatrix}$

??? example "Derivative w.r.t scalar"
    $\frac{\partial y}{\partial \bold{x}} = \begin{pmatrix}\frac{\partial y}{\partial x_1}\\ \vdots \\ \frac{\partial y}{\partial x_n}\end{pmatrix}$

    $\frac{\partial \bold{y}}{\partial x} = \begin{pmatrix} \frac{\partial y_1}{\partial x} & \dots & \frac{\partial y_m}{\partial x}\end{pmatrix}$


- $\dfrac{\partial{a^TXb}}{\partial X} = ab^T$
- $\dfrac{\partial{x^TAx}}{\partial x} = x^T(A+A^T)$ (?)

- Cheatsheets
    - [matrix cookbook](https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf)
    - [matrix calculus](https://www.doc.ic.ac.uk/~ahanda/referencepdfs/MatrixCalculus.pdf)

## Delta notation

| $\Delta$                        | $d$                                                       | $\partial$                                                                | $\delta$                                  |
| ------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------- |
| Global Total Variation          | Local Total Variation                                     | Partial Local Variation                                                   | Elementary Quantity                       |
| Difference between 2 quantities | Difference between 2 close points (time, space, etc.)     | Partial derivative representing local change with respect to one variable | Not necessarily a difference or variation |
| Measures a global change        | Can be standalone: $dx$, $dt$ as infinitesimal quantities | Always as a ratio: $\partial A / \partial x$, $\partial f / \partial t$   | $\delta W = F \cdot dL$                   |


## **Reparametrization trick**

- [https://sassafras13.github.io/ReparamTrick/](https://sassafras13.github.io/ReparamTrick/)
- [https://gregorygundersen.com/blog/2018/04/29/reparameterization/](https://gregorygundersen.com/blog/2018/04/29/reparameterization/)

## Flashcards

??? question "Properties of 4 deltas"
    | $\Delta$                        | $d$                                                       | $\partial$                                                                | $\delta$                                  |
    | ------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------- |
    | Global Total Variation          | Local Total Variation                                     | Partial Local Variation                                                   | Elementary Quantity                       |
    | Difference between 2 quantities | Difference between 2 close points (time, space, etc.)     | Partial derivative representing local change with respect to one variable | Not necessarily a difference or variation |
    | Measures a global change        | Can be standalone: $dx$, $dt$ as infinitesimal quantities | Always as a ratio: $\partial A / \partial x$, $\partial f / \partial t$   | $\delta W = F \cdot dL$                   |


??? question "Einstein notation for $(\mathbf{A} \mathbf{v})_{i}$"
    $u^i = {A^i}_j v^j$

??? question "Einstein notation for $(\mathbf{A} \mathbf{B})_{ik}$"
    ${C^i}_k = {A^i}_j {B^j}_k$

??? question "Einstein notation for $\mathbf{u} \otimes \mathbf{v}$"
    $u^i v_j$

??? question "Einstein notation for $\mathbf{u} \cdot \mathbf{v}$"
    $u_j v^j$

## Notation

* Scalars are written as lower case bold letters.
* Vectors are written as upper case bold letters, such as $\mathbf{z}$, and can be either row (dimensions $(1\times n)$) or column (dimensions $(n\times1)$) vectors. Column vectors are the default choice, unless otherwise
  mentioned. Individual elements are indexed by subscripts, such as $\mathbf{z}_{i}(i\in\{1,\cdot\cdot\cdot,n\})$.
* Matrices are written as upper case bold letters, such as $\mathbf{X}$, and have dimensions $(m\times n)$
  corresponding to $m$ rows and $n$ columns. Individual elements are indexed by double subscripts
  for row and column, such as $\mathbf{X}_{ij}(i\in\{1,\cdot\cdot\cdot,m\},j\in\{1,\cdot\cdot\cdot,n\})$.

## Basic Rules

This document follows numerator layout convention. There is an alternative denominator layout
convention, where several results are transposed. Do not mix different layout conventions.
