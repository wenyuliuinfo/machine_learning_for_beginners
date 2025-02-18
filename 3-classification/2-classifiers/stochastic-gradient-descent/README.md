# Classification - Stochastic Gradient Descent
Stochastic Gradient Descent (SGD) is a simple yet very efficient approach to fitting linear classifiers and regressors under convex loss functions such as (linear) Support Vector Machines and Logistic Regression. Even though SGD has been around in the machine learning community for a long time, it has received a considerable amount of attention just recently in the context of large-scale learning.

SGD has been successfully applied to large-scale and sparse machine learning problems often encountered in text classification and natural language processing. Often, an instance of `SGDClassifier` or `SGDRegressor` will have an equivalent estimator in the scikit-learn library, potentially using a different optimization technique.

## 1. SGD Classification
The class `SGDClassifier` implements a plain stochastic gradient descent learning routine which supports different loss functions for classification. 

SGD has to be fitted with two arrays: an array `X` of shape (n_samples, n_features) holding the training samples, and an array `y` of shape (n_samples) holding the target values for the training samples.

## 2. Multi-class Classification
`SGDClassifier` supports multi-class classification by combining multiple binary classifiers in a "one vs rest" scheme. For each of the K classes, a binary classifier is learned that discriminates between that and all other K-1 classes. At testing time, we compute the confidence score (i.e. the signed distances to the hyperplane) for each classifier and choose the class with the highest confidence.

## 3. Complexity
The major advantage of SGD is its efficiency, which is basically linear in the number of training examples. If `X` is a matrix of size (n, p) training has a cost of O(knp), where k is the number of iterations and p is the average number of non-zero attributes per sample.
