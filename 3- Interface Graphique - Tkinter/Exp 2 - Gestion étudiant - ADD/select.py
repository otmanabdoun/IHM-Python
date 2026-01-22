
import sqlite3

connexion = sqlite3.connect("dbGUIMaster.db")
curseur = connexion.cursor()  

#curseur.execute('''DROP TABLE Etudiant''')
#curseur.execute("""DELETE FROM Etudiant""")


curseur.execute('''CREATE TABLE  IF NOT EXISTS  Etudiant(
    id TEXT,
    Nom TEXT,
    Prenom TEXT,
    Master TEXT
)''')



donnees = [("1","El Fahssi", "Ikram", "Master MQL"), ("2","Ktiti", "Mohamed", "Master MQL"), ("3","Amakran","Hajar", "Master M2I")]
#Exécutions multiples
for donnee in donnees:
    curseur.execute('''INSERT INTO Etudiant (id, Nom, Prenom, Master) VALUES (?, ?, ?, ?)''', donnee)
connexion.commit()


print("\n M2 - Liste des étudiants : MQL et M2I - \n")
curseur.execute("SELECT * FROM Etudiant")
resultats = curseur.fetchall()
for resultat in resultats:
    print(resultat)
    
if curseur.arraysize == 1 :
    print("\nREQUETTE OK  ++++ ")
else:
    print("\nREQUETTE KO  ---- ")
    
print(connexion.total_changes) 