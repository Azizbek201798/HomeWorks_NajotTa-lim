import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
os.system("clear")

def ilova():
    app = QApplication(sys.argv)
    oyna = QWidget()
    oyna.setFont(QFont("Times New Roman",26))
    oyna.setWindowTitle("Register")
    oyna.setStyleSheet("color:rgb(255,0,0)")

    hb1 = QHBoxLayout()
    lb1 = QLabel("Ism: ")
    lnd1 = QLineEdit()
    lnd1.setAlignment(Qt.AlignCenter)
    hb1.addWidget(lb1)
    hb1.addWidget(lnd1)

    hb2 = QHBoxLayout()
    lb2 = QLabel("Familiya: ")
    lnd2 = QLineEdit()
    lnd2.setAlignment(Qt.AlignCenter)
    hb2.addWidget(lb2)
    hb2.addWidget(lnd2)

    hb3 = QHBoxLayout()
    lb3 = QLabel("Guruh: ")
    lnd3 = QLineEdit()
    lnd3.setAlignment(Qt.AlignCenter)
    hb3.addWidget(lb3)
    hb3.addWidget(lnd3)

    hb4 = QHBoxLayout()
    lb4 = QLabel("Jins : ")
    erkak = QRadioButton("Erkak")
    ayol = QRadioButton("Ayol")
    hb4.addWidget(lb4)
    hb4.addWidget(erkak)
    hb4.addWidget(ayol)

    hb5 = QHBoxLayout()
    a = QPushButton("Qo'shish")
    a.setStyleSheet("color: rgb(0,0,255)")
    b = QPushButton("Yopish")
    b.setStyleSheet("color: rgb(0,0,255)")
    hb5.addWidget(a)
    hb5.addWidget(b)

    vb = QVBoxLayout()
    vb.addWidget(hb1)
    vb.addStretch()
    vb.addWidget(hb2)
    vb.addStretch()
    vb.addWidget(hb3)
    vb.addStretch()
    vb.addWidget(hb4)
    vb.addStretch()
    vb.addWidget(hb5)
    vb.addStretch()

    oyna.setLayout(vb)
    oyna.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ilova()