import pandas as pd

df = pd.read_csv("careflow_100_patients_v3.csv")

# Check that it loaded and inspect its structure
print("First 5 rows:")
print(df.head())

print("\nRows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and missing values:")
df.info()