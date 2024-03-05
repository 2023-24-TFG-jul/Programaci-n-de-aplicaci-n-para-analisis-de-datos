#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.2.4
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

        self.labeltable=tk.Label(self.root,text="Tabla",font=('Arial',15))# Creamos un titulo para llamar a la aplicación
        self.labeltable.pack(padx=10,pady=10) #Lo colocamos en la pantalla

        self.textboxtable=tk.Text(self.root,font=('Arial',11),height=1)
        self.textboxtable.pack(padx=30,pady=30)
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
        radioerr,skycamerr,skyscanerr=self.bd2.actualizardatos()#Actualizamos los datos
    
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
        else:
            messagebox.showinfo(title="Operación exitosa",message="Has actualizado los datos con exito")#Sacamops por pantalla el mensaje
    ######################################################################################################################################################################

    #Definimos una función para actualizar las imagenes y que devuelva por pantalla si se incluyen imagenes repetidas
    ######################################################################################################################################################################
    def actualizarimagenes(self):

        cont=self.bd2.actualizarImg() #hacer la actualización de las imagenes
        
        if(cont!=0): #Si el contador no es 0 se imprimira por pantalla que ha habido almenos una entrada de imagenes repetida
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)
            messagebox.showinfo(title="Message",message=messkyscan)
    ############################################################################################################################################################################################

    #Definimos una función para descargar datos
    ############################################################################################################################################################################################
    def descDat(self):
        fechaini=self.textboxIni.get('1.0',tk.END)
        fechaini=fechaini.replace('\n','')
        fechafin=self.textboxFin.get('1.0',tk.END)
        fechafin=fechafin.replace('\n','')
        tabla=self.textboxtable.get('1.0',tk.END)
        tabla=tabla.replace('\n','')
        self.bd2.descdat("*",tabla,fechaini,fechafin)
    ############################################################################################################################################################################################

    #Definimos una función para deascargar las imagenes
    ####afs########################################################################################################################################################################################
    def descImg(self):
        self.bd2.descImg(self.textboxIni.get('1.0',tk.END),self.textboxFin.get('1.0',tk.END))

UI()

