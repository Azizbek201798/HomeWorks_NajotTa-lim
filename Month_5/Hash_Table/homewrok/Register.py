import os
import sys
import bcrypt
from hashlib import sha256
import mysql.connector
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
os.system("clear")

# ESLATMA:
# 1) Bir xil username li foydalanuvchilar kiritilishi mumkin emas!
# 2) Agar Kiritilgan login,parol mavjud bo'lmasa message boxdagi xabarga qarab 

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1000,390)
        self.setMinimumSize(1000,390)
        self.setWindowTitle("Authentification")

        self.btn1 = QPushButton("Sign In",self)
        self.btn1.setGeometry(100,50,300,50)
        self.btn1.setFont(QFont("Times New Roman",25)) 

        self.lb1_1 = QLabel("Username :",self)
        self.lb1_1.setGeometry(30,150,150,30)
        self.lb1_1.setFont(QFont("Times New Roman",20)) 

        self.lb1_2 = QLabel("Password  :",self)
        self.lb1_2.setGeometry(30,200,150,30)
        self.lb1_2.setFont(QFont("Times New Roman",20)) 

        self.ln1_1 = QLineEdit(self)
        self.ln1_1.setGeometry(200,150,250,40)
        self.ln1_1.setFont(QFont("Times New Roman",20)) 
        self.ln1_1.setAlignment(Qt.AlignCenter)

        self.ln1_2 = QLineEdit(self)
        self.ln1_2.setGeometry(200,200,250,40)
        self.ln1_2.setFont(QFont("Times New Roman",20)) 
        self.ln1_2.setAlignment(Qt.AlignCenter)

        self.btn1_1 = QPushButton("Check",self)
        self.btn1_1.setGeometry(330,250,120,40)
        self.btn1_1.setFont(QFont("Times New Roman",20)) 
        # ----------------------------------------------
        self.btn1_1.clicked.connect(self.Check_data)

        self.btn2 = QPushButton("Sign Up",self)
        self.btn2.setGeometry(600,50,300,50)
        self.btn2.setFont(QFont("Times New Roman",25)) 

        self.btn2_1 = QPushButton("Register",self)
        self.btn2_1.setGeometry(770,300,150,40)
        self.btn2_1.setFont(QFont("Times New Roman",20)) 
        # ----------------------------------------------
        self.btn2_1.clicked.connect(self.Insert_data)

        self.lb2_1 = QLabel("UserName :",self)
        self.lb2_1.setGeometry(500,150,150,30)
        self.lb2_1.setFont(QFont("Times New Roman",20)) 

        self.lb2_2 = QLabel("Password  :",self)
        self.lb2_2.setGeometry(500,200,150,30)
        self.lb2_2.setFont(QFont("Times New Roman",20)) 

        self.ln2_1 = QLineEdit(self)
        self.ln2_1.setGeometry(670,150,250,40)
        self.ln2_1.setFont(QFont("Times New Roman",20)) 
        self.ln2_1.setAlignment(Qt.AlignCenter)

        self.ln2_2 = QLineEdit(self)
        self.ln2_2.setGeometry(670,200,250,40)
        self.ln2_2.setFont(QFont("Times New Roman",20)) 
        self.ln2_2.setAlignment(Qt.AlignCenter)

        self.rb_1 = QRadioButton("SHA256",self)
        self.rb_1.setGeometry(700,250,150,40)
        self.rb_1.setFont(QFont("Times New Roman",16)) 

        self.rb_2 = QRadioButton("bcrypt",self)
        self.rb_2.setGeometry(820,250,150,40)
        self.rb_2.setFont(QFont("Times New Roman",16)) 

    def Insert_data(self):
        os.system("cls")
        obj = Connect_database('Register')
        UserName = self.ln2_1.text()
        if self.rb_2.isChecked():
            Password = self.ln2_2.text()
            pr1 = Password.encode('utf-8')
            tuz = bcrypt.gensalt()
            h_password = bcrypt.hashpw(pr1,tuz)
        elif self.rb_1.isChecked():
            Password = self.ln2_2.text()
            pr1 = Password.encode('utf-8')
            h_password = sha256(pr1).hexdigest()
        else :
            h_password = self.ln2_2.text()

        obj.Input_info(UserName,h_password)

        msg = QMessageBox()
        msg.setFont(QFont("Times New Roman",16)) 
        msg.setStyleSheet("background-color: rgb(255,204,153)")
        msg.setIcon(QMessageBox.Information)
        msg.setText("Ma'lumot bazaga qo'shildi")
        msg.setWindowTitle("Info")
        msg.exec_()

    def Check_data(self):
        os.system("clear")
        obj = Connect_database('Register')
        UserName = self.ln1_1.text()
        Password = self.ln1_2.text()
        obj.Check_Info(UserName,Password)

class Connect_database:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
    def __init__(self,baza):
        self.con = mysql.connector.connect(host = 'localhost',user = 'root',
                                           password = 'Najot1995!',database = f"{baza}")
        self.kur = self.con.cursor()
        self.kur.execute("""CREATE TABLE IF NOT EXISTS users(user_id INT PRIMARY KEY AUTO_INCREMENT,
                         Username VARCHAR(30),
                         Password TEXT);""")

    def Input_info(self,UserName,Password):
        sql = """INSERT INTO users(Username,Password) VALUES(%s,%s);"""
        values = (UserName,Password)
        self.kur.execute(sql,values)
        self.con.commit()
        print("Ma'lumot bazaga yozildi")

    def Check_Info(self,UserName,Password): 

        sql = """SELECT * FROM users WHERE Username = %s;"""
        values = UserName
        self.kur.execute(sql,[values])
        result = self.kur.fetchall()
        for x in result:
            if sha256(Password.encode('utf-8')).hexdigest() == list(list(result)[0])[2]:
                msg = QMessageBox()
                msg.setFont(QFont("Times New Roman",16)) 
                msg.setStyleSheet("background-color: rgb(255,204,153)")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Saytga muvaffaqaiyatli kirdingiz!")
                msg.setWindowTitle("Info")
                msg.exec_()
            elif bcrypt.checkpw(Password.encode('utf-8'),list(list(result)[0])[2].encode('utf-8')):
                print(list(list(result)[0])[2].encode('utf-8'))
                print(Password.encode('utf-8'))
                msg = QMessageBox()
                msg.setFont(QFont("Times New Roman",16)) 
                msg.setStyleSheet("background-color: rgb(255,204,153)")
                msg.setIcon(QMessageBox.Information)
                msg.setText("Saytga muvaffaqaiyatli kirdingiz!")
                msg.setWindowTitle("Info")
                msg.exec_()
            else :
                msg = QMessageBox()
                msg.setFont(QFont("Times New Roman",16)) 
                msg.setStyleSheet("background-color: rgb(255,204,153)")
                msg.setIcon(QMessageBox.Information)
                msg.setText("""Bunday userli foydalanuvchi mavjud emas!Avval ro'yxatdan o'ting!""")
                msg.setWindowTitle("Info")
                msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = Register()
    oyna.show()
    sys.exit(app.exec_())