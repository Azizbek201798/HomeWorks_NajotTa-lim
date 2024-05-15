import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector as myc

class Project(QTabWidget):
    def __init__(self,p = None):
        super(Project,self).__init__(p)
        self.setMaximumSize(1700,900)
        self.setMinimumSize(1700,900)
        
        self.setWindowTitle("Baza bilan ishlash")
        self.setFont(QFont("Times New Roman",22))
        
        self.insert_info = QWidget()
        self.insert_info.setStyleSheet("background-color: rgb(250,235,215);")
        self.update_info = QWidget()
        self.update_info.setStyleSheet("background-color: rgb(245,222,179);")
        self.delete_info = QWidget()
        self.delete_info.setStyleSheet("background-color: rgb(152,251,152);")
        self.find_info  =  QWidget()
        self.find_info.setStyleSheet("background-color: rgb(48,213,200);")
        
        self.addTab(self.insert_info,"Insert data")
        self.addTab(self.update_info,"Update data")
        self.addTab(self.delete_info,"Delete data")
        self.addTab(self.find_info,"Find Data")

        self.insert_data()
        self.update_data()
        self.delete_data()
        self.find_data()

        self.tablo_1 = QTableWidget(self)

        self.show_info()
        
    def insert_data(self):
        self.lb = QLabel("Maktab Nomi: ",self.insert_info)
        self.lb.setGeometry(50,50,300,50)
        self.lb.setFont(QFont("Times New Roman",22))
        self.lb.setStyleSheet("color: blue;")
        
        self.ln = QLineEdit(self.insert_info)
        self.ln.setGeometry(360,50,300,50)
        self.ln.setStyleSheet("color: magenta;")
        self.ln.setAlignment(Qt.AlignCenter)
        self.ln.setFont(QFont("Times New Roman",22))

        self.lb1 = QLabel("O'quvchilar soni: ",self.insert_info)
        self.lb1.setGeometry(800,50,300,50)
        self.lb1.setFont(QFont("Times New Roman",22))
        self.lb1.setStyleSheet("color: blue;")
        
        self.ln1 = QLineEdit(self.insert_info)
        self.ln1.setGeometry(1120,50,300,50)
        self.ln1.setStyleSheet("color: magenta;")
        self.ln1.setAlignment(Qt.AlignCenter)
        self.ln1.setFont(QFont("Times New Roman",22))

        self.lb2 = QLabel("Ishchilar soni: ",self.insert_info)
        self.lb2.setGeometry(50,110,300,50)
        self.lb2.setStyleSheet("color: blue;")
        self.lb2.setFont(QFont("Times New Roman",22))
        
        self.ln2 = QLineEdit(self.insert_info)
        self.ln2.setGeometry(360,110,300,50)
        self.ln2.setStyleSheet("color: magenta;")
        self.ln2.setAlignment(Qt.AlignCenter)
        self.ln2.setFont(QFont("Times New Roman",22))
        
        self.lb3 = QLabel("Address: ",self.insert_info)
        self.lb3.setGeometry(800,110,300,50)
        self.lb3.setStyleSheet("color: blue;")
        self.lb3.setFont(QFont("Times New Roman",22))

        self.ln3 = QLineEdit(self.insert_info)
        self.ln3.setGeometry(1120,110,300,50)
        self.ln3.setStyleSheet("color: magenta;")
        self.ln3.setAlignment(Qt.AlignCenter)
        self.ln3.setFont(QFont("Times New Roman",22))
        
        self.btn = QPushButton("Add Data",self.insert_info)
        self.btn.setGeometry(1200,200,300,50)
        self.btn.setFont(QFont("Times New Roman",28))
        self.btn.setStyleSheet("""color: rgb(255,0,0);
                    background-color: rgb(255,255,255);
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 15;
                    border-color: rgb(255,0,0);
                               """)
        self.btn.clicked.connect(self.add_info)
    
    def add_info(self):
        self.con = myc.connect(host = 'localhost',user = 'root',password = 'Najot1995!',database = 'maktab')
        self.kur = self.con.cursor()
        self.kur.execute("""
                CREATE TABLE IF NOT EXISTS maktab(id INT PRIMARY KEY AUTO_INCREMENT,
                nomi VARCHAR(30), oquvchilar_soni INT,ishchilar_soni INT,
                address VARCHAR(30));""")
        
        nomi = self.ln.text()
        oquvchilar_soni = self.ln2.text()
        ishchilar_soni = self.ln1.text()
        address = self.ln3.text()
        
        sql = "INSERT INTO maktab(nomi,oquvchilar_soni,ishchilar_soni,address) VALUES(%s,%s,%s,%s);"
        self.kur.execute(sql,(nomi,oquvchilar_soni,ishchilar_soni,address))
        self.con.commit()
        self.show_info()
        
    def show_info(self,sql = "SELECT * from maktab"):
        self.tablo_1.clear()
        self.tablo_1.setGeometry(50,350,1500,500)
        self.tablo_1.setFont(QFont("Times New Roman",24))
        self.tablo_1.setStyleSheet("color: magenta")
        self.tablo_1.setRowCount(14)
        self.tablo_1.setColumnCount(5)
        self.tablo_1.setHorizontalHeaderLabels(["id","Nomi","O'quvchilar_Soni","Ishchilar_Soni","Address"])
        header = self.tablo_1.horizontalHeader()
        header.setFont(QFont("Times New Roman",24))
        for x in range(5):
            header.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        lb = ["","","","","","","","","","","","","",""]
        self.tablo_1.setVerticalHeaderLabels(lb)
        self.con = myc.connect(host = 'localhost',user = 'root',password = 'Najot1995!',database = 'maktab')
        self.kur = self.con.cursor()
        self.kur.execute(sql)
        index = 0
        for x in self.kur.fetchall():
            self.tablo_1.setItem(index,0,QTableWidgetItem(str(x[0])))
            self.tablo_1.setItem(index,1,QTableWidgetItem(str(x[1])))
            self.tablo_1.setItem(index,2,QTableWidgetItem(str(x[2])))
            self.tablo_1.setItem(index,3,QTableWidgetItem(str(x[3])))
            self.tablo_1.setItem(index,4,QTableWidgetItem(str(x[4])))
            index += 1
    
    def update_data(self):
        self.lb_select = QLabel("Yangi ma'lumotni kiriting: ",self.update_info)
        self.lb_select.setGeometry(50,50,700,50)
        self.lb_select.setStyleSheet("color: blue;")
        self.lb_select.setFont(QFont("Times New Roman",22))
        
        self.select_cmb = QComboBox(self.update_info)
        self.select_cmb.setGeometry(760,50,400,50)
        self.select_cmb.setStyleSheet("color: blue;")
        self.select_cmb.addItems(["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"])
        self.select_cmb.setFont(QFont("Times New Roman",22))

        self.ln_up = QLineEdit(self.update_info)
        self.ln_up.setGeometry(1200,50,400,50)
        self.ln_up.setStyleSheet("color: magenta;")
        self.ln_up.setAlignment(Qt.AlignCenter)
        self.ln_up.setPlaceholderText("Qiymatni kiriting: ")       
        self.ln_up.setFont(QFont("Times New Roman",22))
         
        self.lb_select1 = QLabel("Eski ma'lumotni kiriting",self.update_info)
        self.lb_select1.setGeometry(50,110,600,50)
        self.lb_select1.setStyleSheet("color: blue;")
        self.lb_select1.setFont(QFont("Times New Roman",22))
        
        self.select_cmb1 = QComboBox(self.update_info)
        self.select_cmb1.setGeometry(760,110,400,50)
        self.select_cmb1.setStyleSheet("color: blue;")
        self.select_cmb1.addItems(["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"])
        self.select_cmb1.setFont(QFont("Times New Roman",22))
       
        self.ln_up1 = QLineEdit(self.update_info)
        self.ln_up1.setGeometry(1200,110,400,50)
        self.ln_up1.setStyleSheet("color: magenta;")
        self.ln_up1.setAlignment(Qt.AlignCenter)
        self.ln_up1.setPlaceholderText("Qiymatni kiriting: ")       
        self.ln_up1.setFont(QFont("Times New Roman",22))
        
        self.btn1 = QPushButton("Edit Data",self.update_info)
        self.btn1.setGeometry(1200,200,300,50)
        self.btn1.setFont(QFont("Times New Roman",28))
        self.btn1.setStyleSheet("""color: rgb(255,0,0);
                    background-color: rgb(255,255,255);
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 15;
                    border-color: rgb(255,0,0);
                               """)
        self.btn1.clicked.connect(self.edit_info)

    def edit_info(self):
        ls = ["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"]
        self.con = myc.connect(host = 'localhost',user = 'root',password = 'Najot1995!',database = 'maktab')
        self.kur = self.con.cursor()
        self.kur.execute(f"""UPDATE maktab SET 
                         {ls[self.select_cmb.currentIndex()]} = "{self.ln_up.text()}" 
                         where {ls[self.select_cmb1.currentIndex()]} = "{self.ln_up1.text()}" """)
        self.con.commit()
        self.show_info()
    
    
    def delete_data(self):
        self.lb_delete = QLabel("Ma'lumot ustununi tanlang: ",self.delete_info)
        self.lb_delete.setGeometry(50,50,700,50)
        self.lb_delete.setStyleSheet("color: blue;")
        self.lb_delete.setFont(QFont("Times New Roman",22))
        
        self.delete_cmb = QComboBox(self.delete_info)
        self.delete_cmb.setGeometry(500,50,400,50)
        self.delete_cmb.setStyleSheet("color: blue;")
        self.delete_cmb.addItems(["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"])
        self.delete_cmb.setFont(QFont("Times New Roman",22))
        
        self.ln_up2 = QLineEdit(self.delete_info)
        self.ln_up2.setGeometry(1000,50,400,50)
        self.ln_up2.setStyleSheet("color: magenta;")
        self.ln_up2.setAlignment(Qt.AlignCenter)
        self.ln_up2.setPlaceholderText("Qiymatni kiriting: ")       
        self.ln_up2.setFont(QFont("Times New Roman",22))
        
        self.btn2 = QPushButton("Delete Data",self.delete_info)
        self.btn2.setGeometry(1200,200,300,50)
        self.btn2.setFont(QFont("Times New Roman",28))
        self.btn2.setStyleSheet("""color: rgb(255,0,0);
                    background-color: rgb(255,255,255);
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 15;
                    border-color: rgb(255,0,0);
                               """)
        self.btn2.clicked.connect(self.deleted_info)
        
    def deleted_info(self):
        ls = ["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"]
        self.con = myc.connect(host = 'localhost',user = 'root',password = 'Najot1995!',database = 'maktab')
        self.kur = self.con.cursor()
        if (self.delete_cmb.currentText() == "id"):
            sql = f"Delete from maktab where id = {self.ln_up2.text()};"
        else:
            sql = f"""Delete from maktab where {ls[self.delete_cmb.currentIndex()]} = "{self.ln_up2.text()}";"""
        
        self.kur.execute(sql)
        self.con.commit()
        #self.tablo_1.clear()
        self.show_info()
        
    def find_data(self):
        self.lb_find = QLabel("Ma'lumot ustununi tanlang: ",self.find_info)
        self.lb_find.setGeometry(50,50,700,50)
        self.lb_find.setStyleSheet("color: blue;")
        self.lb_find.setFont(QFont("Times New Roman",22))
        
        self.find_cmb = QComboBox(self.find_info)
        self.find_cmb.setGeometry(500,50,400,50)
        self.find_cmb.setStyleSheet("color: blue;")
        self.find_cmb.addItems(["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"])
        self.find_cmb.setFont(QFont("Times New Roman",22))
        
        self.ln_up3 = QLineEdit(self.find_info)
        self.ln_up3.setGeometry(1000,50,400,50)
        self.ln_up3.setStyleSheet("color: magenta;")
        self.ln_up3.setAlignment(Qt.AlignCenter)
        self.ln_up3.setPlaceholderText("Qiymatni kiriting: ")
        self.ln_up3.textEdited.connect(self.find)       
        self.ln_up3.setFont(QFont("Times New Roman",22))
        
        self.btn3 = QPushButton("Select Data",self.find_info)
        self.btn3.setGeometry(1200,200,300,50)
        self.btn3.setFont(QFont("Times New Roman",28))
        self.btn3.setStyleSheet("""color: rgb(255,0,0);
                    background-color: rgb(255,255,255);
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 15;
                    border-color: rgb(255,0,0);
                               """)
        self.btn3.clicked.connect(self.select_info)
    
    def select_info(self):
        pass
    
    def find(self):
        st = self.ln_up3.text()
        ls = ["id","Nomi","Oquvchilar_Soni","Ishchilar_Soni","Address"]
        sel = ls[self.find_cmb.currentIndex()]
        sql  = f"""SELECT * FROM maktab where {sel} LIKE "{st}%";"""
        self.show_info(sql)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ilova = Project()
    ilova.show()
    sys.exit(app.exec_())
        
    