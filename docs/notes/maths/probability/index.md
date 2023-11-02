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

    Suitable for modeling distributions of real-valued data with a symmetric, bell-shaped curve.

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

### Chain rule
$f_{X,Y}=f_{X|Y}f_{Y}$

$f_{X,Y|Z}=f_{X|Y,Z}f_{Y|Z}$

## Notations
Often times, all the density and probability mass functions are denoted with the same letter (usually p) without any subscripts:

$$f_{θ|Y}(θ|y)= \frac{f_{Θ}(θ)f_{Y|Θ}(y|θ)}{f_{Y}(y)} \rightarrow \frac{p(θ)p(y|θ)}{p(y)} = p(θ|y)$$

| **$p(θ∣d)$**                                                          | **$p(θ;d)$**                                                               |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| $θ$ is dependent on $d$ in a **probabilistic** sense                  | $θ$ is dependent on $d$ in a **parametric** sense                          |
| the **probability of $θ$** changes based on the observed value of $d$ | the **distribution of $θ$** is shaped or characterized by the value of $d$ |
| conditional probability where **$d$ is a random variable**            | $d$ is not a random variable but a **parameter or set of conditions**      |

## Flashcards
??? question "What's the chain rule for conditonnal probabilities?"
    $f_{X,Y|Z}=f_{X|Y,Z}f_{Y|Z}$
