# Classification - Linear Models
Linear Models are a set of methods intended for regression/classification in which the target value is expected to be a linear combination of the features.


## 1. Ridge Classification
The `Ridge` regressor has a classifier variant: `RidgeClassifier`. This classifier first converts binary targets to `{-1, 1}` and then treats the problem as a regression task, optimizing the same objective as Ridge regression. The predicted class corresponds to the sign of the regressor's prediction. For multiclass classification, the problem is treated as multi-output regression, and the predicted class corresponds to the output with the highest value.

The `RidgeClassifier` can be significantly faster than e.g. `LogitsticRegression` with a high number of classes because it can compute the projection matrix only once.

## 2. Ridge Complexity
This method has the same order of complexity as Ordinary Least Squares.

The least squares solution is computed using the singular value decomposition of X. If X is a matrix of shape `(n_samples, n_features)` this method has a cost of O(n_samples*n_features^2), assuming n_samples >= n_features.
