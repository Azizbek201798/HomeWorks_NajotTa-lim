# Task - 1 => DONE by Azizbek

# 	RadioButtondan foydalanib 5ta test tuzing. Agar to'g'ri javob belgilansa +1bal 
# 	qo'shilsin va agar noto'g'ri bo'lsa bal qo'shilmasin va oxirida umumiy bali chiqsin.

import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class ilova(QMainWindow):
    def __init__(self,nm):
        super().__init__()
        self.name = nm
        self.setMaximumSize(750,920)
        self.setMinimumSize(750,920)
        self.setWindowTitle("Test.uz")
        self.ls = {}

        self.tst1 = QLabel("1. Ispaniya davlati poytaxti nima?",self)
        self.tst1.setFont(QFont("Times New Roman",24))
        self.tst1.setGeometry(30,30,600,50)
        self.tst1.setStyleSheet("color:rgb(255,0,255)")
    
        self.a1 = QRadioButton("Toshkent",self)
        self.a1.setFont(QFont("Times New Roman",24))
        self.a1.setGeometry(60,90,600,50)
        self.a1.setStyleSheet("color:rgb(0,0,255)")
        self.a1.clicked.connect(lambda: self.save_answer(1,"Toshkent"))

        self.a2 = QRadioButton("Samarqand",self)
        self.a2.setFont(QFont("Times New Roman",24))
        self.a2.setGeometry(60,150,600,50)
        self.a2.setStyleSheet("color:rgb(0,0,255)")
        self.a2.clicked.connect(lambda: self.save_answer(1,"Samarqand"))

        self.a3 = QRadioButton("Termiz",self)
        self.a3.setFont(QFont("Times New Roman",24))
        self.a3.setGeometry(300,150,600,50)
        self.a3.setStyleSheet("color:rgb(0,0,255)")
        self.a3.clicked.connect(lambda: self.save_answer(1,"Termiz"))

        self.a4 = QRadioButton("Madrid",self)
        self.a4.setFont(QFont("Times New Roman",24))
        self.a4.setGeometry(300,90,600,50)
        self.a4.setStyleSheet("color:rgb(0,0,255)")
        self.a4.clicked.connect(lambda: self.save_answer(1,"Madrid"))

        self.tst2 = QLabel("2. Leo Messida nechta oltin to'p bor?",self)
        self.tst2.setFont(QFont("Times New Roman",24))
        self.tst2.setGeometry(30,210,600,50)
        self.tst2.setStyleSheet("color:rgb(255,0,255)")

        self.b1 = QRadioButton("5 ta",self)
        self.b1.setFont(QFont("Times New Roman",24))
        self.b1.setGeometry(60,270,600,50)
        self.b1.setStyleSheet("color:rgb(0,0,255)")
        self.b1.clicked.connect(lambda: self.save_answer(2,"5 ta"))

        self.b2 = QRadioButton("8 ta",self)
        self.b2.setFont(QFont("Times New Roman",24))
        self.b2.setGeometry(60,330,600,50)
        self.b2.setStyleSheet("color:rgb(0,0,255)")
        self.b2.clicked.connect(lambda: self.save_answer(2,"8 ta"))

        self.b3 = QRadioButton("1 ta",self)
        self.b3.setFont(QFont("Times New Roman",24))
        self.b3.setGeometry(300,270,600,50)
        self.b3.setStyleSheet("color:rgb(0,0,255)")
        self.b3.clicked.connect(lambda: self.save_answer(2,"1 ta"))

        self.b4 = QRadioButton("10 ta",self)
        self.b4.setFont(QFont("Times New Roman",24))
        self.b4.setGeometry(300,330,600,50)
        self.b4.setStyleSheet("color:rgb(0,0,255)")
        self.b4.clicked.connect(lambda: self.save_answer(2,"10 ta"))

        self.tst3 = QLabel("3. Bu yilgi UEFA golibi kim bo'ladi?",self)
        self.tst3.setFont(QFont("Times New Roman",24))
        self.tst3.setGeometry(30,390,600,50)
        self.tst3.setStyleSheet("color:rgb(255,0,255)")

        self.c1 = QRadioButton("Holand",self)
        self.c1.setFont(QFont("Times New Roman",24))
        self.c1.setGeometry(60,450,600,50)
        self.c1.setStyleSheet("color:rgb(0,0,255)")
        self.c1.clicked.connect(lambda: self.save_answer(3,"Holand"))

        self.c2 = QRadioButton("Mbappe",self)
        self.c2.setFont(QFont("Times New Roman",24))
        self.c2.setGeometry(60,510,600,50)
        self.c2.setStyleSheet("color:rgb(0,0,255)")
        self.c2.clicked.connect(lambda: self.save_answer(3,"Mbappe"))

        self.c3 = QRadioButton("Vinisius",self)
        self.c3.setFont(QFont("Times New Roman",24))
        self.c3.setGeometry(300,450,600,50)
        self.c3.setStyleSheet("color:rgb(0,0,255)")
        self.c3.clicked.connect(lambda: self.save_answer(3,"Vinisius"))

        self.c4 = QRadioButton("Bellingem",self)
        self.c4.setFont(QFont("Times New Roman",24))
        self.c4.setGeometry(300,510,600,50)
        self.c4.setStyleSheet("color:rgb(0,0,255)")
        self.c4.clicked.connect(lambda: self.save_answer(3,"Bellingem"))

        self.tst4 = QLabel("4. Najot ... ? Jumlani davom ettiring!",self)
        self.tst4.setFont(QFont("Times New Roman",24))
        self.tst4.setGeometry(30,560,600,50)
        self.tst4.setStyleSheet("color:rgb(255,0,255)")

        self.d1 = QRadioButton("Ta'limda",self)
        self.d1.setFont(QFont("Times New Roman",24))
        self.d1.setGeometry(60,620,600,50)
        self.d1.setStyleSheet("color:rgb(0,0,255)")
        self.d1.clicked.connect(lambda: self.save_answer(4,"Ta'limda"))

        self.d2 = QRadioButton("Umidda",self)
        self.d2.setFont(QFont("Times New Roman",24))
        self.d2.setGeometry(60,680,600,50)
        self.d2.setStyleSheet("color:rgb(0,0,255)")
        self.d2.clicked.connect(lambda: self.save_answer(4,"Umidda"))

        self.d3 = QRadioButton("Omadda",self)
        self.d3.setFont(QFont("Times New Roman",24))
        self.d3.setGeometry(300,620,600,50)
        self.d3.setStyleSheet("color:rgb(0,0,255)")
        self.d3.clicked.connect(lambda: self.save_answer(4,"Omadda"))

        self.d4 = QRadioButton("Bilimda",self)
        self.d4.setFont(QFont("Times New Roman",24))
        self.d4.setGeometry(300,680,600,50)
        self.d4.setStyleSheet("color:rgb(0,0,255)")
        self.d4.clicked.connect(lambda: self.save_answer(4,"Bilimda"))

        self.tst5 = QLabel("5. Yer shakli qanday?",self)
        self.tst5.setFont(QFont("Times New Roman",24))
        self.tst5.setGeometry(30,730,600,50)
        self.tst5.setStyleSheet("color:rgb(255,0,255)")

        self.k1 = QRadioButton("Dumaloq",self)
        self.k1.setFont(QFont("Times New Roman",24))
        self.k1.setGeometry(60,780,600,50)
        self.k1.setStyleSheet("color:rgb(0,0,255)")
        self.k1.clicked.connect(lambda: self.save_answer(5,"Dumaloq"))

        self.k2 = QRadioButton("Uchburchak",self)
        self.k2.setFont(QFont("Times New Roman",24))
        self.k2.setGeometry(60,840,600,50)
        self.k2.setStyleSheet("color:rgb(0,0,255)")
        self.k2.clicked.connect(lambda: self.save_answer(5,"Uchburchak"))

        self.k3 = QRadioButton("Aylana",self)
        self.k3.setFont(QFont("Times New Roman",24))
        self.k3.setGeometry(300,780,600,50)
        self.k3.setStyleSheet("color:rgb(0,0,255)")
        self.k3.clicked.connect(lambda: self.save_answer(5,"Aylana"))

        self.k4 = QRadioButton("Nuqta",self)
        self.k4.setFont(QFont("Times New Roman",24))
        self.k4.setGeometry(300,840,600,50)
        self.k4.setStyleSheet("color:rgb(0,0,255)")
        self.k4.clicked.connect(lambda: self.save_answer(5,"Nuqta"))

        res = QPushButton("Result",self)
        res.setFont(QFont("Times New Roman",24))
        res.setGeometry(500,840,200,50)
        res.setStyleSheet("color:rgb(255,241,255);background-color:rgb(0,125,10)")
        res.clicked.connect(lambda: self.check_test(self.name))

    def save_answer(self,question_number,answer):
        self.ls[question_number] = answer

    def check_test(self,nm):
        tjs,njs = 0,0
        for key in self.ls:
            if self.ls[key] == "Madrid" and key == 1:
                tjs += 1
            elif self.ls[key] == "8 ta" and key == 2:
                tjs += 1
            elif self.ls[key] == "Holand" and key == 3:
                tjs += 1
            elif self.ls[key] == "Ta'limda" and key == 4:
                tjs += 1
            elif self.ls[key] == "Dumaloq" and key == 5:
                tjs += 1
            else :
                njs += 1

        Msg = QMessageBox(self)
        Msg.setFont(QFont("Times New Roman",24))
        Msg.setStyleSheet("color:rgb(255,241,255);background-color:rgb(0,0,0)")
        Msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)
        Msg.setText(f"Umumiy ball : {tjs} ball")
        Msg.setWindowTitle("Natija")
        Msg.show()
        Msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ilova("Messi")
    oyna.show()
    sys.exit(app.exec_())

    # unset GTK_PATH