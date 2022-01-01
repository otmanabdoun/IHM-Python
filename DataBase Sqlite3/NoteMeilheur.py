# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 04:38:07 2021

@author: User
"""
import sqlite3
connexion = sqlite3.connect("dbM2IQL.db") 
curseur = connexion.cursor()

curseur.execute("""SELECT e.Nom, c.note FROM Etudiant as e INNER JOIN
    CF as c ON e.id = c.fk_etudiant
    ORDER BY c.note DESC LIMIT 1""")
print(curseur.fetchone()) 