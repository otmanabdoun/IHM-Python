# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:42:31 2021

@author: User
"""

import sys

from PyQt5.QtSql import *
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, \
    QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout, QLineEdit, QLabel, QGridLayout


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(['ID', 'NOM', 'PRENOM'])
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        self.lblID = QLabel("ID:")
        self.txtID = QLineEdit()
        self.txtID.setPlaceholderText("Numero identifiant Unique")

        self.lblName = QLabel("Nom:")
        self.txtName = QLineEdit()
        self.txtName.setPlaceholderText("Nom de la personne")

        self.lblApellido = QLabel("Prenom:")
        self.txtApellido = QLineEdit()
        self.txtApellido.setPlaceholderText("Prénom de la personne")

        grid = QGridLayout()
        grid.addWidget(self.lblID, 0, 0)
        grid.addWidget(self.txtID, 0, 1)
        grid.addWidget(self.lblName, 1, 0)
        grid.addWidget(self.txtName, 1, 1)
        grid.addWidget(self.lblApellido, 2, 0)
        grid.addWidget(self.txtApellido, 2, 1)

        btnCargar = QPushButton('Charger les données')
        btnCargar.clicked.connect(self.chargeretudiant)

        btnInsertar = QPushButton('Insérer')
        btnInsertar.clicked.connect(self.inseretudiant)

        btnEliminar = QPushButton('Supprimer')
        btnEliminar.clicked.connect(self.supetudiant)

        hbx = QHBoxLayout()
        hbx.addWidget(btnCargar)
        hbx.addWidget(btnInsertar)
        hbx.addWidget(btnEliminar)

        vbx = QVBoxLayout()
        vbx.addLayout(grid)
        vbx.addLayout(hbx)
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(self.table)

        self.setWindowTitle("PyQT :: Liste Etudiants M2I & MQL")
        self.resize(362, 320)
        self.setLayout(vbx)

    def chargeretudiant(self, event):
        index = 0
        query = QSqlQuery()
        query.exec_("select * from person")

        while query.next():
            ids = query.value(0)
            nombre = query.value(1)
            apellido = query.value(2)

            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.table.setItem(index, 1, QTableWidgetItem(nombre))
            self.table.setItem(index, 2, QTableWidgetItem(apellido))

            index += 1

    def inseretudiant(self, event):
        ids = int(self.txtID.text())
        nombre = self.txtName.text()
        apellido = self.txtApellido.text()

        query = QSqlQuery()
        query.exec_("insert into person values({0}, '{1}', '{2}')".format(ids, nombre, apellido))

    def supetudiant(self, event):
        selected = self.table.currentIndex()
        if not selected.isValid() or len(self.table.selectedItems()) < 1:
            return

        ids = self.table.selectedItems()[0]
        query = QSqlQuery()
        query.exec_("delete from person where id = " + ids.text())

        self.table.removeRow(selected.row())
        self.table.setCurrentIndex(QModelIndex())

    def db_connect(self, filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                    "Unable to establish a database connection.\n"
                    "This example needs SQLite support. Please read the Qt SQL "
                    "driver documentation for information how to build it.\n\n"
                    "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True

    def db_create(self):
        query = QSqlQuery()
        query.exec_("create table person(id int primary key, "
                    "firstname varchar(20), lastname varchar(20))")
        query.exec_("insert into person values(101, 'Abdouraouf', 'Youssouf')")
        query.exec_("insert into person values(102, 'Ahajtan', 'Kamar')")
        query.exec_("insert into person values(103, 'Akdi', 'Moaad')")
        query.exec_("insert into person values(104, 'Diamoye', 'Boubacar')")
        query.exec_("insert into person values(105, 'Laktit', 'Haitam')")

    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ejm = Example()
    ejm.init('datafile', 'QSQLITE')
    ejm.show()
    sys.exit(app.exec_())