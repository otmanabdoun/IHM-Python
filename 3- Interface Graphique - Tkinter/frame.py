# -*- coding: utf-8 -*-

from tkinter import *

fenetre = Tk()

fenetre.title("M2I & MQL App")
fenetre.iconbitmap("logo.ico")
fenetre.config(bg = "#87CEEB")
fenetre.geometry("300x250")

menu1 = Menu(fenetre)
menu1.add_cascade(label="Fichier")
menu1.add_cascade(label="Options")
menu1.add_cascade(label="Aide")
fenetre.config(menu = menu1)

cadre1 = Frame(fenetre)
cadre1.pack()
texte1 = Label (fenetre, text = "Saisir le nom de l'étudiant : ")
texte1.pack()
entrée1 = Entry (fenetre)
entrée1.pack()
texte2 = Label (fenetre, text = "Saisir  l'age  de  l'étudiant : ")
texte2.pack()
spinbox1 = Spinbox(fenetre, from_=20, to=30, increment=1)
spinbox1.pack()
case_cocher1 = Checkbutton (fenetre, text = "Master    M2I")
case_cocher2 = Checkbutton (fenetre, text = "Master  MQL")  
case_cocher1.pack()
case_cocher2.pack()
bouton1 = Button (cadre1, text = "Ajouter un étudiant")
bouton1.pack()

fenetre.mainloop()
