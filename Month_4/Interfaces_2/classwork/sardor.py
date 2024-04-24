import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class ilova(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matematik Ifoda")

        self.lb1 = QLabel("Input:")
        self.ln1 = QLineEdit()
        self.lb2 = QLabel("Output:")
        self.ln2 = QLineEdit()

        self.calculate_button = QPushButton("Hisoblash")
        self.calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.lb1)
        layout.addWidget(self.ln1)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.lb2)
        layout.addWidget(self.ln2)
        self.setLayout(layout)

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
        count_digits = numbers

        for i in count_digits:
            res +=str(i)
            res += " "

        if count_digits == 0:
            self.ln2.setText("Matematik ifoda mavjud emas")
        else:
            self.ln2.setText(f"{res}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ilova()
    window.show()
    sys.exit(app.exec_())