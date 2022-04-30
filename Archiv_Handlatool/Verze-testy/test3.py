import csv

f = open('R905031922.csv')
reader = csv.reader(f)

radek=[]
for row in reader:
    radek.append(row[1])
print(radek)

f.close()  


   
