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

??? question "`Group` [](){.fbutton .ok}[](){.fbutton .nok}"
    - $+$ interne composistion
    - $0$ identity element
    - associativity
    - $-a$ inverse
    ##### id: d3d614, box: 3, score: 2/2, next: 18/10/2023, last: 12/10/2023
??? question "`Orbit` [](){.fbutton .ok}[](){.fbutton .nok}"
    $O_x =  \{gx | x \in X, g \in G \}$

    $x \sim_g y \Rightarrow y \in O_x$
    ##### id: 618def, box: 3, score: 2/2, next: 17/10/2023, last: 11/10/2023

??? question "`Stabilizer` [](){.fbutton .ok}[](){.fbutton .nok}"
    $H_x =  \{g \in G | gx = x \}$
    ##### id: e38e3e, box: 2, score: 1/1, next: 13/10/2023, last: 12/10/2023

??? question "`Coset` [](){.fbutton .ok}[](){.fbutton .nok}"
    $gH = \{ gh | h \in H \}$
    ##### id: 170626, box: 2, score: 1/3, next: 16/10/2023, last: 15/10/2023

??? question "`Group representation` [](){.fbutton .ok}[](){.fbutton .nok}"
    $\rho: G \rightarrow GL(n),  \rho (g.h) = \rho(g)\rho(h)$
    ##### id: 85c2dd, box: 2, score: 1/1, next: 17/10/2023, last: 16/10/2023

??? question "`Tangent space` [](){.fbutton .ok}[](){.fbutton .nok}"
    Local coordinate system on a manifold
    ##### id: 45b2b1, box: 2, score: 1/1, next: 12/10/2023, last: 11/10/2023

??? question "List 2 possible structures constructed from the circle and the segment [](){.fbutton .ok}[](){.fbutton .nok}"
    Circle as a manifold, segment as the fiber:

    - Basic cartesian product $\rightarrow$ Ring
    - "Twisted" product $\rightarrow$ Moebius ruban
    ##### id: b2bc31, box: 3, score: 2/2, next: 18/10/2023, last: 12/10/2023
