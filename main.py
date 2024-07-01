"""
Converts csv to json, and json to csv

Allows special characters in other languages such as æøå in Norwegian
"""

import csv
import json

CSV_FILE = 'kommuner.csv'
JSON_FILE = 'kommuner.json'

def read_CSV(csv_file, json_file):
    """
    Reads CSV and writes to JSON
    """
    csv_rows = []
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        write_json(csv_rows, json_file)

def write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data ,ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': ')))

def read_json(json_file):
    return json.loads(open(json_file).read())

def write_csv(data, csv_file):
    """
    Reads JSON and writes CSV
    """
    with open(csv_file, 'w+') as outf:
        writer = csv.DictWriter(outf, data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    write_json(data=read_CSV,json_file=JSON_FILE)
    # write_csv(data=read_json(json_file=JSON_FILE), csv_file=CSV_FILE)