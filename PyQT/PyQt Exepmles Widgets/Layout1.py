from PyQt6.QtWidgets import QApplication, QWidget, \
    QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 QVBoxLayout - M2I & MQL")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)

        vbox = QVBoxLayout()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())