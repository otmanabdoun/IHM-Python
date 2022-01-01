
import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
fen = QWidget()
fen.setWindowTitle("M2I&MQT PyQt Test")
fen.resize(300,200)
fen.move(300,50)
lineEdit = QtWidgets.QLineEdit(fen)
lineEdit.setGeometry(QtCore.QRect(100, 60, 111, 21))
lineEdit.setObjectName("lineEdit")
label = QtWidgets.QLabel(fen)
label.setGeometry(QtCore.QRect(20, 60, 91, 21))
label.setText("PyQt5, OK?")
pushButton = QtWidgets.QPushButton(fen)
pushButton.setGeometry(QtCore.QRect(110, 130, 75, 23))
pushButton.setText("Valider")
fen.show()
app.exec_()