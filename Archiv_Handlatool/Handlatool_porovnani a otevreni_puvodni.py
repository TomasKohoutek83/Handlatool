import pandas as pd
import numpy as py
import os


header_names=['Radek','Ident','Popis','Pocet','Zbytek']  # Pridany nazvy sloupcu
seznam_h=pd.read_csv("R920080633.csv", header=None,skiprows=1,names=header_names) # Precteni a pridani nazvu sloupcu

#seznam_h = pd.read_csv("123456789.csv")
#seznam_s = pd.read_csv("Standart.csv")
#seznam_n = pd.read_csv("Nestandart.csv")

#pridani dataframe pro velikosti agregatu (dle sekvencniho cisla)
standart_1= pd.DataFrame(
    {
        'Radek':[50,49,48,47,46,45,44],
        'Ident':['R900029707','R900029708',"R900022320","R900029705",'R900764645','R900763447','R900763363'],
        'Popis':['UNION NUT          24N/30S-ST3Z00Z','UNION NUT          24N/25S-ST3Z00Z','UNION NUT          24N/20S-ST3Z00Z','UNION NUT          24N-12S-ST3Z00Z','UNION              24T-Z-S-25S-ST3Z00Z','UNION              24S-Z-S-25S-ST3Z00Z','UNION              24S-Z-S-12S-ST3Z00Z'],
        'Pocet':[1,23,4,10,2,5,1],
        'Zbytek':[0,0,0,0,0,0,0],
        
    }
)

nestandart_1= pd.DataFrame(
    {
        'Radek':[34,33,32,31,30,29,28],
        'Ident':['R900762691',None,"R900763043",None,'R900763041',None,'R900762682'],
        'Popis':['MALE CONNECTOR     24SDS-E-S-25S-G1-ST3F00Z','MALE CONNECTOR     24SDS-E-S-25S-G1-ST3F00Z','MALE CONNECTOR     24SDS-E-S-20S-M27X2-ST3F00Z','MALE CONNECTOR     24SDS-E-S-20S-M27X2-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-M18X1 5-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-M18X1 5-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-G3/8-ST3F00Z'],
        'Pocet':[1,1,1,1,1,1,4,],
        'Zbytek':[0,0,0,0,0,0,0]
    }
)

seznam_h_bez_duplicit = seznam_h.drop_duplicates(subset='Popis')    # odstraneni duplicit ze sloupce popis, z duvodu nahrani pod sestav

seznam_h_bez_duplicit= seznam_h.add_prefix("123456789_")
standart_1 = standart_1.add_prefix("Standart_")
nestandart_1 = nestandart_1.add_prefix("Nestandart_")

vedle_sebe_s = pd.merge(seznam_h_bez_duplicit,standart_1,how='outer',left_on='123456789_Ident',right_on='Standart_Ident')

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

vedle_sebe_n = pd.merge(seznam_s_1,nestandart_1,how='outer',left_on='123456789_Ident',right_on='Nestandart_Ident')

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


#with pd.ExcelWriter(r'C:\Users\Tom\Documents\Tutorials\Handlatool\Multisheet.xlsx')as writer:
with pd.ExcelWriter(r'C:/Users/kot5brn/Documents\Multisheet.xlsx')as writer:
    seznam_s_2.to_excel(writer,sheet_name='Standart')
    seznam_s_4.to_excel(writer,sheet_name='Nestandart')
    seznam_s_3_bez_duplicit.to_excel(writer,sheet_name='Atyp')
os.system('start "excel" C:/Users/kot5brn/Documents\Multisheet.xlsx"')  #doplneni funkce automatoickeho otevreni exelu po vytvoreni excelu

    


print("Done")