import pygtk
pygtk.require('2.0')
import gtk

class Base:
    def __init__(self):
        self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.fenetre.show()
   
    def boucle(self):
        gtk.main()
   
    print (__name__)

if __name__ == "__main__":
    base = Base()
    base.boucle() 