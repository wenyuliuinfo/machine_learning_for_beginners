# Classification - Gaussian Processes
Gaussian Processes (GP) are a nonparametric supervised learning method used to solve regression and probabilistic classification problems.

## 1. Gaussian Process Classification (GPC)
The `GaussianProcessClassifier` implements Gaussian processes (GP) for classification purposes, more specifically for probabilistic classification, where test predictions take the form of class probabilities. `GaussianProcessClassifier` places a GP prior on a latent function f, which is then taken through a link function to obtain the probabilistic classification. The latent function f is to allow a convenient formulation of the model.

The Gaussian processes prior mean is assumed to be zero. The prior's covariance is specified by passing a kernel object. The hyperparameters of the kernel are optimized during fitting of `GaussianProcessRegressor` by maximizing the log-marginal-likelihook based on the passed `optimizer`. As the log-marginal-likelihood may have multiple local optima, the optimizer can be started repeatedly by specifying `n_restarts_optimizer`. The first run is always starting from the initial hyperparameter values of the kernel; subsequent runs are from hyperparameter values that have been chosen randomly from the range of allowed values.

## 2. Multi-class Classification
`GaussianProcessClassifier` supports multi-class classification by performing either "one vs rest" or "one vs one" based training and prediction. In "one vs rest", one binary Gaussian process classifier is fitted for each class, which is trained to separate this class from the rest. In "one vs one", one binary Gaussian process classifier is fitted for each pair of classes, which is trained to separate these two classes. The predictions of these binary predictions are combined into multi-class predictions.

## 3. Kernels for Gaussian Processes
Kernels (also called "covariance functions") are an important factor of GPs which determine the shape of prior and posterior of the GP. They encode the assumptions on the function by defining the "similarity" of two datapoints combined with the assumption that similar datapoints should have similar target values. 

Two categories of kernels can be distinguished: stationary kernels depend only on the distance of two datapoints and not on their absolute values and thus invariant to translations in the input space, while non-stationary kernels depend also on the specific values of the datapoints.
