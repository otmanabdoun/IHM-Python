# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import locale




###########################################################################
## Class MyFrameTest
###########################################################################

class MyFrameTest ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"M2I & MQL - Test Project", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 4, 2, 0, 0 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Nom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Prénom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Master", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		m_comboBox1Choices = [ u"Master M2I", u"Master MQL", u"Autre Master" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		gSizer1.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		gSizer1.Add( m_sdbSizer2, 1, wx.BOTTOM|wx.EXPAND, 5 )


		bSizer1.Add( gSizer1, 1, wx.ALL|wx.EXPAND, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"SaveAs", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem1 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"Save" )

		self.m_menu1.AppendSeparator()

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, u"Aide" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


def main():

    app = wx.App()    
    ex = MyFrameTest(None)
    ex.Show()
    app.MainLoop()
    

if __name__ == '__main__':
    main()