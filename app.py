from flask import Flask, request, render_template, redirect, url_for
import pickle
import pandas as pd
from urllib.parse import urlparse

from features import extract_demo_features

app = Flask(__name__)

# ---------------- Load artifacts ----------------
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

with open("model/feature_means.pkl", "rb") as f:
    feature_means = pickle.load(f)

# ---------------- Helpers ----------------
def is_valid_url(url):
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except:
        return False

# ---------------- Routes ----------------
@app.route("/")
def home():
    return redirect(url_for("check"))

@app.route("/check", methods=["GET", "POST"])
def check():
    # GET request → just show page
    if request.method == "GET":
        return render_template("index.html")

    # POST request → process URL
    url = request.form.get("url", "").strip()

    if not is_valid_url(url):
        return render_template(
            "index.html",
            result="Invalid URL format",
            url=url
        )

    # Build full feature vector
    full_features = feature_means.copy()
    demo_features = extract_demo_features(url)

    for k, v in demo_features.items():
        if k in full_features:
            full_features[k] = v

    input_df = pd.DataFrame([full_features])[feature_columns]

    # Probability-based decision
    proba = model.predict_proba(input_df)[0]
    phishing_score = proba[0]   # label 0
    legit_score = proba[1]      # label 1

    if phishing_score >= 0.7:
        result = "Phishing"
    elif legit_score >= 0.7:
        result = "Legitimate"
    else:
        result = "Suspicious / Uncertain"

    return render_template(
        "index.html",
        result=result,
        url=url,
        phishing_score=round(phishing_score, 2),
        legit_score=round(legit_score, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
