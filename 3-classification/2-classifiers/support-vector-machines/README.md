# Classification - Support Vector Machines
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.


## 1. SVC Classification
`SVC`, `NuSVC`, and `LinearSVC` are classes capable of performing binary and multi-class classification on a dataset.

`SVC` and `NuSVC` are similar methods, but accept slightly different sets of parameters and have different mathematical formulations. 

On the other hand, `LinearSVC` is another implementation of Support Vector Classification for the case of a linear kernel. It also lacks some of the attributes of `SVC` and `NuSVC`, like support_. `LinearSVC` uses squared_hinge loss and due to its implementation in liblinear it also regularizes the intercept, if considered. This effect can however be reduced by carefully fine tuning its intercept_scaling parameter, which allows the intercept term to have a different regularization behavior compared to the other features. 
  
## 2. Multi-class Classification
`SVC` and `NuSVC` implement the "one vs one" approach for multi-class classification. In total, $n_classes * (n_classes -1) / 2$ classifiers are constructed and each one trains data from two classes. 

To provide a consistent interface with other classifiers, the `decision_function_shape` option allows to monotonically transform the results of "one vs one" classifiers to a "one vs rest" decision function of shape `(n_samples, n_classes)`, which is the default setting of the parameter.

## 3. Scores and Probabilities
The `decision_function method` of `SVC` and `NuSVC` gives per-class scores for each sample. When the constructor option `probability` is set to `True`, class membership probability estimates are enabled.

The cross-validation involved in Platt scaling is an expensive operation for large datasets. In addition, the probability estimates may be inconsistent with the scores:
- The "argmax" of the scores may not be the argmax of the probabilities
- In binary classification, a sample may be labeled by `predict` as belonging to the positive class even if the output of `predict_proba` is less than 0.5; and similarly, it could be labeled as negative even if the output of `predict_proba` is more than 0.5

## 4. Unbalanced problems
In problems where it is desired to give more importance to certain classes or certain individual samples, the parameters `class_weight` and `sample_weight` can be used.

`SVC` (but not `NuSVC`) implements the parameter `class_weight` in the `fit` method. It's a dictionary of the form `{class_label: value}`, where value is a floating point number > 0 that sets the parameter `C` of class `class_label` to `C * value`.

`SVC`, `NuSVC`, `SVR`, `NuSVR`, `LinearSVC`, `LinearSVR` and `OneClassSVM` implement also weights for individual samples in the `fit` method through the `sample_weight` parameter.
