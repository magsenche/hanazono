# JEPA

JEPA is an architecture for autonomous intelligence proposed by Yann LeCun that aims to learn models of the world in a self-supervised manner. It consists of several modules. The goal of JEPA is to enable humans to plan effectively in unfamiliar situations by predicting what's likely, plausible, impossible.

## Architecture

[Yann LeCun on a vision to make AI systems learn and reason like animals and humans](https://ai.facebook.com/blog/yann-lecun-advances-in-ai-research/)

Accumulated knowledge from prior experience build what we call common sense, which constitutes background knowledge of how the world works.
Allow human to plan effectively in unfamiliar situations by predicting what's likely, plausible, impossible..

??? question "What is the role of accumulated knowledge from prior experience in JEPA?"
    It builds what we call common sense, which constitutes background knowledge of how the world works. This knowledge enables humans to plan effectively in unfamiliar situations by predicting what's likely, plausible, or impossible

Main challenges in AI is to find out how to learn these models in a self-supervised fashion, by changing current architectures and learning paradigms.

![Architecture for autonomus intelligence](../fig/jepa_ylecun_archi.png)

- The configurator module performs executive control: Given a task to be executed, it preconfigures the other modules
- The perception module receives signals from sensors and estimates the current state of the world.
- The world model module constitutes the most complex piece of the architecture. Its role is twofold: (1) to estimate missing information about the state of the world not provided by perception, and (2) to predict plausible future states of the world.
- The cost module computes a single scalar output that predicts the level of discomfort of the agent. It is composed of two submodules: the intrinsic cost, which is hard-wired and immutable (not trainable), and computes the immediate discomfort, and the critic, which is a trainable module that predicts future values of the intrinsic cost.
- The actor module computes proposals for action sequences.
- The short-term memory module keeps track of the current and predicted world state, as well as associated costs.

??? question "List all 6 modules in the JEPA architecture and their roles"
    - The configurator module performs executive control: Given a task to be executed, it preconfigures the other modules
    - The perception module receives signals from sensors and estimates the current state of the world.
    - The world model module constitutes the most complex piece of the architecture. Its role is twofold: (1) to estimate missing information about the state of the world not provided by perception, and (2) to predict plausible future states of the world.
    - The cost module computes a single scalar output that predicts the level of discomfort of the agent. It is composed of two submodules: the intrinsic cost, which is hard-wired and immutable (not trainable), and computes the immediate discomfort, and the critic, which is a trainable module that predicts future values of the intrinsic cost.
    - The actor module computes proposals for action sequences.
    - The short-term memory module keeps track of the current and predicted world state, as well as associated costs.

Yann LeCun promotes Hierarchical JEPA (Joint Embedding Predictive Architecture)

To learn world models in an unsupervised fashion, recently we've been using contrastive methods a lot (which implies showing a lot of incompatibles samples to discrimate positive sample from - and this is not bioplausible). New methods live VICReg / JEPA:

- max MI(x)
- max MI(y)
- max p(y|x)
- min I(z) where z is the latent rpz of x

[Yann LeCun has a bold new vision for the future of AI](https://www.technologyreview.com/2022/06/24/1054817/yann-lecun-bold-new-vision-future-ai-deep-learning-meta/)

??? question "JEPA: What unsupervised method does Yann LeCun advocate for learning world models"
    Yann LeCun promotes Hierarchical JEPA (Joint Embedding Predictive Architecture) and suggests learning world models using contrastive methods, with new methods like VICReg/JEPA that focus on maximizing mutual information and minimizing the latent representation

## I-JEPA

[I-JEPA: The first AI model based on Yann LeCun’s vision for more human-like AI](https://ai.facebook.com/blog/yann-lecun-ai-model-i-jepa/)