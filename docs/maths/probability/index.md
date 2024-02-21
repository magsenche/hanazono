# Probability

## Distributions
=== "Bernoulli"
    $P(X = k;p) = p^k (1-p)^{1-k}, k \in {0,1}$

    $p$ success probability

    Describes an experiment with only two outcomes (success or failure) and is used for binary data.

=== "Binomial"
    $P(X = k;n,p) = \binom{n}{k} p^k (1-p)^{n-k}$

    $n$ number of trial, $p$ success probability

    Used when there are $n$ independent trials, each with a success probability of $p$. It gives the probability of obtaining exactly $k$ successes. It's also the sum of $n$ identical Bernoulli random variables

=== "Poisson"
    $P(X = k;\lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$

    $\lambda$ rate

    Appropriate for modeling the number of times an event occurs in a fixed interval of time or space, given a constant mean rate ($\lambda$).

=== "Normal"
    $f(x;\mu,\sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$

    $\mu$ mean, $\sigma$ standard deviation

    When several normal distributions are multiplied, we often use the precision $J = \frac{1}{\sigma^{2}}$:

    $J_{n} = \sum J_{k}$, $\mu_{n}=\frac{\sum J_{k}\mu_{k}}{J_{n}}$

    Suitable for modeling distributions of real-valued data with a symmetric, bell-shaped curve.

=== "Von Mises"
    $f(x;\mu,\kappa) - \frac{1}{2\pi I_{0}(\kappa)}e^{\kappa cos(x-\mu)}$

    $\mu$ circular mean, $\kappa$ concentration parameter, $I_{0}$ modified Bessel function of the first kind of order 0

    Used for variable with periodic domain (orientation, motion). It can be regarded as the circular analog of a Gaussian distribution.

=== "Gamma"
    === "$k,\theta$"
        $f(x;k,\theta) = \frac{x^{k-1}e^{-x/\theta}}{\theta^k \Gamma(k)}$

        $k$ shape parameter, $\theta$ scale parameter

    === "$\alpha,\beta$"
        $f(x;\alpha,\beta) = x^{\alpha-1}\frac{\beta^{\alpha}e^{-\beta x}}{ \Gamma(\alpha)}$

        $\alpha$ shape parameter, $\beta=\frac{1}{\theta}$ intensity parameter

    Often used to model the time until an event occurs a certain number of times, such as the total lifespan of a system until failure.

=== "Beta"
    $f(x;\alpha,\beta) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}$

    $\alpha, \beta$ shape parameters

    Useful in modeling continuous variables that are limited to a range of 0 to 1, such as probabilities or proportions.

=== "Inverse Gamma"
    $f(x;\alpha,\beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{-\alpha - 1} e^{-\frac{\beta}{x}}$

    $\alpha$ shape parameter, $\beta$ scale parameter, $\Gamma(\alpha)$ gamma function

    Commonly used as the conjugate prior for the variance parameter in normal distributions within Bayesian frameworks. It's suitable for modeling the distribution of positive continuous random variables, particularly for scale parameters in various statistical models.

=== "Dirichlet"
    $f(\mathbf{x};\boldsymbol{\alpha}) = \frac{1}{B(\boldsymbol{\alpha})} \prod_{i=1}^{K}x_i^{\alpha_i - 1}$

    $\mathbf{x} = (x_1, \ldots, x_K)$ K-dimensional vector, $\boldsymbol{\alpha} = (\alpha_1, \ldots, \alpha_K)$ parameters, $B(\boldsymbol{\alpha})$ multivariate beta function

    Used primarily in Bayesian statistics, especially for conjugate priors in models with categorical or multinomial distributions. It's suitable for modeling the probabilities of a K-dimensional random variable where each component is a probability between 0 and 1, and the sum of all components is 1.

=== "Multivariate Normal"
    $f(\mathbf{x};\boldsymbol{\mu}, \boldsymbol{\Sigma}) = \frac{1}{(2\pi)^{k/2}|\boldsymbol{\Sigma}|^{1/2}} \exp\left(-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1}(\mathbf{x} - \boldsymbol{\mu})\right)$

    $\boldsymbol{\mu}$ mean vector, $\boldsymbol{\Sigma}$ covariance matrix, $|\boldsymbol{\Sigma}|$ determinant of the covariance matrix

    Useful for modeling the joint distribution of a set of continuous random variables that are linearly correlated. It's a generalization of the normal distribution to higher dimensions and is widely used in multivariate analysis, pattern recognition, and machine learning.

## Properties

### Central Limit Theorem
`Central Limit Theorem`
: Under appropriate conditions, the distribution of a normalized version of the sample mean converges to a standard normal distribution.

### Chain rule
$f_{X,Y}=f_{X|Y}f_{Y}$

$f_{X,Y|Z}=f_{X|Y,Z}f_{Y|Z}$


### Marginalization

#### Discrete
$p(a)=\sum_b p(a,b)$

$p(a|c)=\sum_b p(a,b|c)=\sum_b p(a|b,c)p(b|c)$

#### Continuous
$p(x)=\int_y p(x,y)dy$

$p(x|z)=\int_y p(x,y|z)dy=\int_y p(x|y,z)p(y|z)dy$

### Variable change
When $f$ is monotonical (increase or decrease):

if $Y=f(X)$, then $p_{Y}(y)=p_{X}(f^{-1}(y))|\frac{df^{-1}}{dy}|$

## Conjugate distributions
| Prior                   | Likelihood                   | Posterior                         |
| ----------------------- | ---------------------------- | --------------------------------- |
| Normal (μ₀, σ₀²)        | Normal (x̄, σ²/n)             | Normal (μₙ, σₙ²)                  |
| Beta (α, β)             | Binomial (n, p)              | Beta (α + x, β + n - x)           |
| Gamma (α, β)            | Poisson (λ)                  | Gamma (α + x, β + 1/n)            |
| Gamma (α, β)            | Exponential (λ)              | Gamma (α + n, β + Σxᵢ)            |
| Dirichlet (α₁, ..., αₖ) | Multinomial (n, p₁, ..., pₖ) | Dirichlet (α₁ + x₁, ..., αₖ + xₖ) |
| Inverse-Gamma (α, β)    | Gamma (k, θ)                 | Inverse-Gamma (α + n, β + Σxᵢ)    |

## Markov Chain
`Markov Chain`
: $P(X_T = x_T | X_{T-1}, ..., X_{0} = x_{T-1}, ..., x_{0})=P(X_T = x_T | X_{T-1} = x_{T-1})$. Memory-less stochastic process. The knowledge of the previous state is all that is necessary to determine the current state

`Markov Random Field`
: Set of random variables satisfying the Markov property for random fields

### Markov Chain Monte Carlo
**Monte–Carlo** is the practice of estimating the properties of a distribution by examining random samples from the distribution

`Monte Carlo sampling`
: Process of estimating the properties of a distribution by examining random samples from the distribution

- [A simple introduction to Markov Chain Monte–Carlo sampling](https://link.springer.com/content/pdf/10.3758/s13423-016-1015-8.pdf)
- [Wikipedia](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Monte-Carlo_par_cha%C3%AEnes_de_Markov)

These initialize a vector of all variables to be inferred, and change it iteratively to produce a sequence of vectors. This is set up in such a way that, over time, the expected number of times of being in a state is proportional to the actual probability of the state given the observed variables.

These methods can deal with arbitrary probability distributions. They are particularly useful if the probability distribution is concentrated in small areas of high probability. However, all the proofs for correctness only hold in the limit of large, often astronomical, numbers of iterations. In practice, Markov Chain methods are usually limited by the difficulty of problems they can solve by available runtime.

In cognitive science, it has been proposed that human decision-makers behave like Markov Chains with a limited number of iterations.

## Notations
Often times, all the density and probability mass functions are denoted with the same letter (usually p) without any subscripts:

$$f_{θ|Y}(θ|y)= \frac{f_{Θ}(θ)f_{Y|Θ}(y|θ)}{f_{Y}(y)} \rightarrow \frac{p(θ)p(y|θ)}{p(y)} = p(θ|y)$$

| **$p(θ∣d)$**                                                          | **$p(θ;d)$**                                                               |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| $θ$ is dependent on $d$ in a **probabilistic** sense                  | $θ$ is dependent on $d$ in a **parametric** sense                          |
| the **probability of $θ$** changes based on the observed value of $d$ | the **distribution of $θ$** is shaped or characterized by the value of $d$ |
| conditional probability where **$d$ is a random variable**            | $d$ is not a random variable but a **parameter or set of conditions**      |

??? question "What's the chain rule for conditonnal probabilities?"
    $f_{X,Y|Z}=f_{X|Y,Z}f_{Y|Z}$

??? question "$Y=f(X)$, what is  $p_{Y}$ as a function of $p_{X}$?"
    $p_{Y}(y)=p_{X}(f^{-1}(y))|\frac{df^{-1}}{dy}|$

??? question "Distribution of RV product exercice"
    === "Question"
        Find $p_Z$ with $X,Y \sim \mathcal{U}(0,1)$ and $Z=XY$
    === "Answer"
        $p_Z = -log(z)$

??? question "What's the principle behind MCMC sampling"
    It's based on iteratively sampling from a Markov chain whose stationary distribution is the target distribution, which in the case of Bayesian computation is most often the posterior distribution $p(θ|y)$

??? question "List 3 example of conjugate distributions "
    | Prior                   | Likelihood                   | Posterior                         |
    | ----------------------- | ---------------------------- | --------------------------------- |
    | Normal (μ₀, σ₀²)        | Normal (x̄, σ²/n)             | Normal (μₙ, σₙ²)                  |
    | Beta (α, β)             | Binomial (n, p)              | Beta (α + x, β + n - x)           |
    | Gamma (α, β)            | Poisson (λ)                  | Gamma (α + x, β + 1/n)            |
    | Gamma (α, β)            | Exponential (λ)              | Gamma (α + n, β + Σxᵢ)            |
    | Dirichlet (α₁, ..., αₖ) | Multinomial (n, p₁, ..., pₖ) | Dirichlet (α₁ + x₁, ..., αₖ + xₖ) |
    | Inverse-Gamma (α, β)    | Gamma (k, θ)                 | Inverse-Gamma (α + n, β + Σxᵢ)    |

??? question "How do you find which conjugate distribution to use?"
    - Compute the likelihood from the data
    - Identify its distribution
    - Use the table to choose a conjugate distribution
