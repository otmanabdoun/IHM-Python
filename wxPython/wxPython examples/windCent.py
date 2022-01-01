import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(350, 200))

        self.Centre()


def main():

    app = wx.App()
    ex = Example(None, title='M2I&MQL - Centering App')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
    
    