seznam = ["ahoj","Zdar"]
seznam1 = ["ahoj","Petr"]
test = []

for jmeno in seznam1:
    if jmeno in seznam:
        test.append(jmeno)

print(test)
