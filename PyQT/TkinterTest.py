# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 01:00:23 2021

@author: User
"""

import tkinter as tk
racine = tk.Tk()
racine.geometry("350x200")
racine.title("M2I&MQL Tkinter")
label = tk.Label(racine, text="Interface de Test avec Tkinter ...")
bouton = tk.Button(racine, text="Quitter", command=racine.quit)
bouton["fg"] = "red"
label.pack()
bouton.pack()
racine.mainloop()