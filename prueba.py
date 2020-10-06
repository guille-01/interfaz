from wx import *

class MyApp(App):
    def OnInit(self):
        f = Frame(None, title= "Titulo de la ventana")
        panel = Panel(f) #Ventana contenedora invisible dentro del frame
        s = BoxSizer(VERTICAL)
        cartelito = StaticText(panel, -1,"Ingrese nombre: ", (4,10))
        nombre = TextCtrl(panel, pos = (115,3))
        s.Add(cartelito)
        s.Add(nombre)
        f.Show()

        return True

app = MyApp()
app.MainLoop()

#Frame -> Parent es padre, o madre. Significa donde esta el frame.
#Este frame es la ventana principal, no esta sobre nadie, por eso va "None", no va arriba ni dentro de nadie.

#BoxSizer: Vertical u Horizontal. Estructura mas sencilla.
