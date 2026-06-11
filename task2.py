import pandas as pd

# Load dataset
df = pd.read_csv("Dataset.csv")

# Remove missing cuisines
df = df.dropna(subset=["Cuisines"])

# User preferences
preferred_cuisine = "North Indian"
preferred_price_range = 3

# Filter restaurants
recommendations = df[
    (df["Cuisines"].str.contains(preferred_cuisine, case=False, na=False))
    & (df["Price range"] == preferred_price_range)
]

# Sort by rating
recommendations = recommendations.sort_values(
    by="Aggregate rating",
    ascending=False
)

# Top 10 recommendations
top_recommendations = recommendations[
    ["Restaurant Name",
     "Cuisines",
     "City",
     "Price range",
     "Aggregate rating"]
].head(10)

print("\n===== RESTAURANT RECOMMENDATIONS =====\n")
print(top_recommendations)