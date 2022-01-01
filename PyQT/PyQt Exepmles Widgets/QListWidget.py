from PyQt6.QtWidgets import QApplication, QWidget,QLabel ,\
    QVBoxLayout,QListWidget
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 ListWidget - M2I & MQL ")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)

        
        vbox = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, "PyQt6")
        self.list_widget.insertItem(1, "wxPython")
        self.list_widget.insertItem(2, "Kivy")
        self.list_widget.insertItem(3, "TKinter")
        self.list_widget.insertItem(4, "Pyside2")
        self.list_widget.setStyleSheet('background-color:White')
        self.list_widget.clicked.connect(self.item_clicked)
        self.label = QLabel("")
        self.setFont(QFont("Sanserif", 13))
        self.setStyleSheet('color:brown')

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_clicked(self):
        item = self.list_widget.currentItem()
        self.label.setText("Vous preférez : " + str(item.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())