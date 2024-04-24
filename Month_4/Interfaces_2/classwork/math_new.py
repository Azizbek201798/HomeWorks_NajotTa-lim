import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class ilova(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(500,300)
        self.setMinimumSize(500,300)
        self.setFont(QFont("Times New Roman",24))
        self.setWindowTitle("Matimatik Ifoda")

        self.lb1 = QLabel("Input(Kiruvchi qiymat) : ")
        self.ln1 = QLineEdit()
        self.btn = QPushButton("Calculate")
        self.btn.clicked.connect(self.calculate)
        self.lb2 = QLabel(f"Output(Chiquvchi ma'lumot) : \n{self.calculate}")
        
        vb = QVBoxLayout()
        vb.addWidget(self.lb1)
        vb.addStretch()
        vb.addWidget(self.ln1)
        vb.addStretch()
        vb.addWidget(self.btn)
        vb.addStretch()
        vb.addWidget(self.lb2)
        self.setLayout(vb)

    def calculate(self):
        res = ""
        exp = self.ln1.text()
        exp = exp.replace("+"," ")
        exp = exp.replace("-"," ")
        exp = exp.replace("/"," ")
        exp = exp.replace("*"," ")
        exp = exp.replace("("," ")
        exp = exp.replace(")"," ")
        numbers = [int(x) for x in exp.split(" ") if x.isdigit()]
        numbers.sort()
        numbers.reverse()
        for x in numbers:
            res += str(x)
            res += " "

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ilova()
    oyna.show()
    sys.exit(app.exec_())