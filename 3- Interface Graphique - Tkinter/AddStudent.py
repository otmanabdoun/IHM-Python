from tkinter import ttk

from tkinter import *

from lxml import etree

def effacer():
    entree1.delete(0, 'end')
    entree2.delete(0, 'end')
    entree3.delete(0, 'end')
    effacer()

def addxml():
    users = etree.Element("etudiants")
    user = etree.SubElement(users, "etudiant")
    user.set("data-id", entree0.get())
    nom = etree.SubElement(user, "nom")
    nom.text = entree1.get()
    prenom = etree.SubElement(user, "prenom")
    prenom.text = entree2.get()
    metier = etree.SubElement(user, "master")
    metier.text = entree3.get()
    print(etree.tostring(users, pretty_print=True))
    tree = etree.ElementTree(users)
    tree.write("Mstdata.xml")
    effacer()
    
def addsql():
    entree1.delete(0, 'end')
    entree2.delete(0, 'end')
    entree3.delete(0, 'end')


tk = Tk()

tk.title("M2I & MQL Add Student")
tk.iconbitmap("logo.ico")
tk.geometry("300x250")
tk.config(bg = "White")

menu1 = Menu(tk)
menu1.add_cascade(label="Fichier")
menu1.add_cascade(label="Options")
menu1.add_cascade(label="Aide")
tk.config(menu = menu1)


texte0 = Label (tk, text = "Id : ")
entree0 = Entry (tk)
texte1 = Label (tk, text = "Nom : ")
entree1 = Entry (tk)
texte2 = Label (tk, text = "Prénom : ")
entree2 = Entry (tk)
texte3 = Label (tk, text = "Master : ")
entree3 = ttk.Combobox(values=["Master M2I", "Master MQL"])

#cadre1 = Frame(tk)
bouton1 = Button (tk, text = "Add > DB")
bouton2 = Button (tk, text = "Add > XML", )
bouton3 = Button (tk, text = "Clear", command=effacer)


texte0.grid(row=0,column=0)
entree0.grid(row=0,column=1)
texte1.grid(row=1,column=0)
entree1.grid(row=1,column=1)
texte2.grid(row=2,column=0)
entree2.grid(row=2,column=1)
texte3.grid(row=3,column=0)
entree3.grid(row=3,column=1)
#cadre1.grid(row=3,column=0)
bouton1.grid(row=4,column=0)
bouton2.grid(row=4,column=1)
bouton3.grid(row=4,column=2)

tk.mainloop()
