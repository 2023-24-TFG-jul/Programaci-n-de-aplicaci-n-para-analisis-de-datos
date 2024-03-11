#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.3.0
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import tkinter as tk
import psycopg2

import sqlalchemy
from BaseDatosLvl2 import BaseDatosLvl2
from tkinter import messagebox

#Clase con la que el usuario interactuará
class UI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        #Destroys current frame and replaces it with a new one.
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class LoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login Page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Login",
                  command=lambda: master.switch_frame(MainPage)).pack()
        
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self,text="Pagina Principal", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Descargas", font=('Arial', 18), command=lambda: master.switch_frame(Descargas)).pack(padx=10, pady=10)
        tk.Button(self, text="Actualizaciones", font=('Arial', 18), command=lambda: master.switch_frame(Actualizaciones)).pack(padx=10, pady=10)

class Descargas(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Descarga de datos", font=('Arial', 18), command=lambda: master.switch_frame(DescDatos)).pack()
        tk.Button(self, text="Descarga de imagenes", font=('Arial', 18), command=lambda: master.switch_frame(DescImg)).pack()
        tk.Button(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack()
    
class DescDatos(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="Introduce la fecha de inicio", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxIni = tk.Text(self, height=1, width=20)
        self.textboxIni.pack()
        tk.Label(self, text="Introduce la fecha de fin", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxFin = tk.Text(self, height=1, width=20)
        self.textboxFin.pack()
        tk.Label(self, text="Introduce la tabla", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxtable = tk.Text(self, height=1, width=20)
        self.textboxtable.pack()
        tk.Button(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)
        tk.Button(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack()
        self.bd2=BaseDatosLvl2()

    #Definimos una función para descargar datos
    ###########################################################################################################################################
    def descDat(self):
        fechaini=self.textboxIni.get('1.0',tk.END)
        fechaini=fechaini.replace('\n','')
        fechafin=self.textboxFin.get('1.0',tk.END)
        fechafin=fechafin.replace('\n','')
        tabla=self.textboxtable.get('1.0',tk.END)
        tabla=tabla.replace('\n','')
        try:
            self.bd2.descdat("*",tabla,fechaini,fechafin)
        except sqlalchemy.exc.ProgrammingError:
            messagebox.showinfo(title="Error",message="""Has introducido mal la tabla o las fechas\n
                                Recuerda introducir las fechas en formato 'YY-MM-DD' \ny la tabla en minúsculas""")
    ###########################################################################################################################################
class DescImg(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="Introduce la fecha de inicio", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxIni = tk.Text(self, height=1, width=20)
        self.textboxIni.pack()
        tk.Label(self, text="Introduce la fecha de fin", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxFin = tk.Text(self, height=1, width=20)
        self.textboxFin.pack()
        tk.Button(self, text="Descargar", font=('Arial', 18), command=self.descImg).pack(padx=10, pady=10)
        tk.Button(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack()
        self.bd2=BaseDatosLvl2()

    #Definimos una función para deascargar las imagenes
    ########################################################################################################################################
    def descImg(self):
        try:
            self.bd2.descImg(self.textboxIni.get('1.0',tk.END),self.textboxFin.get('1.0',tk.END))
        except psycopg2.errors.SyntaxError:
            messagebox.showinfo(title="Error",message="Has introducido mal las fechas\n Recuerda introducir las fechas en formato 'YY-MM-DD-HH'")

class Actualizaciones(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Actualizar datos", font=('Arial', 18), command=self.actualizardatos).pack(padx=10, pady=10)
        tk.Button(self, text="Actualizar imagenes", font=('Arial', 18), command=self.actualizarimagenes).pack(padx=10, pady=10)
        tk.Button(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack()    
        self.bd2=BaseDatosLvl2() 
    

     #Definimos una función que al pulsar el boton actualice los datos
    ##################################################################################################################################################
    def actualizardatos(self):
        radioerr,skycamerr,skyscanerr=self.bd2.actualizardatos()#Actualizamos los datos

        mesradio="" #Inicializamos las variable de los mensajes como vacio para que en caso de que no se modifiquen no añadan nada al mensaje final
        messkyscan=""
        messkycam=""
        if (radioerr !=0): #Si ha habido datos repetidos en radio creamos el mensaje
            mesradio="Has intentado introducir {} archivos repetidos en radio\n".format(radioerr)
        if (skycamerr!=0): #Si ha habido datos repetidos en skycamera creamos el mensaje
            messkycam="Has intentado introducir {} archivos repetidos en skycam\n".format(skycamerr)
        if (skyscanerr!=0): #Si ha habido datos repetidos en skyscanner creamos el mensaje
            messkyscan="Has intentado introducir {} archivos repetidos en skyscanner\n".format(skyscanerr)
        mensaje=mesradio+messkycam+messkyscan #Creamos el mensaje completo uniendo todos
        if (mensaje!=""): #Si ha habido algun dato repetido mostramos por pantalla los que haya habido
            messagebox.showinfo(title="Datos repetidos",message=mensaje)#Sacamops por pantalla el mensaje
        else:
            messagebox.showinfo(title="Operación exitosa",message="Has actualizado los datos con exito")#Sacamops por pantalla el mensaje
    ##########################################################################################################################################

    #Definimos una función para actualizar las imagenes y que devuelva por pantalla si se incluyen imagenes repetidas
    ##########################################################################################################################################
    def actualizarimagenes(self):

        cont=self.bd2.actualizarImg() #hacer la actualización de las imagenes
        
        if (cont!=0): #Si el contador no es 0 se imprimira por pantalla que ha habido almenos una entrada de imagenes repetida
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)
            messagebox.showinfo(title="Message",message=messkyscan)
        else:
            #Sacamos por pantalla el mensaje de que se han actualizado las imagenes con exito
            messagebox.showinfo(title="Operación exitosa",message="Has actualizado todas las imagenes con exito")
    ###########################################################################################################################################
        
if __name__ == "__main__":
    app = UI()
    app.mainloop()

