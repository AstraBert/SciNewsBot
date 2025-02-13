import pandas as pd

csv = pd.read_csv("mbfc_raw.csv")
df = csv.dropna()
df.to_csv("mbfc_processed.csv", index=False)