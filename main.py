import os
import json
import csv

# path to your json files
json_files_path = 'source/'

# output CSV file
csv_file_path = 'output.csv'

# list to hold all extracted data
all_data = []

# loop through each json file
for filename in os.listdir(json_files_path):
    if filename.endswith('.json'):
        with open(os.path.join(json_files_path, filename)) as json_file:
            data = json.load(json_file)
            all_data.append(data)

# write data to CSV
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=data.keys())
    csv_writer.writeheader()
    csv_writer.writerows(all_data)
