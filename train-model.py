import pandas as pd
from features import extract_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
# Load dataset
data = pd.read_csv("PhiUSIIL_Phishing_URL_Dataset.csv")

# Convert URLs to feature vectors
feature_list = []
for url in data['url']:
    feature_list.append(extract_features(url))

X = pd.DataFrame(feature_list)
y = data['label']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)


rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)


print("Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))
print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))


with open("model/model.pkl", "wb") as f:
    pickle.dump(rf, f)