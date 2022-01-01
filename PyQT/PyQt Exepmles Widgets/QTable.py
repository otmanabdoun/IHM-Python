from PyQt6.QtWidgets import QApplication, \
    QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 TableWidget - M2I & MQL")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)

        vbox = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        tableWidget.setStyleSheet('background-color:white')
        tableWidget.setFont(QFont("Times New Roman", 12))
        tableWidget.setItem(0, 0, QTableWidgetItem("Prénom"))
        tableWidget.setItem(0, 1, QTableWidgetItem("Nom"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

        tableWidget.setItem(1, 0, QTableWidgetItem("Ahmed"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Bakkali"))
        tableWidget.setItem(1, 2, QTableWidgetItem("abakkali@gmail.com"))

        tableWidget.setItem(2, 0, QTableWidgetItem("Samira"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Diani"))
        tableWidget.setItem(2, 2, QTableWidgetItem("salmad@gmail.com"))

        vbox.addWidget(tableWidget)

        self.setLayout(vbox)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())