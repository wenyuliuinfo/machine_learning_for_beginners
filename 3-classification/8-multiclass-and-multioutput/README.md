# Classification - Multiclass and Multioutput algorithms
This section of the user guide covers functionality related to multi-learning problems, including multiclass, multilabel, and multioutput classification and regression.

The modules in this section implement meta-estimators, which require a base estimator to be provided in their constructor. Meta-estimators extend the functionality of the base estimator to support multi-learning problems, which is accomplished by transforming the multi-learning problem into a set of simpler problems, then fitting one estimator per problem.

This section covers two modules: `sklearn.multiclass` and `sklearn.multioutput`. The chart below demonstrates the problem types that each module is for, and the corresponding meta-estimators that each module provides.

![Multi-learning-image](../images/multi_learning_chart.png)

## 1. Multiclass Classification
Multiclass classification is a classification task with more than two classes. Each sample can only be labeled as one class.

For example, classification using features extracted from a set of images of fruit, where each image may either be of an orange, an apply, or a pear. Each image is one sample and is labeled as one of the 3 possible classes. Multiclass classification makes the assumption that each sample is assigned to one and only one label - one sample cannot be both a pear and an apple.

While all scikit-learn classifiers are capable of multiclass classification, the meta-estimators offered by `sklearn.multiclass` can change the way they handle more than two classes because this may have an effect on classifier performances (either in terms of generalization error or required computational resources).

### 1.1 One vs One Classifier
The `OneVsOneClassifier` consists in fitting one classifier per class pair. At prediction time, the class with received the most votes is selected. Since it requires to fit `n_classes * (n_classes - 1)/2` classifiers, this method is usually slower than one-vs-rest, due to its O(n_classes^2) complexity. 

However, this method may be advantageous for algorithms such as kernel algorithms which don't scale well with `n_samples`. This is because each individual learning problem only involves a small subset of the data.

### 1.2 One vs Rest Classifier
The `OneVsRestClassifier` consists in fitting one classifier per class. For each classifier, the class is fitted against all the other classes. 

In addition to its computational efficiency (`n_classes` classifiers are needed), one advantage of this approach is its interpretability. Since each class is represented by one and only one classifier, it is possible to gain knowledge about the class by inspecting its corresponding classifier.

### 1.3 Output Code Classifier
The `OutputCodeClassifier` consists in representing each class with a binary code. At fitting time, one binary classifier per bit in the code book is fitted. At prediction time, the classifiers are used to project new points in the class space and the class closest to the points is chosen.

The main advantage of these strategies is that the number of classifiers used can be controlled by the user, either for compressing the model (0 < code_size < 1) or for making the model more robust to errors (code_size > 1).


## 2. Multilabel Classification
Multilabel classification (closely related to multioutput classification) is a classification task labeling each sample with `m` labels from `n_classes` possible classes, where `m` can be 0 to `n_classes` inclusive. This can be thought of as predicting properties of a sample that are not mutually exclusive.

Formally, a binary output is assigned to each class, for every sample. Positive classes are indicated with 1 and negative classes with 0 or -1. It is thus comparable to running `n_classes` binary classification tasks. This approach treats each label independently whereas multilabel classifiers may treat the multiple classes simultaneously, accounting for correlated behavior among them.

### 2.1 Multioutput Classifier
Multilabel classification suppport can be added to any classifier with `MultiOutputClassifier`. This strategy consists of fitting one classifier per target. This allows multiple target variable classifications. The purpose of this class is to extend estimators to be able to estimate a series of target functions that are trained on a single X predictor matrix to predict a series of responses.


## 3. Multiclass-Multiouput Classification
Multiclass-multioutput classification (also known as multitask classification) is a classification task which labels each sample with a set of non-binary preperties. Both the number of properties and the number of classes per property is greater than 2. A single estimator thus handles several joint classification tasks. This is both a generalization of the multilabel classification task, which only considers binary attributes, as well as a generalization of the multiclass classification task, where only one property is considered.

Note that all classifiers handling multiclass-multioutput tasks, support the multilabel classification task as a special scenario. Multitask classification is similar to the multioutput classification task with different model formulations.