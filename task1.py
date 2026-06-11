import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Dataset.csv")

# Handle Missing Values
df["Cuisines"] = df["Cuisines"].fillna("Unknown")

# Features
features = [
    "City",
    "Cuisines",
    "Average Cost for two",
    "Price range",
    "Votes",
    "Has Table booking",
    "Has Online delivery"
]

target = "Aggregate rating"

# Encode categorical columns
encoder = LabelEncoder()

for col in [
    "City",
    "Cuisines",
    "Has Table booking",
    "Has Online delivery"
]:
    df[col] = encoder.fit_transform(df[col])

# Input and Output
X = df[features]
y = df[target]

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n===== MODEL RESULTS =====")
print("MSE :", mse)
print("R2 Score :", r2)

# Feature Importance
importance = model.feature_importances_

plt.figure(figsize=(8,5))
plt.barh(features, importance)
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Feature Importance")
plt.tight_layout()

plt.savefig("outputs/feature_importance.png")

plt.show()