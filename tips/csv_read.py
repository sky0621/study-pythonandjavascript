import csv

with open('data/dummy.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
