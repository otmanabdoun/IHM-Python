import locale
import wx 

def InitLocale(self):
        self.ResetLocale()
        if 'wxMSW' in wx.PlatformInfo:
            import locale
            try:
                lang, enc = locale.getdefaultlocale()
                self._initial_locale = wx.Locale(lang, lang[:2], lang)
                locale.setlocale(locale.LC_ALL, lang)
            except (ValueError, locale.Error) as ex:
                target = wx.LogStderr()
                orig = wx.Log.SetActiveTarget(target)
                wx.LogError("Unable to set default locale: '{}'".format(ex))
                wx.Log.SetActiveTarget(orig)
                
#locale.setlocale(locale.LC_ALL,'C')
#wx.App.InitLocale(self='1252')
#wx.Locale.GetLocaleInfo('French_Morocco')



InitLocale(wx.App)
app = wx.App() 
window = wx.Frame(None, title = "M2I & MQL - wxPython Frame", size = (350,160)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hello M2I &&& MQL students  ;-)", pos = (90,50)) 
window.Show(True) 
app.MainLoop()
