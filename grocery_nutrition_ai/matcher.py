import os
import pandas as pd
from rapidfuzz import process, fuzz

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "nutrition_master.csv")

df = pd.read_csv(DATA_PATH)

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Nutrition dataset not found at {DATA_PATH}")


# Build alias → row index mapping
alias_map = {}

for idx, row in df.iterrows():
    aliases = row["aliases"].split(",")
    for alias in aliases:
        alias_map[alias.strip()] = idx

alias_list = list(alias_map.keys())

def match_item(item_text):
    match, score, _ = process.extractOne(
        item_text,
        alias_list,
        scorer=fuzz.token_sort_ratio
    )

    if score >= 70:
        return df.iloc[alias_map[match]]

    return None
