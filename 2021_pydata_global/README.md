# PyData Global Tutorial

_Thursday, October 28, 2021 from 1:30 PM - 3:30 PM CDT_

This workshop aims to help data science practitioners navigate the sociotechnical challenges of AI fairness. In the first half othe workshop, we talk participants throught a Jupyter notebook showing how Fairlearn can be used to assess and mitigate unfairness in ML models. In the second half, a panel of speakers will discuss best practices for improving fairness of real-world AI systems.

## Fairness Tutorial

In the first half of this workshop, we walk participants through an hour-long tutorial on assessing and mitigating fairness-related harms in the context of an U.S helathcare scenario. Participants will learn how to use the Fairlearn library to assess machine learning models for performance disparities across differetn racial groups.

### About Fairlearn

This tutorial was developed by a team of Fairlearn contributors.
[Fairlearn](www.fairlearn.org) is an open-source, community-driven project to help data scientists improve fairness of AI systems. It includes a Python library for assessing and mitigating fairness-related harms, and various educational resources.

Fairlearn is built on top of popular Python data science libraries, such as [pandas](https://pandas.pydata.org/) and [scikit-learn](https://scikit-learn.org/stable/index.html).

### Set-Up Instructions

To run the Jupyter Notebook on your local machine, we recommend using the [Anaconda Python distribution](https://www.anaconda.com/products/individual).

In a Python virtual environment (Python version >= 3.7), install the necessary libraries by running the following command:

```
pip install -r requirements.txt
```

If you are using `pip20.3`, you may need to append the `--use-deprecated=legacy-resolver` flag to avoid long wait times due to dependency resolution:

```
pip install -r requirements.txt --use-deprecated=legacy-resolver
```


## Panel Discussion

In the second half of this workshop, we invite researchers and industry practitioners to speak on a panel about sociotechnial challenges data scientist face when applying fairness methodology to their work. The panelists will first introduce themselves, and then answer some moderator-provided questions about documenting responsible AI practices, discussing fairness withing your team and organization, and incorporating fainress int he design and evaluation of AI systems.

Panel moderator: Michael Madaio, Postdoctoral Researcher at Microsoft Research

Panelists:
- Hanna Wallach, Principle Research Manager at Microsoft Research
- Kristen Laird, Project Manager, Cognitive Services at Microsoft
- Triveni Gandhi, Senior Industry Data Scientist, Life Sciences and Responsible AI at Dataiku


