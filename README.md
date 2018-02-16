# Complex Word Identification (CWI) Shared Task 2018 - Teaching

This git repository contains a few utilities to support students on the COM4513 and COM6513 modules at the University
of Sheffield attempt the Complex Word Identification Shared Task 2018.

For details of the task, see [CWI Shared Task 2018](https://sites.google.com/view/cwisharedtask2018/)

For this class project, we will be tackling the **binary classification task** for the **monolingual English** and **monolingual Spanish** tracks.

We supplement the datasets by providing the official training, development and test splits of the data.

You will have to use the development data to evaluate your approach's performance and suitability during development. The sentences in this dataset are disjoint from (i.e. do not appear in) the training dataset. The test dataset will not be released until week 10.


## Questions/Issues
Please post all questions to the [module's Google group](https://groups.google.com/a/sheffield.ac.uk/forum/#!forum/com4513-6513-2018-group).


## Getting the datasets
First. **You should have installed git if you do not already have it**. Git can be installed on the university computers from the Software Centre or from the git website/your package manager if you use your own laptop. 

To download the data, you should first clone the repository from the git bash prompt. This downloads the library files. But does not download the data.

    git clone https://github.com/sheffieldnlp/cwisharedtask2018-teaching

The CWI datasets are included as submodules and you must download them by running the following commands. This places the CWI datasets into the folders `cwi/en` and `cwi/spa` for English and Spanish, respectively.

    git submodule init
    git submodule update


## Reading the datasets

All the requiered information is provided in a column format. A complete description is given in the [official shared task page](https://sites.google.com/view/cwisharedtask2018/datasets). Since we are only interested in the binary classification task, we can discard the last column (i.e., gold-standard probability). 

An example of how the data could be read is given in ``example.py``

## Scoring Your Classifiers

The ``report_score`` function in ``utils/score.py`` will be used to assess the performance of your classifier.

``report_score`` expects 2 parameters. A list of gold-standard labels (i.e. from the dev dataset), and a list of predicted labels (i.e. what you classifier predicts on the dev dataset).

    predicted = [1, 0, 0, 1, ...]
    actual = [stance['Stance'] for stance in dev_data]

    report_score(actual, predicted)

This will print a confusion matrix and a final score your classifier. We provide the scores for very simple perceptron based classifier which you should be able to match and eventually beat!

|           	| agree 	| disagree 	| discuss 	| unrelated 	|
|-----------	|-------	|----------	|---------	|-----------	|
| agree     	| 168   	| 2        	| 121     	| 94        	|
| disagree  	| 14    	| 4        	| 66      	| 44        	|
| discuss   	| 54    	| 0        	| 542     	| 182       	|
| unrelated 	| 433   	| 5        	| 1797    	| 1309      	|

Score: 1105.5 out of 2177.0     (50.780891134588884%)
