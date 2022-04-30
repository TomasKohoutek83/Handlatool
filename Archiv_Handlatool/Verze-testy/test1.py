import csv

with open("R905031922.csv") as infile:
    reader = csv.reader(infile)
    radek=[]
    for line in reader:
        radek.append(line[1:])
        print(radek)