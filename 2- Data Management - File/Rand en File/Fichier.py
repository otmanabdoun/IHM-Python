from random import randint
with open("rand.txt", "r") as fichier:
#fichier = open("rand.txt",'r')
    lignes = fichier.readlines()

with open("rand.txt", "w") as fichier:
    fichier = open("rand.txt",'w')
    for i in range(1, 50):
        fichier.write(" Valeur %i : %i \n"%(i,i))
    #fichier.write(" Valeur %i : %i \n"%(i,randint(1, 100)))

    print(lignes)
