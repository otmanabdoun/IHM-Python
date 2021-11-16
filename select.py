
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 02:45:11 2021

@author: User
"""

import sqlite3

connexion = sqlite3.connect("dbM2IQL.db")
curseur = connexion.cursor()  


print("\n M2 - Liste des étudiants : MQL et M2I - \n")
curseur.execute("SELECT * FROM Etudiant")
resultats = curseur.fetchall()
for resultat in resultats:
    print(resultat)
    
if curseur.arraysize == 1 :
    print("\nREQUETTE OK  ++++ ")
else:
    print("\nREQUETTE KO  ---- ")
    
print(connexion.total_changes) 