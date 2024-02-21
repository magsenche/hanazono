# Texture

## Catex
[catex repo](https://github.com/magsenche/catex)

Personal project based on neural cellular automata to generate and understand textures

## Resources
### Texture synthesis
[Wood texture generation](http://www.cs.cornell.edu/projects/wood/simulating_the_structure_and_texture_of_solid_wood.pdf)

### Neural texture synthesis

Texture Generation with Neural Cellular Automata:

- [Original paper](https://arxiv.org/pdf/2105.07299.pdf)
- [Distill post](https://distill.pub/selforg/2021/textures/)
- [Pytorch implementation](https://colab.research.google.com/github/google-research/self-organising-systems/blob/master/notebooks/texture_nca_pytorch.ipynb)
- V2 with new texture loss:
  - vidéo: [Fixing Neural CA Colors with Sliced Optimal Transport ](https://www.youtube.com/watch?v=ZFYZFlY7lgI)
  - paper: [A Sliced Wasserstein Loss for Neural Texture Synthesis](https://arxiv.org/pdf/2006.07229.pdf)
    $\rightarrow$ Change style loss from gram matrix comparison to optimal transport
    - Random projection (high to low dim)
    - Optimal transport loss in this projected low dim space
    - Add a "tag" (mask) to avoid structural information loss $\simeq$ positional encoding

## Datasets
https://pytorch.org/vision/stable/generated/torchvision.datasets.DTD.html
