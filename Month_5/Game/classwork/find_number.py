import os
import sys
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system("cls")

class game(QMainWindow):
    __popitka = 0
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(""))
        self.setMaximumSize(800,300)
        self.setMinimumSize(800,300)
        self.setWindowTitle("Find Number")
        self.count = 0
        self.random_num = random.randint(1,100)

        self.lb1 = QLabel("Sonni kiriting : ",self)
        self.lb1.setFont(QFont("Times New Roman",25))
        self.lb1.setGeometry(100,100,200,50)

        self.lb2 = QLabel("TIMER",self)
        self.lb2.setFont(QFont("Times New Roman",18))
        self.lb2.setGeometry(500,20,100,50)

        self.lb3 = QLabel("0",self)
        self.lb3.setFont(QFont("Times New Roman",18))
        self.lb3.setGeometry(620,20,100,50)
        self.lb3.setStyleSheet("""color:rgb(0,255,0);
                              background-color:rgb(0,0,0);
                              border-color: rgb(0,0,255);
                              border-style:solid;
                              border-width: 4px;
                           """)
        self.lb3.setText(str(self.count))

        self.lb4 = QLabel(f"Siz {self.count} ta urinishda topdiz!",self)
        self.lb4.setFont(QFont("Times New Roman",18))
        self.lb4.setGeometry(200,200,400,50)
        self.lb4.setVisible(False)
        self.lb4.setStyleSheet("""color:rgb(255,0,0);
                           """)

        self.ln1 = QLineEdit(self)
        self.ln1.setFont(QFont("Times New Roman",25))
        self.ln1.setGeometry(320,100,200,50)
        
        self.btn = QPushButton("KIRIT",self)
        self.btn.setFont(QFont("Times New Roman",25))
        self.btn.setGeometry(540,100,100,50)
        self.btn.clicked.connect(self.kirit)

    def kirit(self,num):
        self.count += 1
        if self.ln1.text() == self.random_num:
            self.msg1 = QMessageBox("Yutdingiz!",self)
        else:
            pass
    
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyin = game()
    uyin.show()
    sys.exit(app.exec_())
        