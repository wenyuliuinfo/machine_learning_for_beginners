# Build the Flask web application
import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open("../ufo-model.pkl", "rb"))

# Create the home page
@app.route("/")
def home():
    return render_template("index.html")

# Create the /predict page
@app.route("/predict", methods=["POST"])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    countries = ["Australia", "Canada", "Germany", "UK", "US"]

    return render_template(
        "index.html", prediction_text="Likely country: {}".format(countries[output])
    )

if __name__=="__main__":
    app.run(debug=True)