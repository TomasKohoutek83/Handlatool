from Handlatool_final import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd
import numpy as py
import os

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
        'Ident':['R900762691','R900022325',"R900763043",'R900763042','R900763041','R900762689','R900762682'],
        'Popis':['MALE CONNECTOR     24SDS-E-S-25S-G1-ST3F00Z','MALE CONNECTOR     24SDS-E-S-25S-G1-ST3F00Z','MALE CONNECTOR     24SDS-E-S-20S-M27X2-ST3F00Z','MALE CONNECTOR     24SDS-E-S-20S-M27X2-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-M18X1 5-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-M18X1 5-ST3F00Z','MALE CONNECTOR     24SDS-E-S-12S-G3/8-ST3F00Z'],
        'Pocet':[1,1,1,1,1,1,4,],
        'Zbytek':[0,0,0,0,0,0,0]
    }
)

standart_1 = standart_1.add_prefix("Standart_")
nestandart_1 = nestandart_1.add_prefix("Nestandart_")



class LoginWindow(qtw.QWidget,Ui_Form):

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.setupUi(self)
            self.browse.clicked.connect(self.otevri)
            self.pushButton.clicked.connect(self.uloz)
            self.pushButton_2.clicked.connect(self.vytvor_seznam)
            self.pushButton_2.clicked.connect(self.open_exel)

        def otevri(self): # funkce spusteni Browseru
         #print("Button pressed")   #kontrola funkcnosti po stisknuti Button
            self.open_dialog_box()
        

        def uloz(self):
            otevreny=self.lineEdit.text()
            otevreny_2 = int(otevreny)
            #print("Button pressed")    kontrola funkcnosti
            if otevreny_2 <60:
                self.label_4.setText(otevreny)
            else:
                 self.label_4.setText("NEPLATNY ZAPIS")
            #vypis_vyrobni = self.lineEdit_2.text()
            
        

        def open_dialog_box(self):
            
            filename = QFileDialog.getOpenFileName()
            
            path = filename[0]
            header_names=['Radek','Ident','Popis','Pocet','Zbytek']  # Pridany nazvy sloupcu
            seznam_h= pd.read_csv(path,header=None,skiprows=1,names=header_names) 
            sep_ident = seznam_h.Ident
            # print(sep_ident)
            path2 = path[-14:]        # separace csv 
            self.label_2.setText(path2)


            #header_names=['Radek','Ident','Popis','Pocet','Zbytek']  # Pridany nazvy sloupcu
            #seznam_h=pd.read_csv('R123456789',header=None,skiprows=1,names=header_names) # Precteni a pridani nazvu sloupcu
            seznam_h_bez_duplicit = seznam_h.drop_duplicates(subset='Popis')
            
            vedle_sebe_s = pd.merge(seznam_h_bez_duplicit,standart_1,how='outer',left_on='Ident',right_on='Standart_Ident')

            def srovnani_s(df):
                if df['Ident'] == df['Standart_Ident']:
                    return 1
                else:
                    return 0
            vedle_sebe_s['jine_srovnani']=vedle_sebe_s.apply(srovnani_s,axis=1) #vlozeni sloupce 'Jine_srovnani" dle Identu
            uprava=vedle_sebe_s[['Radek','Ident','Popis','Pocet','Zbytek','jine_srovnani']] # vypis jen konkretnich sloupcu
            uprava[['jine_srovnani']]==1 # vypis hodnoty True and False, dle hodnoty
            seznam_s_1=uprava[uprava["jine_srovnani"]==0] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
            seznam_s_2=uprava[uprava["jine_srovnani"]==1] #vypis cele tabulky dle ==1, pridanim  .index na konec vypise v radku cisla radku kterych se tyka


            
            vedle_sebe_n = pd.merge(seznam_s_1,nestandart_1,how='outer',left_on='Ident',right_on='Nestandart_Ident')

            def srovnani_n(df):
                if df['Ident'] == df['Nestandart_Ident']:
                    return 1
                else:
                     return 0

            vedle_sebe_n['porovnani']=vedle_sebe_n.apply(srovnani_n,axis=1) #vlozeni sloupce 'Jine_srovnani" dle Identu
            vedle_sebe_n[vedle_sebe_n['porovnani'] == 1] #Vypis hodnot dle ==1 a sloupce srovnani

            uprava2=vedle_sebe_n[['Radek','Ident','Popis','Pocet','Zbytek','porovnani']] # vypis jen konkretnich sloupcu
            uprava2[['porovnani']]==1 # vypis hodnoty True and False, dle hodnoty
            seznam_s_3=uprava2[uprava2["porovnani"]==0] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka
            seznam_s_4=uprava2[uprava2["porovnani"]==1] #vypis cele tabulky dle ==0, pridanim  .index na konec vypise v radku cisla radku kterych se tyka

            seznam_s_3_bez_duplicit = seznam_s_3.drop_duplicates(subset='Radek')

            with pd.ExcelWriter(r'C:\Users\Tom\Documents\Tutorials\Handlatool\Multisheet.xlsx')as writer:
            
#with pd.ExcelWriter(r'C:/Users/kot5brn/Documents\Multisheet.xlsx')as writer:
                seznam_s_2.to_excel(writer,sheet_name='Standart')
                seznam_s_4.to_excel(writer,sheet_name='Nestandart')
                seznam_s_3_bez_duplicit.to_excel(writer,sheet_name='Atyp')
                #os.rename(f'C:/Users/Tom\Documents/Tutorials/Handlatool/Multisheet.xlsx','C:/Users/Tom/Documents/Tutorials/Handlatool/{vypis_vyrobni}.xlsx')
        def vytvor_seznam(self):
            vypis_vyrobni = self.lineEdit_2.text()
            vypis_str =str(self.lineEdit_2.text())
            
            os.rename('C:/Users/Tom/Documents/Tutorials/Handlatool/Multisheet.xlsx',f'C:/Users/Tom/Documents/Tutorials/Handlatool/{vypis_str}.xlsx')
            #os.system(f'start "excel" C:/Users/kot5brn/Documents/Python - kody/Handlatool/{vypis_str}.xlsx"')  #doplneni funkce automatoickeho otevreni exelu po vytvoreni excelu

        def open_exel(self):
            vypis_vyrobni = self.lineEdit_2.text()
            vypis_str =str(self.lineEdit_2.text())
            os.system(f'start "excel" C:/Users/Tom/Documents/Tutorials/Handlatool/{vypis_str}.xlsx"')  #doplneni funkce automatoickeho otevreni exelu po vytvoreni excelu

        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())


if __name__ =='__main__':
    app=qtw.QApplication([])

    widget=LoginWindow()
    widget.show()
    app.exec_()