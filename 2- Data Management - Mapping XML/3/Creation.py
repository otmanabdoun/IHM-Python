
import xml.etree.cElementTree as ET

etudiants = ET.Element("etudiants")
master1 = ET.SubElement(etudiants, "M2I")
ET.SubElement(master1, "etudiant1", name="E1").text = "BAAZA Wafae"
ET.SubElement(master1, "etudiant2", name="E2").text = "ALLOUANE Hatim"

tree = ET.ElementTree(etudiants)
tree.write("dataMaster.xml")