from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title= "Titulo de la ventana")
        p = Panel(f)
        sizer = BoxSizer(VERTICAL)
        textoEstatico = StaticText(p, -1, "Ingrese nombre:")
        tNombre = TextCtrl(p) 
        b = Button(p, -1, "Botoncito")
        sizer.Add(textoEstatico, 0, ALL, 10)
        sizer.Add(tNombre, 0, ALL |EXPAND, 10)
        sizer.Add(b, 0, TOP|CENTER, 20)

        p.SetSizer(sizer)
        f.Show()

        return True

app = MyApp()
app.MainLoop()







#Frame -> Parent es padre, o madre. Significa donde esta el frame.
#Este frame es la ventana principal, no esta sobre nadie, por eso va "None", no va arriba ni dentro de nadie.

#BoxSizer: Vertical u Horizontal. Estructura mas sencilla.

#Se usan layouts para acomodar, en wxPython es SetSizer, es para acomodar los objetos dentro de la ventana
#Horizontal viene por defecto.
