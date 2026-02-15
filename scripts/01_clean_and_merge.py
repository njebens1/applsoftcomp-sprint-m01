import pandas as pd
from pathlib import Path

# create output folder

Path("data/preprocessed").mkdir(parents=True, exist_ok=True)


# 1) LOAD CHILD MORTALITY DATA


mort = pd.read_csv("data/raw/child-motality.csv")

# rename country columns to consistent names

mort = mort.rename(columns={
"Country Code": "geo",
"Country Name": "name"
})

# convert wide → long (this is the MOST important step)

mort_long = mort.melt(
id_vars=["geo", "name"],
var_name="year",
value_name="mortality_rate"
)

# convert year to number

mort_long["year"] = pd.to_numeric(mort_long["year"], errors="coerce")

# remove rows with no data

mort_long = mort_long.dropna(subset=["mortality_rate", "year"])


# 2) LOAD GDP DATA


gdp = pd.read_csv("data/raw/gdp-data.csv")

gdp = gdp.rename(columns={
"Country Code": "geo",
"Country Name": "name"
})

gdp_long = gdp.melt(
id_vars=["geo", "name"],
var_name="year",
value_name="gdpcapita"
)

gdp_long["year"] = pd.to_numeric(gdp_long["year"], errors="coerce")
gdp_long = gdp_long.dropna(subset=["gdpcapita", "year"])


# 3) MERGE DATASETS


merged = pd.merge(
mort_long,
gdp_long[["geo", "year", "gdpcapita"]],
on=["geo", "year"],
how="inner"
)

# ensure correct column order

merged = merged[["geo", "name", "year", "mortality_rate", "gdpcapita"]]


# 4) SAVE OUTPUT


merged.to_csv("data/preprocessed/merged.csv", index=False)

print("SUCCESS: merged dataset created!")
