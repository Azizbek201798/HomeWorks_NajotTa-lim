import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random
os.system("cls")

class Tac_Toe:
    def __init__(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyin = Tac_Toe()
    uyin.show()
    sys.exit(app.exec_())