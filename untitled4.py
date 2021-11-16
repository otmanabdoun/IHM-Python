# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 02:45:11 2021

@author: User
"""

import sqlite3

connexion = sqlite3.connect("dbM2IQL.db")
curseur = connexion.cursor()  

curseur.execute('''DROP TABLE Etudiant''')

curseur.execute('''CREATE TABLE IF NOT EXISTS Etudiant(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    Nom TEXT,
    Master TEXT
)''')

curseur.execute("""DELETE FROM Etudiant""")

donnees = [("El Fahssi", "MQL"), ("Ktiti Mohamed", "MQL"), ("Amakran Hajar", "M2I")]
#Exécutions multiples
for donnee in donnees:
    curseur.execute('''INSERT INTO Etudiant (Nom, Master) VALUES (?, ?)''', donnee)
connexion.commit()

donnee=("M2I", )
curseur.execute("SELECT * FROM Etudiant WHERE Master = ?", donnee)
result = curseur.fetchone()
while result:
    print(result)
    result = curseur.fetchone()
