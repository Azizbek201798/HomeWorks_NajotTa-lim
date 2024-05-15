import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector

class baza_connection_first(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Birlashgan Millatlar Tashkiloti")
        self.setMaximumSize(1800,1000)
        self.setMinimumSize(1800,1000)
        
        self.name_lb = QLabel("Davlat Nomi >>> ",self)
        self.name_lb.setFont(QFont("Times New Roman",22))
        self.name_lb.setGeometry(50,50,300,50)
        self.name_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.name_txt = QLineEdit(self)
        self.name_txt.setFont(QFont("Times New Roman",22))
        self.name_txt.setGeometry(360,50,300,50)
        self.name_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.name_txt.setAlignment(Qt.AlignCenter)
        
        self.pop_lb = QLabel("Aholi soni >>> ",self)
        self.pop_lb.setFont(QFont("Times New Roman",22))
        self.pop_lb.setGeometry(50,110,300,50)
        self.pop_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.pop_txt = QLineEdit(self)
        self.pop_txt.setFont(QFont("Times New Roman",22))
        self.pop_txt.setGeometry(360,110,300,50)
        self.pop_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.pop_txt.setAlignment(Qt.AlignCenter)
        
        self.area_lb = QLabel("Maydoni kv_km >>> ",self)
        self.area_lb.setFont(QFont("Times New Roman",22))
        self.area_lb.setGeometry(850,50,300,50)
        self.area_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.area_txt = QLineEdit(self)
        self.area_txt.setFont(QFont("Times New Roman",22))
        self.area_txt.setGeometry(1160,50,300,50)
        self.area_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.area_txt.setAlignment(Qt.AlignCenter)
        
        self.lang_lb = QLabel("Davlat Tili >>> ",self)
        self.lang_lb.setFont(QFont("Times New Roman",22))
        self.lang_lb.setGeometry(850,110,300,50)
        self.lang_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.lang_txt = QComboBox(self)
        self.lang_txt.setFont(QFont("Times New Roman",22))
        self.lang_txt.setGeometry(1160,110,300,50)
        self.lang_txt.setStyleSheet("""color: rgb(112,112,255);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.lang_txt.addItems(["English","o'zbek","Ruskiy","turkish"])
        
        self.nato_lb = QLabel("NATO a'zosimi ",self)
        self.nato_lb.setFont(QFont("Times New Roman",22))
        self.nato_lb.setGeometry(50,170,300,50)
        self.nato_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.nato_yes = QRadioButton("  Ha",self)
        self.nato_yes.setFont(QFont("Times New Roman",22))
        self.nato_yes.setGeometry(360,170,140,50)
        self.nato_yes.setStyleSheet("""color: rgb(112,112,255);""")

        self.nato_no = QRadioButton("  Yo'q",self)
        self.nato_no.setFont(QFont("Times New Roman",22))
        self.nato_no.setGeometry(520,170,140,50)
        self.nato_no.setStyleSheet("""color: rgb(112,112,255);""")
        
        self.pol_lb = QLabel("Boshqaruv shakli  ",self)
        self.pol_lb.setFont(QFont("Times New Roman",22))
        self.pol_lb.setGeometry(850,170,300,50)
        self.pol_lb.setStyleSheet("color: rgb(12,12,255);")
        
        self.parl = QCheckBox("Parlament",self)
        self.parl.setFont(QFont("Times New Roman",22))
        self.parl.setGeometry(1160,170,170,50)
        self.parl.setStyleSheet("""color: red;""")

        self.mon = QCheckBox("Monarxiya",self)
        self.mon.setFont(QFont("Times New Roman",22))
        self.mon.setGeometry(1350,170,170,50)
        self.mon.setStyleSheet("""color: red;""")
        
        self.dem = QCheckBox("Demokratiya",self)
        self.dem.setFont(QFont("Times New Roman",22))
        self.dem.setGeometry(1550,170,170,50)
        self.dem.setStyleSheet("""color: red;""")
        
        self.insert_btn = QPushButton("INSERT DATA",self)
        self.insert_btn.setFont(QFont("Times New Roman",22))
        self.insert_btn.setGeometry(1400,230,300,50)
        self.insert_btn.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.insert_btn.clicked.connect(self.insert_data)

        self.next_btn = QPushButton("NEXT WINDOW",self)
        self.next_btn.setFont(QFont("Times New Roman",22))
        self.next_btn.setGeometry(1400,290,300,50)
        self.next_btn.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.next_btn.clicked.connect(self.next_window)

        self.tablo = QTableWidget(self)
        self.tablo.setGeometry(100,350,1650,600)
        self.tablo.setFont(QFont("Times New Roman",24))
        self.tablo.setStyleSheet("color: magenta")
        self.tablo.setRowCount(20)
        self.tablo.setColumnCount(7)
        self.tablo.setHorizontalHeaderLabels(["Country id","Name","Population","Area","Language","NATO_member","System Goverment"])
        header = self.tablo.horizontalHeader()
        header.setFont(QFont("Times New Roman",20))
        for x in range(7):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
        self.tablo.setVerticalHeaderLabels(lb)
        self.show_info("""Select * from davlat;""")
    
    def insert_data(self):
        os.system("cls")
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

    def next_window(self):
        self.window = baza_connection_second()
        self.window.show()
        self.hide()

class baza_connection_second(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Operations")
        self.setMaximumSize(1800,1000)
        self.setMinimumSize(1800,1000)

        self.btn1 = QPushButton("MAIN WINDOW",self)
        self.btn1.setFont(QFont("Times New Roman",22))
        self.btn1.setGeometry(1400,100,300,50)
        self.btn1.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.btn1.clicked.connect(self.asosiy_menu)

        self.cmb_1 = QComboBox(self)
        self.cmb_1.setFont(QFont("Times New Roman",22))
        self.cmb_1.setGeometry(100,50,300,50)
        self.cmb_1.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.cmb_1.addItems(["Name","NATO_member","Population","Language"])

        self.c_btn_1 = QPushButton("SELECT DATA",self)
        self.c_btn_1.setFont(QFont("Times New Roman",22))
        self.c_btn_1.setGeometry(450,50,300,50)
        self.c_btn_1.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        
        self.label_1 = QLabel("INPUT : ",self)
        self.label_1.setGeometry(800,50,100,50)
        self.label_1.setFont(QFont("Times New Roman",20))
        self.label_1.setStyleSheet("""color: rgb(0,0,0);
                                    """)
        self.ln_1 = QLineEdit(self)
        self.ln_1.setGeometry(920,50,300,50)
        self.ln_1.setFont(QFont("Times New Roman",20))
        self.ln_1.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")

        self.c_btn_2 = QPushButton("UPDATE DATA",self)
        self.c_btn_2.setFont(QFont("Times New Roman",22))
        self.c_btn_2.setGeometry(450,140,300,50)
        self.c_btn_2.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.c_btn_2.clicked.connect(self.update_data)

        self.cmb_2 = QComboBox(self)
        self.cmb_2.setFont(QFont("Times New Roman",22))
        self.cmb_2.setGeometry(100,140,300,50)
        self.cmb_2.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.cmb_2.addItems(["Name","NATO_member","Population"])

        self.label_2 = QLabel("INPUT : ",self)
        self.label_2.setGeometry(800,140,100,50)
        self.label_2.setFont(QFont("Times New Roman",20))
        self.label_2.setStyleSheet("""color: rgb(0,0,0);
                                    """)

        self.ln_2 = QLineEdit(self)
        self.ln_2.setGeometry(920,140,300,50)
        self.ln_2.setFont(QFont("Times New Roman",20))
        self.ln_2.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        
        self.cmb_3 = QComboBox(self)
        self.cmb_3.setFont(QFont("Times New Roman",22))
        self.cmb_3.setGeometry(100,230,300,50)
        self.cmb_3.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")
        self.cmb_3.addItems(["Name","NATO_member","Population"])

        self.c_btn_3 = QPushButton("DELETE DATA",self)
        self.c_btn_3.setFont(QFont("Times New Roman",22))
        self.c_btn_3.setGeometry(450,230,300,50)
        self.c_btn_3.setStyleSheet("""color: rgb(0,255,0);
                                      background-color: black;
                                    border-color: rgb(0,255,0);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.c_btn_3.clicked.connect(self.delete_data)

        self.label_3 = QLabel("INPUT : ",self)
        self.label_3.setGeometry(800,230,100,50)
        self.label_3.setFont(QFont("Times New Roman",20))
        self.label_3.setStyleSheet("""color: rgb(0,0,0);
                                    """)
        self.ln_3 = QLineEdit(self)
        self.ln_3.setGeometry(920,230,300,50)
        self.ln_3.setFont(QFont("Times New Roman",20))
        self.ln_3.setStyleSheet("""color: rgb(0,0,0);
                                    border-color: rgb(112,112,255);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 10;""")

        self.tablo_1 = QTableWidget(self)
        self.tablo_1.setGeometry(100,350,1650,600)
        self.tablo_1.setFont(QFont("Times New Roman",24))
        self.tablo_1.setStyleSheet("color: magenta")
        self.tablo_1.setRowCount(20)
        self.tablo_1.setColumnCount(7)
        self.tablo_1.setHorizontalHeaderLabels(["Country id","Name","Population","Area","Language","NATO_member","System Goverment"])
        header = self.tablo_1.horizontalHeader()
        header.setFont(QFont("Times New Roman",24))
        for x in range(7):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
        self.tablo_1.setVerticalHeaderLabels(lb)
        self.show_info("""Select * from davlat;""")

    def delete_data(self):
        os.system("clear")
        obj = connect_database("Country")
        column,info = None,None
        if self.cmb_3.currentText() == "Name":
            column = self.cmb_3.currentText()
        elif self.cmb_3.currentText() == "Population":
            column = self.cmb_3.currentText()
        elif self.cmb_3.currentText() == "NATO_member":
            column = self.cmb_3.currentText()

        info = self.ln_3.text()
        obj.delete_info(column,info)

    def update_data(self):
        os.system("clear")
        obj = connect_database("Country")
        column,info = None,None
        if self.cmb_2.currentText() == "Name":
            column = self.cmb_2.currentText()
        elif self.cmb_2.currentText() == "Population":
            column = self.cmb_2.currentText()
        elif self.cmb_2.currentText() == "NATO_member":
            column = self.cmb_2.currentText()

        info = self.ln_2.text()
        obj.update_info(column,info)

    def show_info(self,sql):
        os.system("clear")
        obj = connect_database("Country")
        res = obj.get_info(sql)
        for x in range(len(res)):
            self.tablo_1.setItem(x,0,QTableWidgetItem(str(res[x][0])))
            self.tablo_1.setItem(x,1,QTableWidgetItem(str(res[x][1])))
            self.tablo_1.setItem(x,2,QTableWidgetItem(str(res[x][2])))
            self.tablo_1.setItem(x,3,QTableWidgetItem(str(res[x][3])))
            self.tablo_1.setItem(x,4,QTableWidgetItem(str(res[x][4])))
            if res[x][5]:
                y = "YES"
            else:
                y = "NO"
            self.tablo_1.setItem(x,5,QTableWidgetItem(y))
            self.tablo_1.setItem(x,6,QTableWidgetItem(str(res[x][6])))

    def asosiy_menu(self):
        self.win = baza_connection_first()
        self.win.show()
        self.hide()

class connect_database:
    def __init__(self,baza):
        self.con = mysql.connector.connect(host = 'localhost',user = 'root',
                                           password = 'Najot1995!',database = f"{baza}")
        self.kur = self.con.cursor()
        self.kur.execute("""Create table if not exists davlat
                         (country_id int primary key auto_increment,
                         Name varchar(30) NOT NULL,
                         Population int NOT NULL,
                         area float NOT NULL,
                         Language varchar(30) NOT NULL default "English",
                         NATO_member bool NOT NULL default false,
                         System_goverment varchar(30) NOT NULL default "Democratic");""")
        
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

    # def select_info(self,info_1,column,info_2):
    #     sql = """SELECT * FROM davlat LIKE %s WHERE %s == %s;"""
    #     values = (info_1,column,info_2)
    #     self.kur.execute(sql,values)
    #     self.con.commit()

    def update_info(self,column,info):
        sql = """UPDATE davlat SET %s = %s;"""
        values = (column,info)
        self.kur.execute(sql,values)
        self.con.commit()
        print("Bazada ma'lumot yangilandi!")

    def delete_info(self,column,info):
        sql = """DELETE FROM davlat WHERE %s = %s;"""
        values = (column,info)
        self.kur.execute(sql,values)
        self.con.commit()
        print("Bazadan ma'lumot o'chirildi!")

if __name__ == "__main__":
    app  = QApplication(sys.argv)
    project_1 = baza_connection_first()
    project_2 = baza_connection_second()
    project_1.show()
    sys.exit(app.exec_())
