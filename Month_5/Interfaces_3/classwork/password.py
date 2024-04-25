import os
os.system("cls")
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(400,200)
        self.setMinimumSize(400,200)
        self.setStyleSheet("""
            color : rgb(0,0,0);    
            border-radius: 15px;
            """)
        self.setFont(QFont("Times New Roman",32))

        self.lb1 = QLabel("Password",self)
        self.lb1.setFont(QFont("Times New Roman",20))
        self.lb1.setGeometry(20,10,200,40)

        self.lb2 = QLabel("must contain 8 char.",self)
        self.lb2.setFont(QFont("Times New Roman",15))
        self.lb2.setGeometry(20,150,200,40)
        if self.tap(self) == True:
            self.lb2.setStyleSheet("color:rgb(255,0,0)")
        else:
            self.lb2.setStyleSheet("color:rgb(0,125,10)")
        self.ln = QLineEdit(self)
        self.ln.setStyleSheet("""
            color : rgb(0,0,0);
            border-color: rgb(192,192,192);
            border-width: 3px;
            border-style: solid;
            """)
        self.ln.setGeometry(20,60,360,80)
        self.ln.setFont(QFont("Times New Roman",20))
        # self.ln.setEchoMode(QLineEdit.Password)
        self.ln.textChanged.connect(self.tap)

    def tap(self):
        digit_count = sum(char.isdigit() for char in self.ln.text())
        if digit_count < 2:
            return False

        uppercase_count = sum(char.isupper() for char in self.ln.text())
        if uppercase_count < 1:
            return False

        if len(self.ln.text()) < 8:
            return False
        return True
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ilova()
    oyna.show()
    sys.exit(app.exec_())