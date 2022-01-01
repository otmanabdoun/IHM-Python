import sys
from PyQt5 import QtWidgets, uic

def Fermer():
    u.close()

def Activer_But1():
    if u.NS1.text()=="":
        u.Calc.setEnabled(False)
    else:
        u.Calc.setEnabled(True)

def Activer_But2():
    if u.NS2.text()=="" or u.MS2.text()=="":
        u.Calc.setEnabled(False)
    else:
        u.Calc.setEnabled(True)        

def PGCD(a, b):
    while a != b:
        if a>b :
            a=a-b
        else:
            b=b-a
    return a

def PPCM(a, b):
    return (a * b) // PGCD(a,b)

def Fact_Premier(a):
    i=2
    Fa=""
    while a != 1:
        if a % i == 0:
            Fa = Fa + str(i)+ " * "
            a = a // i
        else:
            i = i + 1
    return Fa[:-2]
            

def Premier(a):
    Nd=0
    for i in range(1, a+1) :
        if a % i == 0 :
            Nd = Nd + 1
    if Nd == 2 :
        return "Nombre premier"
    else:
        return "Nombre n'est pas Premier"

def Fact(a):
    F=1
    for i in range (1, a+1):
        F = F * i
    return F

def Calculer():
    if Ind in list(range(3, 6)):
        if u.NS1.text().isdigit()==False:
            QtWidgets.QMessageBox.question(None,'Attention', "Nombre incorrect", QtWidgets.QMessageBox.Ok)
            return None
        else:
            N1=int(u.NS1.text())
    elif Ind in list(range(1, 3)):
        if u.NS2.text().isdigit()==False or u.MS2.text().isdigit()==False:
            QtWidgets.QMessageBox.question(None,'Attention', "Nombre 1 ou nombre 2 incorrect", QtWidgets.QMessageBox.Ok)
            return None
        else:
            N2=int(u.NS2.text())
            M2=int(u.MS2.text())
    if Ind == 1:
        u.Res.setText(str(PGCD(N2,M2)))
    elif Ind == 2:
        u.Res.setText(str(PPCM(N2,M2)))
    elif Ind == 3:
        u.Res.setText(Fact_Premier(N1))
    elif Ind == 4:
        u.Res.setText(Premier(N1))
    elif Ind == 5:
        u.Res.setText(str(Fact(N1)))

def Afficher():
    global Ind
    Ind=u.Choix.currentIndex()
    if Ind in list(range(1,3)):
        u.G_Saisie1.hide()
        u.G_Saisie2.show()
    elif Ind in list(range(3,6)):
        u.G_Saisie2.hide()
        u.G_Saisie1.show()
    else :
        u.G_Saisie1.hide()
        u.G_Saisie2.hide()
    
a = QtWidgets.QApplication(sys.argv)
u=uic.loadUi("interface_calcul.ui")
u.show()
u.G_Saisie1.hide()
u.G_Saisie2.hide()
u.Choix.currentIndexChanged.connect(Afficher)
u.Calc.clicked.connect(Calculer)
u.Ferm.clicked.connect(Fermer)
u.NS1.textEdited.connect(Activer_But1)
u.NS2.textEdited.connect(Activer_But2)
u.MS2.textEdited.connect(Activer_But2)
a.exec_()
sys.exit()
