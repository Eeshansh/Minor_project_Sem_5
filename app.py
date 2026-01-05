from flask import Flask, render_template, request
import pickle
import pandas as pd
from features import extract_features

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
feature_columns = pickle.load(open("features.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        features = extract_features(url)
        input_df = pd.DataFrame([features])[feature_columns]
        prediction = model.predict(input_df)[0]
        result = "Legitimate" if prediction == 1 else "Phishing"

    return render_template("index.html", result=result, url=url)

if __name__ == "__main__":
    app.run(debug=True)
