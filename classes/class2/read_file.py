import csv

rows = []
count = 0

with open('data/foode.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        rows.append(row)
        count += 1
        if count == 1000:
            break

print(len(rows))

with open('data/foode_1000.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in rows:
        writer.writerow(row)

# import csv

# with open('data/foode_1000.csv', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['businessname'], row['descript'], row['violdesc'])