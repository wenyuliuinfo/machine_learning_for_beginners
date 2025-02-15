# Build a Web Application

In this lesson, you will train an ML model on a data set that's out of this world: UFO sightings over the past century.

You will learn:
- How to select a trained model
- How to use that model in a Flask app

We will continue our use of notebooks to clean data and train our model, but you can take the process one step further by exploring using a model in a web app.

## 1. Building an application
There are several ways to build web apps to consume machine learning models. Your web architecture may influence the way your model is trained. Imagine that you are working in a business where the data science group has trained a model that they want you to use in an app.

There are many questions you need to ask:
- **Is it a web app or a mobile app?** If you are building a mobile app or need to use the model in an IoT context, you could use `TensorFlow Lite` and use the model in an Android or iOS app.
- **Where will the model reside?** In the cloud or on-premises.
- **What technology was used to train the model?** The chosen technology may influence the tooling you need to use.
  - **Using TensorFlow** If you are training a model using TensorFlow, for example, that ecosystem provides the ability to convert a TensorFlow model for use in a web app by using `TensorFlow.js`.
  - **Using PyTorch** If you are building a model using a library such as `PyTorch`, you have the option to export it in ONNX (Open Neural Network Exchange) format for use in JavaScript web apps that can use the ONNX Runtime. This option will be explored in a future lession for a Scikit-learn-trained model.
  - **Using Lobe.ai** If you are using an ML SaaS (Software as a Service) system such as Lobe.ai to train a model, this type of software provides ways to export the model for many platforms, including building an API to be queried in the cloud by your online application.


## 2. Libraries
For this lesson, you can use two different Python libraries: Flask and Pickle.

**Flask** Defined as a 'micro-framework' by its creators, Flask provides the basic features of web frameworks using Python and a templating engine to build web pages. 

**Pickle** Pickle is a Python module that serializes and de-serializes a Python object structure. When you select a model, you serialize or flatten its structure for use on the web.

