import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import random
os.system("cls")

# ESLATMA: Birinchi navbatda qilinadigan ishlar ketma ketligi pastda ko'rsatilgan!

# 1) Player 1 va Player 2 ga nom bering;
# 2) Har safar yangi o'yin boshlashdan avval new gameni bosib va albatta keyin start gameni bosing!
# 3) O'ynashda e'tiborli bo'ling;

class Tac_Toe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1250, 608)
        self.setMinimumSize(1250, 608)
        self.setFont(QFont("Times New Roman", 20))
        self.setStyleSheet("""
                background-color:rgb(255,255,255);
                """)
        self.setWindowTitle("Tac-Toe Game")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.player1_score = 0
        self.player2_score = 0

        self.lb1 = QLabel(self)
        self.lb1.setGeometry(0, 0, 608, 608)
        self.lb1.setStyleSheet("background-color: rgb(255,164,248);")

        self.lb2 = QLabel("Player 1: ", self)
        self.lb2.setGeometry(650, 40, 100, 30)
        self.lb2.setFont(QFont("Times New Roman", 20))

        self.lb3 = QLabel("Player 2: ", self)
        self.lb3.setGeometry(650, 100, 100, 30)
        self.lb3.setFont(QFont("Times New Roman", 20))

        self.ln1 = QLineEdit(self)
        self.ln1.setGeometry(770, 40, 300, 40)
        self.ln1.setFont(QFont("Times New Roman", 20))

        self.ln2 = QLineEdit(self)
        self.ln2.setGeometry(770, 100, 300, 40)
        self.ln2.setFont(QFont("Times New Roman", 20))

        self.lb4 = QLabel("0", self)
        self.lb4.setGeometry(1100, 40, 40, 40)
        self.lb4.setFont(QFont("Times New Roman", 22))
        self.lb4.setStyleSheet("""
                color: rgb(255,255,0);
                background-color:rgb(120,52,0);
                border-color:rgb(255,255,0);
                border-radius: 10px;
                border-width: 3px;
                border-style: solid;
                """)
        self.lb4.setAlignment(Qt.AlignCenter)

        self.lb5 = QLabel("0", self)
        self.lb5.setGeometry(1100, 100, 40, 40)
        self.lb5.setFont(QFont("Times New Roman", 22))
        self.lb5.setStyleSheet("""
                color: rgb(255,255,0);
                background-color:rgb(120,52,0);
                border-color:rgb(255,255,0);
                border-radius: 10px;
                border-width: 3px;
                border-style: solid;
                """)
        self.lb5.setAlignment(Qt.AlignCenter)

        self.lb6 = QLabel("O'yin tugadi! G'olib: {player1 or player2}", self)
        self.lb6.setGeometry(660, 500, 500, 40)
        self.lb6.setFont(QFont("Times New Roman", 22))
        self.lb6.setStyleSheet("""
                color: rgb(0,0,0);
                """)
        self.lb6.setAlignment(Qt.AlignCenter)

        self.btn11 = QPushButton("New Game", self)
        self.btn11.setStyleSheet("""
                color: rgb(255,255,0);
                background-color:rgb(0,0,255);
                border-color:rgb(0,234,255);
                border-radius: 20px;
                border-width: 5px;
                border-style: solid;
                text-align: center;
                """)
        self.btn11.setFont(QFont("Times New Roman", 26))
        self.btn11.setGeometry(750, 300, 300, 80)
        self.btn11.clicked.connect(self.new_game)

        self.btn10 = QPushButton("Start Game", self)
        self.btn10.setStyleSheet("""
                color: rgb(255,255,0);
                background-color:rgb(0,0,255);
                border-color:rgb(0,234,255);
                border-radius: 20px;
                border-width: 5px;
                border-style: solid;
                text-align: center;
                """)
        self.btn10.setFont(QFont("Times New Roman", 26))
        self.btn10.setGeometry(750, 200, 300, 80)
        self.btn10.clicked.connect(self.start_game)

        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton("", self)
                button.setFont(QFont("Times New Roman", 60))
                button.setGeometry(j * 204,i * 204, 200, 200)
                button.setStyleSheet("""
                        color: rgb(0,0,0);
                        background-color:rgb(79,3,73);
                        """)
                button.clicked.connect(lambda _, row=i, col=j: self.play(row, col))
                self.buttons.append(button)

    def new_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.update_board()
        self.lb6.setText("")

    def start_game(self):
        player1 = self.ln1.text()
        player2 = self.ln2.text()
        self.lb4.setText("0")
        self.lb5.setText("0")
        self.player1_score = 0
        self.player2_score = 0
        self.lb6.setText("")
        self.new_game()

    def update_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i * 3 + j].setText(self.board[i][j])

    def play(self, row, col):
        if len(self.ln1.text()) == 0 or len(self.ln2.text()) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Xatolik yuz berdi!")
            msg.setInformativeText('Avval isimni kiriting!')
            msg.setWindowTitle("Xatolik")
            msg.exec_()
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.update_board()
            if self.check_winner(self.current_player):
                if self.current_player == 'X':
                    self.player1_score += 1
                    self.lb4.setText(str(self.player1_score))
                    self.lb6.setText("O'yin tugadi! G'olib: " + self.ln1.text())
                else:
                    self.player2_score += 1
                    self.lb5.setText(str(self.player2_score))
                    self.lb6.setText("O'yin tugadi! G'olib: " + self.ln2.text())
                self.board = [[' ' for _ in range(3)] for _ in range(3)]
                self.update_board()
            elif self.is_board_full():
                self.lb6.setText("O'yin tugadi! DURANG!")
                self.board = [[' ' for _ in range(3)] for _ in range(3)]
                self.update_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Tac_Toe()
    window.show()
    sys.exit(app.exec_())