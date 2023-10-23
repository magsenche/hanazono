# Baysian Inference

## Definitions

`maximum likelihood estimator`
: $\hat{\theta}_{MLE}=argmax_{\theta}{P(D|\theta)}$

`maximum a posteriori`
: $\hat{\theta}_{MAP}=argmax_{\theta}{P(\theta|D)} = argmax_{\theta}{P(D|\theta)P(\theta)}$

Both **MLE** and **MAP** are single point estimators of parameters of statistical models

- **MLE**: $\hat{\theta}$ maximizing likelihood ${P(D|\theta)}$. $\theta$ is a fixed value.
- **MAP**: $\hat{\theta}$ maximizing posterior probability ${P(\theta|D)}$. $\theta$ is a random variable.
- **Baysian inference**: the whole probability density mass function $p$

## Properties

1. With an uniform (no) prior, $\hat{\theta}_{MLE} = \hat{\theta}_{MAP}$
2. Use [conjugate distributions](https://vioshyvo.github.io/Bayesian_inference/conjugate-distributions.html) to be sure
posterior is the same family as the prior
3. Two distributions with the same mode/max cannot be differenciated by MLE or MAP
4. No need for evidence/marginal lieklihood $P(D)$ for optimization (same $argmax$)

## Optimization algorithms for intractable models

- **Expectation maximization** ([EM](https://stats.stackexchange.com/a/524802)) iteratively searches MLE/MAP given data
- **Variational inference** ([VI](https://gregorygundersen.com/blog/2021/04/16/variational-inference/)) finds best
approximation $Q(\theta)$ of the true posterior $P(\theta|D)$:
$\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$
- **Sampling methods**
- **Markov Chain Monte Carlo** ([MCMC])
- **Metropolis-Hastings** ([MH])

## Flashcards
??? question "Maximum likelihood estimator"
    $\hat{\theta}_{MLE}=argmax_{\theta}{P(D|\theta)}$

??? question "Maximum a posteriori"
    $\hat{\theta}_{MAP}=argmax_{\theta}{P(\theta|D)} = argmax_{\theta}{P(D|\theta)P(\theta)}$

??? question "When does $\hat{\theta}_{MLE} = \hat{\theta}_{MAP}$ ?"
    With an uniform or no prior

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
