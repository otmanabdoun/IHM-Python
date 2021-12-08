from tkinter import *
from tkinter.ttk import *


import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sys
import traceback
from lxml import etree
import sqlite3

def effacer():
    entree0.delete(0, 'end')
    entree1.delete(0, 'end')
    entree2.delete(0, 'end')
    entree3.delete(0, 'end')
 
def addxml():
    users = etree.Element("etudiants")
    user = etree.SubElement(users, "etudiant")
    user.set("data-id", entree0.get())
    nom = etree.SubElement(user, "nom")
    nom.text = entree1.get()
    #nom.text = "rr"
    prenom = etree.SubElement(user, "prenom")
    prenom.text = entree2.get()
    #prenom.text = "ee"
    master = etree.SubElement(user, "master")
    master.text = entree3.get()
    #master.text = "rr"
    print(etree.tostring(users, pretty_print=True))
    tree = etree.ElementTree(users)
    tree.write("Mstdata.xml")
    effacer()
    
    
def addsql():
    connexion = sqlite3.connect("dbGUIMaster.db")
    curseur = connexion.cursor()  
    curseur.execute('''CREATE TABLE IF NOT EXISTS Etudiant(
        id TEXT,
        Nom TEXT,
        Prenom TEXT,
        Master TEXT
    )''')

    donnee = (entree0.get(), entree1.get(), entree2.get(), entree3.get())
    curseur.execute('insert into Etudiant (id,Nom,Prenom,Master)values(?,?,?,?)',  donnee)        
    connexion.commit()
    if curseur.arraysize == 1 :
        tkinter.messagebox.showinfo("Requête bien exécutée ++ ","Etudiant est bien ajouté  ++ ")
    else:
        tkinter.messagebox.showinfo("Requête Erreur d'exécution ++ ","Etudiant n'est pas ajouté  --- ")
    effacer()


def afficher():
    tkkk = Tk()
    tkkk.title(" Liste des étudiants : MQL et M2I")

    tableau = Treeview(tkkk)
    tableau['columns']=("id", "Nom", "Prenom", "Master")
    tableau.column('id', anchor = CENTER, width=100)
    tableau.column('Nom', anchor = W, width=100)
    tableau.column('Prenom', anchor = W, width=100)
    tableau.column('Master', anchor = W, width=100)                
    tableau.heading('id', text='Identifiant')
    tableau.heading('Nom', text='Nom')
    tableau.heading('Prenom', text='Prénom')
    tableau.heading('Master', text='Master')
    tableau['show'] = 'headings'
    
    connexion = sqlite3.connect("dbGUIMaster.db")
    curseur = connexion.cursor()  
    curseur.execute("SELECT * FROM Etudiant")
    resultats = curseur.fetchall()
    ii=0
    for resultat in resultats:
        tableau.insert(parent='',index='end',iid=ii,text="",values=(resultat[0],resultat[1],resultat[2],resultat[3]))
        ii=ii+1
    tableau.grid(row=5,column=1)
    
    
    tkkk.mainloop()

    

tkk = Tk()

tkk.title("M2I & MQL Add Student")
tkk.iconbitmap("logo.ico")
tkk.geometry("700x400")
tkk.config(bg = "White")

menu1 = Menu(tkk)
menu1.add_cascade(label="Fichier")
menu1.add_cascade(label="Options")
menu1.add_cascade(label="Aide")
tkk.config(menu = menu1)


texte0 = Label (tkk, text = "Id : ")
entree0 = Entry (tkk)
texte1 = Label (tkk, text = "Nom : ")
entree1 = Entry (tkk)
texte2 = Label (tkk, text = "Prénom : ")
entree2 = Entry (tkk)
texte3 = Label (tkk, text = "Master : ")
entree3 = ttk.Combobox(tkk,values=["Master M2I","Master MQL"])
print(dict(entree3))

bouton1 = Button (tkk, text = "Add > DB", command=addsql)
bouton2 = Button (tkk, text = "Add > XML", command=addxml )
bouton3 = Button (tkk, text = "Select", command=afficher)
bouton4 = Button (tkk, text = "Clear", command=effacer)


texte0.grid(row=0,column=0)
entree0.grid(row=0,column=1)
texte1.grid(row=1,column=0)
entree1.grid(row=1,column=1)
texte2.grid(row=2,column=0)
entree2.grid(row=2,column=1)
texte3.grid(row=3,column=0)
entree3.grid(row=3,column=1)
bouton1.grid(row=4,column=0)
bouton2.grid(row=4,column=1)
bouton3.grid(row=4,column=2)
bouton4.grid(row=4,column=3)

tkk.mainloop()