import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("clear")

class dastur(QMainWindow):
    def __init__(self,nm):
        super().__init__()
        self.name = nm
        self.setMaximumSize(700,500)
        self.setMinimumSize(700,500)
        self.setWindowTitle("Test.uz")

        self.tst1 = QLabel("1. Poytaxti Cataloniya bo'lgan davlatni qaysi?",self)
        self.tst1.setFont(QFont("Times New Roman",24))
        self.tst1.setGeometry(50,30,700,50)
        self.tst1.setStyleSheet("color:rgb(255,0,255)")

        self.tv1 = QRadioButton("Serbiya",self)
        self.tv1.setFont(QFont("Times New Roman",24))
        self.tv1.setGeometry(100,90,250,50)
        self.tv1.setStyleSheet("color:rgb(0,0,255)")

        self.tv2 = QRadioButton("Tashkent",self)
        self.tv2.setFont(QFont("Times New Roman",24))
        self.tv2.setGeometry(100,150,250,50)
        self.tv2.setStyleSheet("color:rgb(0,0,255)")

        self.tv3 = QRadioButton("Cataloniya",self)
        self.tv3.setFont(QFont("Times New Roman",24))
        self.tv3.setGeometry(350,90,250,50)
        self.tv3.setStyleSheet("color:rgb(0,0,255)")

        self.tv4 = QRadioButton("Paris",self)
        self.tv4.setFont(QFont("Times New Roman",24))
        self.tv4.setGeometry(350,150,250,50)
        self.tv4.setStyleSheet("color:rgb(0,0,255)")

        self.tst2 = QLabel("2. Yarim finalga qaysi jamoalar chiqadi?",self)
        self.tst2.setFont(QFont("Times New Roman",24))
        self.tst2.setGeometry(50,220,700,50)
        self.tst2.setStyleSheet("color:rgb(255,0,255)")

        self.chv1 = QCheckBox("Real Madrid",self)
        self.chv1.setFont(QFont("Times New Roman",24))
        self.chv1.setGeometry(350,280,250,50)
        self.chv1.setStyleSheet("color:rgb(0,0,255)")

        self.chv2 = QCheckBox("Barselona",self)
        self.chv2.setFont(QFont("Times New Roman",24))
        self.chv2.setGeometry(350,340,250,50)
        self.chv2.setStyleSheet("color:rgb(0,0,255)")

        self.chv3 = QCheckBox("Bavariya",self)
        self.chv3.setFont(QFont("Times New Roman",24))
        self.chv3.setGeometry(100,280,250,50)
        self.chv3.setStyleSheet("color:rgb(0,0,255)")

        self.chv4 = QCheckBox("Liverpul",self)
        self.chv4.setFont(QFont("Times New Roman",24))
        self.chv4.setGeometry(100,340,250,50)
        self.chv4.setStyleSheet("color:rgb(0,0,255)")

        a = QPushButton("Testni tugatish",self)
        a.setFont(QFont("Times New Roman",24))        
        a.setGeometry(440,410,250,50)
        a.setStyleSheet("color:rgb(255,241,255); background-color: rgb(0,125,10)")

        a.clicked.connect(lambda: self.check_test(self.name))
    
        self.cmb = QComboBox(self)
        self.cmb.setFont(QFont("Times New Roman",24))
        self.cmb.setGeometry(10,420,200,40)
        self.cmb.addItem("Barselona")
        self.cmb.addItems(["Real Madrid","Bavariya","M Siti"])

        self.lst = QListWidget(self)
        self.lst.setFont(QFont("Times New Roman",24))
        self.lst.setGeometry(220,420,200,40)
        self.lst.addItem("Barselona")
        self.lst.addItems(["Real Madrid","Bavariya","M Siti"])

    def check_test(self,st):
        tjs,njs = 0,0
        if self.tv3.isChecked():
            tjs += 1
        else :
            njs += 1
        if self.chv2.isChecked() and self.chv4.isChecked():
            tjs += 1
        else :
            njs += 1
        Msg = QMessageBox(self)
        Msg.setFont(QFont("Times New Roman",24))        
        # Msg.setIcon(QMessageBox.Information)
        # Msg.setIcon(QMessageBox.Critical)
        # Msg.setIcon(QMessageBox.Warning)
        # Msg.setIcon(QMessageBox.Question)
        Msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)
        Msg.setText(f"To'g'ri javoblar soni : {tjs}\nNoto'g'ri javoblar soni : {njs}")
        Msg.setInformativeText("Shuni ham bilmadingmi?")
        Msg.setStyleSheet("background-color: rgb(255,0,255)")
        Msg.show()
        Msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pro = dastur("Messi")
    pro.show()
    sys.exit(app.exec_())