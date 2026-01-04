import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os


# Load dataset
data = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# Select numeric features only (drop label from X)
X = data.select_dtypes(include=["number"]).drop(columns=["label"])
y = data["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)

feature_columns = X.columns.tolist()
feature_means = X.mean().to_dict()

with open("model/feature_columns.pkl", "wb") as f:
    pickle.dump(feature_columns, f)

with open("model/feature_means.pkl", "wb") as f:
    pickle.dump(feature_means, f)

# Save trained model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print(data["label"].value_counts())

print("Model trained and saved successfully.")
