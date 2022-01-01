import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(350, 200))

        self.Move((800, 250))


def  main():

    app = wx.App()
    ex = Example(None, title='M2I&MQL - Moving App')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
    