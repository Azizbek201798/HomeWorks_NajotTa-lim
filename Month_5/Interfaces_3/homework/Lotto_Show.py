import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
os.system("clear")

class lotto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1100,700)
        self.setMinimumSize(1100,700)
        self.setWindowTitle("Lotto Show")
        self.setStyleSheet("""
            background-color: rgb(255,229,204);
            color:rgb(0,0,0);
            """)

        self.rb1 = QRadioButton("Omad (36/5)",self)
        self.rb1.setFont(QFont("Times New Roman",12))
        self.rb1.setGeometry(50,30,130,50)
        self.rb1.setStyleSheet("color:rgb(0,0,0)")

        self.rb2 = QRadioButton("Sharqona (36/5)",self)
        self.rb2.setFont(QFont("Times New Roman",12))
        self.rb2.setGeometry(190,30,150,50)
        self.rb2.setStyleSheet("color:rgb(0,0,0)")

        self.rb3 = QRadioButton("Super (36/7)",self)
        self.rb3.setFont(QFont("Times New Roman",12))
        self.rb3.setGeometry(350,30,150,50)
        self.rb3.setStyleSheet("color:rgb(0,0,0)")

        self.ln1 =QLineEdit(self)
        self.ln1.setGeometry(50,100,340,50)
        self.ln1.setFont(QFont("Times New Roman",14))
        self.ln1.setStyleSheet("""
            background-color:rgb(255,255,255);
            border-color: rgb(0,0,255);
            border-width: 3px; 
            border-radius: 12;
            border-style: solid;
            """)
        
        self.bt1 =QPushButton("+",self)
        self.bt1.setGeometry(415,100,70,50)
        self.bt1.setFont(QFont("Times New Roman",30))
        self.bt1.setStyleSheet("""
            background-color:rgb(192,192,192);
            border-color: rgb(255,0,0);
            border-width: 3px; 
            border-radius: 12;
            border-style: solid;
            """)

        self.bt2 = QPushButton("Start",self)
        self.bt2.setGeometry(510,40,80,40)
        self.bt2.setFont(QFont("Times New Roman",14))
        self.bt2.setStyleSheet("""
            background-color:rgb(192,192,192);
            border-color: rgb(0,204,0);
            border-width: 3px; 
            border-radius: 12;
            border-style: solid;
            """)

        self.ln_a = QLabel(self)
        self.ln_a.setGeometry(510,100,560,540)
        self.ln_a.setFont(QFont("Times New Roman",14))
        self.ln_a.setStyleSheet("""
            background-color:rgb(255,255,255);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)
        
        self.lb1 = QLabel(self)
        self.lb1.setGeometry(600,40,40,40)
        self.lb1.setFont(QFont("Times New Roman",14))
        self.lb1.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)
        
        self.lb2 = QLabel(self)
        self.lb2.setGeometry(670,40,40,40)
        self.lb2.setFont(QFont("Times New Roman",14))
        self.lb2.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.lb3 = QLabel(self)
        self.lb3.setGeometry(740,40,40,40)
        self.lb3.setFont(QFont("Times New Roman",14))
        self.lb3.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.lb4 = QLabel(self)
        self.lb4.setGeometry(810,40,40,40)
        self.lb4.setFont(QFont("Times New Roman",14))
        self.lb4.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.lb5 = QLabel(self)
        self.lb5.setGeometry(880,40,40,40)
        self.lb5.setFont(QFont("Times New Roman",14))
        self.lb5.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.lb6 = QLabel(self)
        self.lb6.setGeometry(950,40,40,40)
        self.lb6.setFont(QFont("Times New Roman",14))
        self.lb6.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.lb7 = QLabel(self)
        self.lb7.setGeometry(1020,40,40,40)
        self.lb7.setFont(QFont("Times New Roman",14))
        self.lb7.setStyleSheet("""
            background-color:rgb(255,160,0);
            border-color: rgb(0,0,0);
            border-width: 3px; 
            border-radius: 20;
            border-style: solid;
            """)

        self.btn8 = QPushButton("Telegram",self)
        self.btn8.setGeometry(50,640,200,36)
        self.btn8.setFont(QFont("Times New Roman",14))
        self.btn8.setStyleSheet("""
            background-color:rgb(100,160,255);
            border-color: rgb(0,0,255);
            border-width: 2px; 
            border-radius: 18;
            border-style: solid;
            """)
        
        self.btn9 = QPushButton("You Tube",self)
        self.btn9.setGeometry(270,640,200,36)
        self.btn9.setFont(QFont("Times New Roman",14))
        self.btn9.setStyleSheet("""
            background-color:rgb(100,160,255);
            border-color: rgb(0,0,255);
            border-width: 2px; 
            border-radius: 18;
            border-style: solid;
            """)
        
        self.num1 = QPushButton("1",self)
        self.num1.setFont(QFont("Times New Roman",24))
        self.num1.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num1.setGeometry(50,180,60,60)

        self.num2 = QPushButton("2",self)
        self.num2.setFont(QFont("Times New Roman",24))
        self.num2.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num2.setGeometry(125,180,60,60)

        self.num3 = QPushButton("3",self)
        self.num3.setFont(QFont("Times New Roman",24))
        self.num3.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num3.setGeometry(200,180,60,60)

        self.num4 = QPushButton("4",self)
        self.num4.setFont(QFont("Times New Roman",24))
        self.num4.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num4.setGeometry(275,180,60,60)

        self.num5 = QPushButton("5",self)
        self.num5.setFont(QFont("Times New Roman",24))
        self.num5.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num5.setGeometry(350,180,60,60)

        self.num6 = QPushButton("6",self)
        self.num6.setFont(QFont("Times New Roman",24))
        self.num6.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num6.setGeometry(425,180,60,60)

        self.num7 = QPushButton("7",self)
        self.num7.setFont(QFont("Times New Roman",24))
        self.num7.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num7.setGeometry(50,255,60,60)

        self.num8 = QPushButton("8",self)
        self.num8.setFont(QFont("Times New Roman",24))
        self.num8.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num8.setGeometry(125,255,60,60)

        self.num9 = QPushButton("9",self)
        self.num9.setFont(QFont("Times New Roman",24))
        self.num9.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num9.setGeometry(200,255,60,60)

        self.num10 = QPushButton("10",self)
        self.num10.setFont(QFont("Times New Roman",24))
        self.num10.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num10.setGeometry(275,255,60,60)

        self.num11 = QPushButton("11",self)
        self.num11.setFont(QFont("Times New Roman",24))
        self.num11.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num11.setGeometry(350,255,60,60)

        self.num12 = QPushButton("12",self)
        self.num12.setFont(QFont("Times New Roman",24))
        self.num12.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num12.setGeometry(425,255,60,60)

        self.num13 = QPushButton("13",self)
        self.num13.setFont(QFont("Times New Roman",24))
        self.num13.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num13.setGeometry(50,330,60,60)

        self.num14 = QPushButton("14",self)
        self.num14.setFont(QFont("Times New Roman",24))
        self.num14.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num14.setGeometry(125,330,60,60)

        self.num15 = QPushButton("15",self)
        self.num15.setFont(QFont("Times New Roman",24))
        self.num15.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num15.setGeometry(200,330,60,60)

        self.num16 = QPushButton("16",self)
        self.num16.setFont(QFont("Times New Roman",24))
        self.num16.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num16.setGeometry(275,330,60,60)

        self.num17 = QPushButton("17",self)
        self.num17.setFont(QFont("Times New Roman",24))
        self.num17.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num17.setGeometry(350,330,60,60)

        self.num18 = QPushButton("18",self)
        self.num18.setFont(QFont("Times New Roman",24))
        self.num18.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num18.setGeometry(425,330,60,60)


        self.num19 = QPushButton("19",self)
        self.num19.setFont(QFont("Times New Roman",24))
        self.num19.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num19.setGeometry(50,405,60,60)

        self.num20 = QPushButton("20",self)
        self.num20.setFont(QFont("Times New Roman",24))
        self.num20.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num20.setGeometry(125,405,60,60)

        self.num21 = QPushButton("21",self)
        self.num21.setFont(QFont("Times New Roman",24))
        self.num21.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num21.setGeometry(200,405,60,60)

        self.num22 = QPushButton("22",self)
        self.num22.setFont(QFont("Times New Roman",24))
        self.num22.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num22.setGeometry(275,405,60,60)

        self.num23 = QPushButton("23",self)
        self.num23.setFont(QFont("Times New Roman",24))
        self.num23.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num23.setGeometry(350,405,60,60)

        self.num24 = QPushButton("24",self)
        self.num24.setFont(QFont("Times New Roman",24))
        self.num24.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num24.setGeometry(425,405,60,60)

        self.num25 = QPushButton("25",self)
        self.num25.setFont(QFont("Times New Roman",24))
        self.num25.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num25.setGeometry(50,480,60,60)

        self.num26 = QPushButton("26",self)
        self.num26.setFont(QFont("Times New Roman",24))
        self.num26.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num26.setGeometry(125,480,60,60)

        self.num27 = QPushButton("27",self)
        self.num27.setFont(QFont("Times New Roman",24))
        self.num27.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num27.setGeometry(200,480,60,60)

        self.num28 = QPushButton("28",self)
        self.num28.setFont(QFont("Times New Roman",24))
        self.num28.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num28.setGeometry(275,480,60,60)

        self.num29 = QPushButton("29",self)
        self.num29.setFont(QFont("Times New Roman",24))
        self.num29.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num29.setGeometry(350,480,60,60)

        self.num30 = QPushButton("30",self)
        self.num30.setFont(QFont("Times New Roman",24))
        self.num30.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num30.setGeometry(425,480,60,60)

        self.num31 = QPushButton("31",self)
        self.num31.setFont(QFont("Times New Roman",24))
        self.num31.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num31.setGeometry(50,555,60,60)

        self.num32 = QPushButton("32",self)
        self.num32.setFont(QFont("Times New Roman",24))
        self.num32.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num32.setGeometry(125,555,60,60)

        self.num33 = QPushButton("33",self)
        self.num33.setFont(QFont("Times New Roman",24))
        self.num33.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num33.setGeometry(200,555,60,60)

        self.num34 = QPushButton("34",self)
        self.num34.setFont(QFont("Times New Roman",24))
        self.num34.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num34.setGeometry(275,555,60,60)

        self.num35 = QPushButton("35",self)
        self.num35.setFont(QFont("Times New Roman",24))
        self.num35.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num35.setGeometry(350,555,60,60)

        self.num36 = QPushButton("36",self)
        self.num36.setFont(QFont("Times New Roman",24))
        self.num36.setStyleSheet("""background-color:rgb(255,150,200);
                                   border-radius: 30px;
                                   border-color: rgb(102,0,50);
                                   border-width: 3px;
                                   border-style: solid;
                                """)
        self.num36.setGeometry(425,555,60,60)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oyna = lotto()
    oyna.show()
    sys.exit(app.exec_())