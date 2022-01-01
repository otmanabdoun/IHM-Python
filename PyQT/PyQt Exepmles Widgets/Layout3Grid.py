from PyQt6.QtWidgets import QApplication, QWidget, \
    QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 QGridLayout - M2I & MQL")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)

        grid = QGridLayout()

        btn1 = QPushButton("Click 1")
        btn2 = QPushButton("Click 2")
        btn3 = QPushButton("Click 3")
        btn4 = QPushButton("Click 4")
        btn5 = QPushButton("Click 5")
        btn6 = QPushButton("Click 6")
        btn7 = QPushButton("Click 7")
        btn8 = QPushButton("Click 8")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())