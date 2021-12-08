# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:19:38 2021

@author: User
"""

# First things, first. Import the wxPython package.
import wx

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = wx.Frame(None, title="Hello World")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()