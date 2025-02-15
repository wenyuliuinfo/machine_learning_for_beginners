# Introduction to Classification
In these four lessons, you will explore a fundamental focus of classic machine learning - classification. We will walk through using various classification algorithms with a dataset about all the brilliant cuisines.

Classification is a form of supervised learning that bears a lot in common with regression techniques. If machine learning is all about predicting values or names to things by using datasets, then classification generally falls into two groups: binary classification and multiclass classification.

- **Linear Regression** helps you predict relationships between variables and make accurate predictions on where a new datapoint would fall in relationship to that line. So, you could predict what price a pumpkin would be in September vs. December.
- **Logistic Regression** helps you discover "binary categories": at this price point, is this pumpkin from WholeFoods or Walmart.

Classification uses various algorithms to determine other ways of determining a data point label.

## Table of Content
- [Introduction to Classification](#introduction-to-classification)
  - [Table of Content](#table-of-content)
  - [1. Introduction](#1-introduction)
  - [2. Classifier](#2-classifier)

## 1. Introduction
Classification  is one of the fundamental activities of the machine learning researcher and data scientist. From basic classification of a binary value, to complex image classification and segmentation using computer vision, it's always useful to be able to sort data into classes and ask questions.

To state the process in a more scientific way, your classification method creates a predictive model that enables you to map the relationship between input variables to output variables.

Classification uses classic machine learning features, such as `smoker`, `weight`, and `age` to determine likelihood of developing some disease. As a supervised learning technique similar to the regression methods, your data is labeled and ML algorithms use those labels to classify and predict classes of a dataset and assign them to a group or outcome.

## 2. Classifier
The question we want to ask of this dataset is actually a multiclass question, as we have several potential categories to work with. Given a single input, which of these many categories will the data fit?

Scikit-learn offers several different algorithms to classify data, depending on the kind of problem you want to solve.

