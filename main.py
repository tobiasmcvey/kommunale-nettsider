import csv
import json

csv_file = 'kommuner.csv'
json_file = 'kommuner.json'

def read_CSV(file, json_file):
    csv_rows = []
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data ,ensure_ascii=False, sort_keys=False, indent=4, separators=(',', ': ')))

if __name__ == "__main__":
    read_CSV(csv_file,json_file)