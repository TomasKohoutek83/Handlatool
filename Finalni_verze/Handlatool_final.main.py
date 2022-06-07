'''
Projekt Handlatool
Autor: Tomas Kohoutek
Popis zakladni funkce:
Handlatool slouzi k vytvoreni seznamu pro pripravu vyroby. Tento seznam obsahuje 
tri skupiny materialu Standart, Nestandart, Atyp. Tyto seznamy dale slouzi k 
priprave materialu VOSS do vyroby.

V prvnim kroku musi uzivatel uvest vyrobni cislo zakazky, zadat sekvencni cislo a
nacist soubor ve formatu csv , ktery je exportovan z programu Creo
nebo Invertor od odeleni END. Soubor musi obsahovat Ident,popis a pocet ks.

Pragram dale na pozadi dle vnorenych seznamu k jednotlivym sekvencnim cislum
porovna tyto seznamy s csv souborem.
Odstrani duplicity a vytvori excelovy soubor se tremi listy Standart, Nestandart
a Atyp.
V poslednim kroku tento excelovy soubor otevre.

# V procesu #
Dokoncit seznamy pro sekvencni cisla a vytvorit podminku pro trideni. 
Zajistit pomer otviraneho okna na zaklade nastaveni rozliseni uzivatele
Vlozeni loga do exe souboru

# Bude dopracovano #
Doplnit pres for loop trideni identu dle lokace - uprava Kanban Trackru
Vytvoreni exe souboru

# Potecnialni kroky #
Vytvoreni archivu hotovych seznamu pro analyzu spotreby nebo jinych bodu pro END a LOG
Rozsireni pro jine typy materialu napr: Spojovaci material, potrubi apod.

'''




# Importy 
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd
import numpy as py
import os

from Handlatool_final_QT import Ui_Form

# Seznamy standartu, nestandartu dle sekvencniho cisla pro (L - XXL)
standart_1= pd.DataFrame(
    {
        
        'Ident': ['R900762684', 'R900008261', 'R900766217', 'R900012455', 'R900012988', 'R900763364', 'R900766416', 'R900762671',
                  'R900766207', 'R900012446', 'R900029699', 'R900766405', 'R900012983', 'R900763356', 'R900762689', 'R900022320',
                  'R900766218', 'R900001263', 'R900012456', 'R900767713', 'R900763365', 'R900766417', 'R900762691', 'R900766219',
                  'R900029708', 'R900012990', 'R900012457', 'R900763447', 'R900766418', 'R900002865', 'R900762674', 'R900766209',
                  'R900012448', 'R900029700', 'R900012985', 'R900766408', 'R900763358', 'R900767707', 'R900762692', 'R900766221',
                  'R900012458', 'R900029707', 'R900763449', 'R900002866', 'R900767717', 'R900762675', 'R900766210', 'R900029710',
                  'R900012986', 'R900763359', 'R900012449', 'R900766409', 'R900762693', 'R900766222', 'R900029706', 'R900763448',
                  'R900012459', 'R900766421', 'R900012992', 'R900762676', 'R900766211', 'R900029701', 'R900766410', 'R900012450',
                  'R900012987', 'R900763360', 'R900764637'],
        }
                        )

nestandart_1= pd.DataFrame(
    {
        
        'Ident': ['R901331154','R900030251','R900002864','R900765435','R900765440','R900763650','R900764388','R900767712','R900764643',
                  'R901423992','R900763042','R900765429','R900765206','R901331163','R900765472','R900763641','R900765198','R900765183',
                  'R900763029','R900764632','R900764378','R900023270','R900765191','R901331772','R901423986','R900765182','R900006829',
                  'R900006366','R900763651','R900012989','R900763043','R900764389','R900764644','R900765441','R900765447','R900765433',
                  'R900765435','R900765434','R900765207','R900006026','R900006830','R900767715','R900763652','R900765448','R900764390',
                  'R900764645','R900763044','R901331781','R900765440','R900765208','R900765441','R901327071','R901331459','R900033085',
                  'R900765474','R900765198','R900764381','R900764634','R900763643','R900763034','R900765468','R901331784','R900765199',
                  'R900766420','R900012991','R900764646','R900764391','R900763653','R900765209','R900765448','R900765447','R900051970',
                  'R900763036','R900765503','R900780264','R900764635','R900764382','R900763644','R900765468','R900006832','R900767719',
                  'R900764647','R987202894','R900763654','R900764392','R900002867','R900765208','R900765209','R900765206','R900765207',
                  'R900022437','R901068211','R900765470','R900033078','R900764383','R900765473','R900763645','R900763037','R900765472',
                  'R900765474','R900765469','R900765503'],
    }
                            )

#Pridani nestanaartu 2 (velikost S)
nestandart_2 = pd.DataFrame(
    {
       
        'Ident': ['R900762671','R900766207','R900012446','R900029699','R900766405','R900012983','R900763356','R900762660','R900766203',
                  'R900762674','R900766209','R900012448','R900029700','R900012985','R900766408','R900763358','R900767707','R901331163',
                  'R900765472','R901327071','R901331459','R900033085','R900765474','R900763641','R900765198','R900765183','R900764381',
                  'R900764634','R900763643','R900763034','R900765173','R900765468','R901331784','R900012442','R900012979','R900775754',
                  'R900763352','R900763636','R900766401','R900764377','R900763029','R900764632','R900764378','R900023270','R900765191',
                  'R900765199','R900765182','R901331772','R901423986','R900765169','R900762693','R900766222','R900029706','R900763448',
                  'R900012459','R900766421','R900012992','R900763038','R900002862','R900775755','R900762677','R900766213','R900012451',
                  'R900766412','R900775756','R900765288','R900006832','R900765423','R900765421','R900767719','R900764647','R987202894',
                  'R900763654','R900765208','R900764392','R900002867','R900765209','R900763308','R900764639','R900763647','R900LV2828',
                  'R900764385','R900765206','R901331104','R900766639','R900765207','R900012980','R900762668','R900766204','R900029697',
                  'R900775758','R900765469','R900763026','R900766402','R901423983','R900763353','R900012443','R900764393','R900765174',
                  'R901331114','R900763637','R900765182','R900765169','R900767710','R900012452','R900009395','R900765433','R900765425',
                  'R900765421','R900767711','R900766415','R900763363','R900762682','R900029705','R900766216','R901331136','R900006827',
                  'R900002863','R900764642','R900763649','R900763041','R900764387','R900012454','R900765434','R900765425','R900765429',
                  'R900765423','R901331128','R900765470','R900764395','R900763638','R900012444','R901331760','R900764629','R900763028',
                  'R900023268','R900765183','R900765173','R900765174'],
    }
                               )

# Prirazeni oznaceni do Data Frame
standart_1 = standart_1.add_prefix("Standart_")
nestandart_1 = nestandart_1.add_prefix("Nestandart_")
# Pridan seznam pri velikost S
nestandart_2 = nestandart_2.add_prefix("Nestandart_")

sekvencni_cislo = []


# Zakladni trida
class LoginWindow(qtw.QWidget,Ui_Form):

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.setupUi(self)
            self.browse.clicked.connect(self.otevri)
            self.pushButton.clicked.connect(self.uloz)
            self.pushButton_2.clicked.connect(self.vytvor_seznam)
            self.pushButton_2.clicked.connect(self.open_exel)
            
           
        
# Ulozeni sek.cisla + vypis do lablu. Kontrola spravneho zapisu sek.cisla
        def uloz(self):                                                            
            otevreny=self.lineEdit.text()
            otevreny_2 = int(otevreny)
            
            if otevreny_2 < 7:
            #if otevreny_2 <60:
                self.label_4.setText(otevreny)
                sekvencni_cislo.append(otevreny_2)   
            else:
                self.label_4.setText("NEPLATNY ZAPIS!!!!")
        # Funkce spusteni Browseru
        

        def otevri(self):
            # Vytvoreni promene - otevreny soubor
            filename = QFileDialog.getOpenFileName()
            path = filename[0]
            # Pridany nazvy sloupcu do dataframu
            header_names=['Radek','Ident','Popis','Pocet','Zbytek']                  
            seznam_h= pd.read_csv(path,header=None,skiprows=1,names=header_names)
            # separace csv
            path2 = path[-13:] 
            self.label_2.setText(path2)
            
                   
# Funkce srovani seznamu - Standartni identy
            def srovnani_s(df):
                    if df['Ident'] == df['Standart_Ident']:
                        return 1
                    else:
                        return 0
                    
            def srovnani_n(df):
                    if df['Ident'] == df['Nestandart_Ident']:
                        return 1
                    else:
                        return 0    
            
            if sekvencni_cislo[0] == 1:
                    
                vedle_sebe_s = pd.merge(seznam_h, standart_1, how='outer', left_on='Ident', right_on='Standart_Ident')
                #vlozeni sloupce 'Jine_srovnani" dle Identu
                vedle_sebe_s['jine_srovnani']=vedle_sebe_s.apply(srovnani_s,axis=1)     
                # vypis jen konkretnich sloupcu
                uprava=vedle_sebe_s[['Radek','Ident','Popis','Pocet','Zbytek','jine_srovnani']]
                # vypis hodnoty True and False, dle hodnoty
                uprava[['jine_srovnani']]==1                 
                #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
                seznam_s_1=uprava[uprava["jine_srovnani"]==0]       
                #vypis cele tabulky dle ==1, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
                seznam_s_2=uprava[uprava["jine_srovnani"]==1]                              

            
                vedle_sebe_n = pd.merge(seznam_s_1, nestandart_1, how='outer', left_on='Ident', right_on='Nestandart_Ident')
                #vlozeni sloupce 'Porovnani" dle Identu
                vedle_sebe_n['porovnani']=vedle_sebe_n.apply(srovnani_n,axis=1) 
                #Vypis hodnot dle ==1 a sloupce srovnani        
                #vedle_sebe_n[vedle_sebe_n['porovnani'] == 1]                               
                uprava2=vedle_sebe_n[['Radek','Ident','Popis','Pocet','Zbytek','porovnani']]
                # vypis jen konkretnich sloupcu
                uprava2[['porovnani']]==1              
                #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka                                  
                seznam_s_3=uprava2[uprava2["porovnani"]==0]   
                #vypis cele tabulky dle ==1, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
                seznam_s_4=uprava2[uprava2["porovnani"]==1]                                  
                seznam_s_3_bez_duplicit = seznam_s_3.drop_duplicates(subset='Radek')
                
                # Vytvoreni exceloveho souboru Multisheet
                with pd.ExcelWriter(r'C:/Users/kot5brn/Documents/Python_kody/Handlatool/Multisheet.xlsx')as writer:

                    seznam_s_2.to_excel(writer, sheet_name='Standart')
                    seznam_s_4.to_excel(writer, sheet_name='Nestandart')
                    seznam_s_3_bez_duplicit.to_excel(writer, sheet_name='Atyp')
                
            else:
                vedle_sebe_n = pd.merge(seznam_h, nestandart_2, how='outer', left_on='Ident', right_on='Nestandart_Ident')
                vedle_sebe_n['porovnani'] = vedle_sebe_n.apply(srovnani_n, axis=1)                                                                                        
                uprava2 = vedle_sebe_n[['Radek', 'Ident','Popis', 'Pocet', 'Zbytek', 'porovnani']]                                                                                                                                                        
                seznam_s_6 = uprava2[uprava2["porovnani"] == 1]
         
                # Vytvoreni exceloveho souboru Multisheet
                with pd.ExcelWriter(r'C:/Users/kot5brn/Documents/Python_kody/Handlatool/Multisheet.xlsx')as writer:

                    seznam_s_6.to_excel(writer,sheet_name='Nestandart')
                    
                
        # Prejmenovani Mutlisheet souboru cislem zakazky             
        def vytvor_seznam(self):
            vypis_str =str(self.lineEdit_2.text())
            os.rename('C:/Users/kot5brn/Documents/Python_kody/Handlatool/Multisheet.xlsx',f'C:/Users/kot5brn/Documents/Python_kody/Handlatool/{vypis_str}.xlsx')
        # Automaticke otevreni excelu po jeho ulozeni 
        def open_exel(self):
            vypis_str =str(self.lineEdit_2.text())
            os.system(f'start "excel" C:/Users/kot5brn/Documents/Python_kody/Handlatool/{vypis_str}.xlsx"')  #doplneni funkce automatickeho otevreni exelu po vytvoreni excelu


if __name__ =='__main__':
    app=qtw.QApplication([])

    widget=LoginWindow()
    widget.show()
    app.exec_()

