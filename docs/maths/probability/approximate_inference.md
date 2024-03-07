# Approximate inference
Used when the marginal likelihood is intractable which causes the posterior impossible to solve analytically. There are two kinds of methods:

1. **Simulation**: generate a random sample from the posterior distribution, and use its empirical distribution function as an approximation of the posterior.
2. **Distributional approximation**: approximate the posterior directly by some simpler parametric distribution, such as the normal distribution.

Some approximate algorithms have made inroads in cognitive science and neuroscience

## Variational Bayesian
Variational inference finds best approximation $Q(\theta)$ of the true posterior $P(\theta|D)$

$\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$

??? question "What is the purpose of Variational Inference"
    To find an approximation $Q(\theta)$ of the true posterior $P(\theta|D)$:
    $\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$

For complex probability distributions, belief propagation cannot work in a fully analytical fashion. In fact, the probability distribution of each unobserved variable given the observed variables may be arbitrarily complicated.

Variational Bayes uses the following trick: We approximate the probability distribution of $P(\theta|D)$ by a probability distribution $Q(\theta)$ that depends on a number of parameters $\theta$ . Subsequently, we optimize the parameters of $Q(\theta)$ so that $Q(\theta)$ becomes as similar as possible to the real probability distribution $P(\theta|D)$. Making them the same is not generally possible, so variational methods usually optimize an approximation, the so-called Evidence Lower Bound (ELBo)

$0 \leq D_{KL}[Q(\theta) \parallel P(\theta|D)] \Leftrightarrow 0 \leq - \mathbb{E}_{Q(\theta)}[log(\frac{P(\theta,D)}{Q(\theta)})] + log(P(D)) \Leftrightarrow \underbrace{\mathbb{E}_{Q(\theta)}[log(\frac{P(\theta,D)}{Q(\theta)})]}_{Elbo} \leq \underbrace{log(P(D))}_{evidence}$

`ELBo`
: Evidence Lower bound as $\underbrace{\mathbb{E}_{Q(\theta)}[log(\frac{P(\theta,D)}{Q(\theta)})]}_{Elbo} \leq \underbrace{log(P(D))}_{evidence}$

## Metropolis-Hastings
The Metropolis-Hastings algorithm is a Markov chain Monte Carlo (MCMC) method used for generating samples from a probability distribution, especially when direct sampling is difficult.

Suppose we want to sample from a target distribution $\pi(x)$ but can only compute a function $f(x)$ proportional to it, such that $\pi(x) \propto f(x)$.

The algorithm iterates as follows:

1. **Initialization**: Start with an initial state $x_0$.
2. **Proposal Distribution**: Propose a candidate state $y$ from a proposal distribution $q(x|y)$.
3. **Acceptance Probability**: Calculate the acceptance probability $\alpha(x, y) = \min\left(1, \frac{\pi(y)q(x|y)}{\pi(x)q(y|x)}\right)$
4. **Accept/Reject Step**: Generate a uniform random number $u$ between 0 and 1. If $u \leq \alpha(x, y)$, accept the proposed state $y$; otherwise, keep the current state $x$.
5. **Update**: Set $x$ to the accepted/rejected state and repeat steps 2-4 for a specified number of iterations.

??? question "What are the different steps of Metropolis-Hastings algorithm"
    1. **Initialization**: Start with an initial state $x_0$.
    2. **Proposal Distribution**: Propose a candidate state $y$ from a proposal distribution $q(x|y)$.
    3. **Acceptance Probability**: Calculate the acceptance probability $\alpha(x, y) = \min\left(1, \frac{\pi(y)q(x|y)}{\pi(x)q(y|x)}\right)$
    4. **Accept/Reject Step**: Generate a uniform random number $u$ between 0 and 1. If $u \leq \alpha(x, y)$, accept the proposed state $y$; otherwise, keep the current state $x$.
    5. **Update**: Set $x$ to the accepted/rejected state and repeat steps 2-4 for a specified number of iterations.

The samples obtained after a sufficient number of iterations approximate the target distribution $\pi(x)$.

This method allows exploration of the target distribution even when direct sampling is challenging, as it uses a proposal distribution to explore the space and probabilistically accepts or rejects proposed moves based on the acceptance probability formula.

??? question "What is the main advantage of using Markov Chain Monte Carlo (MCMC) over other sampling methods?"
    One main advantage of MCMC is that it allows for efficient sampling from complex distributions, such as those with multiple modes or heavy tails. This is because MCMC samples are generated iteratively, allowing for a more targeted exploration of the parameter space compared to traditional random sampling methods. Additionally, MCMC can handle high-dimensional data and correlation between variables more effectively than some other methods.

## Belief propagation
In this class of algorithms, we start with some variables, propagate messages through the system, and apply potential corrections. We often assume that the relevant variables have distributions for which the integrals can be analytically solved or approximated. We also assume that the relations between variables are such that they can be described as a (generally) sparse graph. In certain kinds of graphs, belief propagation provides an efficient way of solving many Bayesian problems. Sometimes it is approximately correct even when the assumptions are not satisfied.

## Other optimization algorithms for intractable models

- **Expectation maximization** ([EM](https://stats.stackexchange.com/a/524802)) iteratively searches MLE/MAP given data

??? question "Name at least 3 algorithm to determine parameters of intractable models"
    - Expectation maximization iteratively searches MLE/MAP given data
    - Variational inference  finds best
    approximation
    $Q(\theta)$ of the true posterior $P(\theta|D)$: $\hat{Q}(\theta)=argmin_{Q(\theta)}D_{KL}[Q(\theta) \parallel P(\theta|D)]$
    - Metropolis-Hastings

## Resources

- [Variational Inference](https://gregorygundersen.com/blog/2021/04/16/variational-inference/)
- [Why Metropolis-Hastings works](https://gregorygundersen.com/blog/2019/11/02/metropolis-hastings/)
