import wx

class TestFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, pos=(-1, -1), size=(350, 150))
        panel = wx.Panel(self, -1)
        texte = wx.StaticText(panel, -1, "Bonjour tout le monde!", wx.Point(10, 5), wx.Size(-1, -1))             
        bouton = wx.Button(panel, -1, "Cliquez-moi!",  wx.Point(10, 35), wx.Size(-1, -1))
        self.Bind(wx.EVT_BUTTON, self.creerDiag, bouton)
        
    def creerDiag(self, event):
        dlg = wx.MessageDialog(self, "Merci de m'avoir cliqué, ça fait du bien.",
          "Merci!", wx.ICON_EXCLAMATION | wx.YES_NO | wx.CANCEL)
        dlg.ShowModal()
        dlg.Destroy()

class TestApp(wx.App):
    def OnInit(self):
        frame = TestFrame(None, -1, "M2I & MQL - Test GUI")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

if __name__ == '__main__':
    app = TestApp(0)
    app.MainLoop()   
    
    