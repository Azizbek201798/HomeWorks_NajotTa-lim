import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
os.system("clear")

class calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : rgb(41,171,135); color: rgb(0,255,0)")
        self.setGeometry(100,100,600,480)
        self.setWindowTitle("Program Simple Calculator")
        self.setWindowIcon(QIcon())

        lb1 = QLabel(self)
        lb1.setStyleSheet("""
            background-color:   rgb(64,130,109);
            color:              rgb(57,255,20);
            border-color:       rgb(230,0,38);
            border-radius:      15px;
            border-width:       3px;
            border-style:       solid;""")
        lb1.setText("1-sonni kiriting :")
        lb1.setGeometry(70,50,260,50)
        lb1.setFont(QFont("Times",24))

        self.lnt1 = QLineEdit(self)
        self.lnt1.resize(250,50)
        self.lnt1.move(340,50)
        self.lnt1.setStyleSheet("""
            background-color:   rgb(245,230,209);
            color:              rgb(0,0,255);
            border-color:       rgb(232,50,138);
            border-radius:      15px;
            border-width:       3px;
            border-style:       dotted;""")
        self.lnt1.setFont(QFont("Consolas",22))
        self.lnt1.setAlignment(Qt.AlignCenter)

        lb2 = QLabel(self)
        lb2.setStyleSheet("""
            background-color:   rgb(64,130,109);
            color:              rgb(57,255,20);
            border-color:       rgb(230,0,38);
            border-radius:      15px;
            border-width:       3px;
            border-style:       solid;""")
        lb2.setText("2-sonni kiriting :")
        lb2.setGeometry(70,110,260,50)
        lb2.setFont(QFont("Times",24))

        self.lnt2 = QLineEdit(self)
        self.lnt2.resize(250,50)
        self.lnt2.move(340,110)
        self.lnt2.setStyleSheet("""
            background-color:   rgb(245,230,209);
            color:              rgb(0,0,255);
            border-color:       rgb(232,500,138);
            border-radius:      15px;
            border-width:       3px;
            border-style:       dotted;""")
        self.lnt2.setFont(QFont("Consolas",22))
        self.lnt2.setAlignment(Qt.AlignCenter)

        self.result = QLabel(self)
        self.result.setStyleSheet("""
            color:              rgb(57,255,20);
            """)
        self.result.setVisible(False)
        # self.result.setText("Result :")
        self.result.setGeometry(70,250,260,50)
        self.result.setFont(QFont("Times",40))

        btn = QPushButton("Calculate",self)
        btn.setFont(QFont("Times",24))
        btn.setStyleSheet("""
            background-color:   rgb(0,0,0);
            color:              rgb(0,255,0);
            border-color:       rgb(0,255,0);
            border-radius:      15px;
            border-width:       2px;
            border-style:       inset;""")
        btn.setGeometry(250,170,300,60)
        btn.clicked.connect(self.hisobla)

    def hisobla(self):
        a = self.lnt1.text()
        b = self.lnt2.text()
        self.result.setText(f"Result:{str(int(a) + int(b))}")
        self.result.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = calc()
    project.show()
    sys.exit(app.exec_())

# unset GTK_PATH