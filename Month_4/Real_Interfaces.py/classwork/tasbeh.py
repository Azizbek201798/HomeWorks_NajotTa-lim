import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(300,200)
        self.setWindowIcon(QIcon("C:\\Users\\User\\Downloads\\tasbih.ico"))
        self.setMinimumSize(300,200)
        self.setWindowTitle("Tasbeh")
        self.setStyleSheet("background-color: rgb(0,0,0)")
        self.tablo = QLabel("0",self)
        self.tablo.setFont(QFont("Times New Roman",72))
        self.tablo.setGeometry(50,50,150,100)
        self.tablo.setStyleSheet("""
                color: rgb(0,0,0);
                background-color: rgb(57,255,20);
                border-radius: 10px;
                """)
        self.tablo.setAlignment(Qt.AlignCenter)
        
        self.btn = QPushButton("+",self)
        self.btn.setGeometry(205,50,50,50)
        self.btn.setFont(QFont("Times New Roman",18))
        self.btn.setStyleSheet("""
                color: rgb(0,0,255);
                background-color: rgb(255,255,250);
                border-radius: 25px;
                border-color: rgb(232,244,140);
                border-style: solid;
                border-width: 1px;
                """)
        self.btn.clicked.connect(self.function)

        self.btn1 = QPushButton("C",self)
        self.btn1.setGeometry(205,105,50,50)
        self.btn1.setFont(QFont("Times New Roman",18))
        self.btn1.setStyleSheet("""
                color: rgb(0,0,255);
                background-color: rgb(255,255,250);
                border-radius: 25px;
                border-color: rgb(232,244,140);
                border-style: solid;
                border-width: 1px;
                """)
        self.btn1.clicked.connect(self.clear)
    
    def clear(self):
        self.tablo.setText("0")
    
    def function(self):
        x = int(self.tablo.text())
        if x == 33:
            x = 0
        x = x + 1
        self.tablo.setText(str(x))
        
if __name__ == "__main__":
    ap = QApplication(sys.argv)
    pro = ilova()
    pro.show()
    sys.exit(ap.exec_())
    