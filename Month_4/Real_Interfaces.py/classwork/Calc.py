import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
os.system("clear")

class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(640,950)
        self.setMinimumSize(640,950)
        self.setWindowTitle("Calculator")
        self.setGeometry(0,0,640,950)
        self.setStyleSheet("background-color: rgb(255,143,0)")
    
        self.phone = QLabel(self)
        self.phone.setGeometry(100,30,440,890)
        self.phone.setStyleSheet("""
            background-color: rgb(0,0,0);               
            border-radius: 65px;
            border-color: rgb(128,128,128);
            border-width: 6px;
            border-style: solid;
        """)

        self.C_button = QPushButton("C",self)
        self.C_button.setGeometry(130,400,80,80)
        self.C_button.setFont(QFont("Times New Roman",32))
        self.C_button.setStyleSheet("""
            background-color: rgb(169,169,169);
            border-radius: 40px;                                                                          
        """)

        self.one = QPushButton("1",self)
        self.one.setGeometry(130,500,80,80)
        self.one.setFont(QFont("Times New Roman",32))
        self.one.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;                                                                          
        """)

        self.two = QPushButton("2",self)
        self.two.setGeometry(230,500,80,80)
        self.two.setFont(QFont("Times New Roman",32))
        self.two.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;                                                                          
        """)

        self.three = QPushButton("3",self)
        self.three.setGeometry(330,500,80,80)
        self.three.setFont(QFont("Times New Roman",32))
        self.three.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);                     
            border-radius: 40px;                                                                          
        """)

        self.six = QPushButton("6",self)
        self.six.setGeometry(330,600,80,80)
        self.six.setFont(QFont("Times New Roman",32))
        self.six.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);                   
            border-radius: 40px;                                                                          
        """)

        self.five = QPushButton("5",self)
        self.five.setGeometry(230,600,80,80)
        self.five.setFont(QFont("Times New Roman",32))
        self.five.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;     
                                                                    
        """)

        self.four = QPushButton("4",self)
        self.four.setGeometry(130,600,80,80)
        self.four.setFont(QFont("Times New Roman",32))
        self.four.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;    
        """)

        self.seven = QPushButton("7",self)
        self.seven.setGeometry(130,700,80,80)
        self.seven.setFont(QFont("Times New Roman",32))
        self.seven.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;                                                                          
        """)

        self.eight = QPushButton("8",self)
        self.eight.setGeometry(230,700,80,80)
        self.eight.setFont(QFont("Times New Roman",32))
        self.eight.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;                                                                          
        """)

        self.nine = QPushButton("9",self)
        self.nine.setGeometry(330,700,80,80)
        self.nine.setFont(QFont("Times New Roman",32))
        self.nine.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);                    
            border-radius: 40px;                                                                          
        """)

        self.zero = QPushButton("0",self)
        self.zero.setGeometry(130,800,170,80)
        self.zero.setFont(QFont("Times New Roman",32))
        self.zero.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);                    
            border-radius: 40px;                                                                          
        """)

        self.dot = QPushButton(".",self)
        self.dot.setGeometry(330,800,80,80)
        self.dot.setFont(QFont("Times New Roman",32))
        self.dot.setStyleSheet("""
            background-color: rgb(52,52,52);
            color: rgb(255,255,255);
            border-radius: 40px;                                                                          
        """)
        
        self.plus_minus = QPushButton("+/-",self)
        self.plus_minus.setGeometry(230,400,80,80)
        self.plus_minus.setFont(QFont("Times New Roman",32))
        self.plus_minus.setStyleSheet("""
            background-color: rgb(169,169,169);
            border-radius: 40px;                                                                          
        """)

        self.percent_equal = QPushButton("%",self)
        self.percent_equal.setGeometry(330,400,80,80)
        self.percent_equal.setFont(QFont("Times New Roman",32))
        self.percent_equal.setStyleSheet("""
            background-color: rgb(169,169,169);
            border-radius: 40px;                                                                          
        """)

        self.div = QPushButton("÷",self)
        self.div.setGeometry(430,400,80,80)
        self.div.setFont(QFont("Times New Roman",40))
        self.div.setStyleSheet("""
            color: rgb(255,255,255);                   
            background-color: rgb(255,143,0);
            border-radius: 40px;                                                                          
        """)

        self.mult = QPushButton("x",self)
        self.mult.setGeometry(430,500,80,80)
        self.mult.setFont(QFont("Times New Roman",40))
        self.mult.setStyleSheet("""
            color: rgb(255,255,255);                   
            background-color: rgb(255,143,0);
            border-radius: 40px;                                                                          
        """)

        self.sub = QPushButton("-",self)
        self.sub.setGeometry(430,600,80,80)
        self.sub.setFont(QFont("Times New Roman",40))
        self.sub.setStyleSheet("""
            color: rgb(255,255,255);                   
            background-color: rgb(255,143,0);
            border-radius: 40px;                                                                          
        """)

        self.addition = QPushButton("+",self)
        self.addition.setGeometry(430,700,80,80)
        self.addition.setFont(QFont("Times New Roman",40))
        self.addition.setStyleSheet("""
            color: rgb(255,255,255);                   
            background-color: rgb(255,143,0);
            border-radius: 40px;                                                                          
        """)

        self.equal = QPushButton("=",self)
        self.equal.setGeometry(430,800,80,80)
        self.equal.setFont(QFont("Times New Roman",40))
        self.equal.setStyleSheet("""
            color: rgb(255,255,255);                   
            background-color: rgb(255,143,0);
            border-radius: 40px;                                                                          
        """)

        self.lnt1 = QLineEdit(self)
        self.lnt1.setFont(QFont("Tmes New Roman",12))
        self.lnt1.resize(400,40)
        self.lnt1.move(130,260)
        self.lnt1.setStyleSheet("""
            color:rgb(255,255,255);
            background-color: rgb(0,0,0);     
            border-style: solid;               
            """)
        self.lnt1.setAlignment(Qt.AlignRight)

        self.lnt2 = QLineEdit(self)
        self.lnt2.setFont(QFont("Tmes New Roman",48))
        self.lnt2.resize(400,100)
        self.lnt2.move(130,290)
        self.lnt2.setStyleSheet("""
            color:rgb(255,255,255);
            background-color: rgb(0,0,0);
            border-style: solid;                    
            """)
        self.lnt2.setAlignment(Qt.AlignRight)

        # Operator bosilganda ularni obyekga qo'llash;
        self.C_button.clicked.connect(self.clear_display)
        self.addition.clicked.connect(self.plus_number)
        self.sub.clicked.connect(self.sub_number)
        self.div.clicked.connect(self.div_number)
        self.mult.clicked.connect(self.mult_number)
        self.equal.clicked.connect(self.Result_equal)
        self.percent_equal.clicked.connect(self.calculate_percent)
        self.plus_minus.clicked.connect(self.plus_minus_s)

        #Raqamlar kiritilganda ularni textga yozish;
        self.zero.clicked.connect(lambda : self.number_clicked("0"))
        self.one.clicked.connect(lambda : self.number_clicked("1"))
        self.two.clicked.connect(lambda : self.number_clicked("2"))
        self.three.clicked.connect(lambda : self.number_clicked("3"))
        self.four.clicked.connect(lambda : self.number_clicked("4"))
        self.five.clicked.connect(lambda : self.number_clicked("5"))
        self.six.clicked.connect(lambda : self.number_clicked("6"))
        self.seven.clicked.connect(lambda : self.number_clicked("7"))
        self.eight.clicked.connect(lambda : self.number_clicked("8"))
        self.nine.clicked.connect(lambda : self.number_clicked("9"))
        self.dot.clicked.connect(lambda : self.number_clicked("."))

    def clear_display(self):
        self.lnt1.clear()
        self.lnt2.clear()

    def calculate_percent(self):
        current_text = self.lnt2.text()
        if current_text:    
            percent = float(current_text) / 100
            self.lnt2.setText(str(percent))

    def plus_minus_s(self):
        current_text = self.lnt2.text()
        if current_text and current_text[0] == "-":
            current_text = current_text[1:]
        else :
            self.lnt2.setText("-" + current_text)

    def plus_number(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + "+")
        self.lnt2.clear()

    def sub_number(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + "-")
        self.lnt2.clear()

    def div_number(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + "/")
        self.lnt2.clear()
    
    def mult_number(self):
        current_text = self.lnt2.text()
        self.lnt1.setText(current_text + "*")
        self.lnt2.clear()

    def number_clicked(self,number):
        current_text = self.lnt2.text()
        self.lnt2.setText(current_text + number)        

    def Result_equal(self):
        expression = self.lnt1.text() + self.lnt2.text()
        result = eval(expression)
        self.lnt1.setText(expression + " = " + str(result))
        self.lnt2.setText(str(result)) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pro = ilova()
    pro.show()
    sys.exit(app.exec_())

# unset GTK_PATH