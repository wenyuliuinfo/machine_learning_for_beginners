# Classification Methods for Machine Learning

You will use this dataset with a variety of classifiers to predict a given national cuisine based on a group of ingredients. While doing so, you will learn more about some of the ways that algorithms can be leveraged for classification.

## Lessons
1. [Introduction to Classification](1-introduction/README.md)

## 1. Preparation

Prepare the dataset by balancing the data based on previous lesson.

## 2. Choosing the classifier

After the getting balanced dataset, you need to decide which algorithm to use for training.

Scikit-learn groups classification under Supervised Learning. The following methods all include classification techniques:
- Linear Models
- Support Vector Machines
- Stochastic Gradient Descent
- Nearest Neighbors
- Gaussian Processes
- Decision Trees
- Ensemble Methods
- Multiclass and multioutput algorithms

### Classifier Comparison
Running through several and looking for a good result is a way to choose the classifier. Scikit-learn offers a side-by-side comparison on a created dataset, comparing KNeighbors, SVC two ways, GaussianProcessClassifier, DecisionTreeClassifier, QuadraticDiscrinationAnalysis, as showing here:

![Image](images/comparison.png)

### Decision Approach
A better way than guessing is to follow the ideas on this Multiclass Classification sheet.

![Image](images/decision_approach.png)

### Reasoning
Reasoning through different approaches given the constraints we have:
- **Neural networks are too heavy.** Given our clean, but minimal dataset, and the fact that we are running training locally via notebooks, neural networks are too heavy weight for this task.
- **Decision tree or logistic regression.** A decision tree might work, or logistic regression for multiclass data.
- **Multiclass Boosted Decision Trees.** The multiclass boosted decision tree is most suitable for nonparametric tasks, e.g. tasks designed to build rankings.
