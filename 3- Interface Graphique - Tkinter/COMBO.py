# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 00:54:02 2021

@author: User
"""

from tkinter import *
import tkinter as tk
from tkinter import ttk
user = Tk()
comb = tk.Label(user,
text = "Please select the option")
comb.grid(column=2, row=1)

entree3 = ttk.Combobox(user,
values=[
"Master M2I",
"Master MQL"])
print(dict(entree3))
entree3.grid(column=2, row=2)
#entree3.current(3)
user.mainloop()