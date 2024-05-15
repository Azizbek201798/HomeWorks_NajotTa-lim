import os
os.system("cls")
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

def primes(x):
    for y in range(2, int(x**(0.5))+1):
        if x % y == 0:
            return False
    return True
        
class main_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640,480)
        self.setMinimumSize(640,480)
        # self.setStyleSheet("background-color:rgb(255,0,255)")

        self.lb =QLabel("Sonni kirit : ",self)
        self.lb.resize(200,50)
        self.lb.move(150,250)
        self.lb.setFont(QFont("Consolas",18))

        self.txt = QLineEdit(self)
        self.txt.setGeometry(360,250,200,50)
        self.txt.setFont(QFont("Calibri",20))
        self.txt.setEchoMode(QLineEdit.Password)
        # self.txt.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.btn = QPushButton("Next Window",self)
        self.btn.setGeometry(420,420,200,50)
        self.btn.setFont(QFont("Calibri",20))
        self.btn.clicked.connect(self.next_window)

    def next_window(self):
        self.window = second_window()
        s = ""
        for x in range(2,int(self.txt.text())):
            if primes(x) == True:
                s = s + str(x) + " , "
        self.window.lb1.setText(s)
        self.window.show()
        self.hide()

class second_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        # self.setStyleSheet("background-color:rgb(0,0,255)")
        
        self.lb1 = QLabel(self)
        self.lb1.setFont(QFont("Calibri",22))
        self.lb1.setStyleSheet("color:rgb(0,0,255)")
        self.lb1.setGeometry(50,275,600,50)

        self.btn1 = QPushButton("Main Menu",self)
        self.btn1.setGeometry(420,420,200,50)
        self.btn1.setFont(QFont("Consolas",20))
        self.btn1.clicked.connect(self.Asosiy_menu)

    def Asosiy_menu(self):
        self.win = main_menu()
        self.win.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = main_menu()
    oyna.show()
    sys.exit(app.exec_())