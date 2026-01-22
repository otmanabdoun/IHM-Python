from tkPhone_IHM import Allo_IHM

class Allo(Allo_IHM) :
    def __init__(self, fic='phones.txt') :
        super().__init__(fic)

    def ajouter(self) :
        ajout = ["",""]
        ajout[0] = self.nameEnt.get()
        ajout[1] = self.phoneEnt.get()
        if (ajout[0] == "") or (ajout[1] == "") :
            return
        self.phoneList.append(ajout)
        self.phoneList.sort()
        self.select.delete(0, 'end')
        for i in self.phoneList :
            self.select.insert('end', i[0])
        self.clear()
        self.nameEnt.focus()
        f = open(self.fic, "a")
        f.write("%s*%s\n" % (ajout[0], ajout[1]))
        f.close()

    def supprimer(self) :
        self.clear()
        retrait = ["",""]
        retrait[0], retrait[1] = self.phoneList[int(self.select.curselection()[0])]
        self.phoneList.remove(retrait)
        self.select.delete(0, 'end')
        for i in self.phoneList :
            self.select.insert('end', i[0])
        f = open(self.fic, "w")
        for i in self.phoneList :
            f.write("%s*%s\n" % (i[0], i[1]))
        f.close()

    def afficher(self, event=None) :
        self.clear()
        name, phone = self.phoneList[int(self.select.curselection()[0])]
        self.nameEnt.insert(0, name)
        self.phoneEnt.insert(0, phone)

    def clear(self) :
        self.nameEnt.delete(0, 'end')
        self.phoneEnt.delete(0, 'end')


app = Allo()