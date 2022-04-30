

import pandas as pd

df=pd.read_csv("R905031922.csv")

test = df.Ident
l2=list(test[0::])
l1=["R900029707","R900763363","R900029708","4654654"]

for znak in l1:
    if znak in l2:
        print(znak)
    else:
        print(znak)







