import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector as myc
import mysql.connector

class project(QTabWidget):
    def __init__(self,p = None):
        super(project,self).__init__(p)
        self.setMaximumSize(1600,900)
        self.setMinimumSize(1600,900)
        
        self.setWindowTitle("Baza bilan ishlash")
        self.setFont(QFont("Consolas",22))
        
        self.insert_info = QWidget()
        #self.insert_info.setStyleSheet("background-color: blue;")
        self.update_info = QWidget()
        #self.update_info.setStyleSheet("background-color: red;")
        self.delete_info = QWidget()
        #self.delete_info.setStyleSheet("background-color: magenta;")
        self.find_info  =  QWidget()
        
        self.addTab(self.insert_info,"Insert data")
        self.addTab(self.update_info,"Update data")
        self.addTab(self.delete_info,"Delete data")
        self.addTab(self.find_info,"Find Data")
        
        self.insert_data()
        
    def insert_data(self):
        self.lb = QLabel("Uchish shahri: ",self.insert_info)
        self.lb.setGeometry(50,50,300,50)
        self.lb.setStyleSheet("color: blue;")
        
        self.ln = QLineEdit(self.insert_info)
        self.ln.setGeometry(360,50,300,50)
        self.ln.setStyleSheet("color: magenta;")
        self.ln.setAlignment(Qt.AlignCenter)
        
        self.lb1 = QLabel("Qo'nish shahri: ",self.insert_info)
        self.lb1.setGeometry(800,50,300,50)
        self.lb1.setStyleSheet("color: blue;")
        
        self.ln1 = QLineEdit(self.insert_info)
        self.ln1.setGeometry(1120,50,300,50)
        self.ln1.setStyleSheet("color: magenta;")
        self.ln1.setAlignment(Qt.AlignCenter)
        
        self.lb2 = QLabel("Uchish vaqti: ",self.insert_info)
        self.lb2.setGeometry(50,110,300,50)
        self.lb2.setStyleSheet("color: blue;")
        
        self.ln2 = QLineEdit(self.insert_info)
        self.ln2.setGeometry(360,110,300,50)
        self.ln2.setStyleSheet("color: magenta;")
        self.ln2.setAlignment(Qt.AlignCenter)
        
        self.lb3 = QLabel("Qo'nish vaqti: ",self.insert_info)
        self.lb3.setGeometry(800,110,300,50)
        self.lb3.setStyleSheet("color: blue;")
        
        self.ln3 = QLineEdit(self.insert_info)
        self.ln3.setGeometry(1120,110,300,50)
        self.ln3.setStyleSheet("color: magenta;")
        self.ln3.setAlignment(Qt.AlignCenter)
        
        self.btn = QPushButton("Add Data",self.insert_info)
        self.btn.setGeometry(1200,170,300,50)
        self.btn.setFont(QFont("Calibri",28))
        self.btn.setStyleSheet("""color: rgb(0,128,128);
                    background-color: black;
                    border-width: 3px;
                    border-style: solid;
                    border-color: rgb(0,128,128);
                               """)
        self.btn.clicked.connect(self.add_info)

        self.tablo_1 = QTableWidget(self)
        self.tablo_1.setGeometry(50,350,1500,500)
        self.tablo_1.setFont(QFont("Times New Roman",24))
        self.tablo_1.setStyleSheet("color: magenta")
        self.tablo_1.setRowCount(14)
        self.tablo_1.setColumnCount(5)
        self.tablo_1.setHorizontalHeaderLabels(["id,uchish_shahri,uchish_vaqti,qunish_shahri,qunish_vaqti"])
        header = self.tablo_1.horizontalHeader()
        header.setFont(QFont("Times New Roman",24))
        for x in range(4):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","",""]
        self.tablo_1.setVerticalHeaderLabels(lb)
        self.show_info("""Select * from reys;""")
    
    def add_info(self):
        self.con = myc.connect(host = 'localhost',user = 'root',password = 'Najot1995!',database = 'aeroport')
        self.kur = self.con.cursor()
        self.kur.execute("""
                Create table if not exists reys(id int primary key auto_increment,
                uchish_shahri varchar(30) NOT NULL Default "Toshkent", 
                uchish_vaqti date NOT NULL,qunish_shahri varchar(30) NOT NULL Default "DUBAY",
                qunish_vaqti date NOT NULL);""")
        
        us = self.ln.text()
        uv = self.ln2.text()
        qs = self.ln1.text()
        qv = self.ln3.text()
        
        sql = "INSERT INTO reys(uchish_shahri,uchish_vaqti,qunish_shahri,qunish_vaqti) Values(%s,%s,%s,%s);"
        self.kur.execute(sql,(us,uv,qs,qv))
        self.con.commit()
        
    def show_info(self,sql):
        os.system("clear")
        obj = connect_database("aeroport")
        res = obj.get_info(sql)
        for x in range(len(res)):
            self.tablo_1.setItem(x,0,QTableWidgetItem(str(res[x][0])))
            self.tablo_1.setItem(x,1,QTableWidgetItem(str(res[x][1])))
            self.tablo_1.setItem(x,2,QTableWidgetItem(str(res[x][2])))
            self.tablo_1.setItem(x,3,QTableWidgetItem(str(res[x][3])))
            self.tablo_1.setItem(x,4,QTableWidgetItem(str(res[x][4])))

class connect_database:
    def __init__(self,baza):
        self.con = mysql.connector.connect(host = 'localhost',user = 'root',
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
    ilova = project()
    ilova.show()
    sys.exit(app.exec_())
        
    