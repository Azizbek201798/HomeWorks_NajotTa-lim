import os
os.system("cls")
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class main_menu(QMainWindow):
    size = [8,9,10,11,12,14,16,18,20,22,24,26,28,30,36,42,48,72]
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1040,840)
        self.setMinimumSize(1040,840)
        self.setWindowTitle("Oynani tahrirlash")
        self.move(100,50)

        self.txt = QTextEdit(self)
        self.txt.setGeometry(10,100,600,600)

        self.cmb1 = QComboBox(self)
        self.cmb1.setGeometry(700,250,250,50)
        self.cmb1.addItems(["Arial","Calibri","Poor Richard","Times New Roman"])
        self.cmb1.setFont(QFont("Consolas",20))

        self.cmb2 = QComboBox(self)
        self.cmb2.setGeometry(700,320,250,50)
        for x in self.size:
            self.cmb2.addItem(str(x))
        self.cmb2.setFont(QFont("Consolas",20))

        self.btn = QPushButton("Edit Font",self)
        self.btn.setGeometry(700,380,250,50)
        self.btn.setFont(QFont("Consolas",22))
        self.btn.setStyleSheet("""
            color:rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: dotted;
            border-color:rgb(0,255,0)               
            """)
        self.btn.clicked.connect(self.edit_font)

        self.btn1 = QPushButton("Edit Color",self)
        self.btn1.setGeometry(700,450,250,50)
        self.btn1.setFont(QFont("Consolas",22))
        self.btn1.setStyleSheet("""
            color:rgb(255,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: dotted;
            border-color:rgb(255,255,0)               
            """)
        self.btn1.clicked.connect(self.edit_color)

        self.btn2 = QPushButton("Input Dialog",self)
        self.btn2.setGeometry(700,510,250,50)
        self.btn2.setFont(QFont("Consolas",22))
        self.btn2.setStyleSheet("""
            color:rgb(255,25,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: outset;
            border-color:rgb(255,25,0)               
            """)
        self.btn2.clicked.connect(self.dialog)

    def dialog(self):
        res = QInputDialog.getText(self,"Malumot kiritish : ","Ismingni kirit : ")
        if res[1]:
            self.txt.setText(res[0])

    def edit_font(self): 
        self.txt.setFont(QFont(self.cmb1.currentText(),int(self.cmb2.currentText())))

    def edit_color(self): 
        color = QColorDialog.getColor()
        if color.isValid():
            clr = "color:" + str(color.name()) + ";"
            self.txt.setStyleSheet(clr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = main_menu()
    oyna.show()
    sys.exit(app.exec_())