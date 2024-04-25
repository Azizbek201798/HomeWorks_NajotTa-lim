from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
os.system("clear")

class main_menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640,480)
        self.setMinimumSize(640,480)
        self.move(200,200)
        self.setStyleSheet("background-color:rgb(162,0,109)")
        self.btn = QPushButton("Next Window",self)
        self.btn.setGeometry(420,420,200,50)
        self.btn.setFont(QFont("Calibri",20))
        self.btn.clicked.connect(self.next_window)

        self.lb1 = QLabel("Number : ")
        self.setGeometry(100,100,200,50)
        self.ln1 = QLineEdit()
        self.setGeometry(100,200,200,50)

    def next_window(self):
        self.window = second_window()
        self.window.show()
        self.hide()

class second_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        self.setStyleSheet("background-color:rgb(74,93,35)")
        self.btn1 = QPushButton("Main Menu",self)
        self.btn1.setGeometry(420,420,200,50)
        self.btn1.setFont(QFont("Calibri",20))
        self.btn1.clicked.connect(self.Asosiy_menu)

    def Asosiy_menu(self):
        self.window = main_menu()
        self.window.show()
        self.hide()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pro = main_menu()
    pro.show()
    sys.exit(app.exec_())