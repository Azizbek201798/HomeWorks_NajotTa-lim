import os
os.system("cls")
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class main_menu(QMainWindow):
    name = "Font Dialog"
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1040,840)
        self.setMinimumSize(1040,840)
        self.move(100,50)
        self.txt = QTextEdit(self)
        self.txt.setGeometry (80,100,600,600)
        self.btn = QPushButton("Edit Font", self)
        self.btn.setGeometry(700,380,250,50)
        self.btn.setFont(QFont("Consolas", 22))
        self.btn.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-radius: 15px;
            border-width: 3px;
            border-style: dotted;
            border-color: rgb(0,255,0);
            """)

        self.btn.clicked.connect(lambda: self.edit_font(main_menu.name))

        self.cmb = QFontComboBox(self)
        self.cmb.setFont(QFont("Times New Roman",24))
        self.cmb.setGeometry(700,100,300,40)
        self.cmb.addItems(["Arial","Calibri","Times New Roman"])

    def edit_font(self,st):
        print(st)
        res = QFontDialog.getFont()
        print(res)
        if res[1]:
            self.txt.setFont(res[0])
        else:
            print("Najim oldin Okni bos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mm = main_menu()
    mm.show()
    sys.exit(app.exec_())