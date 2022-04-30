import pandas as pd
import numpy as np


df = pd.read_csv("123456789.csv")
df1 = pd.read_csv("Standart.csv")
#sep_cislo_identu = df.pocet
#sloupce = ["Ident","pocet"]
#sep_ident=df.Ident
#sep_ident = df[["Ident","pocet"]] # pristup ke dvou sloupcum
#print(sep_ident)
#print(df)
#print(sep_ident)

result1 = df[~df.apply(tuple,1).isin(df1.apply(tuple,1))]
print(result1)




# Typ agregatu L
standart_seznam = ('R900765441','R900029707','R900763447','R900764645','R900029705')
nestandart_seznam = ('R900766216','R900029708','R900766219')
atyp_seznam = ('R900763043','R900762691','R900767715','R900763044')

data=pd.DataFrame(standart_seznam)  #vytvoreni dataframu z listu
print(type(data))





# stan_mater = []
# nest_mater = []
# atyp_mater = []

# sekvencni_cislo = str(input("Vypis sekvencni cislo (posledni dve cislice):"))
# sep_sekvencni_cislo = int(sekvencni_cislo[1]) #prevod do int ze stringu

# if sep_sekvencni_cislo == 1:
    
#     vypis=list(sep_ident[0::])
    
#     l1= standart_seznam
#     l2= nestandart_seznam


#     for znak in l1:
#         if znak in vypis:
#             stan_mater.append(znak)

#     print(f"Standartni material je:{stan_mater}")
            
#     for znak in l2:
#         if znak in vypis:
#             nest_mater.append(znak)
#     print(f"Netandartni material je:{nest_mater}")    
    
#     for znak in vypis:
#         if znak not in l1 and l2:
#             atyp_mater.append(znak)

#     print(f"Atypovy material je:{atyp_mater}")     
    
# else:
#     if sep_sekvencni_cislo >3:
#         print("Spatne zadane skvencni cislo!!!")


# __init__.py      prazdny soubor
# https://www.geeksforgeeks.org/python-main-function/?fbclid=IwAR1CFPv4pNW9VAN-ZdzbHIRCegFPo4n9FOAfqhbp_ZVov12MbR6llGCTgJ4    -- stranka s main 
# vyhledat main funkci nebo import, volani funkci y jinych file
# https://www.edureka.co/blog/python-main-function/     -- main