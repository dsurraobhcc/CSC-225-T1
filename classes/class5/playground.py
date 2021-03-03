import csv

with open('2020.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['neighborhood'] == 'Jamaica Plain':
            print(row['open_dt'], row['case_status'], row['case_title'],\
                row['type'], row['neighborhood'])