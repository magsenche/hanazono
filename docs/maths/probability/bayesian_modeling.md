# Bayesian modeling
Bayesian models of perception and action are functional, not causal-mechanistic explanations, in the sense that they do not specify the neural parts and neural operations that implement the Bayesian computation.

## A recipe

1. ### Generative Model
It represents the statistical structure of the world and observations. Mathematicaly, it specifices the probability distributions of all variables in the problem.
    1. **Graph**
        2. Draw a diagram (or PGM) where each node is a variable and each arrow a dependency.
        3. Observations/measurements are at the bottom.
    2. **Equations**
        1. For each variable, write an equation for its probability distribution.
        2. For each observation, assume a noise model. For others, get the distribution from the experimental design or from natural statistics. If there are incoming arrows, the distribution is a conditional one.

2. ### Bayesian inference
Given a particular observation, how should the observer's beliefs about the state of the world be updated? It conclude by specifying how the observer reaches a decision.
    1. **Compute the posterior over the world state of interest given observations**
        The optimal observer does this using the distributions in the generative model. Alternatively, the observer might assume different distributions (e.g.,wrong beliefs). Marginalize (average) over variables other than the observations and the world state of interest.
    2. **Specify the read-out of the posterior (decision rule)**
        1. Assume a utility function
        2. Maximize expected utility under the posterior. (Alternative: sample from the posterior.)
        3. Result: decision rule (mapping from observations to decision). When utility is accuracy, the read-out is to maximize the posterior (MAP decision rule).

3. ### Response probabilities
The response distribution $p(\hat{s}|s)$ is the distribution of the stimulus estimate given the true stimulus. It's different from the posterior distribution $p(s|x)$. For every unique trial in the experiment, compute the probability of the observer making each possible decision given the stimuli on that trial. To do so, use the distribution of the observations given the stimuli (from Step 1) and the decision rule (from Step 2).
    - Good method: Sample observations according to Step 1; for each, apply decision rule; tabulate responses.
    - Better: Integrate numerically over observations.
    - Best (when possible): Integrate analytically over observations.
    - Optional: Add response noise or lapses.

    Note that belief and response distributions are not the same. This can be seen throught their variances $Var(belief)$ is the variability of behavior as measured by the experimenter and $Var(response distribution)$ is the uncertainty of the observer on a given trial

4. ### Model fitting and model comparison
    1. **Compute the parameter log likelihood**
    2. **Maximize the parameter log likelihood**
    3. **Obtain fits to summary statistics** by rereuning the fitted model
    4. **Formulate alternative models**
    5. **Model comparison** using summary statistics
    6. **Evaluate absolute goodness of fit**

??? question "List all steps of bayesian modeling"
    1. Generative Model
        - Graph
        - Equations
    2. Bayesian inference (decision rule)
        - Comptute the posterior
        - Specify the read-out of the posterior
    3. Response probabilities
    4. Model fitting and model comparison
        - Compute the parameter log likelihood
        - Maximize the parameter log likelihood
        - Obtain fits to summary statistics
        - Formulate alternative models
        - Model comparison
        - Evaluate absolute goodness of fit

## Noise, Uncertainty, Variability
- **Noise** to the process by which the observations are generated, it's **trial-to-trial variability**.
- **Uncertainty** reflects the **observer's knowledge** about variables in the world. It's subjective and noise can be a source of uncertainty.
- **Variability** encompasses **anything that varies from trial to trial**. Noise is a form of variablity, uncertainty is not.

## Bayesian Model Selection
Bayesian model selection is a method for choosing between different models based on their posterior probabilities. It naturally incorporates Occam's razor, favoring simpler models unless more complex models are substantially better at explaining the data.

### Bayes Factor
???+ question "What is the Bayes factor and how is it interpreted in Bayesian model selection?"
    The Bayes factor is the ratio of the marginal likelihoods of two models:

    $B_{12} = \frac{p(D|M_1)}{p(D|M_2)}$

    where $p(D|M_i)$ is the marginal likelihood of model $M_i$.

    Interpretation:

    - $B_{12} > 1$: Data supports $M_1$ over $M_2$
    - $B_{12} < 1$: Data supports $M_2$ over $M_1$

### Bayesian Information Criterion (BIC)
The BIC is an approximation to the log of the Bayes factor:

$BIC = -2 \ln(\hat{L}) + k \ln(n)$

where $\hat{L}$ is the maximum likelihood, $k$ is the number of parameters, and $n$ is the number of data points.

Lower BIC values indicate better models.

## Hierarchical Bayesian Models
Hierarchical Bayesian models involve multiple levels of parameters, allowing for more complex and realistic modeling of data.

???+ question "Structure of a Hierarchical Bayesian Model"
    1. Data level: $p(y|\theta)$
    2. Parameter level: $p(\theta|\phi)$
    3. Hyperparameter level: $p(\phi)$

    The joint posterior is given by:

    $p(\theta, \phi|y) \propto p(y|\theta) p(\theta|\phi) p(\phi)$

Advantages:

1. Can model complex dependencies in data
2. Allows for partial pooling of information across groups
3. Naturally handles uncertainty at multiple levels

Challenges:

1. Can be computationally intensive
2. Requires careful specification of priors
3. Interpretation can be more complex than simpler models

## Bayesian Confidence

### Estimate-based Bayesian confidence
Bayesian Confidence $\equalscolon F(p_{s|x}(\hat{s}|x_{obs})$
Based on $\hat{s}$, with $F$ monotonic

### Interval-based Bayesian confidance
Only for continuous reports of a wolrd state. It's some measure of dispertion of the posterior distribution, either as an interval of as the size of such interval.

## Some definitions

`measurement`
: Abstraction of the noisy internal representation of a stimulus, that live in the same space as the stimulus itself

`model mismatch`
: When the observer as an incorrect knowledge of the generative model because of wrong belief, learning difficulties, experiment world $\neq$ real world

## References
- [Bayesian Model for perception and action](https://www.cns.nyu.edu/malab/static/files/Bayesian_models_of_perception_and_action_v3.pdf)

??? question "Posterior mean estimate exercice"
    === "Question"
        An observer infers a stimulus s from a measurement $x_{obs}$. As in the chapter, the
        measurement distribution $p(x|s)$ is Gaussian with mean $s$ and variance $\sigma^2$. We use the prior $p(s) = e^{−λs}$

        1. Derive an equation for the posterior mean estimate.
        2. Derive an equation for the distribution of the posterior mean estimate for given s.
    === "Answer"
        1. $\hat{s}_{PM}=x_{obs}-\lambda \sigma^2$
        2. $\hat{s} \sim \mathcal{N}(s-\lambda \sigma^2,\sigma^2)$

??? question "Luggage carousel problem"
    === "Question"
        You are one of 100 passengers waiting for your bag at an airport luggage carousel. Your bag looks the same as 5% of all bags.

        1. Derive a general expression for the probability that the bag you are viewing (which matches your bag visually) is your own, as a function of the number of bags you have viewed so far.
        2. How many bags must you view (without finding your own) before the posterior probability that the bag you are viewing (which matches your own visually) is greater than 70%?
    === "Answer"
        1. $\frac{1}{0.95+0.05*(100-i)}$
        2. $i=91$
