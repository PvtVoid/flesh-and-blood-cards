import csv
import json
from pathlib import Path

def generate_json_file():
    print("Generating foiling.json from foiling.csv...")

    foiling_array = []

    csvPath = Path(__file__).parent / "../../../csvs/english/foiling.csv"
    jsonPath = Path(__file__).parent / "../../../json/english/foiling.json"

    with csvPath.open(newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        next(reader)

        for row in reader:
            foiling_object = {}

            foiling_object['id'] = row[0]
            foiling_object['name'] = row[1]

            foiling_array.append(foiling_object)

    json_object = json.dumps(foiling_array, indent=4, ensure_ascii=False)

    with jsonPath.open('w', newline='\n', encoding='utf8') as outfile:
        outfile.write(json_object)

    print("Successfully generated foiling.json\n")