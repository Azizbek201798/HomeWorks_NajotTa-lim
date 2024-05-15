import os
import sys
import mysql.connector as myc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class baza_connection(QMainWindow):
    def __init__(self,db_name = "country"):
        super().__init__()
        self.setWindowTitle("Birlashgan Millatlar Tashkiloti")
        self.setMaximumSize(1800,1000)
        self.setMinimumSize(1800,1000)
        try:
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!",database = f"{db_name}")
            self.kur = self.mdb.cursor()
        except: 
            self.mdb = myc.connect(host = "localhost", user = "root", password = "Najot1995!")
            self.kur = self.mdb.cursor()
            self.kur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")

        self.name_lb = QLabel("Davlat Nomi >>> ",self)
        self.name_lb.setFont(QFont("Poor Richard",22))
        self.name_lb.setGeometry(50,50,300,50)
        self.name_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.name_txt = QLineEdit(self)
        self.name_txt.setFont(QFont("Poor Richard",22))
        self.name_txt.setGeometry(360,50,300,50)
        self.name_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.name_txt.setAlignment(Qt.AlignCenter)
        
        self.pop_lb = QLabel("Aholi soni >>> ",self)
        self.pop_lb.setFont(QFont("Poor Richard",22))
        self.pop_lb.setGeometry(50,110,300,50)
        self.pop_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.pop_txt = QLineEdit(self)
        self.pop_txt.setFont(QFont("Poor Richard",22))
        self.pop_txt.setGeometry(360,110,300,50)
        self.pop_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.pop_txt.setAlignment(Qt.AlignCenter)

        
        self.area_lb = QLabel("Maydoni kv_km >>> ",self)
        self.area_lb.setFont(QFont("Poor Richard",22))
        self.area_lb.setGeometry(850,50,300,50)
        self.area_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.area_txt = QLineEdit(self)
        self.area_txt.setFont(QFont("Poor Richard",22))
        self.area_txt.setGeometry(1160,50,300,50)
        self.area_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.area_txt.setAlignment(Qt.AlignCenter)
        
        self.lang_lb = QLabel("Davlat Tili >>> ",self)
        self.lang_lb.setFont(QFont("Poor Richard",22))
        self.lang_lb.setGeometry(850,110,300,50)
        self.lang_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.lang_txt = QComboBox(self)
        self.lang_txt.setFont(QFont("Poor Richard",22))
        self.lang_txt.setGeometry(1160,110,300,50)
        self.lang_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.lang_txt.addItems(["English","o'zbek","Ruskiy","turkish"])
        
        self.nato_lb = QLabel("NATO a'zosimi ",self)
        self.nato_lb.setFont(QFont("Poor Richard",22))
        self.nato_lb.setGeometry(50,170,300,50)
        self.nato_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.nato_yes = QRadioButton("  Ha",self)
        self.nato_yes.setFont(QFont("Poor Richard",22))
        self.nato_yes.setGeometry(360,170,140,50)
        self.nato_yes.setStyleSheet("""color: rgb(112,112,255);""")

        self.nato_no = QRadioButton("  Yo'q",self)
        self.nato_no.setFont(QFont("Poor Richard",22))
        self.nato_no.setGeometry(520,170,140,50)
        self.nato_no.setStyleSheet("""color: rgb(112,112,255);""")
        
        self.pol_lb = QLabel("Boshqaruv shakli  ",self)
        self.pol_lb.setFont(QFont("Poor Richard",22))
        self.pol_lb.setGeometry(850,170,300,50)
        self.pol_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.parl = QCheckBox("Parlament",self)
        self.parl.setFont(QFont("Poor Richard",22))
        self.parl.setGeometry(1160,170,170,50)
        self.parl.setStyleSheet("""color: red;""")

        self.mon = QCheckBox("Monarxiya",self)
        self.mon.setFont(QFont("Poor Richard",22))
        self.mon.setGeometry(1350,170,170,50)
        self.mon.setStyleSheet("""color: red;""")
        
        self.dem = QCheckBox("Demokratiya",self)
        self.dem.setFont(QFont("Poor Richard",22))
        self.dem.setGeometry(1550,170,170,50)
        self.dem.setStyleSheet("""color: red;""")
        
        self.insert_btn = QPushButton("INSERT    DATA",self)
        self.insert_btn.setFont(QFont("Poor Richard",22))
        self.insert_btn.setGeometry(1400,230,300,50)
        self.insert_btn.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        
        self.insert_btn.clicked.connect(self.InputInfo_Product)
    
    def create_table(self):
        self.kur.execute(f"""CREATE TABLE IF NOT EXISTS mamlakat
                            (
                            nomi VARCHAR(50),
                            aholisi INT,
                            maydoni INT,
                            tili VARCHAR(30),
                            boshqaruv_shakli VARCHAR(20),
                            nato_azosimi VARCHAR(10)
                        );""")

    def InputInfo_Product(self):
        res_1 = ""
        res_2 = ""
        if self.parl.isChecked():
            res += self.parl.text()
        if self.mon.isChecked():
            res += self.parl.text()
        if self.dem.isChecked():
            res += self.parl.text()
        
        if self.nato_yes.isChecked():
            res_2 = self.nato_yes.text()
        if self.nato_no.isChecked():
            res_2 = self.nato_no.text()

        sql = """INSERT INTO mamlakat(nomi,aholisi,maydoni,tili,boshqaruv_shakli,nato_azosimi) VALUES (%s,%s,%s,%s,%s,%s);"""
        self.kur.execute(sql,(self.name_txt.text(),int(self.pop_txt.text()),int(self.area_txt.text()),
                              self.lang_txt.currentText(),res_1,res_2))
        self.mdb.commit()
        
if __name__ == "__main__":
    app  = QApplication(sys.argv)
    project = baza_connection()
    project.show()
    # project.create_table()
    project.InputInfo_Product()
    sys.exit(app.exec_())