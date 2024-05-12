#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.5.0
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import tkinter as tk
import customtkinter as ctk
import psycopg2
import matplotlib.pyplot as plt
import sqlalchemy
from sqlalchemy.exc import DataError
from BaseDatosLvl2 import BaseDatosLvl2
from tkinter import messagebox


#########################################################################################################################
class Page(ctk.CTkFrame):
    def __init__(self, master,titulo):
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self,text=titulo, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)




#Clase con la que el usuario interactuará
class UI(ctk.CTk):

    #Definimos el constructor de la primera pagina de la interfaz de usuario
    #########################################################################################################################
    def __init__(self):
        ctk.CTk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage)
    #########################################################################################################################
    
    #Definimos una función para cambiar de frame
    #########################################################################################################################
    def switch_frame(self, frame_class):
        #Destroys current frame and replaces it with a new one.
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
    #########################################################################################################################
        
#########################################################################################################################
    
#Definimos la clase de log in 
#########################################################################################################################
class LoginPage(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Login Page")
        ctk.CTkButton(self, text="Login",
                  command=lambda: master.switch_frame(MainPage)).pack()
#########################################################################################################################

#Definimos la clase de la pagina principal
#########################################################################################################################        
class MainPage(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Main Page")
        ctk.CTkButton(self, text="Descargas", font=('Arial', 18), command=lambda: master.switch_frame(Descargas)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Actualizaciones", font=('Arial', 18), command=lambda: master.switch_frame(Actualizaciones)).pack(padx=10, pady=10)
#########################################################################################################################

#Definimos la clase de la pagina de descargas
#########################################################################################################################
class Descargas(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Descargas")
        ctk.CTkButton(self, text="Descarga de datos", font=('Arial', 18), command=lambda: master.switch_frame(DescDatos)).pack()
        ctk.CTkButton(self, text="Descarga de imagenes", font=('Arial', 18), command=lambda: master.switch_frame(DescImg)).pack()
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack()
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos
#########################################################################################################################    
class DescDatos(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Descarga de datos")
        ctk.CTkButton(self, text="Radio", font=('Arial', 18), command=lambda:master.switch_frame(DescRadio)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="RadioProc", font=('Arial', 18), command=lambda:master.switch_frame(DescRadioProc)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Skyscanner", font=('Arial', 18), command=lambda:master.switch_frame(DescSkyscanner)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="SkyscannerProc", font=('Arial', 18), command=lambda:master.switch_frame(DescSkyscannerProc)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Skycamera", font=('Arial', 18), command=lambda:master.switch_frame(DescSkyCammera)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="SkycameraProc", font=('Arial', 18), command=lambda:master.switch_frame(DescSkyCammeraProc)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack()
        self.bd2=BaseDatosLvl2()
#########################################################################################################################
class Desc(Page):
    def __init__(self, master,titulo):
        self.bd2=BaseDatosLvl2()
        Page.__init__(self, master,titulo)
        ctk.CTkLabel(self, text="Introduce la fecha de inicio", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxIni = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de inicio YY-MM-DD")
        self.textboxIni.pack()
        ctk.CTkLabel(self, text="Introduce la fecha de fin", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxFin = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de final YY-MM-DD")
        self.textboxFin.pack()

    def get_dates(self):
        self.fechain = self.textboxIni.get().strip()
        self.fechafi = self.textboxFin.get().strip()
    
    def crearPopUp(self,mensaje):
        # Crea una ventana de diálogo
        dialog = ctk.CTkToplevel(self)
        dialog.title("Error")
        dialog.geometry("200x100")

        # Mensaje de error
        label = ctk.CTkLabel(dialog, text=mensaje, wraplength=180)
        label.pack(pady=10)

        # Botón para cerrar el diálogo
        close_button = ctk.CTkButton(dialog, text="Cerrar", command=dialog.destroy)
        close_button.pack()
#TODO: hacer una función que devuelva las fechas pasadas por el usuario, y que lleguen hasta la variación 2
class DescBase(Desc):
    def __init__(self, master,titulo,tabla):
        self.tabla=tabla
        Desc.__init__(self, master,titulo)
        self.bd2=BaseDatosLvl2()
        self.fechaini=""
        self.fechafin=""

   
    ###########################################################################################################################################
      
    
    def descDat(self):
        self.get_dates()
        self.fechaini = self.fechain.replace('\n','')
        self.fechafin = self.fechafi.replace('\n','')
        try:
            self.bd2.descdat("*",self.tabla,self.fechaini,self.fechafin)
        except DataError as e:
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                            """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
        except Exception as e:
            print(e)
            self.crearPopUp("""Ha ocurrido un error inesperado\n {e} \n""")
    ###########################################################################################################################################
class DescVar1(DescBase):
    def __init__(self, master,titulo,tabla):
        self.tabla=tabla
        self.bd2=BaseDatosLvl2()
        DescBase.__init__(self, master,titulo,tabla)
        # Make a check mark to select each possible column in radio
        colum = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
        self.bd2.cur.execute(colum, (tabla,))
        columns = [column[0] for column in self.bd2.cur.fetchall()]
        columElim=["TIMESTAMP","Year","Month","Dia","YearDay","Hour","Minute","date"]
        numcol=[]
        for i in range(len(columns)):
            if columns[i] in columElim:
                numcol.append(i)
        for i in reversed(numcol):
            columns.pop(i)
        # Make a check mark to select each possible column in radio

        num_columns = 4
        self.vars = {column: ctk.BooleanVar() for column in columns}
        for i, column in enumerate(columns):
            if i % num_columns == 0:
                frame = ctk.CTkFrame(self)
                frame.pack(side="top")
            ctk.CTkCheckBox(frame, text=column,variable=self.vars[column], font=('Arial', 12)).pack(side="left")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)

        
    ###########################################################################################################################################

    #Definimos una función para descargar datos
    ###########################################################################################################################################
    def descDat(self):
        self.get_dates()
        self.fechaini = self.fechain.replace('\n','')
        self.fechafin = self.fechafi.replace('\n','')
        checked_columns = [column for column, var in self.vars.items() if var.get()]
        columnas=",".join(checked_columns)
        try:
            self.bd2.descdat(columnas,self.tabla,self.fechaini,self.fechafin)
        except ValueError as e:
            self.crearPopUp("""No has escogido ninguna tabla\n""")
        except DataError as e:
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                                """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
        except Exception as e:
            print(e)
            self.crearPopUp("""Ha ocurrido un error inesperado\n {e} \n""")
    ###########################################################################################################################################
    
class DescVar2(DescVar1):
    def __init__(self, master,titulo,tabla):
        self.tabla=tabla
        self.bd2=BaseDatosLvl2()
        DescVar1.__init__(self, master,titulo,tabla)
        ctk.CTkButton(self, text="Graficar", font=('Arial', 18), command=self.graficar).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack()  
    #Definimos una función para graficar los datos
    ###########################################################################################################################################
    def graficar(self):
        checked_columns = [column for column, var in self.vars.items() if var.get()]
        self.get_dates()
        self.fechaini = self.fechain.replace('\n','')
        self.fechafin = self.fechafi.replace('\n','')
        dataframe=self.bd2.obtenerdat("*",self.tabla,self.fechaini,self.fechafin)
        plt.figure(figsize=(10, 6))  # Create a new figure with custom size
        for column in checked_columns:
            plt.plot(dataframe[column], label=column)  # Plot each column
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph of Columns')
        plt.legend()  # Show legend with column names
        plt.show()  # Display the graph
    ###########################################################################################################################################
#########################################################################################################################
        
#Definimos la clase de la pagina de descarga de datos de la tabla radio
#########################################################################################################################
class DescRadio(DescVar2):

    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescVar2.__init__(self, master,"Tabla Radio","radio")
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla radio procesada
#########################################################################################################################
class DescRadioProc(DescVar2):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescVar2.__init__(self, master,"Tabla RadioProc","radioproc")
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skyscanner
#############################################################################################################################################
class DescSkyscanner(DescBase):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescBase.__init__(self, master,"Tabla Skyscanner","skyscanner")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack()
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skyscanner procesada
###########################################################################################################################################
class DescSkyscannerProc(DescBase):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescBase.__init__(self, master,"Tabla SkyScannerProc","skyscannerproc")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack()
    ###########################################################################################################################################
#########################################################################################################################
            
#Definimos la clase de la pagina de descarga de datos de la tabla skycamera
###########################################################################################################################################
class DescSkyCammera(DescVar1):

    def __init__(self, master):
        DescVar1.__init__(self, master,"Tabla Skycamera","skycamera")
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack()
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skycamera procesada
###########################################################################################################################################
class DescSkyCammeraProc(DescVar2):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescVar2.__init__(self, master,"Tabla SkyCameraProc","skycameraproc")
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de imagenes
#########################################################################################################################
class DescImg(Desc):
    #Definimos el constructor de la clase
    ########################################################################################################################################
    def __init__(self, master):
        Desc.__init__(self, master,"Descarga de imagenes")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descImg).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack()
        self.bd2=BaseDatosLvl2()
    ########################################################################################################################################
        
    #Definimos una función para deascargar las imagenes
    ########################################################################################################################################
    def descImg(self):
        try:
            self.bd2.descImg(self.textboxIni.get('1.0',tk.END),self.textboxFin.get('1.0',tk.END))
        except psycopg2.errors.SyntaxError:
            self.crearPopUp("Has introducido mal las fechas\n Recuerda introducir las fechas en formato 'YY-MM-DD-HH'")
    ########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de actualizaciones
#########################################################################################################################
class Actualizaciones(ctk.CTkFrame):
    #Definimos el constructor de la clase
    ########################################################################################################################################
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self, font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        ctk.CTkButton(self, text="Actualizar datos", font=('Arial', 18), command=self.actualizardatos).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Actualizar imagenes", font=('Arial', 18), command=self.actualizarimagenes).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack()    
        self.bd2=BaseDatosLvl2() 
    ########################################################################################################################################

    #Definimos una función para crear un pop up
    ########################################################################################################################################
    def crearPopUp(self,mensaje):
        # Crea una ventana de diálogo
        dialog = ctk.CTkToplevel(self)
        dialog.title("Error")
        dialog.geometry("200x100")

        # Mensaje de error
        label = ctk.CTkLabel(dialog, text=mensaje, wraplength=180)
        label.pack(pady=10)

        # Botón para cerrar el diálogo
        close_button = ctk.CTkButton(dialog, text="Cerrar", command=dialog.destroy)
        close_button.pack()
    ########################################################################################################################################    

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
           self.crearPopUp(mensaje)#Sacamops por pantalla el mensaje
        else:
            self.crearPopUp("Has actualizado los datos con exito")#Sacamops por pantalla el mensaje
    ##########################################################################################################################################

    #Definimos una función para actualizar las imagenes y que devuelva por pantalla si se incluyen imagenes repetidas
    ##########################################################################################################################################
    def actualizarimagenes(self):

        cont=self.bd2.actualizarImg() #hacer la actualización de las imagenes
        
        if (cont!=0): #Si el contador no es 0 se imprimira por pantalla que ha habido almenos una entrada de imagenes repetida
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)
            self.crearPopUp(messkyscan)
        else:
            #Sacamos por pantalla el mensaje de que se han actualizado las imagenes con exito
            self.crearPopUp("Has actualizado todas las imagenes con exito")
    ###########################################################################################################################################
#########################################################################################################################

#Ejecutamos la interfaz de usuario     
#########################################################################################################################   
if __name__ == "__main__":
    app = UI()
    app.mainloop()
#########################################################################################################################