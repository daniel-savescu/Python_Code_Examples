import csv

with open('emp.csv','r') as f:
    r = csv.reader(f)
    data = list(r)
    for row in data:
        for column in row:
            print(column,'\t', end='')
        print()