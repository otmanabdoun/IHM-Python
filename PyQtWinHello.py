

import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
fen = QWidget()
fen.setWindowTitle("M2I & MQL - Windows Hello")
fen.resize(500,250)
fen.move(300, 200)
fen.show()
app.exec_()