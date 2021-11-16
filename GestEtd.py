import sqlite3
connexion = sqlite3.connect("dbM2IQL.db") 
curseur = connexion.cursor()
curseur.execute("PRAGMA foreign_keys = ON") 
curseur.executescript("""
    CREATE TABLE IF NOT EXISTS Etudiant(
    id INTEGER PRIMARY KEY,
    Nom TEXT,
    Master TEXT);

    CREATE TABLE IF NOT EXISTS CF(
    id_cf INTEGER PRIMARY KEY ,
    fk_etudiant INTEGER NOT NULL,
    note INTEGER,
    FOREIGN KEY(fk_etudiant) REFERENCES Etudiant(id)
    ON DELETE CASCADE);
    DELETE FROM Etudiant;
""")
donnees_Etudiant = [(1, "El Fahssi", "MQL"), (2, "Ktiti Mohamed", "MQL"), 
    (3, "Amakran Hajar", "M2I")]
donnees_CF = [(1, 1, 10),(2, 2, 17), (3, 3, 15)]
curseur.executemany("INSERT INTO Etudiant (id, Nom, Master) VALUES (?, ?, ?)", donnees_Etudiant)
curseur.executemany("INSERT INTO CF (id_cf,fk_etudiant, note) VALUES (?, ?, ?)", donnees_CF)
connexion.commit()

for etudiant in curseur.execute("SELECT * FROM Etudiant"):
    print("Etudiants :", etudiant)
for notecf in curseur.execute("SELECT * FROM CF"):
    print("Notes CF :", notecf)
connexion.close()