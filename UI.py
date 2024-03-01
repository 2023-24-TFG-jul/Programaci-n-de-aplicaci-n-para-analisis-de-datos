#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.0.3
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import tkinter as tk
from BaseDatosLvl2 import BaseDatosLvl2
from tkinter import messagebox


class UI:
    def __init__(self):
        self.root=tk.Tk()
        self.label=tk.Label(self.root,text="Your Messsage",font=('Arial',18))
        self.label.pack(padx=10,pady=10)

        self.check_state=tk.IntVar()
        self.check= tk.Checkbutton(self.root,text="",font=('Arial',16),variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.buttonActDat=tk.Button(self.root,text="Actualizar datos",font=('Arial',18),command=self.actualizardatos)
        self.buttonActDat.pack(padx=10,pady=10)
        self.buttonActImg=tk.Button(self.root,text="Actualizar imagenes",font=('Arial',18),command=self.actualizarimagenes)
        self.buttonActImg.pack(padx=10,pady=10)
        self.bd2=BaseDatosLvl2()    
        self.root.mainloop()
        
    
    def actualizardatos(self):
        radioerr=0
        skycamerr=0
        skyscanerr=0
        try:
           self.bd2.actualizardatos()
        except "radioerr":
            radioerr=radioerr+1
        except "skycamerr":
            skycamerr=skycamerr+1
        except "skyscanerr":
            skyscanerr=skyscanerr+1
        mesradio=""
        messkyscan=""
        messkycam=""
        if (radioerr !=0):
            mesradio="Has intentado introducir {} archivos repetidos en radio\n".format(radioerr)
        if (skycamerr!=0):
            messkycam="Has intentado introducir {} archivos repetidos en skycam\n".format(skycamerr)
        if(skyscanerr!=0):
            messkyscan="Has intentado introducir {} archivos repetidos en skyscanner\n".format(skyscanerr)
        mensaje=mesradio+messkycam+messkyscan
        if(mensaje!=""):
            messagebox.showinfo(title="Datos repetidos",message=mensaje)
            

    def actualizarimagenes(self):
        cont=0
        try:
            self.bd2.actualizarImg()
        except "imgerr":
            cont=cont+1
        if(cont!=0):
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)


        # if self.check_state.get()==0:
        #     print(self.textbox.get('1.0',tk.END))
        # else:
        #     messagebox.showinfo(title="Message",message=self.textbox.get('1.0',tk.END))
    
UI()