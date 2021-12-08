# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 00:55:49 2021

@author: User
"""

from tkinter import *
from math import *

def evaluer(event) :
    chaine.configure(text = '=> ' + str(eval(entree.get())))


fenetre = Tk()

fenetre.title("Calculatrice App")
fenetre.iconbitmap("logo.ico")
fenetre.config(bg = "White")
fenetre.geometry("400x200")

entree = Entry(fenetre)
entree.bind('<Return>', evaluer)
chaine = Label(fenetre)
texte1 = Label (fenetre, text = "Saisir votre opératon : ")
texte2 = Label (fenetre, text = "Résultats : ")

texte1.pack()
entree.pack()
texte2.pack()
chaine.pack()

fenetre.mainloop()