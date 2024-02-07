# Tensor computation libraries

## List

- [Thread twitter](https://twitter.com/kimbochen/status/1426941414433193986)
- [From PyTorch to JAX: towards neural net frameworks that purify stateful code](https://sjmielke.com/jax-purify.htm)
- [What I Wish Someone Had Told Me About Tensor Computation Libraries](https://www.georgeho.org/tensor-computation-libraries/)
- [Jax overview](http://alexminnaar.com/2020/08/15/jax-overview.html)
- [Torch Autograd mechanics](https://pytorch.org/docs/stable/notes/autograd.html)
- [Understanding Computational Graphs in PyTorch](https://jdhao.github.io/2017/11/12/pytorch-computation-graph/)
- [Slides about automatic differentiation](https://www.cs.toronto.edu/~rgrosse/courses/csc321_2018/slides/lec10.pdf)

## What they do ?

1. define and build computational graphs
2. use computational graphs (such as autodifferentation used to compute gradients)
3. operate directly on the computation graph (e.g. for mathematical simplification)
4. optimize the computation

## How do they differ ?

1. static vs dynamics graphs: define-and-run vs define-by-run
2. lazy vs eager execution: variables evaluated when defined or when needed
3. usage: autodifferentiaion
4. code execution and compilation

## Flashcards