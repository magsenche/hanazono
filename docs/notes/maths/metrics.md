# Metrics

## Kullback-Leibler divergence
`KL divergence`
: $$D_{KL}[P\parallel Q] = \sum_{x \in \chi}P(x)\log(\frac{P(x)}{Q(x)}) = \int_{x \in \chi}p\log(\frac{p}{q})dx = H(p,q)-H(p)$$

    $P$ represents the data, observations

    $Q$ represents the model, theories, approximation of $P$

### Interpretations

- number of bits required for encoding samples of $P$ using a code optimized for $Q$ rather than one optimized for $P$
- expected excess surprise from using $Q$ as a model when the actual distribution is $P$
- relative entropy of $P$ w.r.t $Q$

### Properties

- divergence
- distance (not metric, because no triangle inequality)

## Jensen-Shannon divergence
`JS divergence`
: $$ D_{JS}[p\parallel q] = \frac{1}{2} D_{KL}[p\parallel {\frac{p+q}{2}}] + \frac{1}{2} D_{KL}[q\parallel {\frac{p+q}{2}}]$$

### Properties

- symmetrical
- if log base 2, normalized between 0 and 1

## Wasserstein metric
`wasserstein distance`
: $$W_p(\mu, \nu) := \left( \inf_{\pi \in \Pi(\mu, \nu)} \int_{\mathcal{X} \times \mathcal{X}} d(x, y)^p \, \mathrm{d}\pi(x, y) \right)^{1/p}$$

### Properties
- also named Earth Mover’s distance
- linked to optimal transport
- minimum energy cost of moving a pile of dirt in the shape of one probability distribution to the shape of the other distribution
- hard to compute

### Sliced Wasserstein loss

[A Sliced Wasserstein Loss for Neural Texture Synthesis](https://arxiv.org/pdf/2006.07229.pdf)

De manière général, pour faire du style transfer, on utilise les matrices de gram (expliqué dans le papier), mais visiblement c'est mieux leur méthode.

En gros, ils projetent les features (high dim) dans une espace aléatoire de basse dimension, puis ils font une metrique de transport optimal dans cet espace.

Un des problèmes de leur loss, c'est que avec leur metrique de transport optimal, ils perdent la structure (qui peut être très importante). Pour pallier ça, ils proposent de rajouter une feature qui encode cette structure (comme du positional encoding)

??? question "`KL div` [](){.fbutton .ok}[](){.fbutton .nok}"
    $$D_{KL}[P\parallel Q] = \sum_{x \in \chi}P(x)\log(\frac{P(x)}{Q(x)}) = \int_{x \in \chi}p\log(\frac{p}{q})dx = H(p,q)-H(p)$$

    $P$: data, observations

    $Q$: model, theories, approximation of $P$
    ##### id: ced04e, box: 2, score: 1/2, next: 16/10/2023, last: 15/10/2023

??? question "Interpretation of the KL div [](){.fbutton .ok}[](){.fbutton .nok}"
    - number of bits required for encoding samples of $P$ using a code optimized for $Q$ rather than one optimized for $P$
    - expected excess surprise from using $Q$ as a model when the actual distribution is $P$
    - relative entropy of $P$ w.r.t $Q$
    ##### id: 8507b7, box: 1, score: 1/2, next: 16/10/2023, last: 16/10/2023

??? question "`JS div` [](){.fbutton .ok}[](){.fbutton .nok}"
    $$ D_{JS}[p\parallel q] = \frac{1}{2} D_{KL}[p\parallel {\frac{p+q}{2}}] + \frac{1}{2} D_{KL}[q\parallel {\frac{p+q}{2}}]$$
    ##### id: df5cc5, box: 3, score: 2/3, next: 18/10/2023, last: 12/10/2023

??? question "List 3 properties of the wasserstein metric [](){.fbutton .ok}[](){.fbutton .nok}"
    - also named Earth Mover’s distance
    - linked to optimal transport
    - minimum energy cost of moving a pile of dirt in the shape of one probability distribution to the shape of the other distribution
    - hard to compute
    ##### id: 48d027, box: 1, score: 0/0, next: 07/10/2023, last: 07/10/2023

??? question "`Wasserstein distance` [](){.fbutton .ok}[](){.fbutton .nok}"
    $$W_p(\mu, \nu) := \left( \inf_{\pi \in \Pi(\mu, \nu)} \int_{\mathcal{X} \times \mathcal{X}} d(x, y)^p \, \mathrm{d}\pi(x, y) \right)^{1/p}$$
    ##### id: 388c26, box: 1, score: 0/0, next: 07/10/2023, last: 07/10/2023