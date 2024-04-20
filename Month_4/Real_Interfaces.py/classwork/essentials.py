import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class full_name(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,600,600)
        self.setWindowTitle("My first project!")
        self.setWindowIcon(QIcon())
        lb = QLabel(self)
        lb.setText("Messi")
        lb.setGeometry(150,260,500,100)
        lb.setFont(QFont("Poor Richard",24))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    project = full_name()
    project.show()
    sys.exit(app.exec_())
