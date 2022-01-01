from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,\
    QHBoxLayout,QRadioButton,QGroupBox , QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 QRadioButton - M2I & MQL")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)
        self.radio_btn()
        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)

        self.label = QLabel("Bonjour <->")
        self.label.setFont(QFont("Times New Roman", 14))

        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def radio_btn(self):
        self.grpbox = QGroupBox("Choisir votre Langage de Programmation : ")
        self.grpbox.setFont(QFont("Times New Roman", 15))

        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Python")
        self.rad1.setChecked(True)
        self.rad1.setFont(QFont("Times New Roman", 14))
        self.rad1.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad1)

        self.rad2 = QRadioButton("Java")
        self.rad2.setFont(QFont("Times New Roman", 14))
        self.rad2.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad2)

        self.rad3 = QRadioButton("C++")
        self.rad3.setFont(QFont("Times New Roman", 14))
        self.rad3.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad3)

        self.rad4 = QRadioButton("C#")
        self.rad4.setFont(QFont("Times New Roman", 14))
        self.rad4.toggled.connect(self.on_selected)
        hbox.addWidget(self.rad4)


        self.grpbox.setLayout(hbox)

    def on_selected(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            self.label.setText("Vous optez pour le langage : " + radio_button.text())




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())