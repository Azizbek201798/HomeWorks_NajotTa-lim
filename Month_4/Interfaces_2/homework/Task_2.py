# Task - 2 => DONE by Azizbek

# 	Restoran menyusini tuzuvchi dastur tuzing. 
#   Unda 1-taomlar ro'yhati, 2-taomlar ro'yhati, ichimliklar va desert ro'yhatidagi 
# 	kamida 5tadan ma'lumotlarni CheckBox orqali tanlaydi va oxirida Chek ro'yhati chiqarilsin. 
# 	Chek quyidagi ko'rinishda bo'lishi kerak:
# 	1-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# 	2-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# 	Ichimliklar: tanlanganlar ro'yhati (narxlari bilan)
# 	Desert: tanlanganlar ro'yhati (narxlari bilan)

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("clear")

class ilova(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restoran menyusi")
        self.setMaximumSize(1250,300)
        self.setMinimumSize(1250,300)
        self.setFont(QFont("Times New Roman",24))
        self.setStyleSheet("color:rgb(0,0,0);backgroun-color:rgb(0,0,0)")
        self.prices = {}

        self.hb1 = QHBoxLayout()
        self.lb1 = QLabel("Restoran Menyusi")
        self.lb1.setStyleSheet("color:rgb(0,125,10);")
        self.lb1.setFont(QFont("Times New Roman",32))
        self.hb1.addWidget(self.lb1,alignment=Qt.AlignCenter)

        self.hb2 = QHBoxLayout()
        self.lb1_1 = QLabel("1-Ovqat      :")
        self.lb1_1.setStyleSheet("color:rgb(255,125,10);")
        self.lb1_1.setFont(QFont("Times New Roman",24))
        self.lb1_2 = QCheckBox("Ko'za Sho'rva")
        self.lb1_2.clicked.connect(lambda: self.save_price("Ko'za Sho'rva",11000))
        self.lb1_3 = QCheckBox("Mastava")
        self.lb1_3.clicked.connect(lambda: self.save_price("Mastava",21000))
        self.lb1_4 = QCheckBox("Qaynatma")
        self.lb1_4.clicked.connect(lambda: self.save_price("Qaynatma",21000))
        self.lb1_5 = QCheckBox("Moshxo'rda")
        self.lb1_5.clicked.connect(lambda: self.save_price("Moshxo'rda",21000))
        self.lb1_6 = QCheckBox("Makaron sho'rva")
        self.lb1_6.clicked.connect(lambda: self.save_price("Makaron sho'rva",31000))
        self.hb2.addWidget(self.lb1_1)
        self.hb2.addStretch()
        self.hb2.addWidget(self.lb1_2)
        self.hb2.addStretch()
        self.hb2.addWidget(self.lb1_3)
        self.hb2.addStretch()
        self.hb2.addWidget(self.lb1_4)
        self.hb2.addStretch()
        self.hb2.addWidget(self.lb1_5)
        self.hb2.addStretch()
        self.hb2.addWidget(self.lb1_6)

        self.hb3 = QHBoxLayout()
        self.lb1_1 = QLabel("2-Ovqat      :")
        self.lb1_1.setStyleSheet("color:rgb(255,125,10);")
        self.lb1_1.setFont(QFont("Times New Roman",24))
        self.lb1_2 = QCheckBox("Shashlik")
        self.lb1_2.clicked.connect(lambda: self.save_price("Shashlik",10000))
        self.lb1_3 = QCheckBox("Tandir go'sht")
        self.lb1_3.clicked.connect(lambda: self.save_price("Tandir go'sht",30000))
        self.lb1_4 = QCheckBox("Tandir Somsa")
        self.lb1_4.clicked.connect(lambda: self.save_price("Tandir Somsa",20000))
        self.lb1_5 = QCheckBox("Bishteks Standart")
        self.lb1_5.clicked.connect(lambda: self.save_price("Bishteks Standart",24000))
        self.lb1_6 = QCheckBox("Manti")
        self.lb1_6.clicked.connect(lambda: self.save_price("Manti",26000))
        self.hb3.addWidget(self.lb1_1)
        self.hb3.addStretch()
        self.hb3.addWidget(self.lb1_2)
        self.hb3.addStretch()
        self.hb3.addWidget(self.lb1_3)
        self.hb3.addStretch()
        self.hb3.addWidget(self.lb1_4)
        self.hb3.addStretch()
        self.hb3.addWidget(self.lb1_5)
        self.hb3.addStretch()
        self.hb3.addWidget(self.lb1_6)        
        
        self.hb4 = QHBoxLayout()
        self.lb1_1 = QLabel("Ichimliklar :")
        self.lb1_1.setStyleSheet("color:rgb(255,125,10);")
        self.lb1_1.setFont(QFont("Times New Roman",24))
        self.lb1_2 = QCheckBox("Pepsi")
        self.lb1_2.clicked.connect(lambda: self.save_price("Pepsi",10000))
        self.lb1_3 = QCheckBox("Coca-Cola")
        self.lb1_3.clicked.connect(lambda: self.save_price("Coca-Cola",10000))
        self.lb1_4 = QCheckBox("Dena Multifruct")
        self.lb1_4.clicked.connect(lambda: self.save_price("Dena Multifruct",10000))
        self.lb1_5 = QCheckBox("Soknaya-Dolina")
        self.lb1_5.clicked.connect(lambda: self.save_price("Soknaya-Dolina",25000))
        self.lb1_6 = QCheckBox("Mirinda")
        self.lb1_6.clicked.connect(lambda: self.save_price("Mirinda",35000))
        self.hb4.addWidget(self.lb1_1)
        self.hb4.addStretch()
        self.hb4.addWidget(self.lb1_2)
        self.hb4.addStretch()
        self.hb4.addWidget(self.lb1_3)
        self.hb4.addStretch()
        self.hb4.addWidget(self.lb1_4)
        self.hb4.addStretch()
        self.hb4.addWidget(self.lb1_5)
        self.hb4.addStretch()
        self.hb4.addWidget(self.lb1_6)

        self.hb5 = QHBoxLayout()
        self.lb1_1 = QLabel("Desert        :")
        self.lb1_1.setStyleSheet("color:rgb(255,125,10);")
        self.lb1_1.setFont(QFont("Times New Roman",24))
        self.lb1_2 = QCheckBox("Tort")
        self.lb1_2.clicked.connect(lambda: self.save_price("Tort",10000))
        self.lb1_3 = QCheckBox("Medovik")
        self.lb1_3.clicked.connect(lambda: self.save_price("Medovik",20000))
        self.lb1_4 = QCheckBox("Muzqaymoq-Qaymoqli")
        self.lb1_4.clicked.connect(lambda: self.save_price("Muzqaymoq-Qaymoqli",30000))
        self.lb1_5 = QCheckBox("Safiya-Mix")
        self.lb1_5.clicked.connect(lambda: self.save_price("Safiya-Mix",20000))
        self.lb1_6 = QCheckBox("Quymoq-Olchali")
        self.lb1_6.clicked.connect(lambda: self.save_price("Quymoq-Olchali",40000))
        self.hb5.addWidget(self.lb1_1)
        self.hb5.addStretch()
        self.hb5.addWidget(self.lb1_2)
        self.hb5.addStretch()
        self.hb5.addWidget(self.lb1_3)
        self.hb5.addStretch()
        self.hb5.addWidget(self.lb1_4)
        self.hb5.addStretch()
        self.hb5.addWidget(self.lb1_5)
        self.hb5.addStretch()
        self.hb5.addWidget(self.lb1_6)

        self.hb6 = QHBoxLayout()
        self.chek = QPushButton("CHEK CHIQAR")
        self.chek.clicked.connect(lambda: self.show_check())
        self.chek.setStyleSheet("color:rgb(255,0,0);")
        self.chek.setFont(QFont("Times New Roman",24))
        self.hb6.addWidget(self.chek,alignment=Qt.AlignCenter)

        vb = QVBoxLayout()
        vb.addLayout(self.hb1)
        vb.addStretch()
        vb.addLayout(self.hb2)
        vb.addStretch()
        vb.addLayout(self.hb3)
        vb.addStretch()
        vb.addLayout(self.hb4)
        vb.addStretch()
        vb.addLayout(self.hb5)
        vb.addStretch()
        vb.addLayout(self.hb6)
        vb.addStretch()

        self.setLayout(vb)

    def save_price(self,name,price):
        self.prices[name] = price

    def show_check(self):
        t_1 = ""
        t_2 = ""
        ichimlik = ""
        desert = ""
        for x in self.prices:
            if x == "Ko'za Sho'rva" or x == "Mastava" or x == "Qaynatma" or x == "Moshxo'rda" or x == "Makaron sho'rva":
                t_1 += (x +" : "+ str(self.prices[x])+" ; ")
            if x == "Shashlik" or x == "Tandir go'sht" or x == "Tandir Somsa" or x == "Bishteks Standart" or x == "Manti":
                t_2 += (x +" : "+ str(self.prices[x])+" ; ")
            if x == "Pepsi" or x == "Coca-Cola" or x == "Dena Multifruct" or x == "Soknaya-Dolina" or x == "Mirinda":
                ichimlik += (x +" : "+ str(self.prices[x])+" ; ")
            if x == "Tort" or x == "Medovik" or x == "Muzqaymoq-Qaymoqli" or x == "Safiya-Mix" or x == "Quymoq-Olchali":
                desert += (x +" : "+ str(self.prices[x])+" ; ")

        Msg = QMessageBox(self)
        Msg.setFont(QFont("Times New Roman",15))
        Msg.setStyleSheet("color:rgb(255,255,255);background-color:rgb(0,0,0)")
        Msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Yes)
        Msg.setText(f"1-ovqat: {t_1}\n\n2-ovqat: {t_2}\n\nIchimliklar: {ichimlik}\n\nDesert: {desert}")
        Msg.setWindowTitle("Chek")
        Msg.show()
        Msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ilova()
    oyna.show()
    sys.exit(app.exec_())

# unset GTK_PATH


