

import wx 
 
class MDIFrame(wx.MDIParentFrame): 
   def __init__(self): 
      wx.MDIParentFrame.__init__(self, None, -1, "M2I & MQL - Multi Windows", 
                                 size = (600,400)) 
      menu = wx.Menu() 
      menu.Append(5000, "&New Window") 
      menu.Append(5001, "&Exit") 
      menubar = wx.MenuBar() 
      menubar.Append(menu, "&File") 
		
      self.SetMenuBar(menubar) 
      self.Bind(wx.EVT_MENU, self.OnNewWindow, id = 5000) 
      self.Bind(wx.EVT_MENU, self.OnExit, id = 5001) 
		
   def OnExit(self, evt): 
      self.Close(True)  
		
   def OnNewWindow(self, evt): 
      win = wx.MDIChildFrame(self, -1, "M2I & MQL - New Window")
      win.Show(True) 
		
app = wx.App() 
frame = MDIFrame() 
frame.Show() 
app.MainLoop()
