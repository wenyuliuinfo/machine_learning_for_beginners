# Classification Methods for Machine Learning

Classification is a form of **Supervised Learning** that uses a lot of regression algorithms. There are generally two types of classification: binary classification and multiclass classification.

## Lessons
- [1. Linear Models](1-linear-models/README.md)
- [2. Support Vector Machines](2-support-vector-machines/README.md)
- [3. Stochastic Gradient Descent](3-stochastic-gradient-descent/README.md)
- [4. Nearest Neighbors](4-nearest-neighbors/README.md)
- [5. Gaussian Processes](5-gaussian-processes/README.md)
- [6. Decision Trees](6-decision-trees/README.md)
- [7. Ensemble Methods](7-ensemble-methods/README.md)
- [8. Multiclass and multioutput algorithms](8-multiclass-and-multioutput/README.md)


## 1. Choosing the classifier

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


### Reasoning
Reasoning through different approaches given the constraints we have:
- **Neural networks are too heavy.** Given our clean, but minimal dataset, and the fact that we are running training locally via notebooks, neural networks are too heavy weight for this task.
- **Decision tree or logistic regression.** A decision tree might work, or logistic regression for multiclass data.
- **Multiclass Boosted Decision Trees.** The multiclass boosted decision tree is most suitable for nonparametric tasks, e.g. tasks designed to build rankings.
