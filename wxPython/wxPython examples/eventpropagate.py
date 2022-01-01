
import wx

class MyPanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        print('Evénement est déclanché de la classe Button')
       # e.Skip()


class MyButton(wx.Button):

    def __init__(self, *args, **kw):
        super(MyButton, self).__init__(*args, **kw)

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

    def OnButtonClicked(self, e):

        print('Evénement est déclanché de la classe Button')
        #e.Skip()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):

        mpnl = MyPanel(self)

        MyButton(mpnl, label='Ok', pos=(15, 15))

        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)

        self.SetTitle('M2I & MQL - Propagate event')
        self.Centre()

    def OnButtonClicked(self, e):

        print('Evénement est déclanché de la classe Frame')
        e.Skip()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()