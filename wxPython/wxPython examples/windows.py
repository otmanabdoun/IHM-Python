import wx

app = wx.App()

frame = wx.Frame(None, title='M2I & MAL : Simple App')

#frame.Centre()
#frame.Move((800, 250))

frame.SetDimensions(700, 150, 340, 200)	

frame.Show()

app.MainLoop()

