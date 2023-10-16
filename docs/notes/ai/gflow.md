## GFlowNets

[Gflownets foundations](https://arxiv.org/pdf/2111.09266.pdf)

[Prof. YOSHUA BENGIO - GFlowNets, Consciousness & Causality](https://www.youtube.com/watch?v=M49TMqK5uCE)

> For Yoshua Bengio, GFlowNets are the most exciting thing on the horizon of Machine Learning today. He believes they can solve previously intractable problems and hold the key to unlocking machine abstract reasoning itself. This discussion explores the promise of GFlowNets and the personal journey Prof. Bengio traveled to reach them.


In active learning, the model can economicaly ask an oracle (eg the world) the most interesting samples to learn. How to approximate the oracle effectively ? Should use uncertainty, entropy etc..

An idea is machine teaching, where human give the most informative samples to the model.

A method to estimate posterior distribution or unormalized probability distribution/energy function is to use [markov chain monte carlo sampling](../maths/markov.md)

Issues are that at high dimension, it exponentially complicated to do that. But we can break this expoentiality with machine learning, this is why Bengio calls systematic generalization: generalize far from the data in a meaningful way.

Gflownet analogy with parametrized "planche a clou" which approximate the desired reward function.

Gflownet can be used no only for sampling, but also estimate (any ?) distribution

Abstraction gives power of generalization. It lacks in current AI. Discrete concepts emerge as a way to provide good generalization

Abstract causal dependences are what are conserved accross scenarios eg if I go to the moon, same laws of physics.

??? question "What are GFlowNets for? [](){.fbutton .ok}[](){.fbutton .nok}"
    To generalize and abstract information in high-dimensional spaces
    ##### id: af46fe, box: 1, score: 0/2, next: 16/10/2023, last: 16/10/2023

??? question "In active learning scenarios with GFlowNets, what is the objective? [](){.fbutton .ok}[](){.fbutton .nok}"
    To economically determine the most informative samples for the model to learn from
    ##### id: ef995a, box: 1, score: 0/0, next: 09/10/2023, last: 09/10/2023