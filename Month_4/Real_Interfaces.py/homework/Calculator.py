import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
os.system("clear")

class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(800,950)
        self.setMinimumSize(800,950)
        self.setGeometry(600,0,800,950)
        self.setWindowIcon(QIcon(""))
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color:rgb(255,165,0)")

        phone = QLabel(self)
        phone.setStyleSheet("""
            background-color:   rgb(0,0,0);
            border-color:       rgb(85,93,80);
            border-radius:      70px;
            border-width:       6px;
            border-style:       solid;""")
        phone.setGeometry(185,20,450,910)

        self.lnt1 = QLineEdit(self)
        self.lnt1.resize(350,50)
        self.lnt1.setStyleSheet("""
            background-color:   rgb(0,0,0);
            color:              rgb(255,255,255);
            border-radius:      15px;
            border-style:       solid;""")
        self.lnt1.setFont(QFont("Times New Roman",15))
        self.lnt1.move(250,250)
        self.lnt1.setAlignment(Qt.AlignRight)

        self.lnt2 = QLineEdit(self)
        self.lnt2.resize(350,100)
        self.lnt2.setStyleSheet("""
            background-color:   rgb(0,0,0);
            color:              rgb(255,255,255);
            border-radius:      15px;
            border-style:       solid;""")
        self.lnt2.setFont(QFont("Times New Roman",70))
        self.lnt2.move(250,300)
        self.lnt2.setAlignment(Qt.AlignRight)

        self.C_button = QPushButton("C",self)
        self.C_button.setStyleSheet("""
            background-color:   rgb(192,192,192);
            color:              rgb(0,0,0);
            border-radius:      45px;
            border-width:       6px;
            border-style:       solid;""")
        self.C_button.setGeometry(220,400,90,90)
        self.C_button.setFont(QFont("Times New Roman",45))

        self.Puls_Minus = QPushButton("+/-",self)
        self.Puls_Minus.setStyleSheet("""
            background-color:   rgb(192,192,192);
            color:              rgb(0,0,0);
            border-radius:      45px;
            border-width:       6px;
            border-style:       solid;""")
        self.Puls_Minus.setGeometry(320,400,90,90)
        self.Puls_Minus.setFont(QFont("Times New Roman",33))

        self.percent = QPushButton("%",self)
        self.percent.setStyleSheet("""
            background-color:   rgb(192,192,192);
            color:              rgb(0,0,0);
            border-radius:      45px;
            border-width:       6px;
            border-style:       solid;""")
        self.percent.setGeometry(420,400,90,90)
        self.percent.setFont(QFont("Times New Roman",42))

        self.div = QPushButton("÷",self)
        self.div.setStyleSheet("""
            background-color:   rgb(255,165,0);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.div.setGeometry(520,400,90,90)
        self.div.setFont(QFont("Times New Roman",55))

        self.mult = QPushButton("x",self)
        self.mult.setStyleSheet("""
            background-color:   rgb(255,165,0);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.mult.setGeometry(520,500,90,90)
        self.mult.setFont(QFont("Times New Roman",38))

        self.sub = QPushButton("-",self)
        self.sub.setStyleSheet("""
            background-color:   rgb(255,165,0);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.sub.setGeometry(520,600,90,90)
        self.sub.setFont(QFont("Times New Roman",43))

        self.add = QPushButton("+",self)
        self.add.setStyleSheet("""
            background-color:   rgb(255,165,0);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.add.setGeometry(520,700,90,90)
        self.add.setFont(QFont("Times New Roman",35))

        self.equal = QPushButton("=",self)
        self.equal.setStyleSheet("""
            background-color:   rgb(255,165,0);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.equal.setGeometry(520,800,90,90)
        self.equal.setFont(QFont("Times New Roman",35))

        self.seven = QPushButton("7",self)
        self.seven.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.seven.setGeometry(220,500,90,90)
        self.seven.setFont(QFont("Times New Roman",40))

        self.eight = QPushButton("8",self)
        self.eight.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.eight.setGeometry(320,500,90,90)
        self.eight.setFont(QFont("Times New Roman",40))

        self.nine = QPushButton("9",self)
        self.nine.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.nine.setGeometry(420,500,90,90)
        self.nine.setFont(QFont("Times New Roman",40))

        self.six = QPushButton("6",self)
        self.six.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.six.setGeometry(420,600,90,90)
        self.six.setFont(QFont("Times New Roman",40))

        self.five = QPushButton("5",self)
        self.five.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.five.setGeometry(320,600,90,90)
        self.five.setFont(QFont("Times New Roman",40))

        self.four = QPushButton("4",self)
        self.four.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.four.setGeometry(220,600,90,90)
        self.four.setFont(QFont("Times New Roman",40))

        self.three = QPushButton("3",self)
        self.three.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.three.setGeometry(420,700,90,90)
        self.three.setFont(QFont("Times New Roman",40))

        self.two = QPushButton("2",self)
        self.two.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.two.setGeometry(320,700,90,90)
        self.two.setFont(QFont("Times New Roman",40))

        self.one = QPushButton("1",self)
        self.one.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.one.setGeometry(220,700,90,90)
        self.one.setFont(QFont("Times New Roman",40))

        self.dot = QPushButton(".",self)
        self.dot.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.dot.setGeometry(420,800,90,90)
        self.dot.setFont(QFont("Times New Roman",45))

        self.zero = QPushButton("0",self)
        self.zero.setStyleSheet("""
            background-color:   rgb(52,52,52);
            color:              rgb(255,255,255);
            border-radius:      45px;
            border-style:       solid;""")
        self.zero.setGeometry(220,800,190,90)
        self.zero.setFont(QFont("Times New Roman",40))
        
        # Har bir operator tugmasi bosilganda ularni obyektga qo'llash!
        self.C_button.clicked.connect(self.clear_display)
        self.Puls_Minus.clicked.connect(self.plus_minus_sign)
        self.percent.clicked.connect(self.calculate_percent)
        self.div.clicked.connect(self.div_clicked)
        self.mult.clicked.connect(self.mult_clicked)
        self.sub.clicked.connect(self.operator_clicked)
        self.add.clicked.connect(self.operator_clicked)
        self.equal.clicked.connect(self.calculate_result)

        # Har bir raqam tugmasi bosilganda ularni obyektga qo'llash!
        self.zero.clicked.connect(lambda: self.number_clicked("0"))
        self.one.clicked.connect(lambda: self.number_clicked("1"))
        self.two.clicked.connect(lambda: self.number_clicked("2"))
        self.three.clicked.connect(lambda: self.number_clicked("3"))
        self.four.clicked.connect(lambda: self.number_clicked("4"))
        self.five.clicked.connect(lambda: self.number_clicked("5"))
        self.six.clicked.connect(lambda: self.number_clicked("6"))
        self.seven.clicked.connect(lambda: self.number_clicked("7"))
        self.eight.clicked.connect(lambda: self.number_clicked("8"))
        self.nine.clicked.connect(lambda: self.number_clicked("9"))
        self.dot.clicked.connect(lambda: self.number_clicked("."))

    def clear_display(self):
        self.lnt2.clear()
        self.lnt1.clear()

    def plus_minus_sign(self):
        current_text = self.lnt2.text()
        if current_text and current_text[0] == "-":
            self.lnt2.setText(current_text[1:])
        else:
            self.lnt2.setText("-" + current_text)

    def calculate_percent(self):
        current_text = self.lnt2.text()
        if current_text:
            percent_value = float(current_text) / 100
            self.lnt2.setText(str(percent_value))

    def operator_clicked(self):
        button = self.sender()
        operator = button.text()
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + " " + operator)
        self.lnt2.clear()

    def mult_clicked(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + " " + "*")
        self.lnt2.clear()

    def div_clicked(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + " " + "//")
        self.lnt2.clear()

    def number_clicked(self, number):
        current_text = self.lnt2.text()
        self.lnt2.setText(current_text + number)

    def calculate_result(self):
        expression = self.lnt1.text() + " " + self.lnt2.text()
        try:
            result = eval(expression)
            self.lnt1.setText(expression + " = "+str(result))
            self.lnt2.setText(str(result))
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pro = ilova()
    pro.show()
    sys.exit(app.exec_())

