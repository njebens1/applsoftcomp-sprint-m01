import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

Path("paper/figs").mkdir(parents=True, exist_ok=True)

df = pd.read_csv("data/preprocessed/merged.csv")

df["gdpcapita"] = pd.to_numeric(df["gdpcapita"], errors="coerce")
df["mortality_rate"] = pd.to_numeric(df["mortality_rate"], errors="coerce")
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df = df.dropna(subset=["gdpcapita", "mortality_rate", "year"])

# Scatter plot (color = year)
plt.figure(figsize=(8, 6))
sc = plt.scatter(df["gdpcapita"], df["mortality_rate"], c=df["year"])

plt.xlabel("GDP per capita")
plt.ylabel("Child mortality rate")
plt.title("Child mortality vs GDP per capita")
plt.colorbar(sc, label="Year")

plt.tight_layout()
plt.savefig("paper/figs/scatter.png", dpi=200)

print("SUCCESS: saved paper/figs/scatter.png")
