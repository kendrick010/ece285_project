# ECE 285 Project

> [!NOTE]  
> 5-minute Demo Video: https://youtu.be/xO4jU_GmQsQ

## Abstract

Masked Autoencoders (MAEs) are a self-supervised learning framework introduced by He et al. (2021), known for their ability to learn meaningful representations by reconstructing masked portions of input images. Although MAEs have shown strong performance on large multi-class image sets, their effectiveness in more specialized visual domains remains underexplored. This project aims to replicate the MAE architecture and train it on a visual art dataset to investigate whether MAEs can generalize to niche domains, such as artistic imagery and representation.

## Environment

This project was ran both on Datahub (UCSD) and locally. To install and run this project locally, we recommend setting up a conda environment.

```
conda env create -f environment.yml
conda activate ECE285_PROJECT
```

## Dataset

We will be using the [Wiki-Art : Visual Art Encyclopedia](https://www.kaggle.com/datasets/ipythonx/wikiart-gangogh-creating-art-gan) Dataset sourced by Innat on Kaggle. This dataset is composed of 96,014 art gallery images ranging from abstract to landscape themes sourced from [WikiArt.org](WikiArt.org) and the [GANGogh Training Dataset](https://academictorrents.com/details/1d154cde2fab9ec8039becd03d9bb877614d351b).

## Getting Started

Dowload the [Wiki-Art : Visual Art Encyclopedia](https://www.kaggle.com/datasets/ipythonx/wikiart-gangogh-creating-art-gan) Dataset and store it in the `/data` directory.

Configure the global variables in the `ECE285_Project.ipynb` notebook and run.
