import requests
import os
os.system("cls")
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

url = "https://nbu.uz/uz/exchange-rates/json/"

response = requests.get(url)

data = response.json()

# for i in data:
#     print(i)

class ilova(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600,500)
        self.setMinimumSize(600,500)
        self.setStyleSheet("""
            color : rgb(0,0,0);    
            border-radius: 15px;
            """)
        self.setFont(QFont("Times New Roman",32))

        self.lb1 = QLabel("SUM",self)
        self.lb1.setFont(QFont("Times New Roman",20))
        self.lb1.setGeometry(400,100,120,40)
        self.lb1.setStyleSheet("""
            background-color : rgb(255,229,204);    
            color : rgb(255,0,0);
            """)
        self.lb1.setAlignment(Qt.AlignCenter)

        self.lb2 = QLabel(self)
        self.lb2.setFont(QFont("Times New Roman",20))
        self.lb2.setGeometry(400,200,120,40)
        self.lb2.setStyleSheet("""
            background-color : rgb(255,229,204);    
            color:rgb(255,0,0);
            """)
        self.lb2.setAlignment(Qt.AlignCenter)
        # self.lb2.setText(str(int(self.ln.text()) * ))

        self.cmb = QComboBox(self)
        self.cmb.setGeometry(100,100,120,40)
        for x in data:
            self.cmb.addItem(x["code"])
        
        self.ln = QLineEdit(self)
        self.ln.setGeometry(100,200,120,40)
        
    # def tap(self):
    #     digit_count = sum(char.isdigit() for char in self.ln.text())
    #     if digit_count < 2:
    #         return False

    #     uppercase_count = sum(char.isupper() for char in self.ln.text())
    #     if uppercase_count < 1:
    #         return False

    #     if len(self.ln.text()) < 8:
    #         return False
    #     return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = ilova()
    oyna.show()
    sys.exit(app.exec_())