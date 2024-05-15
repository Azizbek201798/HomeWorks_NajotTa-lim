import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class xvay(QMainWindow):

  def __init__(self):
    self.n = 0
    super().__init__()
    self.setGeometry(500,100,1100,600)

    self.lbl = QLabel(self)
    self.lbl.setGeometry(0,0,600,600)
    self.lbl.setStyleSheet("background-color: rgb(0,0,0)")




    self.lblplayer1 = QLabel(self)
    self.lblplayer1.setGeometry(640,40,150,50)
    self.lblplayer1.setText("Player1:")
    self.lblplayer1.setFont(QFont("Times New Roman",24))

    self.lblplayer2 = QLabel(self)
    self.lblplayer2.setGeometry(640,120,150,50)
    self.lblplayer2.setFont(QFont("Times New Roman",24))
    self.lblplayer2.setText("Player2:")





    self.name1 = QLineEdit(self)
    self.name1.setGeometry(800,40,200,50)
    self.name1.setFont(QFont("Times New Roman",24))
    self.name1.setStyleSheet("border-width: 40 px; border-color:4 px")

    self.name2 = QLineEdit(self)
    self.name2.setGeometry(800,120,200,50)
    self.name2.setFont(QFont("Times New Roman",24))
    self.name2.setStyleSheet("border-width: 40 px; border-color:4 px")



    self.sch2 = QLabel(self)
    self.sch2.setText("0")
    self.sch2.setStyleSheet("""
      background-color:rgb(128,0,0);
      border-color:  #ffff00;
      border-width: 3px;
      border-style: solid;
      color: #ffff00 ;
      """)
    self.sch2.setGeometry(1010,40,50,50)

    self.sch1 = QLabel(self)
    self.sch1.setText("0")
    self.sch1.setStyleSheet("""
      background-color:rgb(128,0,0);
      border-color:  #ffff00;
      border-width: 3px;
      border-style: solid;
      color: #ffff00 ;
      """)
    self.sch1.setGeometry(1010,120,50,50)



    self.withcomp = QRadioButton(self)
    self.withcomp.setGeometry(700,200,365,70)
    self.withcomp.setStyleSheet("""
      background-color: rgb(0,25,255);
      border-color: rgb(255,255,0);
      border-width: 3px;
      border-style: solid;

      """)

    self.start = QPushButton(self)
    self.start.setText("Start Game")
    self.start.setGeometry(750,300,250,70)
    self.start.clicked.connect(self.startt)
    self.start.setFont(QFont("Times New Roman",30))
    self.start.setStyleSheet("""
      background-color: rgb(0,25,255);
      border-color: rgb(0,150,255);
      border-width: 3px;
      border-style: solid;
      color: #ffff00 ;
      """)


    self.newgame = QPushButton(self)
    self.newgame.setGeometry(750,400,250,70)
    self.newgame.setText("New Game")
    self.newgame.clicked.connect(self.new)
    self.newgame.setFont(QFont("Times New Roman",30))
    self.newgame.setStyleSheet("""
      background-color: rgb(0,25,255);
      border-color: rgb(0,150,255);
      border-width: 3px;
      border-style: solid;
      selection-color: rgb(234,24,233);
      color: #ffff00 ;""")



    self.result = QLabel(self)
    self.result.setGeometry(700,520,400,70)
    self.result.setText("")
    # self.result.setVisible(True)

    self.bn = QPushButton(self)
    self.bn.setGeometry(0,0,200,200)
    self.bn.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn.clicked.connect(self.bnl)
    self.bn.setFont(QFont("Times New Roman",55))


    self.bn1= QPushButton(self)
    self.bn1.setGeometry(200,0,200,200)
    self.bn1.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn1.clicked.connect(self.bn1l)
    self.bn1.setFont(QFont("Times New Roman",55))



    self.bn2 = QPushButton(self)
    self.bn2.setGeometry(400,0,200,200)
    self.bn2.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn2.clicked.connect(self.bn2l)
    self.bn2.setFont(QFont("Times New Roman",55))

    self.bn3 = QPushButton(self)
    self.bn3.setGeometry(0,200,200,200)
    self.bn3.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn3.clicked.connect(self.bn3l)
    self.bn3.setFont(QFont("Times New Roman",55))


    self.bn4 = QPushButton(self)
    self.bn4.setGeometry(200,200,200,200)
    self.bn4.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn4.clicked.connect(self.bn4l)
    self.bn4.setFont(QFont("Times New Roman",55))

    self.bn5 = QPushButton(self)
    self.bn5.setGeometry(400,200,200,200)
    self.bn5.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn5.clicked.connect(self.bn5l)
    self.bn5.setFont(QFont("Times New Roman",55))


    self.bn6 = QPushButton(self)
    self.bn6.setGeometry(0,400,200,200)
    self.bn6.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn6.clicked.connect(self.bn6l)
    self.bn6.setFont(QFont("Times New Roman",55))

    self.bn7 = QPushButton(self)
    self.bn7.setGeometry(200,400,200,200)
    self.bn7.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn7.clicked.connect(self.bn7l)
    self.bn7.setFont(QFont("Times New Roman",55))


    self.bn8 = QPushButton(self)
    self.bn8.setGeometry(400,400,200,200)
    self.bn8.setStyleSheet("""
      background-color: rgb(0,0,255);
      border-color: rgb(255,255,255);
      border-width: 3px;
      border-style: solid;""")
    self.bn8.setFont(QFont("Times New Roman",55))
    self.bn8.clicked.connect(self.bn8l)

  def name(self):
    return f"{self.name1}"

  def bnl(self):
    if self.n % 2 == 0:
      self.bn.setText("x")
    else:
      self.bn.setText("0")
    self.n += 1
    self.check()
    if self.withcomp.isChecked():
      print("dhsubhd")

  def bn1l(self):
    if self.n % 2 == 0:
      self.bn1.setText("x")
    else:
      self.bn1.setText("0")
    self.n += 1
    self.check()


  def bn2l(self):
    if self.n % 2 == 0:
      self.bn2.setText("x")
    else:
      self.bn2.setText("0")
    self.n += 1
    self.check()



  def bn3l(self):
    if self.n % 2 == 0:
      self.bn3.setText("x")
    else:
      self.bn3.setText("0")
    self.n += 1
    self.check()



  def bn4l(self):
    if self.n % 2 == 0:
      self.bn4.setText("x")
    else:
      self.bn4.setText("0")
    self.n += 1
    self.check()



  def bn5l(self):
    if self.n % 2 == 0:
      self.bn5.setText("x")
    else:
      self.bn5.setText("0")
    self.n += 1
    self.check()


  def bn6l(self):
    if self.n % 2 == 0:
      self.bn6.setText("x")
    else:
      self.bn6.setText("0")
    self.n += 1
    self.check()


  def bn7l(self):
    if self.n % 2 == 0:
      self.bn7.setText("x")
    else:
      self.bn7.setText("0")
    self.n += 1
    self.check()


  def bn8l(self):
    if self.n % 2 == 0:
      self.bn8.setText("x")
    else:
      self.bn8.setText("0")
    self.n += 1
    self.check()

  def startt(self):
    self.bn.setText("")
    self.bn1.setText("")
    self.bn2.setText("")
    self.bn3.setText("")
    self.bn4.setText("")
    self.bn5.setText("")
    self.bn6.setText("")
    self.bn7.setText("")
    self.bn8.setText("")


  def new(self):

    self.bn.setText("")
    self.bn1.setText("")
    self.bn2.setText("")
    self.bn3.setText("")
    self.bn4.setText("")
    self.bn5.setText("")
    self.bn6.setText("")
    self.bn7.setText("")
    self.bn8.setText("")

    # self.name1.setText("")
    # self.name2.setText("")

    self.result.setText("")

  def check(self):
    bn = self.bn.text()
    bn1 = self.bn1.text()
    bn2 = self.bn2.text()
    bn3 = self.bn3.text()
    bn4 = self.bn4.text()
    bn5 = self.bn5.text()
    bn6 = self.bn6.text()
    bn7 = self.bn7.text()
    bn8 = self.bn8.text()

    z1 = int(self.sch1.text())
    z2 = int(self.sch2.text())
    k = self.name2.text()
    k1 = self.name1.text()


    if k == "" or k1 == "":
      msg = QMessageBox()
      msg.setIcon(QMessageBox.Critical)
      msg.setText("Error")
      msg.setInformativeText('Nickname kiritmadingiz')
      msg.setWindowTitle("Error")
      msg.exec_()

    if bn == bn1 == bn2 == "x" or bn == bn1 == bn2 == "0":
      if self.n % 2 == 0:
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {k}")
        self.sch1.setText(str(z1+1))
      else:
        if z2+1 == 3:
          self.result.setText(f"birinchi {k1}")
        self.sch2.setText(str(z2+1))
      self.n = 0

    if bn3 == bn4 == bn5 == "x" or bn3 == bn4 == bn5 == "0":
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0
    if bn7 == bn8 == bn6 == "x" or bn7 == bn8 == bn6 == "0":
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0

    if bn == bn6 == bn3 == "x" or bn == bn6 == bn3 == "0" :
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0

    if bn1 == bn4 == bn7 == "x" or bn1 == bn4 == bn7 == "0" :
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0

    if bn2 == bn5 == bn8 == 'x' or bn2 == bn5 == bn8 == '0':
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0

    if bn == bn4 == bn8 == 'x' or bn == bn4 == bn8 == '0' :
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0

    if bn2 == bn4 == bn6 == 'x' or bn2 == bn4 == bn6 == '0' :
      if self.n % 2 == 0:
        self.sch1.setText(str(z1+1))
        if z1+1 == 3:
          self.result.setText(f"ikkinchi {self.name2}")
      else:
        self.sch2.setText(str(z2+1))
        if z2+1 == 3:
          self.result.setText(f"birinchi {self.name1}")
      self.n = 0


  def komp(self):

    bn = self.bn.text()
    bn1 = self.bn1.text()
    bn2 = self.bn2.text()
    bn3 = self.bn3.text()
    bn4 = self.bn4.text()
    bn5 = self.bn5.text()
    bn6 = self.bn6.text()
    bn7 = self.bn7.text()
    bn8 = self.bn8.text()

    if bn == bn1 == "x" and bn2 == "":
      self.bn2.setText("0")
    if bn == bn2 == "x" and bn1 == "":
      self.bn1.setText("0")
    if bn2 == bn1 == "x" and bn == "":
      self.bn.setText("0")

    if bn3 == bn5 == "x" and bn4 == "":
      self.bn4.setText("0")
    if bn4 == bn5 == "x" and bn3 == "":
      self.bn3.setText("0")
    if bn3 == bn4 == "x" and bn5 == "":
      self.bn5.setText("0")

    if bn6 == bn8 == "x" and bn7 == "":
      self.bn7.setText("0")
    if bn7 == bn8 == "x" and bn6 == "":
      self.bn6.setText("0")
    if bn == bn3 == "x" and bn6 == "":
      self.bn6.setText("0")

    if bn == bn6 == "x" and bn3 == "":
      self.bn3.setText("0")
    if bn1 == bn4 == "x" and bn7 == "":
      self.bn7.setText("0")
    if bn7 == bn4 == "x" and bn1 == "":
      self.bn1.setText("0")
    if bn2 == bn5 == "x" and bn8 == "":
      self.bn8.setText("0")
    if bn2 == bn8 == "x" and bn5 == "":
      self.bn5.setText("0")
    if bn5 == bn8 == "x" and bn2 == "":
      self.bn2.setText("0")

    if bn == bn4 == "x" and bn8 == "":
      self.bn8.setText("0")
    if bn == bn8 == "x" and bn4 == "":
      self.bn4.setText("0")
    if bn4 == bn8 == "x" and bn == "":
      self.bn.setText("0")
    if bn4 == bn2 == "x" and bn6 == "":
      self.bn6.setText("0")
    if bn4 == bn6 == "x" and bn2 == "":
      self.bn2.setText("0")

    elif bn == "":
      self.bn.setText("0")
    elif bn1 == "":
      self.bn1.setText("0")
    elif bn2 == "":
      self.bn2.setText("0")
    elif bn3 == "":
      self.bn3.setText("0")
    elif bn4 == "":
      self.bn4.setText("0")
    elif bn5 == "":
      self.bn5.setText("0")
    elif bn6 == "":
      self.bn6.setText("0")
    elif bn7 == "":
      self.bn7.setText("0")
    elif bn8 == "":
      self.bn8.setText("0")

if __name__ == "__main__":
  app = QApplication([])
  oyna = xvay()
  oyna.show()
  sys.exit(app.exec_())