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
        self.setWindowTitle("Oynani tahrirlash")
        self.move(100,50)

        self.txt = QTextEdit(self)
        self.txt.setGeometry(10,100,600,600)

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
        self.btn.clicked.connect(lambda: self.edit_font(main_menu.name))

    def edit_font(self,st): 
        print(st)
        font,res = QFontDialog.getFont()
        if res: 
            self.txt.setFont(font)
        else :
            print("Aziz oldin Ok ni")

        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = main_menu()
    oyna.show()
    sys.exit(app.exec_())