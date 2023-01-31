import csv
import json
from pathlib import Path

def generate_json_file():
    print("Generating icon.json from icon.csv...")

    icon_array = []

    csvPath = Path(__file__).parent / "../../../csvs/english/icon.csv"
    jsonPath = Path(__file__).parent / "../../../json/english/icon.json"

    with csvPath.open(newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        next(reader)

        for row in reader:
            icon_object = {}

            icon_object['icon'] = row[0]
            icon_object['description'] = row[1]

            icon_array.append(icon_object)

    json_object = json.dumps(icon_array, indent=4, ensure_ascii=False)

    with jsonPath.open('w', newline='\n', encoding='utf8') as outfile:
        outfile.write(json_object)

    print("Successfully generated icon.json\n")