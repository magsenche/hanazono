# Probabilistic Graphical Models

Probabilistic model for which a graph expresses the conditional dependence structure between random variables.

Class of statistical models that represent the relationships between variables in a system as a graph.

Used to model systems in which the variables are interdependent, and the relationships between the variables are represented by edges in the graph.

## Example

``` mermaid
graph LR;
    A[a] --> P[uniform];
    B[b] --> P;
    P[Uniform] --> Q[Normal];
    K[k] --> Q;
    Q --> R[Exponential];
    P --> S[Binomial];
    R --> S;
    S --> T[Poisson];
```

- $Uniform(a,b)$
- $Normal(\mu=\frac{a+b}{2},\sigma^2=\frac{(b-a)^2}{k})$
- $Exponential(\lambda =\frac{1}{\sigma})$
- $Binomial(n=\lceil{b-a}\rceil,p=min(1,\lambda))$
- $Poisson(\lambda=p\times n)$

## Ressources

- [CS 228 - Probabilistic Graphical Models](https://ermongroup.github.io/cs228-notes/)

## Flashcards

??? question "What is a probabilistic graphical model?"
    A probabilistic graphical model is a statistical model that uses a graph to represent the conditional dependence structure between random variables. It is used to model systems where the variables are interdependent and the relationships between them are represented by edges in the graph.

??? question "Identify the following graphical model"
    === "Question"
        - $Uniform(a,b)$
        - $Normal(\mu=\frac{a+b}{2},\sigma^2=\frac{(b-a)^2}{k})$
        - $Exponential(\lambda =\frac{1}{\sigma})$
        - $Binomial(n=\lceil{b-a}\rceil,p=min(1,\lambda))$
        - $Poisson(\lambda=p\times n)$
    === "Answer"
        ``` mermaid
        graph LR;
            A[a] --> P[uniform];
            B[b] --> P;
            P[Uniform] --> Q[Normal];
            K[k] --> Q;
            Q --> R[Exponential];
            P --> S[Binomial];
            R --> S;
            S --> T[Poisson];
        ```