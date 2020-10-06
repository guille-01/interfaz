from wx import *

class MyApp(App):
    def OnInit(self):  #Como seria con def __init__ ?
        self.f = f = Frame(None, title = "Titulo de la ventana")
        p = Panel(f)
        sizer = BoxSizer(VERTICAL)
        self.textoEstatico = textoEstatico = StaticText(p, -1, "Ingrese nombre:")
        self.tNombre = tNombre = TextCtrl(p) #Caja de texto
        b = Button(p, -1, "Botoncito")
        b.Bind(EVT_BUTTON, self.accion) #Enlazar evento y una accion
        b.Bind(EVT_SET_FOCUS, self.cambiaColor)
        sizer.Add(textoEstatico, 0, ALL, 10)
        sizer.Add(tNombre, 0, ALL |EXPAND, 10)
        sizer.Add(b, 0, TOP|CENTER, 20)

        p.SetSizer(sizer)
        f.Show()

        return True

#Esta funcion hace que obtenga el valor, y asigne a otro metodo como el staticText, explicado despues.
#Ademas, abre y muestra otra ventana, y con la pregunta que hice de como cerrar la primera: la respuesta es self.f.Close()
    
    def cambiaColor(self, event):
        pass
    
    def accion(self, event):
        v = self.tNombre.GetValue()
        self.textoEstatico.SetLabel(v)  #Con lo que ponemos en el campo, se apreta en el campo y se manda al staticText
        f2 = Frame(None, title = "Otra ventana", pos = (2000, 2))
        f2.Show()
        self.f.Show(False)

app = MyApp()
app.MainLoop()


#Bind sirve para enlazar un evento con un handler (manejador), el manejador es una funcion
#event como segundo parametro se usa por convencion y para otras funciones





#Frame -> Parent es padre, o madre. Significa donde esta el frame.
#Este frame es la ventana principal, no esta sobre nadie, por eso va "None", no va arriba ni dentro de nadie.

#BoxSizer: Vertical u Horizontal. Estructura mas sencilla.

#Se usan layouts para acomodar, en wxPython es SetSizer, es para acomodar los objetos dentro de la ventana
#Horizontal viene por defecto.
