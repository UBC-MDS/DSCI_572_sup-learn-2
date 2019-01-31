# DSCI 572: Supervised Learning II

An introduction to optimization for machine learning. Computation of derivatives. Deep learning.

2019 Instructor: [Mike Gelbart](https://mikegelbart.com)



## 2019 Lecture Schedule

**Course structure**: this course will be delivered as a [flipped classroom](https://en.wikipedia.org/wiki/Flipped_classroom), which means you are expected to watch the lecture videos _before_ class. While you're not expected to understand everything just from watching a video once, you're expected to come to class with a basic familiarity of what it's all about; we won't be starting again from scratch in class. During the lecture time itself, we will work on practical examples in Python. As a result of the extra 1-2 hours of time spent watching the videos per week, we will aim to make the labs shorter than in other courses.

**Some context**: these videos are from Mike's undergraduate machine learning course, CPSC 340, which contains a lot of the same material. They were filmed in January-April 2018. You can find the accompanying slides, and some supplementary readings, [here](https://ubc-cs.github.io/cpsc340/). By the end of MDS we will cover roughly everything in CPSC 340, although often skipping over the implementation details. On the other hand, we cover machine learning topics that do not appear in CPSC 340, like time series data and natural language data. In MDS we also benefit greatly from the statistical perspective of "stat stream" courses. 

**Video timings**: video links have start times embedded in them, which is where you are supposed to start watching from. End times are specified below if you're not supposed to watch the whole video. I recommend watching the videos at 1.25x speed.

| #   |  Topic  | To watch _before_ class | Optional reading |
|-----|--------|--------------|--------------|
|   1    | [Gradient descent](lectures/lecture1.ipynb) | [Optimization video](https://youtu.be/bzj1L997uT8?t=67), [Gradient descent video](https://youtu.be/ao34xqQvuT4) |  |
|   2   |   [Numerical errors](lectures/lecture2.ipynb)  | none | Chapter 2 of Ascher and Greif's book, [available online for students](http://epubs.siam.org/doi/book/10.1137/9780898719987) (you must be on campus wifi) |
|   3 |   [Computing derivatives](lectures/lecture3.ipynb)  | none | [Autograd tutorial](https://github.com/HIPS/autograd/blob/master/docs/tutorial.md), [Automatic Differentiation in Machine Learning: a Survey](http://jmlr.org/papers/volume18/17-468/17-468.pdf), [Dougal Maclaurin's Thesis](https://dougalmaclaurin.com/phd-thesis.pdf) section 2.5 and Chapter 4  | 
|   4   | [Neural networks: `predict`](lectures/lecture4.ipynb)  | 3Blue1Brown's [But what *is* a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), [Second part of neural network predict video](https://youtu.be/w60cKkCV_Qk?t=1466) | [DL Book](http://www.deeplearningbook.org/) chapter 6, [video](https://www.youtube.com/watch?v=bHvf7Tagt18), [Fortune article](http://fortune.com/ai-artificial-intelligence-deep-machine-learning/), various resources below |
| 5   | [Stochastic gradient, neural networks: `fit`](lectures/lecture5.ipynb)  | 3Blue1Brown's [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w&index=2&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), [Stochastic gradient video](https://youtu.be/lmqV5Z5HZzc?t=106), [First part of neural network fit video](https://youtu.be/3l9pyhpxGtU?t=124) **up to 36:00**. | [Why Momentum Really Works](https://distill.pub/2017/momentum/), [Bottoming out](http://www.argmin.net/2016/04/18/bottoming-out/), [DL Book](http://www.deeplearningbook.org/) chapters 7-8, [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)
|   6   | [Convolutions, intro to convolutional neural networks](lectures/lecture6.ipynb) | [Second part of neural network fit video](https://youtu.be/3l9pyhpxGtU?t=2188) | [Convolutional Neural Networks](http://cs231n.github.io/convolutional-networks/) (many students found this one helpful! :star:), [An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/), [ConvNet notes](http://cs231n.github.io/convolutional-networks/), [DL Book](http://www.deeplearningbook.org/) chapter 9  |
|  7  |  [Convolutional neural networks: `predict`](lectures/lecture7.ipynb) | [Convolutional neural network video](https://youtu.be/qb01ggeiT_g)  | [Notes from Coursera Deep Learning courses by Andrew Ng](https://www.slideshare.net/TessFerrandez/notes-from-coursera-deep-learning-courses-by-andrew-ng), [Visualizing and Understanding Convolutional Neural Networks](https://cs.nyu.edu/~fergus/papers/zeilerECCV2014.pdf), [The Building Blocks of Interpretability](https://distill.pub/2018/building-blocks/) |
| 8 | [CNN review, deep learning wrap-up, supervised learning diagnostics](lectures/lecture8.ipynb) | [Part 2 of Ali Rahimi @ NIPS 2017](https://youtu.be/Qi1Yry33TQE?t=11m) (video, 10min at 1x speed) | :point_left: the entire Ali Rahimi video, some [disturbing results](https://arxiv.org/pdf/1312.6199.pdf) and follow up papers [here](https://arxiv.org/abs/1412.6572) (see Figure 1 :scream:) and [here](https://arxiv.org/abs/1606.04435), [deepart](https://deepart.io/), [paper on artwork](https://arxiv.org/pdf/1508.06576v2.pdf), [kaggle competition writeup](http://jeffreydf.github.io/diabetic-retinopathy-detection/)  |

## Labs

1. [Optimization, gradient descent](labs/lab1.ipynb)
2. [Floating point issues, computing derivatives](labs/lab2.ipynb)
3. [Neural networks](labs/lab3.ipynb)
4. [Convolutional neural networks](labs/lab4.ipynb)


## Reference Material

#### ML-related textbooks
* James, Gareth; Witten, Daniela; Hastie, Trevor; and Tibshirani, Robert. An Introduction to Statistical Learning: with Applications in R. 2014. Plus [Python code](https://github.com/JWarmenhoven/ISLR-python) and [more Python code](https://github.com/mscaudill/IntroStatLearn).
* Russell, Stuart, and Peter Norvig. Artificial intelligence: a modern approach. 1995.
* David Poole and Alan Mackwordth. Artificial Intelligence: foundations of computational agents. 2nd edition (2017). [Free e-book](http://artint.info/).
* Kevin Murphy. Machine Learning: A Probabilistic Perspective. 2012.
* Christopher Bishop. Pattern Recognition and Machine Learning. 2007.
* Pang-Ning Tan, Michael Steinbach, Vipin Kumar. Introduction to Data Mining. 2005.
* Mining of Massive Datasets. Jure Leskovec, Anand Rajaraman, Jeffrey David Ullman. 2nd ed, 2014.

#### Math for ML

* [Mathematics for Machine Learning](https://mml-book.github.io/)
* [The Matrix Calculus You Need For Deep Learning](http://parrt.cs.usfca.edu/doc/matrix-calculus/index.html)
* [Introduction to Optimizers](https://blog.algorithmia.com/introduction-to-optimizers/)

#### Other ML resources

* [A Course in Machine Learning](http://ciml.info/)
* [Nando de Freitas lecture videos](https://www.youtube.com/watch?v=PlhFWT7vAEw) and [online course](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/)

#### Deep learning resources
* [Dive into Deep Learning](http://d2l.ai/chapter_introduction/index.html), a book based on STAT 157 at UC Berkeley.
* [Deep learning YouTube series](https://www.youtube.com/watch?v=aircAruvnKk) by 3Blue1Brown.
* [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) (free online book).
* [Deep Learning](http://www.deeplearningbook.org/). Ian Goodfellow, Yoshua Bengio and Aaron Courville.
* [Deep Learning with Python](https://machinelearningmastery.com/deep-learning-with-python). Jason Brownlee.
* [Stanford UFLDL tutorial](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial) (or [here](http://deeplearning.stanford.edu/tutorial/))
* [Geoff Hinton Coursera lectures](https://www.youtube.com/playlist?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9)
* [CS231n: Convolutional Neural Networks for Visual Recognition (Stanford)](http://cs231n.github.io/)
* [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning)
* [Practical Deep Learning For Coders, Part 1](http://course.fast.ai/) and some more resources on their blog [here](http://www.fast.ai/2016/12/19/favorite-posts/)
* [A Guide to Deep Learning](http://yerevann.com/a-guide-to-deep-learning/)
* [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning), which is a list of other resources
