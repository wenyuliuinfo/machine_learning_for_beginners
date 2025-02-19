# Classification - Decision Trees
Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data featrues. A tree can be seen as a piecewise constant approximation.

For instance, in the example below, decision trees learn from data to approximate a sine curve with a set of if-then-else decision rules. The deeper the tree, the more complex the decision rules and the fitter the model.

## 1. Decision Trees Classification
`DecisionTreeClassifier` is a class capable of performing multi-class classification on a dataset.

As with other classifiers, `DecisionTreeClassifier` takes as input two arrays: an array X, sparse or dense, of shape (n_samples, n_features) holding the training samples, and an array y of integer values, shape (n_samples,), holding the class labels for the training samples.

## 2. Multi-class Classification
`DecisionTreeClassifier` is capable of both binary classification and multiclass classification.

In case that there are multiple classes with the same and highest probability, the classifier will predict the class with the lowest index amongst those classes.

## 3. Complexity
In general, the run time cost to construct a balanced binary tree is O(n_samples*n_features*log(n_samples)) and query time O(log(n_samples)). Although the tree construction algorithm attempts to generate balanced trees, they will not always be balanced. Assuming that the subtrees remain approximately balanced, the cost at each node consists of searching through O(n_features) to find the feature that offers the largest reduction in the impurity criterion.