# -*- coding: utf-8 -*-
from lxml import etree

users = etree.Element("etudiants")

users_data = [
("11", "BOUZIKI Abderrahman", "Master MQL"),
("12", "ANMRANI Yassine", "Master MQL"),
("13", "MKHECHEN Bilal", "Master M2I"),
("14", "ARAROU Hayat", "Master M2I"),
("15", "BEN HADDOU Mohamed", "Master MQL"),
]

for user_data in users_data:
    user = etree.SubElement(users, "etudiant")
    user.set("data-id", user_data[0])
    nom = etree.SubElement(user, "nom")
    nom.text = user_data[1]
    metier = etree.SubElement(user, "master")
    metier.text = user_data[2]

print(etree.tostring(users, pretty_print=True))

tree = etree.ElementTree(users)
tree.write("ListeM.xml")
