import pandas as pd

df = pd.read_csv("123456789.csv")
sep_cislo_identu = df.pocet
sep_ident = df.Ident

# Typ agregatu L
standart_seznam = ('R900765441','R900029707','R900763447','R900764645','R900029705')
nestandart_seznam = ('R900766216','R900029708','R900766219')
atyp_seznam = ('R900763043','R900762691','R900767715','R900763044')

stan_mater = []
nest_mater = []
atyp_mater = []

sekvencni_cislo = str(input("Vypis sekvencni cislo (posledni tri cislice):"))
sep_sekvencni_cislo = int(sekvencni_cislo[1]) #prevod do int ze stringu

if sep_sekvencni_cislo == 1:
    
    vypis=list(sep_ident[0::])
    l1= standart_seznam
    l2= nestandart_seznam
    l3= atyp_seznam

    for znak in l1:
        if znak in vypis:
            stan_mater.append(znak)

    print(f"Standartni material je:{stan_mater}")
            
    for znak in l2:
        if znak in vypis:
            nest_mater.append(znak)
    print(f"Netandartni material je:{nest_mater}")    
    
    for znak in l3:
        if znak in vypis:
            atyp_mater.append(znak)

    print(f"Atypovy material je:{atyp_mater}")     
    

else:
    print(f"Sekvencni cislo je chybne!!!")





