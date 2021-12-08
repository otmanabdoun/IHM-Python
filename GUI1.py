# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:47:41 2021

@author: User
"""

import tkinter as tk
racine = tk . Tk ()
label = tk . Label ( racine , text ="J ' adore Python !")
bouton = tk . Button ( racine , text =" Quitter ", command = racine . destroy )
label . pack ()
bouton . pack ()