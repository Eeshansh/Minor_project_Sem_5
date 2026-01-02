from flask import Flask
import pickle
from flask import request, jsonify
from features import extract_features



app = Flask(__name__)

@app.route("/")
def home():
    return "Phishing URL Detection API is running"

if __name__ == "__main__":
    app.run(debug=True)

   
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL not provided"}), 400

    # Extract features
    features = extract_features(url)
    features_df = pd.DataFrame([features])

    # Predict
    prediction = model.predict(features_df)[0]

    result = "Phishing" if prediction == 1 else "Legitimate"

    return jsonify({
        "url": url,
        "prediction": result
    })