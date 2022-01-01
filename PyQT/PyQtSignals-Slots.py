

from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Vous avez cliqué sur le Boutton!')
    alert.exec()

button.clicked.connect(on_button_clicked)
button.show()
app.exec()

