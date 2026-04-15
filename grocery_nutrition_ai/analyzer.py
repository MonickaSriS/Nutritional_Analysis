import re
from matcher import match_item

def normalize_quantity(text):
    text = text.lower()

    if "kg" in text:
        return float(re.findall(r"\d+\.?\d*", text)[0]) * 1000
    if "gm" in text or "g " in text:
        return float(re.findall(r"\d+\.?\d*", text)[0])
    if "lb" in text:
        return float(re.findall(r"\d+\.?\d*", text)[0]) * 453
    if "oz" in text:
        return float(re.findall(r"\d+\.?\d*", text)[0]) * 28

    return 100  # fallback 100g

def extract_item_name(line):
    # Remove numbers, prices, units
    line = line.lower()
    line = re.sub(r'\d+\.?\d*', '', line)   # remove numbers
    line = re.sub(r'kg|gm|g|pcs|pc|pieces|tpces', '', line)
    line = re.sub(r'rs|₹', '', line)
    line = re.sub(r'\s+', ' ', line)
    return line.strip()

def analyze(text):
    total = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}

    for line in text.split("\n"):
        clean_name = extract_item_name(line)


        if len(clean_name) < 3:
            continue

        food = match_item(clean_name)

        if food is not None:
            qty = normalize_quantity(line)
            factor = qty / 100

            total["calories"] += food.calories_per_100g * factor
            total["protein"] += food.protein_per_100g * factor
            total["carbs"] += food.carbs_per_100g * factor
            total["fat"] += food.fat_per_100g * factor

    return total

