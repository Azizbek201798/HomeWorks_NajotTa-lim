# """PyQt5 orqali 2ta label, 1ta lineedit va 1ta button yarating.
#  1-labelni nomini ‘Input’. 1-buttonni bosganda 1-lineeditga matematik ifoda yoziladi va sizning
#    vazifangiz ushbu matematik ifodada nechta sonlar ishtirok etganligini va ushbu sonlarni xonalar
#      bo’yicha kamayish tartibida 2-labelda chiqaring.
# """

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

# def calculate_numbers():
#     expression = line_edit.text()
#     numbers = [int(num) for num in expression if num.isdigit()]
#     sorted_numbers = sorted(numbers, reverse=True)
#     label1.setText(f"Number of digits: {len(numbers)}")
#     label2.setText(f"Sorted in descending order: {sorted_numbers}")

# app = QApplication(sys.argv)

# window = QWidget()
# window.setWindowTitle("Number Statistics")

# label1 = QLabel("Input")
# line_edit = QLineEdit()
# button = QPushButton("Calculate")
# label2 = QLabel()

# button.clicked.connect(calculate_numbers)

# layout = QVBoxLayout()
# layout.addWidget(label1)
# layout.addWidget(line_edit)
# layout.addWidget(button)
# layout.addWidget(label2)

# window.setLayout(layout)
# window.show()

# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matematik Ifoda")
        self.setGeometry(100, 100, 300, 150)

        self.input_label = QLabel("Input:")
        self.input_lineedit = QLineEdit()
        self.output_label = QLabel("")

        self.calculate_button = QPushButton("Hisoblash")
        self.calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_lineedit)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    def calculate(self):
        expression = self.input_lineedit.text()
        numbers = [int(x) for x in expression if x.isdigit()]
        count_digits = len(numbers)

        if count_digits == 0:
            self.output_label.setText("Matematik ifoda mavjud emas")
        else:
            self.output_label.setText(f"Matematik ifodada {count_digits} ta son mavjud")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    