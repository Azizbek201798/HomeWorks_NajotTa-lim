import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class baza_connection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Birlashgan Millatlar Tashkiloti")
        self.setMaximumSize(1800,1000)
        self.setMinimumSize(1800,1000)
        
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
        
        self.insert_btn.clicked.connect(self.insert_data)

        self.delete_btn = QPushButton("DELETE", self)
        self.delete_btn.setFont(QFont("Poor Richard", 22))
        self.delete_btn.setGeometry(1400, 290, 300, 50)
        self.delete_btn.setStyleSheet("""color: rgb(255, 0, 0);
                                          background-color: black;
                                          border-color: rgb(255, 0, 0);
                                          border-width: 3px;
                                          border-style: solid;
                                          border-radius: 15;""")
        self.delete_btn.clicked.connect(self.delete_data)

        self.update_btn = QPushButton("UPDATE", self)
        self.update_btn.setFont(QFont("Poor Richard", 22))
        self.update_btn.setGeometry(1000, 290, 300, 50)
        self.update_btn.setStyleSheet("""color: rgb(255, 255, 0);
                                          background-color: black;
                                          border-color: rgb(255, 255, 0);
                                          border-width: 3px;
                                          border-style: solid;
                                          border-radius: 15;""")
        self.update_btn.clicked.connect(self.update_data)

        self.select_combo = QComboBox(self)
        self.select_combo.setFont(QFont("Poor Richard", 22))
        self.select_combo.setGeometry(100, 290, 300, 50)
        self.select_combo.setStyleSheet("""color: rgb(112, 112, 255);
                                            border-color: rgb(112, 112, 255);
                                            border-width: 3px;
                                            border-style: solid;
                                            border-radius: 10;""")
        self.select_combo.addItems(["Name", "Language", "Population"])
        self.select_combo.currentIndexChanged.connect(self.select_data)        

        self.tablo = QTableWidget(self)
        self.tablo.setGeometry(100,350,1650,600)
        self.tablo.setFont(QFont("Calibri",20))
        self.tablo.setStyleSheet("color: magenta")
        self.tablo.setRowCount(20)
        self.tablo.setColumnCount(7)
        self.tablo.setHorizontalHeaderLabels(["Country id","Name","Population","Area","Language","NATO member","System Goverment"])
        header = self.tablo.horizontalHeader()
        header.setFont(QFont("Calibri",20))
        for x in range(7):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","","","","","","","",""]
        self.tablo.setVerticalHeaderLabels(lb)
        self.show_info("""Select * from davlat where name = "O'zbekiston" """)
        
    def insert_data(self):
        os.system("cls")
        print("Navbat endi sizlarga")
        obj = connect_database("Country")
        name = self.name_txt.text()
        pp = int(self.pop_txt.text())
        area = float(self.area_txt.text())
        lang = self.lang_txt.currentText()
        nato = self.nato_yes.isChecked()
        txt = ""
        if self.parl.isChecked():
            txt = txt + " " + "Parlament"
        if self.mon.isChecked():
            txt = txt + " " + "Monarxiya"
        if self.dem.isChecked():
            txt = txt + " " + "Demokratiya"
        obj.input_info(name,pp,area,lang,nato,txt)
        self.show_info()

    def show_info(self,sql):
        obj = connect_database("Country")
        res = obj.get_info(sql)
        for x in range(len(res)):
            self.tablo.setItem(x,0,QTableWidgetItem(str(res[x][0])))
            self.tablo.setItem(x,1,QTableWidgetItem(str(res[x][1])))
            self.tablo.setItem(x,2,QTableWidgetItem(str(res[x][2])))
            self.tablo.setItem(x,3,QTableWidgetItem(str(res[x][3])))
            self.tablo.setItem(x,4,QTableWidgetItem(str(res[x][4])))
            if res[x][5]:
                y = "YES"
            else:
                y = "NO"
            self.tablo.setItem(x,5,QTableWidgetItem(y))
            self.tablo.setItem(x,6,QTableWidgetItem(str(res[x][6])))
            
    def delete_data(self):
        selected_row = self.tablo.currentRow()
        country_id = self.tablo.item(selected_row, 0).text()
        obj = connect_database("Country")
        obj.delete_info(country_id)
        self.show_info()

    def update_data(self):
        selected_row = self.tablo.currentRow()
        country_id = self.tablo.item(selected_row, 0).text()
        name = self.name_txt.text()
        pp = int(self.pop_txt.text())
        area = float(self.area_txt.text())
        lang = self.lang_txt.currentText()
        nato = self.nato_yes.isChecked()
        txt = ""
        if self.parl.isChecked():
            txt = txt + " " + "Parlament"
        if self.mon.isChecked():
            txt = txt + " " + "Monarxiya"
        if self.dem.isChecked():
            txt = txt + " " + "Demokratiya"
        obj = connect_database("Country")
        obj.update_info(country_id, name, pp, area, lang, nato, txt)
        self.show_info()

    def select_data(self):
        selected_column = self.select_combo.currentIndex()
        column_names = ["name", "Language", "population"]
        column_name = column_names[selected_column]
        search_value = self.name_txt.text()
        sql = f"SELECT * FROM davlat WHERE {column_name} = '{search_value}';"
        self.show_info(sql)

class connect_database:
    def __init__(self,baza):
        self.con = mysql.connector.connect(host = 'localhost',user = 'root',
                                           password = 'Najot1995!',database = f"{baza}")
        self.kur = self.con.cursor()
        self.kur.execute("""Create table if not exists davlat
                         (country_id int primary key auto_increment,
                         name varchar(30) NOT NULL,
                         population int NOT NULL,
                         area float NOT NULL,
                         Language varchar(30) NOT NULL default "English",
                         NATO_MEMBER bool NOT NULL default false,
                         System_goverment varchar(30) NOT NULL default "Democratic");""")
        
    def delete_info(self, country_id):
        sql = f"DELETE FROM davlat WHERE country_id = {country_id};"
        self.kur.execute(sql)
        self.con.commit()
        print("Ma'lumot o'chirildi")

    def update_info(self, country_id, nm, pp, ar, lg, nmm, sg):
        sql = """UPDATE davlat SET name = %s, population = %s, area = %s,
                 Language = %s, NATO_MEMBER = %s, System_goverment = %s
                 WHERE country_id = %s;"""
        values = (nm, pp, ar, lg, nmm, sg, country_id)
        self.kur.execute(sql, values)
        self.con.commit()
        print("Ma'lumot bazada yangilandi")

    def input_info(self,nm,pp,ar,lg,nmm,sg):
        sql = """INSERT INTO davlat(name,population,area,Language,NATO_Member,
            System_goverment) VALUES(%s,%s,%s,%s,%s,%s);"""
        values = (nm,pp,ar,lg,nmm,sg)
        self.kur.execute(sql,values)
        self.con.commit()
        print("Ma'lumot bazaga yozildi")
    
    def get_info(self,sql = "SELECT * from davlat"):
        self.kur.execute(sql)
        return self.kur.fetchall()

if __name__ == "__main__":
    app  = QApplication(sys.argv)
    project = baza_connection()
    project.show_info("SELECT * FROM davlat;")
    project.show()
    sys.exit(app.exec_())
