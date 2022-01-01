import wx

# Création d'un nouveau cadre, dérivé du wxPython 'Frame'.
class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(-1, -1), size=(350, 150))

        # À l'intérieur du cadre, créer un panneau..
        panel = wx.Panel(self, -1)

        # Créer un texte dans le panneau
        texte = wx.StaticText(panel, -1, "Bonjour tout le monde!", wx.Point(10, 5), wx.Size(-1, -1))
                
        # Créer un bouton dans le panneau
        bouton = wx.Button(panel, -1, "Cliquez-moi!",  wx.Point(10, 35), wx.Size(-1, -1))
        # lier le bouton à une fonction:
        self.Bind(wx.EVT_BUTTON, self.creerDiag, bouton)
        
    # fonction qui affiche une boîte de dialogue
    def creerDiag(self, event):
        dlg = wx.MessageDialog(self, "Merci de m'avoir cliqué, ça fait du bien.",
          "Merci!", wx.ICON_EXCLAMATION | wx.YES_NO | wx.CANCEL)
        dlg.ShowModal()
        dlg.Destroy()
        

# Chaque application wxWidgets doit avoir une classe dérivée de wx.App
class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, -1, "M2I & MQL - Test GUI")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = TestApp(0) # créer une nouvelle instance de l'application
    app.MainLoop()   # lancer l'application
    
    