# Complex Word Identification (CWI) Shared Task 2018 - Teaching

This git repository contains a few utilities to support students on the COM4513 and COM6513 modules at the University of Sheffield attempt the Complex Word Identification Shared Task 2018.

The task consists of predicting which words could be **difficult** and which could be *easy* for a non-native speaker, e.g.:

> "Both China and the Philippines **flexed** their *muscles* on Monday."

For details of the task, see [CWI Shared Task 2018](https://sites.google.com/view/cwisharedtask2018/)

For this class project, we will be tackling the **binary classification task** for the **monolingual English** and **monolingual Spanish** tracks.

We provide the official training, development and test splits of the datasets for both languages.

You will have to use the development data to evaluate your approach's performance and suitability during development. The sentences in this subset are disjoint from (i.e. do not appear in) the training data. The test data will not be released until week 10.


## Questions/Issues
Please post all questions to the [module's Google group](https://groups.google.com/a/sheffield.ac.uk/forum/#!forum/com4513-6513-2018-group).


## Getting started
First. **You should have installed git if you do not already have it**. Git can be installed on the university computers from the Software Centre or from the git website/your package manager if you use your own laptop. 

To download the library files and the datasets, you should clone the repository from the git bash prompt.

    git clone https://github.com/sheffieldnlp/cwisharedtask2018-teaching


## Reading the datasets

All the required information is provided in a column format. A complete description is given in the [official shared task page](https://sites.google.com/view/cwisharedtask2018/datasets). Since we are only interested in the binary classification task, we can discard the last column (i.e., gold-standard probability). 

The English dataset (training and development) is originally divided in three files, corresponding to the source they were collected from. You are welcome to use them as such, but we are also providing them joined together in a single file for training and a single one for development.

An example of how the data could be read is given in ``dataset.py``


## Scoring Your Classifiers

The ``report_score`` function in ``utils/scorer.py`` will be used to assess the performance of your classifier.

``report_score`` expects 2 parameters. A list of gold-standard labels (i.e. from the development data), and a list of predicted labels (i.e. what you classifier predicts on the development data).

    predicted = [1, 0, 0, 1, ...]
    actual = [1, 1, 0, 1, ...]

    report_score(actual, predicted)

A standard method for evaluating a classifier is to calculate the F1 score of its predictions. In our case, we could compute the F1 score for each class, independently. Since we would like an overall score that considers the performance in both classes, ``report_score`` will print the macro-F1 score. As you will notice, there is some imbalance between the classes (the number of *complex* instances is lower than that of *simple* instances). As such, we use macro-F1 as an overall performance metric to avoid favouring the bigger class. While this is the metric that will be used to assess your classifier, you can get more detailed per-class scores calling ``report_score`` with parameter ``detailed=True``.

We have implemented a simple classifier as baseline. This classifier uses Logistic Regression to learn a prediction model that relies on two features from the target word/phrase: its length in characters and its length in tokens. The code for the baseline can be found in ``baseline.py``. On the development data, this baseline achieves macro-F1 scores of 0.69 and 0.72 for English and Spanish, respectively. You should aim to beat these scores!
