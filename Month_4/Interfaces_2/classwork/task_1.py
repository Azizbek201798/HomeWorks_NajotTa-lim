import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("clear")

def ilova():
    app = QApplication(sys.argv)
    oyna = QWidget()
    oyna.setFont(QFont("Times New Roman",24))

    btn1 = QPushButton("Continue Game")
    btn2 = QPushButton("New Game")
    btn3 = QPushButton("Records")
    btn4 = QPushButton("Exit")

    vb = QVBoxLayout()
    vb.addWidget(btn1)
    vb.addStretch()
    vb.addWidget(btn2)
    vb.addStretch()
    vb.addWidget(btn3)
    vb.addStretch()
    vb.addWidget(btn4)

    lb = QLabel("Ismingizni kiriting : ")
    text = QLineEdit()
    sbm = QPushButton("SUBMIT")

    hb = QHBoxLayout()
    hb.addWidget(lb)
    hb.addWidget(text)
    hb.addWidget(sbm)
    
    vb.addLayout(hb)
    oyna.setLayout(vb)
    oyna.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ilova()
