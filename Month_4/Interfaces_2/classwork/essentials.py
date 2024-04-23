import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system("clear")

class ilova:
    app = QApplication(sys.argv)
    oyna = QWidget()
    oyna.setFont(QFont("Calibri",24))

    btn1 = QLabel("Ism: ")
    k1 = QLineEdit()
    btn2 = QLabel("Familiya: ")
    k2 = QLineEdit()
    btn3 = QLabel("Guruh: ")
    k3 = QLineEdit()

    vb = QVBoxLayout()
    vb.addWidget(btn1)
    vb.addStretch()
    vb.addWidget(btn2)
    vb.addStretch()
    vb.addWidget(btn3)
    vb.addStretch()

    lb = QLabel("Ismingni kirit : ")
    txt = QLineEdit("Jins: ")
    sp1 = QPushButton("Erkak")
    sp2 = QPushButton("Ayol")

    sb1 = QPushButton("Qo'shish")
    sb2 = QPushButton("Qo'shish")

    hb1 = QHBoxLayout()
    hb1.addWidget(sp1)
    hb1.addWidget(sp2)
    vb.addLayout(hb1)

    hb2 = QHBoxLayout()
    hb2.addWidget(sb1)
    hb2.addWidget(sb2)

    vb.addLayout(hb2)
    oyna.setLayout(vb)
    oyna.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ilova()