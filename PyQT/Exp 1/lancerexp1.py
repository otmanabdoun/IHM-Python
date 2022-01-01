import sys
from PyQt5 import QtWidgets, uic

def Fermer():
    Fen.close()
    
App = QtWidgets.QApplication(sys.argv)
Fen=uic.loadUi("interface.ui")
Fen.show()
Fen.Fe.clicked.connect(Fermer)
App.exec_()
sys.exit()
