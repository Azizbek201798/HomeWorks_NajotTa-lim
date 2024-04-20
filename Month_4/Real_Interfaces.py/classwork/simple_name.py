import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class name(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : rgb(0,128,128)")
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("Program Barselona")
        self.setWindowIcon(QIcon())

        lb = QLabel(self)
        lb.setText("""Barselona
                Barselona
                                Barselona""")
        lb.setStyleSheet("""color : rgb(0,255,0)""")
        lb.setGeometry(70,100,600,300)
        lb.setFont(QFont("Times",24))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = name()
    project.show()
    sys.exit(app.exec_())

# unset GTK_PATH