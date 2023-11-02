# Baysian Inference

## Likelihood
In bayesian inference, the parameter is thought as a random variable. So the sampling distribution notation changes a bit to make sure it is a conditionnal probability distribution: $f(y,\theta) \rightarrow f_{Y|\Theta}(y;\theta)$

Depending on how $f_{Y|\Theta}(y;\theta)$ is seen:

- $y \mapsto f_{Y|\Theta}(y;\theta)$ sampling distribution
- $\theta \mapsto f_{Y|\Theta}(y;\theta)$ likelihood function

## Prior distribution
Its a marginal distribution $f_{\Theta}(\theta)$ of the parameter

It can also be seen as a parametric distribution $f_{\Theta|\Phi}(\theta|\phi)$ for the parameter ${\Theta}$ where $\phi$ are **hyperparameters**

### Uninformative
We should use as a vague priori distribution as possible, e.g. uniform distribution if:

- **no strong beliefs** about the possible values of the parameter
- results **not influenced by beliefs**

This can be quite subjective. Also, the posterior distribution famiy can also add some kind of belief to the results

### Informative

- let prior knowledge influence the posterior distribution
- make the solution more stable with the smaller sample sizes
- make the sampling from the posterior n more efficient (highly improbable regions of the parameter space not sampled from)
- can introduce restrictions (e.g. support of the posterior)

### Improper
When the prior function cannot be normalized to be a proper distribution, but the resulting posterior is valid:

- $p(\theta) \propto \theta^{-1}(1-\theta)^{-1}$ (Haldane’s prior, posterior ok as long as at least 1 success and 1 error)
- $p(\mu) \propto 1$ (normal distribution with $\sigma = \infin$)


## Bayesian model
$f_{\Theta,Y}(\theta,y)=f_{Y|\Theta}(y|\theta)f_{\Theta}(\theta)$

The full joint distribution is rarely computed or handled explicitly. Instead, the Bayesian inference is based on computing conditional and marginal densities from it.

## Posterior distribution
Conditional distribution of the parameter given the data $f_{\Theta|Y}(\theta|y)$. It's computed using Bayes' theorem

Can be summarized using the Baysian confidence interval $I_{\alpha}$, $P(\Theta \in I_{\alpha})|Y=y) = 1-\alpha$

### Posterior predictive distribution
The predictive distribution $f_{\tilde{Y}|Y}(\tilde{y}|y)$ of the new observations $\tilde{Y}$ given the data $Y$ we just derived. It's used to predict new observations based on previous ones

Computed using $f_{\tilde{Y}|Y}(\tilde{y}|y) = \int_{\Omega}f_{\tilde{Y}|\Theta}(\tilde{y}|\theta)f_{\Theta|Y}(\theta|y)d\theta=E_{f_{\Theta|Y}}[f_{\tilde{Y}|\Theta}(\tilde{y}|\theta)|Y=y]$

## Marginal likelihood
The normalizing constant $f_{Y}(y)$ of the Bayes’ theorem

Computed by marginalizing out the parameter from the full joint probability distribution, which can be hard or even impossible

$f_{Y}(y) = \int_{\Omega}f_{\Theta,Y}(\theta,y)d\theta \underset{Bayes}{=} \int_{\Omega}f_{Y|\Theta}(y|\theta)f_{\Theta}(\theta)d\theta$

## Conjugate distributions
| Prior                   | Likelihood                   | Posterior                         |
| ----------------------- | ---------------------------- | --------------------------------- |
| Normal (μ₀, σ₀²)        | Normal (x̄, σ²/n)             | Normal (μₙ, σₙ²)                  |
| Beta (α, β)             | Binomial (n, p)              | Beta (α + x, β + n - x)           |
| Gamma (α, β)            | Poisson (λ)                  | Gamma (α + x, β + 1/n)            |
| Gamma (α, β)            | Exponential (λ)              | Gamma (α + n, β + Σxᵢ)            |
| Dirichlet (α₁, ..., αₖ) | Multinomial (n, p₁, ..., pₖ) | Dirichlet (α₁ + x₁, ..., αₖ + xₖ) |
| Inverse-Gamma (α, β)    | Gamma (k, θ)                 | Inverse-Gamma (α + n, β + Σxᵢ)    |

## Estimators
`maximum likelihood estimator`
: $\hat{\theta}_{MLE}=argmax_{\theta}{P(y|\theta)}$

`maximum a posteriori`
: $\hat{\theta}_{MAP}=argmax_{\theta}{P(\theta|Y)} \underset{Bayes}{=} argmax_{\theta}{P(Y|\theta)P(\theta)}$

`bayes estimator`
: $\hat{\theta}_{Bayes} := E[\theta|Y]$

Both **MLE** and **MAP** are single point estimators of parameters of statistical models

- **MLE**: $\hat{\theta}$ maximizing likelihood ${P(y|\theta)}$. $\theta$ is a fixed value.
- **MAP**: $\hat{\theta}$ maximizing posterior probability ${P(\theta|y)}$. $\theta$ is a random variable.
- **Baysian inference**: the whole probability density mass function $p$

### Properties

1. With an uniform (no) prior, $\hat{\theta}_{MLE} = \hat{\theta}_{MAP}$
2. Use [conjugate distributions](https://vioshyvo.github.io/Bayesian_inference/conjugate-distributions.html) to be sur posterior is the same family as the prior
3. Two distributions with the same mode/max cannot be differenciated by MLE or MAP
4. No need for evidence/marginal lieklihood $P(y)$ for optimization (same $argmax$)

## Approximate inference
Used when the marginal likelihood is intractable which causes the posterior impossible to solve analytically. There are two kinds of methods:

1. **Simulation**: generate a random sample from the posterior distribution, and use its empirical distribution function as an approximation of the posterior.
2. **Distributional approximation**: approximate the posterior directly by some simpler parametric distribution, such as the normal distribution.

### Optimization algorithms for intractable models

- **Expectation maximization** ([EM](https://stats.stackexchange.com/a/524802)) iteratively searches MLE/MAP given data
- **Variational inference** ([VI](https://gregorygundersen.com/blog/2021/04/16/variational-inference/)) finds best
approximation $Q(\theta)$ of the true posterior $P(\theta|D)$:
$\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$
- **Sampling methods**
- **Markov Chain Monte Carlo**
- **Metropolis-Hastings**

## Ressources

- [Baysian inference](https://vioshyvo.github.io/Bayesian_inference/index.html)
- [Baysian Model for perception and action](https://www.cns.nyu.edu/malab/static/files/Bayesian_models_of_perception_and_action_v3.pdf)

## Flashcards
??? question "In which case is it impossible to differentiate two distributions using $\hat{\theta}_{MLE}$ or $\hat{\theta}_{MAP}$"
    Two distributions with the same mode/max cannot be differenciated by MLE or MAP

??? question "Name at least 3 algorithm to determine parameters of intractable models"
    - Expectation maximization iteratively searches MLE/MAP given data
    - Variational inference  finds best
    approximation
    $Q(\theta)$ of the true posterior $P(\theta|D)$: $\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$
    - Sampling methods
    - Markov Chain Monte Carlo
    - Metropolis-Hastings

??? question "What is the purpose of Variational Inference"
    To find an approximation $Q(\theta)$ of the true posterior $P(\theta|D)$:
    $\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$

??? question "What are the properties of using conjugate distributions in Bayesian inference?"
    When using conjugate distributions, the posterior distribution has the same family as the prior distribution. This makes it easier to compute the posterior distribution and can make optimization algorithms such as Expectation Maximization (EM) or Variational Inference more efficient.

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

??? question "Thumbstack tossing exercice"
    === "Question"
        Assume we have tossed a thumbtack $n=30$ times, and observed that it has landed point up $y=16$ times.

        What is the predictive distribution for the number of successes, if we throw the same thumbtack $m=10$ more times?
    === "Answer"
        $\hat{Y}|Y \sim BêtaBin(m,y+1,n-y+1)$

        [Full correction](https://vioshyvo.github.io/Bayesian_inference/index.html#prediction-example)

??? question "Explain what are the different types of priors"
    - Informative
    - Uninformative
    - Improper
