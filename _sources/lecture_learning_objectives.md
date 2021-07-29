![](lectures/img/572_banner.png)

# Lecture Learning Objectives

The lecture-specific learning objectives for the course are presented below.

## Lecture 1: Floating Point Numbers

- Compare and contrast the representations of integers and floating point numbers
- Explain how double-precision floating point numbers are represented by 64 bits
- Identify common computational issues caused by floating point numbers, e.g., rounding, overflow, etc.
- Calculate the "spacing" of a 64 bit floating point number in Python
- Write code defensively against numerical errors
- Use `numpy.iinfo()`/`numpy.finfo()` to work out the possible numerical range of an integer or float dtype

## Lecture 2: Optimization & Gradient Descent

- Explain the difference between a model, loss function, and optimization algorithm in the context of machine learning
- Explain and implement the gradient descent algorithm
- Apply gradient descent to linear and logistic regression
- Use `scipy.optimize.minimize()` to minimize a function

## Lecture 3: Stochastic Gradient Descent

- Explain and implement the stochastic gradient descent algorithm
- Explain the advantages and disadvantages of stochastic gradient descent as compared to gradient descent
- Explain what are epochs, batch sizes, iterations, and computations in the context of gradient descent and stochastic gradient descent

## Lecture 4: Introduction to Neural Networks & Pytorch

- Describe the difference between `numpy` and `torch` arrays (`np.array` vs. `torch.Tensor`)
- Explain fundamental concepts of neural networks such as layers, nodes, activation functions, etc.
- Create a simple neural network in PyTorch for regression or classification

## Lecture 5: Training Neural Networks

- Explain how backpropagation works at a high level
- Describe the difference between training loss and validation loss when creating a neural network
- Identify and describe common techniques to avoid overfitting/apply regularization to neural networks, e.g., early stopping, drop out, L2 regularization
- Use `PyTorch` to develop a fully-connected neural network and training pipeline

## Lecture 6: Convolutional Neural Networks Part 1

- Describe the terms convolution, kernel/filter, pooling, and flattening
- Explain how convolutional neural networks (CNNs) work
- Calculate the number of parameters in a given CNN architecture
- Create a CNN in `PyTorch`
- Discuss the key differences between CNNs and fully connected NNs

## Lecture 7: Convolutional Neural Networks Part 2

- Load image data using `torchvision.datasets.ImageFolder()` to train a network in PyTorch
- Explain what "data augmentation" is and why we might want to do it
- Be able to save and re-load a PyTorch model
- Tune the hyperparameters of a PyTorch model using [Ax](https://ax.dev/)
- Describe what transfer learning is and the different flavours of it: "out-of-the-box", "feature extractor", "fine tuning"

## Lecture 8: Advanced Neural Networks

- Describe what an autoencoder is at a high level and what they can be useful for
- Describe what a generative adversarial network is at a high level and what they can be useful for
- Describe what a multi-input model is and what they can be useful for
