![](lectures/img/572_banner.png)

# DSCI 572: Supervised Learning II

An introduction to deep learning with Python and Pytorch. Covers optmization, neural network basics, convolutional neural networks, and advanced topics such as autoencoders and generative adversarial networks.

- [Canvas Course Page](https://canvas.ubc.ca/courses/59090)
- [Course Jupyter Book](https://pages.github.ubc.ca/MDS-2020-21/DSCI_572_sup-learn-2_students/README.html)
- [OneDrive Folder](https://ubcca-my.sharepoint.com/:f:/g/personal/tomas_beuzen_ubc_ca/EnKLTLl7VDlKvJ9EM123qacBVeOq3az6m2Q-regia2Ct4A?e=HaR1cc)

## Teaching team

| Position                 | Name                         | Slack handle |
|--------------------------|------------------------------|--------------|
| Lecture & lab instructor | Tomas Beuzen                 | `@tom`       |
| Teaching assistant       | Alireza Iranpour             | `@Alireza`   |
| Teaching assistant       | Aaron Berk                   | `@Aaron`     |
| Teaching assistant       | Tristan Pinsonneault-Marotte | `@Tristan Pinsonneault-Marotte`     |
| Teaching assistant       | Peter Gysbers                | `@Peter (TA)`   |
| Teaching assistant       | Ali Seyfi                    | `@Ali (TA)`   |

## Course Schedule

The [MDS calendar](https://ubc-mds.github.io/calendar/) is the best resource for finding lecture, lab, quiz and office hour times.

| Activity                                                    | Frequency | Time                                     | Synchronous/Asynchronous? | Recorded? |
|-------------------------------------------------------------|-----------|------------------------------------------|---------------------------|-----------|
| [Lectures](#lectures)                                       | 2 / week  | Pre-recorded & released at start of week | Asynchronous              | Yes       |
| [Lecture Viewing Parties and Q&A](#lecture-viewing-parties) | 2 / week  | Mon & Wed 10:30-12pm (PDT)               | Synchronous               | Yes |
| [Labs](#labs-and-quizzes)                                   | 1 / week  | Mon or Tues 2-4pm (PDT)                   | Synchronous               | Partially |
| [Quizzes](#labs-and-quizzes)                                | 2 / block | Week 3 & 5                               | Synchronous               | No        |
| [Office Hours](#office-hours)                               | 2 / week  | TBA                                      | Synchronous               | No        |

### Lectures

Find the lecture schedule below. I'm developing new material for this course, but I've included links to old lectures and other useful videos for those that are interested.

| # | Topic  | Optional Watching/Reading |
|---|--------|--------------|
| 1 | [Floating Point Errors](lectures/lecture1_floating-point.ipynb) | <ul><li>[Float Toy](https://evanw.github.io/float-toy/)</li><li>Chapter 2 of Ascher and Greif's book, [available online for students](http://epubs.siam.org/doi/book/10.1137/9780898719987) (you must be on campus wifi)</li></ul> |
| 2 | [Optimization and Gradient Descent](lectures/lecture2_gradient-descent.ipynb) | <ul><li>[Mike's old optimization video](https://youtu.be/bzj1L997uT8?t=67)</li><li>[Mike's old gradient descent video](https://youtu.be/ao34xqQvuT4)</li></ul> |
| 3 | [Stochastic Gradient Descent](lectures/lecture3_stochastic-gradient-descent.ipynb) | <ul><li>[Mike's old stochastic gradient video](https://youtu.be/lmqV5Z5HZzc?t=106)</li></ul> |
| 4 | [Introduction to Neural Networks & PyTorch](lectures/lecture4_pytorch-neural-networks-pt1.ipynb) | <ul><li>[3Blue1Brown's video - But what is a Neural Network?](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)</li><li> [StatQuest's video - Neural Networks Part 1: Inside the Black Box](https://www.youtube.com/watch?v=CqOfi41LfDw)</li><li>[Second part of Mike's old neural network video](https://youtu.be/w60cKkCV_Qk?t=1466)</li><li>[DL Book Chapter 6](http://www.deeplearningbook.org/) </li></ul>|
| 5 | [Training Neural Networks](lectures/lecture5_neural-networks-pt2.ipynb) | <ul><li>[3Blue1Brown's video - Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w&index=2&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)</li><li>[StatQuest's video - Neural Networks Part 2: Backpropagation Main Ideas](https://www.youtube.com/watch?v=IN2XmBhILt4)</li><li>[Mike's old neural network fit video](https://youtu.be/3l9pyhpxGtU?t=124) (last 15 min is about convolutions)</li></ul>
| 6 | Convolutional Neural Networks Part 1 | <ul><li>[Mike's old convolutional neural network video](https://youtu.be/qb01ggeiT_g)</li><li>[Convolutional Neural Networks](http://cs231n.github.io/convolutional-networks/)</li><li>[A guide to convolution arithmetic for deep learning](https://arxiv.org/pdf/1603.07285.pdf)</li><li>[An Intuitive Explanation of Convolutional Neural Networks](https://ujjwalkarn.me/2016/08/11/intuitive-explanation-convnets/)</li><li>[DL Book Chapter 9](http://www.deeplearningbook.org/)</li></ul>|
| 7 |  Convolutional Neural Networks Part 2 | TBD|
| 8 |  Advanced Neural Networks | TBD |

### Labs and Quizzes

You are responsible for the following deliverables, which will determine your course grade:

| Assessment       | Weight | Due Date                          | Location                  |
|------------------|--------|-----------------------------------|---------------------------|
| Lab Assignment 1 | 15%    | Saturday, Jan 16 at 23:59         | Submit to Github & Canvas |
| Lab Assignment 2 | 15%    | Saturday, Jan 23 at 23:59         | Submit to Github & Canvas |
| Quiz 1           | 20%    | Tuesday, Jan 26 at 8:00 and 20:00 | Canvas                    |
| Lab Assignment 3 | 15%    | Saturday, Jan 30 at 23:59         | Submit to Github & Canvas |
| Lab Assignment 4 | 15%    | Saturday, Feb 6 at 23:59          | Submit to Github & Canvas |
| Quiz 2           | 20%    | Tuesday, Feb 9 at 8:00 and 20:00  | Canvas                    |

Labs are Jupyter notebooks comprised of more comprehensive exercises aimed at demonstrating and reinforcing concepts learned during lectures. Quizzes will be conducted on Canvas in week 3 and week 5, are open book and are typically 40 mins long with a focus on short-answer questions. More information on quizzes will be provided closer to their dates.

### Office Hours

We will be hosting multiple office hours during the block as a resource for you to ask questions, get help, or just hang out with us and other students. See the [MDS calendar](https://ubc-mds.github.io/calendar/) for an up-to-date schedule of office hours.

## Dealing With COVID-19

The [COVID-19 pandemic](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/events-as-they-happen) has affected us all in different ways: it's okay to not be okay, and we all need to support each other during this time. With that said:

- My (virtual) door is always open, please feel free to talk to me about how you're doing and if/how I can help you (and if I can't help you, I can point you in the direction of someone who can);
- You don't ever need to explain yourself; if you need support, need to miss a class, or need extra time for an assignment, just ask;
- UBC has [great student support resources](https://students.ubc.ca/covid19) related to COVID-19 (and otherwise).

Further, teaching/learning an intense graduate course like MDS online is a very new concept to all of us. If you have feedback on how I can improve the teaching experience, don't hesitate to reach out - I'm sure things won't be perfect from the get-go.

Finally, here is an official statement from UBC regarding the online learning experience:

>*During this pandemic, the shift to online learning has greatly altered teaching and studying at UBC, including changes to health and safety considerations. Keep in mind that some UBC courses might cover topics that are censored or considered illegal by non-Canadian governments. This may include, but is not limited to, human rights, representative government, defamation, obscenity, gender or sexuality, and historical or current geopolitical controversies. If you are a student living abroad, you will be subject to the laws of your local jurisdiction, and your local authorities might limit your access to course material or take punitive action against you. UBC is strongly committed to academic freedom, but has no control over foreign authorities (please visit http://www.calendar.ubc.ca/vancouver/index.cfm?tree=3,33,86,0 for an articulation of the values of the University conveyed in the Senate Statement on Academic Freedom). Thus, we recognize that students will have legitimate reason to exercise caution in studying certain subjects. If you have concerns regarding your personal situation, consider postponing taking a course with manifest risks, until you are back on campus or reach out to your academic advisor to find substitute courses. For further information and support, please visit: http://academic.ubc.ca/support-resources/freedom-expression.*

## Optional Reference/Learning Materials

### Deep learning resources
- [Dive into Deep Learning](http://d2l.ai/chapter_introduction/index.html), a book based on STAT 157 at UC Berkeley.
- [Deep learning YouTube series](https://www.youtube.com/watch?v=aircAruvnKk) by 3Blue1Brown.
- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/) (free online book).
- [Deep Learning](http://www.deeplearningbook.org/). Ian Goodfellow, Yoshua Bengio and Aaron Courville.
- [Deep Learning with Python](https://machinelearningmastery.com/deep-learning-with-python). Jason Brownlee.
- [Stanford UFLDL tutorial](http://deeplearning.stanford.edu/wiki/index.php/UFLDL_Tutorial) (or [here](http://deeplearning.stanford.edu/tutorial/))
- [Geoff Hinton Coursera lectures](https://www.youtube.com/playlist?list=PLoRl3Ht4JOcdU872GhiYWf6jwrk_SNhz9)
- [CS231n: Convolutional Neural Networks for Visual Recognition (Stanford)](http://cs231n.github.io/)
- [Grokking Deep Learning](https://www.manning.com/books/grokking-deep-learning)
- [Practical Deep Learning For Coders, Part 1](http://course.fast.ai/) and some more resources on their blog [here](http://www.fast.ai/2016/12/19/favorite-posts/)
- [A Guide to Deep Learning](http://yerevann.com/a-guide-to-deep-learning/)
- [Awesome Deep Learning](https://github.com/ChristosChristofidis/awesome-deep-learning), which is a list of other resources
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/)

### ML-related textbooks

- Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems by Aurélien Géron. Code/notebooks available [here](https://github.com/ageron/handson-ml2). (Endorsed by an MDS student!)
- James, Gareth; Witten, Daniela; Hastie, Trevor; and Tibshirani, Robert. An Introduction to Statistical Learning: with Applications in R. 2014. Plus [Python code](https://github.com/JWarmenhoven/ISLR-python) and [more Python code](https://github.com/mscaudill/IntroStatLearn).
- Russell, Stuart, and Peter Norvig. Artificial intelligence: a modern approach. 1995.
- David Poole and Alan Mackwordth. Artificial Intelligence: foundations of computational agents. 2nd edition (2017). [Free e-book](http://artint.info/).
- Kevin Murphy. Machine Learning: A Probabilistic Perspective. 2012.
- Christopher Bishop. Pattern Recognition and Machine Learning. 2007.
- Pang-Ning Tan, Michael Steinbach, Vipin Kumar. Introduction to Data Mining. 2005.
- Mining of Massive Datasets. Jure Leskovec, Anand Rajaraman, Jeffrey David Ullman. 2nd ed, 2014.

### Math for ML

- [Mathematics for Machine Learning](https://mml-book.github.io/)
- [The Matrix Calculus You Need For Deep Learning](http://parrt.cs.usfca.edu/doc/matrix-calculus/index.html)
- [Introduction to Optimizers](https://blog.algorithmia.com/introduction-to-optimizers/)

### Other ML resources

- [A Course in Machine Learning](http://ciml.info/)
- [Nando de Freitas lecture videos](https://www.youtube.com/watch?v=PlhFWT7vAEw) and [online course](https://www.cs.ox.ac.uk/people/nando.defreitas/machinelearning/)

### Interesting ML Competition Write-Ups

- [Diabetic retinopathy Kaggle competition write-up](http://jeffreydf.github.io/diabetic-retinopathy-detection/)
- [Galaxy Zoo Kaggle competition write-up](https://benanne.github.io/2014/04/05/galaxy-zoo.html)
- [National Data Science Bowl competition write-up](https://benanne.github.io/2015/03/17/plankton.html)

## Policies

Please see the general [MDS policies](https://ubc-mds.github.io/policies/).
