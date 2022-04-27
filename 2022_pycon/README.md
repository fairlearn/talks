# PyCon 2022 Tutorial<br>_Assessing and mitigating unfairness in AI systems_

_Thursday, April 28 from 1:30 PM - 4:30 PM MDT_

Fairness in AI systems is an interdisciplinary field of research and practice that aims to understand and address some of the negative impacts of AI systems on society, with an emphasis on improving the impacts of such systems on historically underserved and marginalized communities.

In this tutorial, we will walk through the process of assessing and mitigating fairness-related harms in the context of the U.S. health care system. Specifically, we will consider a scenario involving patient health risk modeling that has demonstrated racial disparities (Obermeyer et al., 2019). This tutorial will consist of a mix of instructional content and hands-on demonstrations using Jupyter notebooks. Participants will use the Fairlearn library to assess an ML model for performance disparities across different racial groups and mitigate those disparities using a variety of algorithmic techniques. Participants will also learn how to explore, document, and communicate fairness issues, drawing on resources such as datasheets for datasets and model cards.

Participants are expected to have intermediate Python skills and familiarity with Scikit-Learn. For maximal benefit, participants should have some experience training and evaluating supervised models in Python.

## Set-up Instructions

### Option 1: Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fairlearn/talks/blob/main/2022_pycon/pycon-2022-students.ipynb)

For this tutorial, we encourage participants to run the tutorial notebook through Google Colab to avoid issues with local environment set-up. Click on the button above to launch a free compute envrionment for executing the Jupyter notebook and writing Python code. 

### Option 2: Local Set-up

If you want to follow along in this tutorial on your local machine, we recommend using the [Anaconda Python distribution](https://www.anaconda.com/products/individual).

Participants will need to download the Jupyter notebook [pycon-2022-students.ipynb](https://raw.githubusercontent.com/LeJit/talks/pycon_2022/2022_pycon/pycon-2022-students.ipynb).

#### __Conda installation__

If you are using _Anaconda_, install the necessary libraries by running the following command:

```
conda env create -f environment.yml
```

#### __Pip installation__ 

In a Python virtual environment (Python version >= 3.7), install the necessary libraries by running the following command:

```
pip install -r requirements.txt
```

If you are using `pip20.3`, you may need to append the `--use-deprecated=legacy-resolver` flag to avoid long wait times due to dependency resolution:

```
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

You can run the `checkenv.py` script to assert if the packages were installed correctly.

## Dataset

For this tutorial, we use a pre-processed version of the [Diabetes 130-US hospitals](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008)

The original data file can be found in `data/diabetic_data.csv`. 

The processed dataset we use is located in `data/diabetic_preprocessed.csv`. If you want to further explore how we cleaned and processed the original dataset, you can refer to `preprocess.py`.

## About Fairlearn

[Fairlearn](www.fairlearn.org) is an open-source, community-driven project to help data scientists improve the fairness of AI systems. It includes a Python library for assessing and mitigating fairness-related harms, and various education resources.

Fairlearn is built on topo of popular Python data science libraries, such as [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/index.html).
