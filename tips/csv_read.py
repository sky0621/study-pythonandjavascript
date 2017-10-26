import csv

with open('data/dummy.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

with open('data/dummy.csv') as f:
    reader = csv.DictReader(f)
    print(list(reader))
