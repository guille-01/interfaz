"""(3.3) Almacenar en dos listas paralelas, nombres y sexos de 8 personas.
Cargar los nombres en cajas de texto y el sexo seleccionarlo a través de botones de opción.
Mostrar los nombres de las mujeres en otro frame. 
"""



from wx import *

class MyApp(App):
    def OnInit(self):
        self.listaHombres = listaHombres = []
        self.listaMujeres = listaMujeres = []
        f = Frame(None, title= "Programa")
        panel = Panel(f) #Ventana contenedora invisible dentro del frame
        self.rb1 = RadioButton(panel, label = "silvia", pos = (10,10))
        self.rb2 = RadioButton(panel, label = "Mujer",  pos= (10, 40))
        sizer = BoxSizer(VERTICAL)
        b = Button(panel, -1, "Finalizar")
        self.tNombre = tNombre = TextCtrl(panel, -1, "Nombre") 
        sizer.Add(tNombre)
        sizer.Add(self.rb1)
        sizer.Add(self.rb2)
        sizer.Add(b, 0 ,TOP|CENTER,280)
        panel.SetSizer(sizer)
        f.Show()
        return True

        

"""def cargarNombres(self, event):
        b.SetLabel("Perfecto!, queres cargar mas nombres?")
        f2 = Frame(None, title = "Otra ventana", pos = (2000, 2))
        f2.Show()
        self.f.Close()  #Quiero cambiarle el nombre al boton de finalizar por "perfecto, quieres cargar mas?" """
                        


        

app = MyApp()
app.MainLoop()



"""for i in range (5):
            i = 10
            self.caja = caja = TextCtrl(panel, pos = (0,i))
            i = i + 10"""