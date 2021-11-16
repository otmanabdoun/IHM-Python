# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 02:55:41 2021

@author: User
"""

import tkinter as tk
from os.path import isfile
# class
class Allo_IHM :
    def __init__(self, fic) :
        self.phoneList = []
        self.fic = fic
        if isfile(self.fic) :
            with open(self.fic) as f :
                for line in f :
                    self.phoneList.append(line[:-1].split('*'))
        else :
            with open(self.fic, "w", encoding="utf8") :
                pass
        self.phoneList.sort()
        self.root = tk.Tk()
        self.root.title("Allo !")
        self.root.config(relief=tk.RAISED, bd=3)
        self.makeWidgets()
        self.nameEnt.focus()
        self.root.mainloop()
    def makeWidgets(self) :
        frameH = tk.Frame(self.root, relief=tk.GROOVE, bd=2)
        frameH.pack()
        tk.Label(frameH, text="Nom :").grid(row=0, column=0, sticky=tk.W)
        self.nameEnt = tk.Entry(frameH)
        self.nameEnt.grid(row=0, column=1, sticky=tk.W, padx=5, pady=10)
        tk.Label(frameH, text="Tel :").grid(row=1, column=0, sticky=tk.W)
        self.phoneEnt = tk.Entry(frameH)
        self.phoneEnt.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        b = tk.Button(frameH, text="Effacer ", command=self.clear)
        b.grid(row=2, column=0, columnspan=2, pady=3)
        frameM = tk.Frame(self.root)
        frameM.pack()
        self.scroll = tk.Scrollbar(frameM)
        self.select = tk.Listbox(frameM, yscrollcommand=self.scroll.set, height=6)
        self.scroll.config(command=self.select.yview)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y, pady=5)
        self.select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, pady=5)        
        for i in self.phoneList :
            self.select.insert(tk.END, i[0])
            self.select.bind("<Double-Button-1>", lambda event : self.afficher(event))
            frameB = tk.Frame(self.root, relief=tk.GROOVE, bd=3)
            frameB.pack(pady=3)
            b1 = tk.Button(frameB, text="Ajouter ", command=self.ajouter)
            b2 = tk.Button(frameB, text="Supprimer", command=self.supprimer)
            b3 = tk.Button(frameB, text="Afficher ", command=self.afficher)
            b1.pack(side=tk.LEFT, pady=2)
            b2.pack(side=tk.LEFT, pady=2)
            b3.pack(side=tk.LEFT, pady=2)
    def ajouter(self) :
        pass
    def supprimer(self) :
        pass
    def afficher(self, event=None) :
        pass
    def clear(self) :
        pass

if __name__ == '__main__' :
    app = Allo_IHM("./phones.txt")