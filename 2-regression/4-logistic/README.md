# Logistic Regression to predict categories

## Table of Content
  - [1. Introduction](#1-introduction)
  - [2. Logistic Regression](#2-logistic-regression)

## 1. Introduction
In this lesson on regression, one of the basic classic ML techniques, we will take a look at Logistic Regression. You would use this technique to discover patterns to predict binary categories.

In this lesson, you will learn:
- A new library for data visualization
- Techniques for logistic regression

## 2. Logistic Regression
Logitstic regression differs from linear regression, which you learned about previously, in a few important ways.

### Binary Classification
Logistic regression does not offer the same features as linear regression. The former offer a prediction about a binary category whereas the latter is capable of predicting continual values, for example given the origin of a pumpkin and the time of harvest, how much its price will rise.

### Data pre-processing: feature and label encoding
The pumpkins dataset contains string values for all its columns. Working with categorical data is intuitive for humans but not for machines.

Machine Learning algorithms work well with numbers. So encoding is a very important step in the data pre-processing phase, since it enables us to turn categorical data into numerical data, without losing any information.

### Analyze Relationships between Variables
Now that we have pre-processed our data, we can analyze the relationships between the features and the label to grasp an idea of how well the model will be able to predict the label given the features.

The best way to perform this kind of analysis is plotting the data. We'll be using again the Seaborn `catplot` function, to visualize the relationships between `Item`, `Size`, `Variety` and `Color` in a categorical plot.