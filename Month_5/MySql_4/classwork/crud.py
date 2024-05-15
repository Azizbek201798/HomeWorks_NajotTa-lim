import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector as myc
os.system("clear")

class Project(QTabWidget):
    def __init__(self,p = None):
        super(Project,self).__init__(p)
        self.setMaximumSize(1600,900)
        self.setMinimumSize(1600,900)
        self.setWindowTitle("Baza bilan ishlash!")
        self.setFont(QFont("Times New Roman",22))

        self.insert_info = QWidget()
        # self.insert_info.setStyleSheet("background-color : rgb(250,235,215);")
        self.update_info = QWidget()
        # self.update_info.setStyleSheet("background-color : rgb(245,222,179);")
        self.delete_info = QWidget()
        # self.delete_info.setStyleSheet("background-color : rgb(152,251,152);")
        self.find_info = QWidget() 
        # self.find_info.setStyleSheet("background-color : rgb(48,213,200);")

        self.addTab(self.insert_info,"Insert Data")
        self.addTab(self.update_info,"Update Data")
        self.addTab(self.delete_info,"Delete Data")
        self.addTab(self.find_info,"Find Data")

        self.tablo = QTableWidget(self)

        self.insert_data()
        self.update_data()
        self.delete_data()
        self.find_data()

        self.show_info()

    def insert_data(self):

        self.lb1 = QLabel("Uchish shaxri : ",self.insert_info)
        self.lb1.setGeometry(50,50,300,50)
        self.lb1.setStyleSheet("color : blue")

        self.ln1 = QLineEdit(self.insert_info)
        self.ln1.setGeometry(360,50,300,50)
        self.ln1.setStyleSheet("color : magenta")
        self.ln1.setAlignment(Qt.AlignCenter)

        self.lb2 = QLabel("Qo'nish shaxri : ",self.insert_info)
        self.lb2.setGeometry(800,50,300,50)
        self.lb2.setStyleSheet("color : blue")

        self.ln2 = QLineEdit(self.insert_info)
        self.ln2.setGeometry(1120,50,300,50)
        self.ln2.setStyleSheet("color : magenta")
        self.ln2.setAlignment(Qt.AlignCenter)

        self.lb3 = QLabel("Uchish vaqti : ",self.insert_info)
        self.lb3.setGeometry(50,110,300,50)
        self.lb3.setStyleSheet("color : blue")

        self.ln3 = QLineEdit(self.insert_info)
        self.ln3.setGeometry(360,110,300,50)
        self.ln3.setStyleSheet("color : magenta")
        self.ln3.setAlignment(Qt.AlignCenter)

        self.lb4 = QLabel("Qo'nish vaqti : ",self.insert_info)
        self.lb4.setGeometry(800,110,300,50)
        self.lb4.setStyleSheet("color : blue")

        self.ln4 = QLineEdit(self.insert_info)
        self.ln4.setGeometry(1120,110,300,50)
        self.ln4.setStyleSheet("color : magenta")
        self.ln4.setAlignment(Qt.AlignCenter)

        self.btn1 = QPushButton("Add Data",self.insert_info)
        self.btn1.setGeometry(1200,170,300,50)
        self.btn1.setFont(QFont("Times New Roman",22))
        self.btn1.setStyleSheet("""color : rgb(0,128,128);
                    background-color: black;
                    border-style : solid;
                    border-width: 3px;
                    border-radius : 25;""")
        self.btn1.clicked.connect(self.add_info)

    def add_info(self):
        self.con = myc.connect(host = 'localhost',user = 'root', password = 'Najot1995!',database = 'aeroport')
        self.kur = self.con.cursor()
        self.kur.execute("""
                        CREATE TABLE IF NOT EXISTS reys(id INT PRIMARY KEY AUTO_INCREMENT,
                        uchish_shaxri VARCHAR(30) NOT NULL DEFAULT "Tashkent",
                        uchish_vaqti DATE NOT NULL, qunish_shaxri VARCHAR(30) NOT NULL DEFAULT "DUBAY",
                        qunish_vaqti DATE NOT NULL);""")

        ush = self.ln1.text()
        qsh = self.ln2.text()
        uv  = self.ln3.text()
        qv  = self.ln4.text() 

        sql = "INSERT INTO reys(uchish_shaxri, uchish_vaqti, qunish_shaxri, qunish_vaqti) VALUES (%s,%s,%s,%s);"
        self.kur.execute(sql,(ush,uv,qsh,qv))
        self.con.commit()
        self.show_info()

    def show_info(self,sql = "SELECT * FROM reys;"):

        self.tablo.clear()
        self.tablo.setGeometry(50,300,1500,500)
        self.tablo.setFont(QFont("Times New Roman",24))
        self.tablo.setStyleSheet("color: magenta")
        self.tablo.setRowCount(14)
        self.tablo.setColumnCount(5)
        self.tablo.setHorizontalHeaderLabels(["id","Uchish shahri","Uchish vaqti","Qo'nish shahri","Qo'nish vaqti"])
        header = self.tablo.horizontalHeader()
        header.setFont(QFont("Times New Roman",24))
        for x in range(5):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","",""]
        self.tablo.setVerticalHeaderLabels(lb)

        self.con = myc.connect(host = 'localhost',user = 'root', password = 'Najot1995!',database = 'aeroport')
        self.kur = self.con.cursor()
        self.kur.execute(sql)
        index = 0
        for x in self.kur.fetchall():
            self.tablo.setItem(index,0,QTableWidgetItem(str(x[0])))
            self.tablo.setItem(index,1,QTableWidgetItem(str(x[1])))
            self.tablo.setItem(index,2,QTableWidgetItem(str(x[2])))
            self.tablo.setItem(index,3,QTableWidgetItem(str(x[3])))
            self.tablo.setItem(index,4,QTableWidgetItem(str(x[4])))
            index += 1

    def update_data(self):

        self.lb_select = QLabel("O'zgartirilayotgan ustunni tanlang : ",self.update_info)
        self.lb_select.setGeometry(50,50,650,50)
        self.lb_select.setStyleSheet("color  : blue")

        self.select_cmb = QComboBox(self.update_info)
        self.select_cmb.setGeometry(550,50,400,50)
        self.select_cmb.setStyleSheet("color  : blue")
        self.select_cmb.addItems(["id","Uchish shaxri","Qo'nish shaxri","Uchish vaqti","Qo'nish vaqti"])

        self.ln_up = QLineEdit(self.update_info)
        self.ln_up.setGeometry(1000,50,400,50)
        self.ln_up.setStyleSheet("color : magenta")
        self.ln_up.setAlignment(Qt.AlignCenter)
        self.ln_up.setPlaceholderText("Qiymatni kiriting : ")

        self.lb_select_1 = QLabel("Reys ma'lumotini tanlang : ",self.update_info)
        self.lb_select_1.setGeometry(50,110,650,50)
        self.lb_select_1.setStyleSheet("color  : blue")

        self.select_cmb_1 = QComboBox(self.update_info)
        self.select_cmb_1.setGeometry(550,110,400,50)
        self.select_cmb_1.setStyleSheet("color  : blue")
        self.select_cmb_1.addItems(["id","Uchish shaxri","Qo'nish shaxri","Uchish vaqti","Qo'nish vaqti"])

        self.ln_up1 = QLineEdit(self.update_info)
        self.ln_up1.setGeometry(1000,110,400,50)
        self.ln_up1.setStyleSheet("color : magenta")
        self.ln_up1.setAlignment(Qt.AlignCenter)
        self.ln_up1.setPlaceholderText("Qiymatni kiriting : ")

        self.btn2 = QPushButton("Edit Data",self.update_info)
        self.btn2.setGeometry(1200,170,300,50)
        self.btn2.setFont(QFont("Times New Roman",22))
        self.btn2.setStyleSheet("""color : rgb(0,128,128);
                    background-color: black;
                    border-style : solid;
                    border-width: 3px;
                    border-radius : 25;""")
        self.btn2.clicked.connect(self.edit_info)

    def edit_info(self):
        ls = ["id","uchish_shaxri", "qunish_shaxri", "uchish_vaqti", "qunish_vaqti"]
        self.con = myc.connect(host = 'localhost',user = 'root', password = 'Najot1995!',database = 'aeroport')
        self.kur = self.con.cursor()
        self.kur.execute(f"""UPDATE reys SET {ls[self.select_cmb.currentIndex()]} = "{self.ln_up.text()}"
                         WHERE {ls[self.select_cmb_1.currentIndex()]} = "{self.ln_up1.text()}" """)
        self.con.commit()
        self.show_info()

    def delete_data(self):
        
        self.lb_delete = QLabel("Ma'lumot ustunni tanlang : ",self.delete_info)
        self.lb_delete.setGeometry(50,50,700,50)
        self.lb_delete.setStyleSheet("color  : blue")

        self.delete_cmb = QComboBox(self.delete_info)
        self.delete_cmb.setGeometry(400,50,400,50)
        self.delete_cmb.setStyleSheet("color  : blue")
        self.delete_cmb.addItems(["id","Uchish shaxri","Qo'nish shaxri","Uchish vaqti","Qo'nish vaqti"])

        self.ln_up2 = QLineEdit(self.delete_info)
        self.ln_up2.setGeometry(900,50,400,50)
        self.ln_up2.setStyleSheet("color : magenta")
        self.ln_up2.setAlignment(Qt.AlignCenter)
        self.ln_up2.setPlaceholderText("Qiymatni kiriting : ")

        self.btn3 = QPushButton("Delete Data",self.delete_info)
        self.btn3.setGeometry(1200,170,300,50)
        self.btn3.setFont(QFont("Times New Roman",22))
        self.btn3.setStyleSheet("""color : rgb(0,128,128);
                    background-color: black;
                    border-style : solid;
                    border-width: 3px;
                    border-radius : 25;""")
        self.btn3.clicked.connect(self.deleted_info)

    def deleted_info(self):
        ls = ["id","uchish_shaxri", "qunish_shaxri", "uchish_vaqti", "qunish_vaqti"]
        self.con = myc.connect(host = 'localhost',user = 'root', password = 'Najot1995!',database = 'aeroport')
        self.kur = self.con.cursor()
        if (self.delete_cmb.currentText() == "id"):
            sql = f"DELETE FROM reys WHERE id = {self.ln_up2.text()};"
        else :
            sql = f"""DELETE FROM reys WHERE {ls[self.delete_cmb.currentIndex()]} = "{self.ln_up2.text()}";"""

        self.kur.execute(sql)
        self.con.commit()
        self.show_info()
          
    def find_data(self):

        self.lb_find = QLabel("Ma'lumot ustunni tanlang : ",self.find_info)
        self.lb_find.setGeometry(50,50,700,50)
        self.lb_find.setStyleSheet("color  : blue")

        self.find_cmb = QComboBox(self.find_info)
        self.find_cmb.setGeometry(400,50,400,50)
        self.find_cmb.setStyleSheet("color  : blue")
        self.find_cmb.addItems(["id","Uchish shaxri","Qo'nish shaxri","Uchish vaqti","Qo'nish vaqti"])

        self.ln_up3 = QLineEdit(self.find_info)
        self.ln_up3.setGeometry(900,50,400,50)
        self.ln_up3.setStyleSheet("color : magenta")
        self.ln_up3.setAlignment(Qt.AlignCenter)
        self.ln_up3.setPlaceholderText("Qiymatni kiriting : ")
        self.ln_up3.textEdited.connect(self.find)

        self.btn4 = QPushButton("Select Data",self.find_info)
        self.btn4.setGeometry(1200,170,300,50)
        self.btn4.setFont(QFont("Times New Roman",22))
        self.btn4.setStyleSheet("""color : rgb(0,128,128);
                    background-color: black;
                    border-style : solid;
                    border-width: 3px;
                    border-radius : 25;""")
        self.btn4.clicked.connect(self.select_info)

    def select_info(self):
        pass

    def find(self):
        st = self.ln_up3.text()
        ls = ["id","uchish_shaxri", "qunish_shaxri", "uchish_vaqti", "qunish_vaqti"]
        sel = ls[self.find_cmb.currentIndex()]
        sql = f"""SELECT * FROM reys WHERE {sel} LIKE "{st}%"; """
        self.show_info(sql)


class connect_database:
    def __init__(self,baza):
        self.con = myc.connect(host = 'localhost',user = 'root',
                                           password = 'Najot1995!', database = f"{baza}")
        self.kur = self.con.cursor()
        self.kur.execute("""Create table if not exists reys(id int primary key auto_increment,
                uchish_shahri varchar(30) NOT NULL Default "Toshkent", 
                uchish_vaqti date NOT NULL,qunish_shahri varchar(30) NOT NULL Default "DUBAY",
                qunish_vaqti date NOT NULL);""")        
        
    def get_info(self,sql = "SELECT * from reys"):
            self.kur.execute(sql)
            return self.kur.fetchall()       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ilova = Project()
    ilova.show()
    sys.exit(app.exec_())