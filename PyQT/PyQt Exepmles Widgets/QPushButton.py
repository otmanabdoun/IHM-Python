from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Button - M2I & MQL")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 500,400)
        self.create_widgets()
 
    def create_widgets(self):
        btn = QPushButton("Cliquer Ici ", self)
        #btn.move(100,100)
        btn.setGeometry(100,100, 100,100)
        btn.setStyleSheet('background-color:red')
        btn.setIcon(QIcon("qt.png"))

        
        label = QLabel("Exp Label", self)
        label.move(100,220)
        label.setStyleSheet('color:green')
        label.setFont(QFont("Times New Roman", 15))
  
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
