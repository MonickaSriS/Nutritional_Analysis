import json
import sys
from ocr import extract_text
from analyzer import analyze

image_path = sys.argv[1]

text = extract_text(image_path)
nutrition = analyze(text)

recommendation = (
    "Consider buying smaller quantities of high-calorie items like rice and oil. "
    "Add more vegetables and protein-rich pulses to balance nutrition."
)

output = {
    "nutrition": nutrition,
    "recommendation": recommendation
}

print(json.dumps(output))
