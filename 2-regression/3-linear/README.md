# Build a Regression Model using Scikit-learn: regression methods

## 1. Introduction
While visualization allows you to make sense of data, the real power of Machine Learning comes from training models. Models are trained on historic data to automatically capture data dependencies, and they allow you to predict outcomes for new data, which the model has not seen before.

In this lesson, you will learn about two types of regression: basic Linear Regression and Polynomial Regression, along with some of the math underlying these techniques.
Those models will allow us to predict pumpkin prices depending on different input data.

You are loading this data so to ask questions of it:
- When is the best time to buy pumpkins?
- What price can I expect of a miniature pumpkins?
- Should I buy them in half-bushel baskets or by the 1 and 1/9 bushel box?


## 2. Linear Regression
The goal of a linear regression exercise is to be able to plot a line to:
- **Show variable relations.** Show the relationship between variables
- **Make predictions.** Make accurate predictions on where a new datapoint would fall in relationship to that line.

It is typical of Least-squares Regression to draw this type of line. The term "least-squares" means that all the datapoints surrounding the regression line are squared and them added up.
Ideally, that final sum is as small as possible, because we want a low number of errors, or `least-squares`.

We do so since we want to model a line that has the least cumulative distance from all of our data points. We also square the terms before adding them since we are concerned with its magnitude rather than its direction.

### Correlation
One more term to understand is the **Correlation Coefficient** between given X and Y variables. Using a scatterplot, you can quickly visualize this coefficient. A plot with datapoints scattered in a neat line have high correlation, but a plot with datapoints scattered everywhere between X and Y have a low correlation.

A good linear regression model will be one that has a high correlation coefficient using the least-squares regression method with a line of regression.


## 3. Polynomial Regression
Another type of regression is Polynomial Regression. While sometimes there's a linear relationship between variables - the bigger the pumpkin in volume, the higher the price - sometimes these relationships cannot be plotted as a plane or straight line.

Polynomial regression creates a curved line to better fit nonlinear data. In our case, if we include a squared `DayOfYear` variable into input data, we should be able to fit our data with a parabolic curve, which will have a minimum at a certain point within the year.

Scikit-learn includes a helpful pipeline API to combine different steps of data processing together. A pipeline is a chain of estimators. In our case, we will create a pipeline that first adds polynomial features to the model, and then trains the regression.

Pipelines can be used in the same manner as the original `LinearRegression` object, i.e. we can `fit` the pipeline, and then use `predict` to get the prediction results.
Using polynomial regression, we can get slightly lower MSE and higher determination, but not significantly.


## 4. Categorical Features
In the ideal world, we want to be able to predict prices for different pumpkin varieties using the same model. However, `Variety` column is somewhat different from columns like `Month`, because it contains non-numeric values. Such columns are called **categorical**.

To take variety into account, we first need to convert it to nemeric form, or **encode** it. There are several way we can do it:
- **Simple numeric encoding** will build a table of different varieties, and then replace the variety name by an index in that table. This is not the best idea for linear regression, because linear regression takes the actual numeric value of the index, and adds it to the result, multiplying by some coefficient. 
- **One-hot encoding** will replace the `Variety` column by 4 different columns, one for each variety. Each column will contain `1` if the corresponding row is of a given variety, and `0` otherwise. This means that there will be four coefficients in linear regression, one for each pumpkin variety, responsible for "starting price" for that particular variety.
