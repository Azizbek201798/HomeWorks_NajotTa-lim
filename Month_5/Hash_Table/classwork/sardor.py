import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as myc
from hashlib import sha256
import bcrypt

class login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Log in')
        self.setMaximumSize(800, 600)
        self.setMinimumSize(800, 600)

        self.user1 = QLabel("user:", self)
        self.user1.setFont(QFont("Poor Richard", 22))
        self.user1.setGeometry(100, 100, 300, 50)

        self.user_ln1 = QLineEdit("", self)
        self.user_ln1.setFont(QFont("Poor Richard", 22))
        self.user_ln1.setGeometry(200, 100, 300, 50)

        self.password1 = QLabel("password:", self)
        self.password1.setFont(QFont("Poor Richard", 22))
        self.password1.setGeometry(20, 170, 300, 50)

        self.password_ln1 = QLineEdit("", self)
        self.password_ln1.setFont(QFont("Poor Richard", 22))
        self.password_ln1.setGeometry(200, 170, 300, 50)
        self.password_ln1.setEchoMode(QLineEdit.Password)

        self.check_btn = QPushButton("Check", self)
        self.check_btn.setFont(QFont("Poor Richard",22))
        self.check_btn.setGeometry(400,250,300,60)
        self.check_btn.setStyleSheet("""color: white;
                                    background-color: rgb(0,255,0);
                                    border-color: rgb(50,205,50);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.check_btn.clicked.connect(self.show_info)



    def show_info(self):
        usrr = self.user_ln1.text()
        psww = self.password_ln1.text()
        psww = psww.encode('utf-8')
        kod = sha256(psww).hexdigest()

        self.con = myc.connect(host='localhost', user='root', password='2005', database='malumotlar')
        self.kur = self.con.cursor()

        self.kur.execute("SELECT * FROM users WHERE user = %s AND password = %s", (usrr, kod))
        result = self.kur.fetchone()

        if result:
            QMessageBox.information(self, "Success", f"Welcome {usrr}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Warning", "User or Password is incorrect", QMessageBox.Ok)

        self.con.close()




class registration(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration')
        self.setMaximumSize(800, 600)
        self.setMinimumSize(800, 600)

        self.user = QLabel("user:", self)
        self.user.setFont(QFont("Poor Richard", 22))
        self.user.setGeometry(100, 100, 300, 50)

        self.user_ln = QLineEdit("", self)
        self.user_ln.setFont(QFont("Poor Richard", 22))
        self.user_ln.setGeometry(200, 100, 300, 50)

        self.password = QLabel("password:", self)
        self.password.setFont(QFont("Poor Richard", 22))
        self.password.setGeometry(20, 170, 300, 50)

        self.password_ln = QLineEdit("", self)
        self.password_ln.setFont(QFont("Poor Richard", 22))
        self.password_ln.setGeometry(200, 170, 300, 50)
        self.password_ln.setEchoMode(QLineEdit.Password)

        self.sha256_btn = QRadioButton("sha256",self)
        self.sha256_btn.setFont(QFont("Poor Richard",18))
        self.sha256_btn.setGeometry(350,220,300,60)

        self.bcrypt_btn = QRadioButton("bcrypt",self)
        self.bcrypt_btn.setFont(QFont("Poor Richard",18))
        self.bcrypt_btn.setGeometry(500,220,300,60)

        self.rgstr_btn = QPushButton("Register", self)
        self.rgstr_btn.setFont(QFont("Poor Richard",22))
        self.rgstr_btn.setGeometry(400,280,300,60)
        self.rgstr_btn.setStyleSheet("""color: white;
                                    background-color: rgb(0,255,0);
                                    border-color: rgb(50,205,50);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.rgstr_btn.clicked.connect(self.add_info)
        
    def add_info(self):
        usr = self.user_ln.text()
        psw = self.password_ln.text()
        if self.sha256_btn.isChecked():
            psw = psw.encode('utf-8')
            kod = sha256(psw).hexdigest()
        elif self.bcrypt_btn.isChecked():
            psw = psw.encode('utf-8')
            kod = bcrypt.hashpw(psw,bcrypt.gensalt())
        self.con = myc.connect(host='localhost', user='root', password='2005', database='malumotlar')
        self.kur = self.con.cursor()

        self.kur.execute("SELECT * FROM users WHERE user = %s", (usr,))
        result = self.kur.fetchone()

        if result:
            QMessageBox.warning(self, "Warning", "This username already exists.", QMessageBox.Ok)
        else:
            sql = "INSERT INTO users (user, password) VALUES (%s, %s)"
            self.kur.execute(sql, (usr, kod))
            self.con.commit()
            QMessageBox.information(self, "Success", "User registered successfully.", QMessageBox.Ok)

        self.con.close()


class baza_connection(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram")
        self.setMaximumSize(800, 600)
        self.setMinimumSize(800, 600)

        self.sign_btn = QPushButton("Sign up", self)
        self.sign_btn.setFont(QFont("Poor Richard",22))
        self.sign_btn.setGeometry(250,270,300,60)
        self.sign_btn.setStyleSheet("""color: white;
                                    background-color: rgb(30,144,255);
                                    border-color: rgb(65,105,225);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.sign_btn.clicked.connect(self.registratsiya)


        self.log_btn = QPushButton("Log in", self)
        self.log_btn.setFont(QFont("Poor Richard",22))
        self.log_btn.setGeometry(250,200,300,60)
        self.log_btn.setStyleSheet("""color: white;
                                    background-color: rgb(30,144,255);
                                    border-color: rgb(65,105,225);
                                    border-width: 3px;
                                    border-style: solid;
                                    border-radius: 15;""")
        self.log_btn.clicked.connect(self.kirish)
    def kirish(self):
        self.third_window = login()
        self.third_window.show()


    def registratsiya(self):
        self.second_window = registration()
        self.second_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = baza_connection()
    project.show()
    sys.exit(app.exec_())