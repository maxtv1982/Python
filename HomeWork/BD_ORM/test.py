import json


with open('tests_data.json', encoding="utf-8") as f:
    json_data = json.load(f)
for item in json_data:
    print(item["model"].capitalize())
    print(item["fields"])