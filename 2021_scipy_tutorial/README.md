# SciPy 2021 Tutorial<br>_Fairness in AI systems:<br>From social context to practice using Fairlearn_

_Tuesday, July 13 from 9:00 AM - 1:00 PM CDT_

Fairness in AI systems is an interdisciplinary field of research and practice that aims to understand and address some of the negative impacts of AI systems on society. In this tutorial, we will walk through the process of assessing and mitigating fairness-related harms in the context of the U.S. health care system. This tutorial will consist of a mix of instructional content and hands-on demonstrations using Jupyter notebooks. Participants will use the Fairlearn library to assess ML models for performance disparities across different racial groups and mitigate those disparities using a variety of algorithmic techniques.

## Set-up Instructions

### Option 1: Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1HDiMzQ_P2NHT66OuAq1bBiBfCyNtCXlO)

For this tutorial, we encourage participants to run the tutorial notebook through Google Colab to avoid issues with local environment set-up. Click on the button above to launch the free compute environment for executing the Jupyter notebook and writing Python code. 


### Option 2: Local Set-Up

If you want to follow along in this tutorial on your local machine, we recommend using the [Anaconda Python distribution](https://www.anaconda.com/products/individual).

Participants will need to download the Jupyter notebook _name goes here_.

In a Python virtual environment (Python version >= 3.7), install the necessary libraries by running the following command:

```
pip install -r requirements.txt
```

If you are using `pip20.3`, you may need to append the `--use-deprecated=legacy-resolver` flag to avoid long wait times due to dependency resolution:

```
pip install -r requirements.txt --use-deprecated=legacy-resolver
```

You can run the `checkenv.py` script to assert if the packages were installed correctly.

## The Dataset

For this tutorial, we use a pre-processed version of the [U.S. Hospital Diabetes](https://archive.ics.uci.edu/ml/datasets/Diabetes+130-US+hospitals+for+years+1999-2008#) dataset. The original data file can be found in `data/diabetic_data.csv`. 

The processed dataset we use is located in `data/diabetic_preprocessed.csv`. If you want to further explore how we cleaned and processed the original dataset, you can refer to `preprocess.py`.

## About Fairlearn

This tutorial was developed by a team of Fairlearn contributors.
[Fairlearn](www.fairlearn.org) is an open-source, community-driven project to help data scientists improve fairness of AI systems. It includes a Python library for assessing and mitigating fairness-related harms, and various educational resources.

Fairlearn is built on top of popular Python data science libraries, such as [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/index.html).
