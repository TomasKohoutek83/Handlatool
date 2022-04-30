from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon

import pandas as pd


class Ui_Form(object):
    def setupUi(self,Form):
        Form.setObjectName("Form")
        Form.resize(519,344)
        self.pushButton=QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80,130,113,32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self,Form):
        _translate=QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form","Form"))
        self.pushButton.setText(_translate("Form","Browse File"))
        self.pushButton.clicked.connect(self.pushButton_handler )    # Pridana funkce kliku



    def pushButton_handler(self):
        print("Button pressed")   #kontrola funkcnosti po stisknuti Button
        self.open_dialog_box()
    
    def open_dialog_box(self):                      #Otevreni okna Win
        filename = QFileDialog.getOpenFileName()
        path = filename[0]                          #Cteni csv
        df = pd.read_csv(path)
        sep_ident = df.Ident
        print(sep_ident)

     


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
