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

def rule_based_detection(url):
    score = 0

    if len(url) > 75:
        score += 1
    if "@" in url:
        score += 1
    if url.count(".") > 4:
        score += 1
    if "-" in url:
        score += 1
    if not url.startswith("https"):
        score += 1
    if any(word in url.lower() for word in ["login", "verify", "update", "secure", "account"]):
        score += 1

    return "Phishing" if score >= 2 else "Legitimate"



@app.route("/")
def home():
    return redirect(url_for("check"))

@app.route("/check", methods=["GET", "POST"])
def check():
    result = None
    url = ""
    mode = "rule" 

    if request.method == "POST":
        url = request.form.get("url", "")
        mode = request.form.get("mode", "rule")  # rule = default

        if not is_valid_url(url):
            return render_template(
                "index.html",
                result="Invalid URL format",
                url=url,
                mode=mode
            )

        # RULE-BASED (DEFAULT)
        if mode == "rule":
            result = rule_based_detection(url)

        # ML-BASED (EXPERIMENTAL)
        elif mode == "ml":
            features = extract_demo_features(url)

            input_df = pd.DataFrame(
                [[features.get(col, 0) for col in FEATURE_COLUMNS]],
                columns=FEATURE_COLUMNS
            )

            prediction = model.predict(input_df)[0]

            # ARFF definition: 1 = Legit, -1 = Phishing
            result = "Legitimate" if prediction == 1 else "Phishing"

    return render_template(
    "index.html",
    result=result,
    url=url,
    mode=mode
)

if __name__ == "__main__":
    app.run(debug=True)
