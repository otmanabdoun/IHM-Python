import wx
class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)
        self.InitUI()
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        nmi = wx.MenuItem(fileMenu, wx.ID_NEW, '&New\tCtrl+N')
        nmi.SetBitmap(wx.Bitmap('new.jpg'))
        fileMenu.AppendItem(nmi)
        omi = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open\tCtrl+O')
        omi.SetBitmap(wx.Bitmap('open.jpg'))
        fileMenu.AppendItem(omi)
        fileMenu.AppendSeparator()
        smi = wx.Menu()
        smi.Append(wx.ID_ANY, 'Save File...')
        smi.Append(wx.ID_ANY, 'Save As...')
        fileMenu.AppendMenu(wx.ID_SAVE, 'Save', smi)
        fileMenu.AppendSeparator()
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        qmi.SetBitmap(wx.Bitmap('quit.jpg'))
        fileMenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.SetSize((350, 250))
        self.SetTitle('M2I & MQL - Submenu')
        self.Centre()
    def OnQuit(self, e):
        self.Close()
def main():
    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()
if __name__ == '__main__':
    main()
