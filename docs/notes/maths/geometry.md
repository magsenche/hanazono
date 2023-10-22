# Geometry

## Definitions

`Group`
:   A mathematical group is a collection of things (like the set of integers), and a way to combine two members of the group that makes a third (like addition of two integers, that always creates another integer), in a way that satisfies a few rules:

    1. There is an identity element, which is a member of the group that when combined with any other element doesn’t change it. For adding integers the identity element is 0, since a + 0 = a for all a.
    2. Every member of the group has an inverse, defined by its property that combining an element with its inverse produces the identity element. In our integer-addition example the inverse of any integer a is −a, since −a + a = 0, and 0 is the identity element.
    3. Associativity applies, which just means the order in which you perform operations doesn’t matter: (a + b) + c = a + (b + c)

    [Check appendix A](https://arxiv.org/pdf/2209.15563.pdf)

`Orbit`
: $O_x =  \{gx | x \in X, g \in G \}$
: $x \sim_g y \Rightarrow y \in O_x$

`Stabilizer`
: $H_x =  \{g \in G | gx = x \}$

`Coset`
: $gH = \{ gh | h \in H \}$

`Group representation`
: $\rho: G \rightarrow GL(n),  \rho (g.h) = \rho(g)\rho(h)$

`Fiber`
: The fiber refers to the vector space defined at each point of a manifold
: A way to paste a copy of an object at each point of a manifold.
: Examples with circle as a manifold, segment as the fiber:

    - Basic cartesian product $\rightarrow$ Ring
    - "Twisted" product $\rightarrow$ Moebius ruban

`Tangent space`
: The tangent space defines a coordinate system locally on a manifold

??? question "`Group`"
    - $+$ interne composistion
    - $0$ identity element
    - associativity
    - $-a$ inverse

??? question "`Orbit`"
    $O_x =  \{gx | x \in X, g \in G \}$

    $x \sim_g y \Rightarrow y \in O_x$

??? question "`Stabilizer`"
    $H_x =  \{g \in G | gx = x \}$

??? question "`Coset`"
    $gH = \{ gh | h \in H \}$

??? question "`Group representation`"
    $\rho: G \rightarrow GL(n),  \rho (g.h) = \rho(g)\rho(h)$

??? question "`Tangent space`"
    Local coordinate system on a manifold

??? question "List 2 possible structures constructed from the circle and the segment"
    Circle as a manifold, segment as the fiber:
    - Basic cartesian product $\rightarrow$ Ring
    - "Twisted" product $\rightarrow$ Moebius ruban
