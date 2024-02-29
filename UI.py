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
        self.bd2.actualizardatos()

    def actualizarimagenes(self):
        self.bd2.actualizarImg()
        # if self.check_state.get()==0:
        #     print(self.textbox.get('1.0',tk.END))
        # else:
        #     messagebox.showinfo(title="Message",message=self.textbox.get('1.0',tk.END))
    
UI()