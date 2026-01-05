from flask import Flask, request, render_template, redirect, url_for
import pickle
import pandas as pd
from urllib.parse import urlparse

from features import extract_demo_features

app = Flask(__name__)

# Load model + columns
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/feature_columns.pkl", "rb") as f:
    FEATURE_COLUMNS = pickle.load(f)

def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return parsed.scheme in ["http", "https"] and bool(parsed.netloc)
    except:
        return False

@app.route("/")
def home():
    return redirect(url_for("check"))

@app.route("/check", methods=["GET", "POST"])
def check():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "")

        if not is_valid_url(url):
            return render_template("index.html",
                                   result="Invalid URL format",
                                   url=url)

        features = extract_demo_features(url)

        # Build dataframe in correct order
        input_df = pd.DataFrame([[features.get(col, 0) for col in FEATURE_COLUMNS]],
                                columns=FEATURE_COLUMNS)

        prediction = model.predict(input_df)[0]

        # Dataset definition:
        # 1 = Legitimate, 0 = Phishing
        if prediction == 1:
            result = "Legitimate"
        elif prediction == -1:
            result = " phishing"
        else:
            result = "Suspicious URL!"

    return render_template("index.html", result=result, url=url)

if __name__ == "__main__":
    app.run(debug=True)
