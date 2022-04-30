import csv


rows = []
with open('R905031922.csv', 'r') as csvfile: 
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data = ', '.join(row)
        rows.append(data)
# print(rows)


print(rows)



