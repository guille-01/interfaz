import wx 

class MiAplicacion(wx.Frame):
    def __init__ (self, parent, title):
        wx.Frame .__init__(self,parent=parent, title=title, size=(300,200))     #Con el import wx despues cuando llamo a un metodo pongo wx.Metodo
        sizer = wx.BoxSizer(wx.VERTICAL)

        textC= wx.TextCtrl(self, style = wx.TE_MULTILINE, pos = (25, 0), size= (100,100))  #Te_Multiline hace que pueda escribir en varias lineas
        texto2 = wx.TextCtrl(self, style = wx.TE_MULTILINE, pos = (155,0), size = (100,100))
        suma = wx.Button(self, -1, u"Sumar", pos = (3,105), size = (60,40))
        resta =  wx.Button(self, -1, u"Restar", pos = (70,105), size = (60,40))
        multiplicar =  wx.Button(self, -1, u"Multiplicar", pos = (137,105), size = (65,40))
        dividir = wx.Button(self, -1, u"Dividir", pos = (207,105), size = (60,40))
        self.Centre(True)
        self.Show()
#a
#BoxSizer hace arreglos verticales y horizontales. Es el más sencillo

if __name__=='__main__':
    app = wx.App()
    frame = MiAplicacion(None, u"Mi primera aplicacion")
    app.MainLoop()