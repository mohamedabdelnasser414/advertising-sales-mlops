import os
import pandas as pd

# Define input and output file paths.
input_file = "data/Advertising_And_Sales.csv"
output_file = "data/cleaned_data.csv"

# Check that the original dataset exists before continuing.
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Dataset not found: {input_file}")

# Load the advertising sales dataset.
df = pd.read_csv(input_file, sep="\t")

# Clean column names by removing extra spaces.
df.columns = df.columns.str.strip()

# Remove ID column
if "ID" in df.columns:
    df.drop("ID", axis=1, inplace=True)

# Remove rows with missing values.
df.dropna(inplace=True)

# Remove duplicate rows if any exist.
df.drop_duplicates(inplace=True)

# Save the cleaned dataset.
df.to_csv(output_file, index=False)

# Display basic output for verification.
print("Data preprocessing complete")
print(f"Original dataset: {input_file}")
print(f"Cleaned dataset saved to: {output_file}")
print("Dataset shape:", df.shape)
print(df.head())
