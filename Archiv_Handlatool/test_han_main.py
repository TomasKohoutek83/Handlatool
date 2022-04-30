from test_han import Ui_Form

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon
import pandas as pd


class LoginWindow(qtw.QWidget,Ui_Form):

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.setupUi(self)
            self.browse.clicked.connect(self.otevri)
            self.pushButton.clicked.connect(self.uloz)


        def otevri(self): # funkce spusteni Browseru
         #print("Button pressed")   #kontrola funkcnosti po stisknuti Button
            self.open_dialog_box()
        
        def uloz(self):
            otevreny=self.lineEdit.text()
            #print("Button pressed")    kontrola funkcnosti
            self.label_4.setText(otevreny)
           

        def open_dialog_box(self):
            
            filename = QFileDialog.getOpenFileName()
            
            path = filename[0]
            df = pd.read_csv(path)
            sep_ident = df.Ident
            # print(sep_ident)
            path2 = path[-13:]        # separace csv 
            self.label_2.setText(path2)
        
        


    

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