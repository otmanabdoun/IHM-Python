# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 01:15:33 2021

@author: User
"""

with open("truc.txt", "w", encoding='utf8') as f:
    s = 'MASTERS  QL & 2I \n'
    f.write(s) 
    l = [' IHM ', ' ML ', ' WEB ']
    f.writelines(l)    

with open("truc2.txt", "w", encoding='utf8') as f2:
    f2 = open("truc2.txt", "w", encoding='utf8')
    print("Les Modules des deux masters", file=f2)

with open("truc.txt", "r", encoding='utf8') as f:
    s = f.read()
    print(s)

with open("truc.txt", "r", encoding='utf8') as f:
    s = f.readlines()
    print(s)



x = pickle.load(f)
pickle.dump(x, f)