#Nombre: Prototipo
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.003
#Descripción: Algo habra que
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd
from BaseDatosLvl1 import BaseDatosLvl1
from BaseDatosLvl2 import BaseDatosLvl2
from psycopg2 import sql
from sqlalchemy import create_engine
##########################################################################################################################
#Parametros de la base de datos
import tkinter as tk
from BaseDatosLvl2 import BaseDatosLvl2

import datetime
tzinfo='2023-10-01 00:00:00'
dato = str(tzinfo)[14:16]
print(dato)
# root=tk.Tk()
# root.geometry("800x500")
# root.title("Acceso base datos")
# label=tk.Label(root,text="Introduzca su usuario", font=('arial',18))
# label.pack(padx=20,pady=20)

# textbox=tk.Text(root,font=('Arial',16),height=1)
# textbox.pack(padx=30,pady=30)

# buttonframe=tk.Frame(root)
# buttonframe.columnconfigure(0,weight=1)
# buttonframe.columnconfigure(1,weight=1)
# buttonframe.columnconfigure(2,weight=1)

# btn1=tk.Button(buttonframe,text="1",font=('Arial',18))
# btn1.grid(row=0,column=0,sticky=tk.W+tk.E)
# btn2=tk.Button(buttonframe,text="2",font=('Arial',18))
# btn2.grid(row=0,column=1,sticky=tk.W+tk.E)
# btn3=tk.Button(buttonframe,text="3",font=('Arial',18))
# btn3.grid(row=0,column=2,sticky=tk.W+tk.E)
# btn4=tk.Button(buttonframe,text="4",font=('Arial',18))
# btn4.grid(row=1,column=0,sticky=tk.W+tk.E)

# btn5=tk.Button(buttonframe,text="5",font=('Arial',18))
# btn5.grid(row=1,column=1,sticky=tk.W+tk.E)

# btn6=tk.Button(buttonframe,text="6",font=('Arial',18))
# btn6.grid(row=1,column=2,sticky=tk.W+tk.E)

# buttonframe.pack(fill='x')

# anotherbutton=tk.Button(root,text="TEST")
# anotherbutton.place(x=200,y=200,height=100,width=100)

# root.mainloop()