# DSCI 572: Supervised Learning II

Welcome to Supervised Learning II! In this course, we delve into the world of deep learning using Python and PyTorch. You'll learn about optimization, the fundamentals of neural networks, and convolutional neural networks. We'll also explore some advanced topics such as generative adversarial networks.

## Important links 

- [Course Jupyter book](https://ubc-mds.github.io/DSCI_572_sup-learn-2/README.html)

## Course learning outcomes    

<details>
  <summary>Click to expand!</summary>

By the end of this course, you will be able to:
- Identify common computational issues caused by floating-point arithmatic, e.g., rounding, overflow, etc., and program defensively against these errors.
- Explain how the gradient descent algorithm and its variants work.
- Explain the fundamental concepts of neural networks including layers, nodes, and activation functions and gain proficiency in implementing basic neural networks using `PyTorch`.  
- Illustrate the process of backpropagation in neural network training. 
- Explain how convolutional neural networks work and implement them for image classification using PyTorch. 
- Explain and apply transfer learning and the different flavours of it: "out-of-the-box", "feature extractor", "fine tuning".
- Describe at a high level the basic principles and architecture of Generative Adversarial Networks (GANs)

</details>

## Deliverables

<details>
  <summary>Click to expand!</summary>
    
The following deliverables will determine your course grade:

| Assessment       | Weight  | Where to submit|
| :---:            | :---:   |:---:  | 
| Lab Assignment 1 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 2 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 3 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| Lab Assignment 4 | 12%     | [Gradescope](https://www.gradescope.ca/courses/11554) |
| iClicker participation     | 2%      | [iClicker Cloud](https://join.iclicker.com/DAZZ) | 
| Quiz 1           | 25%     | [Canvas](https://canvas.ubc.ca/courses/123600)     |
| Quiz 2           | 25%     | [Canvas](https://canvas.ubc.ca/courses/123600)     |

See [Calendar](https://ubc-mds.github.io/calendar/) for the due dates. 
</details>


## Teaching Team
<details>
  <summary>Click to expand!</summary>

    
| Role           | Name             | 
| ---------------- | -------------- |
| Lecture Instructor | Varada Kolhatkar |
| Lab Instructor     | Varada Kolhatkar |
| Teaching Assistant | Ali Balapour |
| Teaching Assistant | Prajeet Bajpai |
| Teaching Assistant | Wenxuan (Skylar) Fang |
| Teaching Assistant | Abdul Muntakim Rafi |
    
</details>
   

## Lectures 

### Format
<details>
  <summary>Click to expand!</summary>
    
I strongly recommend reviewing the corresponding lecture notes before each lecture. During the lectures, I will focus on the key concepts. It's also highly advised to download the relevant datasets and run the lecture Jupyter notebooks on your own. Experimenting with the code will greatly improve your understanding.

</details>

### Lecture schedule

This course occurs during **Block 4** in the 2023/24 school year.

| # | Topic                                      | Resources and optional readings            |
|---|--------------------------------------------|--------------------------------------------|
| 1 | Floating Point Errors                      | <li> [Floating Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)</li>
| 2 | Optimization and Gradient Descent          | |
| 3 | Stochastic Gradient Descent                | |
| 4 | Introduction to Neural Networks & PyTorch  | |
| 5 | Training Neural Networks                   | |
| 6 | Convolutional Neural Networks Part 1       | <li> [Stanford cs231 CNNs notes](https://cs231n.github.io/convolutional-networks/) </li> |
| 7 | Convolutional Neural Networks Part 2       | |
| 8 | Advanced Deep Learning                     | |

## Installation
 
We are providing you with a `conda` environment file which is available [here](dsci572env.yml). You can download this file and create a conda environment for the course and activate it as follows. 

```
conda env create -f dsci572env.yml
conda activate 572
```

In order to use this environment in `Jupyter`, you will have to install `nb_conda_kernels` in the environment where you have installed `Jupyter` (typically the `base` environment). You will then be able to select this new environment in `Jupyter`. If you're unable to see the environment in Jupyter, you might have to install the kernel manually. See the documentation [here](https://ipython.readthedocs.io/en/stable/install/kernel_install.html). For more details on this, refer to your [521 lecture 7](https://pages.github.ubc.ca/MDS-2023-24/DSCI_521_platforms-dsci_students/lectures/7-virtual-environments.html#).

I've only attempted to install this environment file on a few machines, and you may encounter issues with certain packages from the `yml` file when executing the commands above. This is not uncommon and may suggest that the specified package version is not yet available for your operating system via `conda`. When this occurs, you have a couple of options:

1. Modify the local version of the `yml` file to remove the line containing that package.
2. Create the environment without that package. 
3. Activate the environment and install the package manually either with `conda install` or `pip install` in the environment.   

_Note that this is not a complete list of the packages we'll be using in the course and there might be a few packages you will be installing using `conda install` later in the course. But this is a good enough list to get you started._ 

## Course communication
<details>
  <summary>Click to expand!</summary>

We are all here to support your learning and success in the course and the program. Here's how our communication will work during the course.

### Clarifications on the lecture notes or lab questions

If there is any clarification on the lecture material or lab questions, I'll post a Slack message on our course channel and tag you. **It is your responsibility to read the messages whenever you are tagged.** (I know that there are too many things for you to keep track of. You do not have to read all the messages but please make sure to carefully read the messages whenever you are tagged.) 

### Questions on lecture material or labs

If you have questions about the lecture material or lab questions, please post them on the course Slack channel rather than direct messaging me or the TAs. Here are the advantages of doing so: 
- You'll get a quicker response. 
- Your classmates will benefit from the discussion. 

When you ask your question on the course channel, please avoid tagging the instructor unless it's specific for the instructor (e.g., if you notice some mistake in the lecture notes). If you tag a specific person, other teaching team members or your colleagues are discouraged to respond. This decreases the response rate on the channel. 

Please use some consistent convention when you ask questions on Slack to facilitate easy search for others or future you. For example, if you want to ask a question on Exercise 3.2 from Lab 1, start your post with the label `lab1-ex2.3`. Or if you have a question on lecture 2 material, start your post with the label `lecture2`. Once the question is answered/solved, you can add "(solved)" tag before the label (e.g., (solved) `lab1-ex2.3`. Do not delete your post even if you figure out the answer on your own. The question and the discussion can still be beneficial to others.  

### Questions related to grading

If you have concerns related to grading:

1. First, ensure that you have thoroughly reviewed your response, our solution key, and any TA feedback.
2. Verify that your concerns align with our 'Reasonable grading concerns' policy, which you can read [here](https://ubc-mds.github.io/policies/).

If you believe your concerns are valid:
- For assignments: Submit a regrade request on Gradescope.
- For quizzes: Directly message the TA responsible for grading that question. (I will inform you on Slack who has graded what after grades are returned.)
- If you cannot resolve the issue with the TA, send a Slack message to the instructor, including the relevant TA in the conversation.

### Questions related to your personal situation or talking about sensitive information
 
I am open to having a conversation with you. If you'd like to discuss any sensitive matters, please send me a direct message on Slack (and mention/tag me) instead of posting it in the course channel. It may take some time for me to respond, but I'll make every effort to reply as promptly as I can. If I cannot address your issue directly, I can at least direct you to the appropriate person who may be able to assist you. 
</details>

## Reference Material
<details>
  <summary>Click to expand!</summary>

### Deep learning resources

- [3Blue1Brown Deep learning YouTube series](https://www.youtube.com/watch?v=aircAruvnKk)
- [Yann LeCun's NYU Deep Learning course](https://atcold.github.io/pytorch-Deep-Learning/)
- [Geoff Hinton's Coursera lectures](https://www.youtube.com/playlist?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9)
- [CS231n: Convolutional Neural Networks for Visual Recognition (Stanford)](http://cs231n.github.io/)
- [Introduction to Deep Learning](https://sebastianraschka.com/blog/2021/dl-course.html)
- [Deep Learning for Computer Vision (U of Michigan)](https://web.eecs.umich.edu/~justincj/teaching/eecs498/FA2020/)
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/)
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/)
- [_Awesome_ Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning)
- [_Awesome_ ML Youtube channels](https://github.com/JoseDeFreitas/awesome-youtubers#machine-learning)

### ML-related textbooks

- [Dive into Deep Learning](http://d2l.ai/index.html)
- [Deep Learning](http://www.deeplearningbook.org/) by Ian Goodfellow, Yoshua Bengio and Aaron Courville
- [An Introduction to Statistical Learning: with Applications in R](https://www.statlearning.com/) by Gareth James, Daniela Witten, Trevor Hastie, and Rob Tibshirani (Python code [here](https://github.com/JWarmenhoven/ISLR-python) and [here](https://github.com/mscaudill/IntroStatLearn)).
- [Artificial intelligence: a modern approach](https://aima.cs.berkeley.edu/global-index.html) by Stuart Russell and Peter Norvig.
- [Artificial Intelligence: foundations of computational agents](http://artint.info/) by David Poole and Alan Mackwordth.
- Pattern Recognition and Machine Learning by Christopher Bishop.
- [Probabilistic Machine Learning: An Introduction](https://probml.github.io/pml-book/book1.html) by [Kevin Murphy](https://www.cs.ubc.ca/~murphyk/).

### Math for ML

- [Mathematics for Machine Learning](https://mml-book.github.io/)
- [The Matrix Calculus You Need For Deep Learning](http://parrt.cs.usfca.edu/doc/matrix-calculus/index.html)

### Other ML resources

- [A Course in Machine Learning](http://ciml.info/)
- [Nando de Freitas lecture videos](https://www.youtube.com/watch?v=PlhFWT7vAEw) and [online course](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/)

## License

© 2023 Varada Kolhatkar, Arman Seyed-Ahmadi, Tomas Beuzen, Mike Gelbart, and Aaron Berk

Software licensed under [the MIT License](https://spdx.org/licenses/MIT.html), non-software content licensed under [the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See the [license file](LICENSE.md) for more information.