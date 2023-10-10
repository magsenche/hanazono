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
??? question "Maximum likelihood estimator [](){.fbutton .ok}[](){.fbutton .nok}"
    $\hat{\theta}_{MLE}=argmax_{\theta}{P(D|\theta)}$
    ##### id: d37e63, box: 2, score: 3/5, next: 12/10/2023, last: 11/10/2023

??? question "Maximum a posteriori [](){.fbutton .ok}[](){.fbutton .nok}"
    $\hat{\theta}_{MAP}=argmax_{\theta}{P(\theta|D)} = argmax_{\theta}{P(D|\theta)P(\theta)}$
    ##### id: e8b6b6, box: 2, score: 1/2, next: 13/10/2023, last: 12/10/2023

??? question "When does $\hat{\theta}_{MLE} = \hat{\theta}_{MAP}$ ? [](){.fbutton .ok}[](){.fbutton .nok}"
    With an uniform or no prior
    ##### id: 3fe433, box: 1, score: 0/1, next: 11/10/2023, last: 11/10/2023

??? question "Describe the Expectation-Maximization algorithm to fit a Gaussian mixture Model? [](){.fbutton .ok}[](){.fbutton .nok}"

    1. **Initialization:**
          - Initialize means, covariances, and weights randomly.
          - Set the maximum number of iterations and convergence threshold.
    2. **Iteration:**
          - Repeat the following steps until convergence or until the maximum number of iterations is reached.
    3. **Expectation Step (E-step):**
          - For each data point:
            - Calculate the probability that it belongs to each Gaussian component.
            - Update the responsibilities based on these probabilities.
    4. **Maximization Step (M-step):**
          - For each Gaussian component:
            - Update the weight based on the sum of responsibilities.
            - Update the mean based on weighted data points.
            - Update the covariance based on weighted data point deviations from the mean.
    5. **Convergence Check:**
          - Measure the change in parameters from the previous iteration.
          - If the change is below the convergence threshold, stop iterating.
    6. **Result:**
          - Return the final parameters: means, covariances, and weights.

    ##### id: 7dc4ef, box: 1, score: 0/0, next: 27/09/2023, last: 27/09/2023

??? question "In which case is it impossible to differentiate two distributions using $\hat{\theta}_{MLE}$ or $\hat{\theta}_{MAP}$ [](){.fbutton .ok}[](){.fbutton .nok}"
    Two distributions with the same mode/max cannot be differenciated by MLE or MAP
    ##### id: 7c6972, box: 1, score: 0/0, next: 27/09/2023, last: 27/09/2023

??? question "Name at least 3 algorithm to determine parameters of intractable models [](){.fbutton .ok}[](){.fbutton .nok}"
    - Expectation maximization iteratively searches MLE/MAP given data
    - Variational inference  finds best
    approximation
    $Q(\theta)$ of the true posterior $P(\theta|D)$: $\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$
    - Sampling methods
    - Markov Chain Monte Carlo
    - Metropolis-Hastings

    ##### id: a21379, box: 1, score: 0/1, next: 12/10/2023, last: 12/10/2023

??? question "What is the purpose of Variational Inference [](){.fbutton .ok}[](){.fbutton .nok}"
    To find an approximation $Q(\theta)$ of the true posterior $P(\theta|D)$:

    $$\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$$
    ##### id: ea2055, box: 1, score: 0/0, next: 27/09/2023, last: 27/09/2023