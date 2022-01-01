# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 03:45:26 2021

@author: User
"""


from lxml import etree

users = etree.Element("etudiants")
user = etree.SubElement(users, "etudiant")
user.set("data-id", "11")
nom = etree.SubElement(user, "nom")
nom.text = "BOUZIKI Abderrahman"
metier = etree.SubElement(user, "master")
metier.text = "Master MQL"
print(etree.tostring(users, pretty_print=True))

tree = etree.ElementTree(users)
tree.write("data1.xml")
