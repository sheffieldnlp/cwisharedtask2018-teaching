# Complex Word Identification (CWI) Shared Task 2018 - Teaching

This git repository contains a few utilities to support students on the COM4513 and COM6513 modules at the University
of Sheffield attempt the Complext Word Identification Shared Task 2018.

For details of the task, see [CWI Shared Task 2018](https://sites.google.com/view/cwisharedtask2018/)

We supplement the dataset by providing training, development and test splits of the data.

You will have to use the development data to evaluate your approach's performance and suitability during development. The articles in this dataset are disjoint from (i.e. do not appear in) the training dataset. The test dataset will not be released until week 10.

We provide our own scorer and dataset reader (small adaptations from the original release by fakenewschallenge) in the ``utils/`` folder/package. A visual explanation of the scorer is available [here](https://docs.google.com/a/sheffield.ac.uk/spreadsheets/d/1ADOwjhlE-KCPyGvy2me7njO6IwM8RQDc4j1_iMOTFMc/edit?usp=sharing).

## Questions/Issues
Please post all questions to the [module's Google group](https://groups.google.com/a/sheffield.ac.uk/forum/#!forum/com4513-6513-2017-group).

## Getting Started
First. **You should have installed git if you do not already have it**. Git can be installed on the university computers from the Software Centre or from the git website/your package manager if you use your own laptop. 

To download the data, you should first clone the repository from the git bash prompt. This downloads the library files. But does not download the data.

    git clone https://github.com/sheffieldnlp/fakenewschallenge-teaching

The FNC dataset is inlcuded as a submodule and can be FNC Dataset is included as a submodule. You must download the fnc-1 dataset by running the following commands. This places the fnc-1 dataset into the folder `fnc-1/`

    git submodule init
    git submodule update


## Loading the data
### Example code is given in ``example.py``

We have made a dataset reader that partitions the data into the training, development and test splits.

### dataset class
The dataset class reads the FNC-1 dataset and loads the stances and article bodies into two separate containers.

    dataset = DataSet()

You can access these through the ``.stances`` and ``.articles`` variables

    print("Total stances: " + str(len(dataset.stances)))
    print("Total bodies: " + str(len(dataset.articles)))

* ``.articles`` is a dictionary of articles, indexed by the body id. For example, the text from the 144th article can be printed with the following command:
   ``print(dataset.articles[144])``

### split() function (``utils/generate_test_splits.py``)
The split function inputs a dataset and will split the dataset into training data, development data and test data. Test data will not be released at this point in time.

    data_splits = split(dataset)

    training_data = data_splits['training']
    dev_data = data_splits['dev']
    test_data = data_splits['test']

* Each of the training/dev/test partitions will contain a list of dictionaries. Each entry corresponds to one training example. This contains a body id (article text), a headline and a stance. There are four possible stances: agree, disagree, discuss and unrelated. (see ``utils/score.py`` for a list of these.
    ``{'Body ID': 144,
'Headline': 'Axl Rose NOT Dead: Fake MSNBC Death Hoax Goes Viral On Facebook', 'Stance': 'unrelated'}``

### Base directory
We expect the FNC dataset to be loaded into ``fnc-1/`` and the dataset split ids to come from ``splits/``. If you need to change these, then you may be doing something unexpected. We recommend setting your python working directory to be the root of this repository.

## Scoring Your Classifier

The ``report_score`` function in ``utils/score.py`` will be used to assess the performance of your classifier.

``report_score`` expects 2 parameters. A list of actual stances (i.e. from the dev dataset), and a list of predicted stances (i.e. what you classifier predicts on the dev dataset).

    predicted = ['unrelated','discuss',...]
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
