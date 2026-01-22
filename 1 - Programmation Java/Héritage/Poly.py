
class Master: 
          def ModuleWEB(self): 
                 print("Développement Web") 
class M2I(Master):
           def ModuleWEB(self): 
                  print("Web Sémantique") 
class MQL(Master): 
           def ModuleWEB(self): 
                  print("PHP OO")

E=Master()
E.ModuleWEB()

E=M2I()
E.ModuleWEB()

E=MQL()
E.ModuleWEB()
