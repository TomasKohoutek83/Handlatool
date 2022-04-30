import pandas as pd
import numpy as py

seznam_h = pd.read_csv("123456789.csv")
seznam_s = pd.read_csv("Standart.csv")
seznam_n = pd.read_csv("Nestandart.csv")

seznam_h = seznam_h.add_prefix("123456789_")
seznam_s = seznam_s.add_prefix("Standart_")
seznam_n = seznam_n.add_prefix("Nestandart_")

vedle_sebe_s = pd.merge(seznam_h,seznam_s,how='outer',left_on='123456789_Ident',right_on='Standart_Ident')

def srovnani_s(df):
    if df['123456789_Ident'] == df['Standart_Ident']:
          return 1
    else:
          return 0


vedle_sebe_s['jine_srovnani']=vedle_sebe_s.apply(srovnani_s,axis=1) #vlozeni sloupce 'Jine_srovnani" dle Identu
vedle_sebe_s[vedle_sebe_s['jine_srovnani'] == 1] #Vypis hodnot dle ==1 a sloupce srovnani

uprava=vedle_sebe_s[['123456789_Radek','123456789_Ident','123456789_Popis','123456789_Pocet','123456789_Zbytek','jine_srovnani']] # vypis jen konkretnich sloupcu
uprava[['jine_srovnani']]==1 # vypis hodnoty True and False, dle hodnoty

seznam_s_1=uprava[uprava["jine_srovnani"]==0] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
seznam_s_2=uprava[uprava["jine_srovnani"]==1] #vypis cele tabulky dle ==1, pridanim  .index na konec vypise v radku cisla radku kterych se tyka

########################        Druha cast kodu              ##########################

vedle_sebe_n = pd.merge(seznam_s_1,seznam_n,how='outer',left_on='123456789_Ident',right_on='Nestandart_Ident')

def srovnani_n(df):
    if df['123456789_Ident'] == df['Nestandart_Ident']:
          return 1
    else:
          return 0


vedle_sebe_n['porovnani']=vedle_sebe_n.apply(srovnani_n,axis=1) #vlozeni sloupce 'Jine_srovnani" dle Identu
vedle_sebe_n[vedle_sebe_n['porovnani'] == 1] #Vypis hodnot dle ==1 a sloupce srovnani


uprava2=vedle_sebe_n[['123456789_Radek','123456789_Ident','123456789_Popis','123456789_Pocet','123456789_Zbytek','porovnani']] # vypis jen konkretnich sloupcu
uprava2[['porovnani']]==1 # vypis hodnoty True and False, dle hodnoty

seznam_s_3=uprava2[uprava2["porovnani"]==0] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
seznam_s_4=uprava2[uprava2["porovnani"]==1] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka



###########################    Odstraneni duplicitz z Atypu  a tisk do excelu   #######################

seznam_s_3_bez_duplicit = seznam_s_3.drop_duplicates(subset='123456789_Radek')

with pd.ExcelWriter(r'C:\Users\Tom\Documents\Tutorials\Handlatool\Multisheet.xlsx')as writer:
    seznam_s_2.to_excel(writer,sheet_name='Standart')
    seznam_s_4.to_excel(writer,sheet_name='Nestandart')
    seznam_s_3_bez_duplicit.to_excel(writer,sheet_name='Atyp')

print("Done")
