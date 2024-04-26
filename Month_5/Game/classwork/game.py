import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random
os.system("cls")

class game(QMainWindow):
    __popitka = 0
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(""))
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        self.setWindowTitle("Game")
        
        self.area = QLabel(self)
        self.area.setGeometry(78,78,400,400)
        self.area.setStyleSheet("background-color: cyan;")
        
        self.btn1 = self.button_generate("1",80,80)
        self.btn1.clicked.connect(self.btn1_click)
        
        self.btn2 = self.button_generate("2",180,80)
        self.btn2.clicked.connect(self.btn2_click)
        
        self.btn3 = self.button_generate("3",280,80)
        self.btn3.clicked.connect(self.btn3_click)
        
        self.btn4 = self.button_generate("4",380,80)
        self.btn4.clicked.connect(self.btn4_click)
        
        self.btn5 = self.button_generate("5",80,180)
        self.btn5.clicked.connect(self.btn5_click)
        
        self.btn6 = self.button_generate("6",180,180)
        self.btn6.clicked.connect(self.btn6_click)
        
        self.btn7 = self.button_generate("7",280,180)
        self.btn7.clicked.connect(self.btn7_click)
        
        self.btn8 = self.button_generate("8",380,180)
        self.btn8.clicked.connect(self.btn8_click)
        
        self.btn9 = self.button_generate("9",80,280)
        self.btn9.clicked.connect(self.btn9_click)
        
        self.btn10 = self.button_generate("10",180,280)
        self.btn10.clicked.connect(self.btn10_click)
        
        self.btn11 = self.button_generate("11",280,280)
        self.btn11.clicked.connect(self.btn11_click)
        
        self.btn12 = self.button_generate("12",380,280)
        self.btn12.clicked.connect(self.btn12_click)
        
        self.btn13 = self.button_generate("13",80,380)
        self.btn13.clicked.connect(self.btn13_click)
        
        self.btn14 = self.button_generate("14",180,380)
        self.btn14.clicked.connect(self.btn14_click)
        
        self.btn15 = self.button_generate("15",280,380)
        self.btn15.clicked.connect(self.btn15_click)
        
        self.btn16 = self.button_generate("",380,380)
        self.btn16.clicked.connect(self.btn16_click)
        self.ls = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,
                   self.btn6,self.btn7,self.btn8,self.btn9,self.btn10,
                   self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,]
        self.set_Number()
        
    def set_Number(self):
        ls = []
        while len(ls) < 15:
            num = random.randint(1,15)
            if ls.count(num) == 0:
                ls.append(num)
        for x,y in zip(self.ls,ls):
            x.setText(str(y))
        
    def button_generate(self,raqam,x,y):
        btn1 = QPushButton(f"{raqam}",self)
        btn1.setGeometry(x,y,100,100)
        btn1.setFont(QFont("Consolas",48))
        btn1.setStyleSheet("""
            color: rgb(0,255,0);
            background-color: rgb(0,0,0);
            border-color: rgb(0,255,0);
            border-width: 3px;
            border-style: solid;
            """)
        return  btn1

    def btn1_click(self):
        game.__popitka += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn1.text())
            self.btn1.setText("")
        elif self.btn5.text() == "":
            self.btn5.setText(self.btn1.text())
            self.btn1.setText("")
        else:
            game.__popitka -=1 
    def btn2_click(self):
        game.__popitka += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn2.text())
            self.btn2.setText("")
        elif self.btn3.text() == "":
            self.btn3.setText(self.btn2.text())
            self.btn2.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn2.text())
            self.btn2.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn3_click(self):
        game.__popitka += 1
        if self.btn2.text() == "":
            self.btn2.setText(self.btn3.text())
            self.btn3.setText("")
        elif self.btn4.text() == "":
            self.btn4.setText(self.btn3.text())
            self.btn3.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn3.text())
            self.btn3.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn4_click(self):
        game.__popitka += 1
        if self.btn3.text() == "":
            self.btn3.setText(self.btn4.text())
            self.btn4.setText("")
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn4.text())
            self.btn4.setText("")
        else:
            game.__popitka -=1 
    def btn5_click(self):
        game.__popitka += 1
        if self.btn1.text() == "":
            self.btn1.setText(self.btn5.text())
            self.btn5.setText("")
        elif self.btn9.text() == "":
            self.btn9.setText(self.btn5.text())
            self.btn5.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn5.text())
            self.btn5.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn6_click(self):
        game.__popitka += 1
        if self.btn5.text() == "":
            self.btn5.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn2.text() == "":
            self.btn2.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn6.text())
            self.btn6.setText("")
        elif self.btn10.text() == "":
            self.btn10.setText(self.btn6.text())
            self.btn6.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn7_click(self):
        game.__popitka += 1
        if self.btn3.text() == "":
            self.btn3.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn7.text())
            self.btn7.setText("")
        elif self.btn11.text() == "":
            self.btn11.setText(self.btn7.text())
            self.btn7.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn8_click(self):
        game.__popitka += 1
        if self.btn4.text() == "":
            self.btn4.setText(self.btn8.text())
            self.btn8.setText("")
        elif self.btn12.text() == "":
            self.btn12.setText(self.btn8.text())
            self.btn8.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn8.text())
            self.btn8.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn9_click(self):
        game.__popitka += 1
        if self.btn5.text() == "":
            self.btn5.setText(self.btn9.text())
            self.btn9.setText("")
        elif self.btn13.text() == "":
            self.btn13.setText(self.btn9.text())
            self.btn9.setText("")
        elif self.btn10.text() == "":
            self.btn10.setText(self.btn9.text())
            self.btn9.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn10_click(self):
        game.__popitka += 1
        if self.btn9.text() == "":
            self.btn9.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn11.text() == "":
            self.btn11.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn6.text() == "":
            self.btn6.setText(self.btn10.text())
            self.btn10.setText("")
        elif self.btn14.text() == "":
            self.btn14.setText(self.btn10.text())
            self.btn10.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn11_click(self):
        game.__popitka += 1
        if self.btn10.text() == "":
            self.btn10.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn12.text() == "":
            self.btn12.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn7.text() == "":
            self.btn7.setText(self.btn11.text())
            self.btn11.setText("")
        elif self.btn15.text() == "":
            self.btn15.setText(self.btn11.text())
            self.btn11.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn12_click(self):
        game.__popitka += 1
        if self.btn11.text() == "":
            self.btn11.setText(self.btn12.text())
            self.btn12.setText("")
        elif self.btn16.text() == "":
            self.btn16.setText(self.btn12.text())
            self.btn12.setText("")
        elif self.btn8.text() == "":
            self.btn8.setText(self.btn12.text())
            self.btn12.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn13_click(self):
        game.__popitka += 1
        if self.btn9.text() == "":
            self.btn9.setText(self.btn13.text())
            self.btn13.setText("")
        elif self.btn14.text() == "":
            self.btn14.setText(self.btn13.text())
            self.btn13.setText("")
        else:
            game.__popitka -=1 
    def btn14_click(self):
        game.__popitka += 1
        if self.btn13.text() == "":
            self.btn13.setText(self.btn14.text())
            self.btn14.setText("")
        elif self.btn15.text() == "":
            self.btn15.setText(self.btn14.text())
            self.btn14.setText("")
        elif self.btn10.text() == "":
            self.btn10.setText(self.btn14.text())
            self.btn14.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn15_click(self):
        game.__popitka += 1
        if self.btn14.text() == "":
            self.btn14.setText(self.btn15.text())
            self.btn15.setText("")
        elif self.btn11.text() == "":
            self.btn11.setText(self.btn15.text())
            self.btn15.setText("")
        elif self.btn16.text() == "":
            self.btn16.setText(self.btn15.text())
            self.btn15.setText("")
        else:
            # msg = QMessageBox(self)
            # msg.setText("X A T O")
            # msg.setIcon(QMessageBox.Critical)
            # msg.show()
            # msg.exec()
            game.__popitka -=1 
    def btn16_click(self):
        game.__popitka += 1
        if self.btn15.text() == "":
            self.btn15.setText(self.btn16.text())
            self.btn16.setText("")
        elif self.btn12.text() == "":
            self.btn12.setText(self.btn16.text())
            self.btn16.setText("")
        else:
            game.__popitka -=1 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyin = game()
    uyin.show()
    sys.exit(app.exec_())
        