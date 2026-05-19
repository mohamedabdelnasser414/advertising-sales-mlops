import os
import joblib
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Define dataset and model paths.
input_file = "data/cleaned_data.csv"
model_output = "models/sales_model.pkl"

# Check cleaned dataset exists.
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Cleaned dataset not found: {input_file}")

# Load cleaned dataset.
df = pd.read_csv(input_file)

# Define input features and target variable.
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Linear Regression model.
model = LinearRegression()

# Train model.
model.fit(X_train, y_train)

# Make predictions.
predictions = model.predict(X_test)

# Evaluate model.
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

# Save trained model.
joblib.dump(model, model_output)

# Display results.
print("Model training complete")
print(f"Model saved to: {model_output}")
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")
