# Classification - Ensemble methods
Ensemble methods combine the predictions of several base estimators built with a given learning algorithm in order to improve generalizability/robustness over a single estimator.

Two very famous examples of ensemble methods are gradient-boosted trees and random forests.

## 1. Grandient-boosted Trees Classification
Grandient Tree Boosting or Gradient Boosted Decision Trees (GBDT) is a generalization of boosting to arbitrary differentiable loss functions. 

Scikit-learn provides two implementations of gradient-boosted trees: `HistGradientBoostingClassifier` vs `GradientBoostingClassifier` for classification, and the corresponding classes for regression. 

Gradient Boosting for classification builds an additive model in a forward stage-wise fasion; it allows for the optimization of arbitrary differentiable loss functions. In each stage `n_classes_` regression trees are fit on the negative gradient of the loss function, e.g. binary or multiclass log loss. Binary classification is a special case where only a single regression tree is built. `GradientBoostingClassifier` and `GradientBoostingRegressor` might be preferred for small sample sizes since binning may lead to split points that are too approximate in this setting.

## 2. Random Forests Classification
The `sklearn.ensemble` module includes two averaging algorithms based on randomized decision trees: the RandomForest algorithm and the Extra-Trees methods. Both algorithms are perturb-and-combine techniques specifically designed for trees. This means a diverse set of classifiers is created by introducing randomness in the classifier construction. The prediction of the ensemble is given as the averaged prediction of the individual classifiers.

In random forests (`RandomForestClassifier` and `RandomForestRegressor` classes), each tree in the ensemble is built from a sample drawn with replacement from the training set. When splitting each node during the construction of a tree, the best split is found through an exhaustive search of the features values of either all input features or a random subset of size `max_features`.

The purpose of these two sources of randomness is to decrease the variance of the forest estimator. Indeed, individual decision trees typically exhibit high variance and tend to overfit. The injected randomness in forests yield decision trees with somewhat decoupled prediction errors. By taking an average of those predictions, some errors can cancel out. Random forests achieve a reduced variance by combining diverse trees, sometimes at the cost of a slight increase in bias.
