import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing cuisines
df = df.dropna(subset=["Cuisines"])

# Use first cuisine as target
df["Cuisine_Label"] = df["Cuisines"].apply(
    lambda x: x.split(",")[0].strip()
)

# Features
X = df[
    ["Price range", "Votes", "Aggregate rating"]
]

# Target
le = LabelEncoder()
y = le.fit_transform(df["Cuisine_Label"])

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n===== CUISINE CLASSIFICATION =====")
print("Accuracy:", accuracy)