import csv

with open('R905031922.csv') as file:
    csv_reader = csv.reader(file)

    for line in csv_reader:
        print(line)


