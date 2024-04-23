import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class dastur(QMainWindow):
    def __init__(self,nm):
        super().__init__()
        self.name = nm
        self.setMaximumSize(1040,800)
        self.setMinimumSize(1040,800)
        self.setWindowTitle("Test")

        tst1 = QLabel("1.  Poytaxti Tirana bo'lgan davlatni ko'rsating?",self)
        tst1.setGeometry(50,30,700,50)
        tst1.setStyleSheet("color: rgb(255,0,255)")
        tst1.setFont(QFont("Poor Richard",24))

        tv1 = QRadioButton("Serbiya",self)
        tv1.setGeometry(100,90,250,50)
        tv1.setStyleSheet("color: rgb(0,0,255)")
        tv1.setFont(QFont("Poor Richard",24))

        tv2 = QRadioButton("Albaniya",self)
        tv2.setGeometry(600,90,250,50)
        tv2.setStyleSheet("color: rgb(0,0,255)")
        tv2.setFont(QFont("Poor Richard",24))

        tv3 = QRadioButton("O'zbekiston",self)
        tv3.setGeometry(100,160,250,50)
        tv3.setStyleSheet("color: rgb(0,0,255)")
        tv3.setFont(QFont("Poor Richard",24))

        tv4 = QRadioButton("Shvetsiya",self)
        tv4.setGeometry(600,160,250,50)
        tv4.setStyleSheet("color: rgb(0,0,255)")
        tv4.setFont(QFont("Poor Richard",24))

        tst2 = QLabel("2.  Yarim finaldagi jamoalarni tanlang?  ",self)
        tst2.setGeometry(50,230,700,50)
        tst2.setStyleSheet("color: rgb(255,0,255)")
        tst2.setFont(QFont("Poor Richard",24))

        chc1 = QCheckBox("Barselona",self)
        chc1.setGeometry(100,290,250,50)
        chc1.setStyleSheet("color: rgb(0,0,255)")
        chc1.setFont(QFont("Poor Richard",24))

        chc2 = QCheckBox("PSJ",self)
        chc2.setGeometry(100,350,250,50)
        chc2.setStyleSheet("color: rgb(0,0,255)")
        chc2.setFont(QFont("Poor Richard",24))

        chc3 = QCheckBox("Real Madrid",self)
        chc3.setGeometry(600,290,250,50)
        chc3.setStyleSheet("color: rgb(0,0,255)")
        chc3.setFont(QFont("Poor Richard",24))

        chc4 = QCheckBox("M City",self)
        chc4.setGeometry(600,350,250,50)
        chc4.setStyleSheet("color: rgb(0,0,255)")
        chc4.setFont(QFont("Poor Richard",24))

        tst3 = QLabel("3.  Markaziy osiyo davlatlarini tanlang?  ",self)
        tst3.setGeometry(50,430,700,50)
        tst3.setStyleSheet("color: rgb(255,0,255)")
        tst3.setFont(QFont("Poor Richard",24))
        
        chc1 = QCheckBox("Eron",self)
        chc1.setGeometry(100,550,250,50)
        chc1.setStyleSheet("color: rgb(0,0,255)")
        chc1.setFont(QFont("Poor Richard",24))
        
        chc2 = QCheckBox("Falastin",self)
        chc2.setGeometry(100,490,250,50)
        chc2.setStyleSheet("color: rgb(0,0,255)")
        chc2.setFont(QFont("Poor Richard",24))
        
        chc3 = QCheckBox("O'zbekiston",self)
        chc3.setGeometry(600,490,250,50)
        chc3.setStyleSheet("color: rgb(0,0,255)")
        chc3.setFont(QFont("Poor Richard",24))
        
        chc4 = QCheckBox("Afg'oniston",self)
        chc4.setGeometry(600,550,250,50)
        chc4.setStyleSheet("color: rgb(0,0,255)")
        chc4.setFont(QFont("Poor Richard",24))
        
        check = QPushButton("Testni tugatish",self)
        check.setGeometry(650,650,350,50)
        check.setStyleSheet("color: rgb(255,241,255); background-color: rgb(0,125,10);")
        check.setFont(QFont("Poor Richard",24))
        check.clicked.connect(lambda:self.check_test(self.name))
    
    def check_test(self,st):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = dastur("Marjona")
    project.show()
    sys.exit(app.exec_())
