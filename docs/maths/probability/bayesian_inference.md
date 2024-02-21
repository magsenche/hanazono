# Bayesian inference
Bayesian inference is closely tied to the notion of *optimal* behavior. This serves as a motivation for building [Bayesian models](./bayesian_modeling.md)

When building any kinds of models, there are three options to handle hyperparameters:

1. fix them to constant values
2. use a point estimates estimated from the data
3. set a probability distribution over them

When doing bayesian modeling, we often choose the third option

## Likelihood
It captures th informaition content of the (sensory) observation relevant to distinguish a world state from another. In other words, it contains all information about the variable that can objectively be obtained from the measurement.

It's a **function** of the world state/hypothesis/parameter, not a distribution ($\sum \neq 1$)

Depending on how $f_{Y|\Theta}$ is seen:

- $\theta \mapsto f_{Y|\Theta}(\theta;y)$ likelihood function
- $y \mapsto f_{Y|\Theta}(y;\theta)$ sampling distribution

## Prior distribution
It summarizes the information content of our past observations; our background knwoledge.

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

Can be summarized using the Bayesian confidence interval $I_{\alpha}$, $P(\Theta \in I_{\alpha})|Y=y) = 1-\alpha$

### Posterior predictive distribution
The predictive distribution $f_{\tilde{Y}|Y}(\tilde{y}|y)$ of the new observations $\tilde{Y}$ given the data $Y$ we just derived. It's used to predict new observations based on previous ones

Computed using $f_{\tilde{Y}|Y}(\tilde{y}|y) = \int_{\Omega}f_{\tilde{Y}|\Theta}(\tilde{y}|\theta)f_{\Theta|Y}(\theta|y)d\theta=E_{f_{\Theta|Y}}[f_{\tilde{Y}|\Theta}(\tilde{y}|\theta)|Y=y]$

### Marginal posterior distribution
$p(\theta_{1}|y) = \int p(\theta|y)d\theta_{2}$ where $\theta=(\theta_{1},\theta_{2})$

It's used when the parameter vector $\theta$ has two compenents and we are only interested about one of them, e.g $\theta_{1}$. In this case, $\theta_{2}$ is called a **nuisance parameter**

### Conditional posterior distribution
In the previous example we can also write, $p(\theta|y)=p(\theta_{1},\theta_{2}|y)=p(\theta_{1}|\theta_{2},y)p(\theta_{2}|y)$
where $p(\theta_{1}|\theta_{2},y)$ is called **conditional posterior distribution**

## Marginal likelihood
The normalizing constant $f_{Y}(y)$ of the Bayes’ theorem

Computed by marginalizing out the parameter from the full joint probability distribution, which can be hard or even impossible

$f_{Y}(y) = \int_{\Omega}f_{\Theta,Y}(\theta,y)d\theta \underset{Bayes}{=} \int_{\Omega}f_{Y|\Theta}(y|\theta)f_{\Theta}(\theta)d\theta$

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
- **Bayesian inference**: the whole probability density mass function $p$
- Bayes estimator **minimizes the expected squared error**

### Properties

1. With an uniform (no) prior, $\hat{\theta}_{MLE} = \hat{\theta}_{MAP}$
2. Use [conjugate distributions](https://vioshyvo.github.io/Bayesian_inference/conjugate-distributions.html) to be sur posterior is the same family as the prior
3. Two distributions with the same mode/max cannot be differenciated by MLE or MAP
4. No need for evidence/marginal lieklihood $P(y)$ for optimization (same $argmax$)

### Bias
`bias`
: $Bias[\theta|\hat{\theta}] = \mathbb{E}[\hat{\theta}|\theta]-\theta$

`bias-variance decomposition of MSE`
: $MSE[\hat{\theta}|\theta]=Bias[\hat{\theta}|\theta]^2+\mathbb{V}[\hat{\theta}|\theta]$

## Decision making
`Expected utility`
: $EU(a,x)=\mathbb{E}_{s|x}[U(s,a)]=\int_s U(s,a)p(s|x)ds$

In the simplest form, an agent will perform $a = argmax_aEU(a,x)$

The specification of a cost (or utility) function for real-life decision problems is a difficult task, although there are multiple obvious ingredients of the cost function.

Correct computation of the Bayesian posterior is the essence of optimal decision-making.
### 0-1 Utility
Leads to MAP estimate

### Quadtratic utility
Leads to posterior mean estimate

### Absolute error
Leads to median estimate

## Resources
- [Bayesian inference](https://vioshyvo.github.io/Bayesian_inference/index.html)
- [Bayesian Model for perception and action](https://www.cns.nyu.edu/malab/static/files/Bayesian_models_of_perception_and_action_v3.pdf)

??? question "In which case is it impossible to differentiate two distributions using $\hat{\theta}_{MLE}$ or $\hat{\theta}_{MAP}$"
    Two distributions with the same mode/max cannot be differenciated by MLE or MAP

??? question "What are the properties of using conjugate distributions in Bayesian inference?"
    When using conjugate distributions, the posterior distribution has the same family as the prior distribution. This makes it easier to compute the posterior distribution and can make optimization algorithms such as Expectation Maximization (EM) or Variational Inference more efficient.

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

??? question "Traduit posterior, likelihood et prior en français"
    Plausibilité, Vraisemblance, Crédence
