 
#import sys, os.path
#from PySide import QtCore, QtGui, QtSql

import sys
from PySide import QtCore, QtGui, QtSql
  
h = 300
l = 400
 
class Frame(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.resize(l,h)
        self.setFont(QtGui.QFont("Verdana"))
        self.setWindowTitle("Bases de données")
 
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('Master') 
        self.db.open() 
        
        query = QtSql.QSqlQuery()
        query.exec_('''create table Etudiant (id INTEGER PRIMARY KEY,nom TEXT, master TEXT)''') 
        self.db.commit() 
        self.db.close() 
 
app = QtGui.QApplication(sys.argv)
frame = Frame()
frame.show()
sys.exit(app.exec_())