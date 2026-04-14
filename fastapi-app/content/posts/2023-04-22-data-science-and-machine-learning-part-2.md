---
title: Data Science & Machine Learning - Part 2
description: crunching numbers in the cloud
tags: python sklearn tensor-flow kaggle google-colab
---

Last week I've completed the [Complete Machine Learning and Data Science: From Zero to Mastery](https://www.udemy.com/course/complete-machine-learning-and-data-science-zero-to-mastery/) course by [Andrei Neagoie](https://www.udemy.com/user/andrei-neagoie/) and [Daniel Bourke](https://www.udemy.com/user/daniel-bourke-52/) I was telling you about in part 1 of this Data Science (DS) & Machine Learning (ML) blog. I won't lie to you, it was quite the marathon. I went from DS and plotting charts in the first 10 miles straight to [scikit-learn](https://scikit-learn.org/stable/index.html) (sklearn) mid-race and then finished with a sprint through the world of [TensorFlow](https://www.tensorflow.org/) (TF).  sklearn is... I think the official description summarizes it spot on:

>`Scikit-learn` is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection, model evaluation, and many other utilities.

TL;DR (Too **long;** didn't read) it's an impressive library addressed to everyone that's serious about ML. It can do so much for you at each and every step involved in ML that you basically cannot do without it. At first it was overwhelming, but day by day I began to appreciate this library's utility and extensive documentation. [Daniel Bourke](https://www.udemy.com/user/daniel-bourke-52/) did his best to cover sklearn in the Massive Online Open Course (MOOC) I mentioned in the beggining. He did a great job to send me in the right direction. I even got to use what he taught me and submitted my first two competition entries on [Kaggle](https://www.kaggle.com). They're both tutorial competitions and award no prizes, but they've provided me with a sandbox in which to apply my recently acquired knowledge. My confidence went up and so did my motivation to learn more about this domain.

The other topic I mentioned was TF, one of the most popular ML and Deep Learning (DL) libraries to date. Alongside sklearn and PyTorch, they are at the forefront. If sklearn is focused on general ML, TF and PyTorch are better suited for DL, a subcategory of ML. TF was developed by Google, while PyTorch is the child of Meta's AI Research lab. They are both cutting-edge ML learning applications. According to popular opinion, PyTorch is more `pythonic`, easier to grasp for a Python developer, while TF can prove a tougher egg to crack. I decided to learn both, starting with PyTorch. Moreover, [ZTM Academy](https://zerotomastery.io/) has MOOCs for both these libraries and they are both part of their [Become a Machine Learning Engineer](https://zerotomastery.io/career-paths/become-a-machine-learning-engineer/) career path. Even better, the DS & ML course I just completed is part of this same path and preceeds PyTorch, followed by TF. Guess I've done something right, right?

While touching on these amazing libraries I've also tapped more into the power of [Kaggle](https://www.kaggle.com) and it's own flavour of cloud-based Jupyter Notebook and recently did quite a bit of learning in [Google Colab](https://colab.research.google.com) (Colab). The later is used extensively in the ML community with applications including:

- Getting started with TensorFlow
- Developing and training neural networks
- Experimenting with TPUs
- Disseminating AI research
- Creating tutorials

Even their [Welcome to Colab!](https://colab.research.google.com) homepage is a Jupyter Notebook tutorial on how to use Colab, another Jupyter Notebook flavour, somewhat different from the vanilla-one and Kaggle's. It's also the source of that bullet-list you've just read. The best part of Colab is that you can natively sync with Google Drive for extensive storage and you can also get access to professional GPU runtimes for training your DL models. Those GPUs translate in a 30x speed boost when compared to using a CPU. The Tensors, the bread-and-butter of TF, are objects optimized for GPU processing.

I'll leave you with one of my Colab notebook's which cover's how to classify dog breeds based on images. You can check it out here: [End-to-end Multi-class Dog Breed Classification](https://colab.research.google.com/drive/101AR8iI2u_CQt9DH3Km_Ha_-SYMqtAyk).
