#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.1.0
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import tkinter as tk
from BaseDatosLvl2 import BaseDatosLvl2
from tkinter import messagebox

#Clase con la que el usuario interactuará
class UI:

    #Definimos un constructor que inicialice toda la clase con sus cosas necesarias
    ######################################################################################################################################################################################
    def __init__(self):
        self.root=tk.Tk() #Creamos la pantalla de la aplicación
        self.labelAct=tk.Label(self.root,text="Actualizaciones",font=('Arial',25))# Creamos un titulo para llamar a la aplicación
        self.labelAct.pack(padx=10,pady=10) #Lo colocamos en la pantalla

        

        self.check_state=tk.IntVar() #Creamos un check que estara en la pantalla
        self.check= tk.Checkbutton(self.root,text="",font=('Arial',16),variable=self.check_state) #Creamos un chek button que registre el estado del check
        self.check.pack(padx=10,pady=10) #Lo colocamos en la pantalla
        #Creamos el boton que actualizara los datos
        self.buttonActDat=tk.Button(self.root,text="Actualizar datos",font=('Arial',18),command=self.actualizardatos)
        self.buttonActDat.pack(padx=10,pady=10)
        #Creamos un boton que actualizara las imagenes
        self.buttonActImg=tk.Button(self.root,text="Actualizar imagenes",font=('Arial',18),command=self.actualizarimagenes)
        self.buttonActImg.pack(padx=10,pady=10)

        self.labelDesc=tk.Label(self.root,text="Descargas",font=('Arial',25))# Creamos un titulo para llamar a la aplicación
        self.labelDesc.pack(padx=10,pady=10) #Lo colocamos en la 
        
        self.labelIni=tk.Label(self.root,text="Fecha inicio",font=('Arial',15))# Creamos un titulo para llamar a la aplicación
        self.labelIni.pack(padx=10,pady=10) #Lo colocamos en la pantalla

        self.textboxIni=tk.Text(self.root,font=('Arial',11),height=1)
        self.textboxIni.pack(padx=30,pady=30)

        self.labelFin=tk.Label(self.root,text="Fecha Fin",font=('Arial',15))# Creamos un titulo para llamar a la aplicación
        self.labelFin.pack(padx=10,pady=10) #Lo colocamos en la pantalla

        self.textboxFin=tk.Text(self.root,font=('Arial',11),height=1)
        self.textboxFin.pack(padx=30,pady=30)

        #Creamos un boton que actualizara las imagenes
        self.buttonDescDat=tk.Button(self.root,text="Descargar Datos",font=('Arial',18),command=self.descDat)
        self.buttonDescDat.pack(padx=10,pady=10)

        #Creamos un boton que actualizara las imagenes
        self.buttonDescImg=tk.Button(self.root,text="Descargar imagenes",font=('Arial',18),command=self.descImg)
        self.buttonDescImg.pack(padx=10,pady=10)




        self.bd2=BaseDatosLvl2() #Inicializamos la base de datos que vamos a conectar y utilizar

        self.root.mainloop()#Iniciamos la aplicación
    ########################################################################################################################################################################

    #Definimos una función que al pulsar el boton actualice los datos
    ########################################################################################################################################################################
    def actualizardatos(self):
        radioerr=0 #numero de archivos repetidos en radio
        skycamerr=0 #numero de archivos repetidos en skycam
        skyscanerr=0 #numero de archivos repetidos en skyscanerr

        try:
           self.bd2.actualizardatos()#Actualizamos los datos
        except "radioerr": # Cuando Devuelve un error de datos repetidos de radio añade uno al contador de radierr
            radioerr=radioerr+1
        except "skycamerr": # Cuando Devuelve un error de datos repetidos de skycamera añade uno al contador de skycamerr
            skycamerr=skycamerr+1
        except "skyscanerr": # Cuando Devuelve un error de datos repetidos de skyscanner añade uno al contador de skyscanerr
            skyscanerr=skyscanerr+1
        mesradio="" #Inicializamos las variable de los mensajes como vacio para que en caso de que no se modifiquen no añadan nada al mensaje final
        messkyscan=""
        messkycam=""
        if (radioerr !=0): #Si ha habido datos repetidos en radio creamos el mensaje
            mesradio="Has intentado introducir {} archivos repetidos en radio\n".format(radioerr)
        if (skycamerr!=0): #Si ha habido datos repetidos en skycamera creamos el mensaje
            messkycam="Has intentado introducir {} archivos repetidos en skycam\n".format(skycamerr)
        if(skyscanerr!=0): #Si ha habido datos repetidos en skyscanner creamos el mensaje
            messkyscan="Has intentado introducir {} archivos repetidos en skyscanner\n".format(skyscanerr)
        mensaje=mesradio+messkycam+messkyscan #Creamos el mensaje completo uniendo todos
        if(mensaje!=""): #Si ha habido algun dato repetido mostramos por pantalla los que haya habido
            messagebox.showinfo(title="Datos repetidos",message=mensaje)#Sacamops por pantalla el mensaje
    ######################################################################################################################################################################

    #Definimos una función para actualizar las imagenes y que devuelva por pantalla si se incluyen imagenes repetidas
    ######################################################################################################################################################################
    def actualizarimagenes(self):

        cont=0 #Contador de excepciones que saltan
        try:
            self.bd2.actualizarImg() #hacer la actualización de las imagenes
        except "imgerr": #Por cada excepción que salga sumara 1 al contador
            cont=cont+1
        if(cont!=0): #Si el contador no es 0 se imprimira por pantalla que ha habido almenos una entrada de imagenes repetida
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)
            messagebox.showinfo(title="Message",message=messkyscan)
    ############################################################################################################################################################################################

    #Definimos una función para descargar datos
    ############################################################################################################################################################################################
    def descDat(self):
        self.bd2.descdat("*","radio","23-12-10","23-12-10")
    ############################################################################################################################################################################################

    #Definimos una función para deascargar las imagenes
    ############################################################################################################################################################################################
    def descImg(self):
        self.bd2.descImg("23-12-29-10","23-12-29-10")

UI()
