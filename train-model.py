import pandas as pd
import pickle
from scipy.io import arff
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

# Load ARFF dataset
data, meta = arff.loadarff("Training_Dataset.arff")
df = pd.DataFrame(data)

# Convert target to int
df["Result"] = df["Result"].astype(int)

# Split features and label
X = df.drop(columns=["Result"])
y = df["Result"]

# Save feature names (FREEZE)
feature_columns = X.columns.tolist()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Create model directory
os.makedirs("model", exist_ok=True)

# Save model and columns
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("model/feature_columns.pkl", "wb") as f:
    pickle.dump(feature_columns, f)

print("Model trained and saved successfully")
