import pandas as pd

df = pd.read_csv("careflow_patients_data.csv")

print(df.head(100))
print(df.columns)