#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.0.2
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

        self.textbox=tk.Text(self.root,font=('Arial',16))
        self.textbox.pack(padx=10,pady=10)

        self.check_state=tk.IntVar()
        self.check= tk.Checkbutton(self.root,text="Show Messagebox",font=('Arial',16),variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button=tk.Button(self.root,text="Show Message",font=('Arial',18),command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get()==0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="Message",message=self.textbox.get('1.0',tk.END))
    
UI()