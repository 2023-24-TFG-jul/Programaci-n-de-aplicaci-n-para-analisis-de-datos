#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.7.6
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import customtkinter as ctk
import psycopg2
import matplotlib.pyplot as plt
from sqlalchemy.exc import DataError
from BaseDatosLvl2 import BaseDatosLvl2
import numpy as np
from AnalisisIA import AnalisisIA
from Log import Log
#########################################################################################################################
#Inicializamos una clase generica de la que heredaran todas las paginas
class Page(ctk.CTkFrame):
    def __init__(self, master,titulo):
        self.log=Log()
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self,text=titulo, font=('Helvetica', 30, "bold")).pack(side="top", fill="x", pady=5) #Creamos un label con el titulo de la pagina
        if(titulo!="Login Page"): #Si no es la pagina de login creamos un boton para cerrar sesion
            logout_button = ctk.CTkButton(self, text="Cerrar Sesion",fg_color="#8B0000", hover_color="#A52A2A", font=('Arial', 18),command=lambda: master.switch_frame(LoginPage))
            logout_button.place(relx=0.99, rely=0.01, anchor='ne')
    #Definimos una función generica que notificara al usuario de lo que se quiera
    def crearPopUp(self,mensaje):
        # Crea una ventana de diálogo
        dialog = ctk.CTkToplevel(self)
        dialog.title("Notificación") #Ponemos titulo a la ventana
        dialog.geometry("300x150") #Ponemos un tamaño a la ventana
        dialog.attributes('-topmost', True)  # Esta línea hace que la ventana emergente permanezca en primer plano
        # Bloquea la interacción con la ventana de la que proviene
        dialog.grab_set()
        # Mensaje de notificación
        label = ctk.CTkLabel(dialog, text=mensaje, wraplength=180)
        label.pack(pady=10)
        # Botón para cerrar el diálogo
        close_button = ctk.CTkButton(dialog, text="Cerrar", command=dialog.destroy)
        close_button.pack()



#Clase con la que el usuario interactuará
class UI(ctk.CTk):

    #Definimos el constructor de la primera pagina de la interfaz de usuario
    #########################################################################################################################
    def __init__(self):
        ctk.CTk.__init__(self)
        self._frame = None
        self.switch_frame(LoginPage) #Empezamos en la pagina de login
        self.overrideredirect(False)  # Esto asegura que la barra de título y los controles de la ventana sigan visibles
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()-70))

    #########################################################################################################################
    
    #Definimos una función para cambiar de frame
    #########################################################################################################################
    def switch_frame(self, frame_class):
        #destruye el frame actual y crea uno nuevo de la pagina que se le pase
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, fill='both')
    #########################################################################################################################
        
#########################################################################################################################
    
#Definimos la clase de log in
#########################################################################################################################
class LoginPage(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Login Page")
        self.user=ctk.CTkEntry(self, height=1, width=200,placeholder_text="Usuario")# caja de texto para el usuario
        self.user.pack(padx=10, pady=10)
        self.password=ctk.CTkEntry(self, height=1, width=200,placeholder_text="Contraseña",show="*") # caja de texto para la contraseña
        self.password.pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Login",font=('Arial', 18),command=lambda: self.login(master)).pack(padx=10, pady=10) #Boton para logearse
        self.user.bind("<Return>", self.login_event) #Si se pulsa enter se logea en el usuario
        self.password.bind("<Return>", self.login_event) #Si se pulsa enter se logea en la pasword
    #########################################################################################################################

    #Definimos una función para logearse
    #########################################################################################################################
    def login(self,master):
        user=self.user.get() #Obtenemos el usuario
        password=self.password.get() #Obtenemos la contraseña
        if user=="admin" and password=="admin": #Si el usuario y la contraseña son admin se logea
            master.switch_frame(MainPage)
        else:
            self.crearPopUp("Usuario o contraseña incorrectos") #Si no se logea se crea un pop up
    #########################################################################################################################

    #Definimos una función para logearse al pulsar enter
    #########################################################################################################################
    def login_event(self, event): 
        self.login(self.master)
#########################################################################################################################

#Definimos la clase de la pagina principal
#########################################################################################################################
class MainPage(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Main Page") #Inicializamos la Main page
        #Creamos los botones de la pagina principal
        #Boton de descargas
        ctk.CTkButton(self, text="Descargas", font=('Arial', 18),width=190, command=lambda: master.switch_frame(Descargas)).pack(padx=10, pady=10)
        #Boton de analisis de los datos
        ctk.CTkButton(self, text="Analisis de los datos",font=('Arial', 18),width=190, command=lambda: master.switch_frame(Analisis)).pack(padx=10, pady=10)
        #Boton de actualizaciones
        ctk.CTkButton(self, text="Actualizaciones", font=('Arial', 18),width=190, command=lambda: master.switch_frame(Actualizaciones)).pack(padx=10, pady=10)
#########################################################################################################################

#Definimos la clase de la pagina de descargas
#########################################################################################################################
class Descargas(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Descargas") #Inicializamos la pagina de descargas
        #Creamos los botones de la pagina de descargas
        #Boton de descarga de datos
        ctk.CTkButton(self, text="Descarga de datos", font=('Arial', 18),width=210, command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)
        #Boton de descarga de imagenes
        ctk.CTkButton(self, text="Descarga de imagenes", font=('Arial', 18),width=210, command=lambda: master.switch_frame(DescImg)).pack(padx=10, pady=10)
        #Boton de para volver a la pagina principal
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=160,command=lambda: master.switch_frame(MainPage),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos
#########################################################################################################################
class DescDatos(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Descarga de datos") #Inicializamos la pagina de descarga de datos
        #Creamos los botones de la pagina de descarga de datos
        #Boton de descarga de datos de la tabla radio
        ctk.CTkButton(self, text="Radio", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescRadio)).pack(padx=10, pady=10)
        #Boton de descarga de datos de la tabla radio procesada
        ctk.CTkButton(self, text="RadioProc", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescRadioProc)).pack(padx=10, pady=10)
        #Boton de descarga de datos de la tabla skyscanner
        ctk.CTkButton(self, text="Skyscanner", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescSkyscanner)).pack(padx=10, pady=10)
        #Boton de descarga de datos de la tabla skyscanner procesada
        ctk.CTkButton(self, text="SkyscannerProc", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescSkyscannerProc)).pack(padx=10, pady=10)
        #Boton de descarga de datos de la tabla skycamera
        ctk.CTkButton(self, text="Skycamera", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescSkyCammera)).pack(padx=10, pady=10)
        #Boton de descarga de datos de la tabla skycamera procesada
        ctk.CTkButton(self, text="SkycameraProc", font=('Arial', 18),width=200, command=lambda:master.switch_frame(DescSkyCammeraProc)).pack(padx=10, pady=10)
        #Boton de volver a la pagina de descargas
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=150,command=lambda: master.switch_frame(Descargas),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
#########################################################################################################################

#Definimos la clase generica de descarga que el resto de páginas de descargas heredarán
#########################################################################################################################
class Desc(Page):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master,titulo):
        self.bd2=BaseDatosLvl2() #Inicializamos la conexion con la base de datos
        Page.__init__(self, master,titulo) #Inicializamos la pagina con el titulo que se le pase
        #Creamos los campos de texto para introducir las fechas
        #Fecha de inicio
        ctk.CTkLabel(self, text="Introduce la fecha de inicio", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxIni = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de inicio YY-MM-DD")
        self.textboxIni.pack(padx=10, pady=10)
        #Fecha de fin
        ctk.CTkLabel(self, text="Introduce la fecha de fin", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxFin = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de final YY-MM-DD")
        self.textboxFin.pack(padx=10, pady=10)
    #########################################################################################################################

    #Definimos una función para obtener las fechas introducidas por el usuario
    #########################################################################################################################
    def get_dates(self):
        self.fechain = self.textboxIni.get().strip()
        self.fechafi = self.textboxFin.get().strip()
    #########################################################################################################################
#########################################################################################################################

#Definimos la clase que permite realizar la primera descarga de datos sin graficar ni seleccionar columnas
#########################################################################################################################
class DescBase(Desc):
    #Definimos el constructor de la clase
    #########################################################################################################################
    def __init__(self, master,titulo,tabla):
        self.tabla=tabla #Guardamos la tabla de la que se van a descargar los datos
        Desc.__init__(self, master,titulo) #Inicializamos la pagina de con el titulo que se pase	
        self.bd2=BaseDatosLvl2() #Inicializamos la conexion con la base de datos
        self.fechaini="" #Inicializamos la fecha de inicio
        self.fechafin="" #Inicializamos la fecha de fin
    #########################################################################################################################
    
    #Definimos una función para descargar los datos
    ###########################################################################################################################################
    def descDat(self):
        self.get_dates() #Obtenemos las fechas introducidas por el usuario
        self.fechaini = self.fechain.replace('\n','') #Guardamos la fecha de inicio en un formato adecuado
        self.fechafin = self.fechafi.replace('\n','') #Guardamos la fecha de fin en un formato adecuado
        try: #Intentamos descargar los datos
            self.bd2.descdat("*",self.tabla,self.fechaini,self.fechafin) #Descargamos los datos
        except DataError as error: #Si no se interoducen fechas se crea un pop up expresandolo
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                            """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
            self.log.injeErr(error) #Guardamos el error en el log
        except Exception as error: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("""Ha ocurrido un error inesperado\n {error} \n""")
            self.log.injeErr(error) #Guardamos el error en el log
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de descarga que permite esciger variables y descargarlos
#########################################################################################################################
class DescVar1(DescBase):
    columnas={} #Inicializamos las columnas que se pueden descargar
    columnasres=[] #Inicializamos las columnas que se van a descargar

    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master,titulo,tabla,columnas):
        self.tabla=tabla #Guardamos la tabla de la que se van a descargar los datos
        self.bd2=BaseDatosLvl2() #Inicializamos la conexion con la base de datos
        DescBase.__init__(self, master,titulo,tabla) #Inicializamos la pagina de descarga con el titulo y la tabla que se le pase
        self.columnas=columnas #Guardamos las columnas que se pueden descargar
        if columnas.get("Titulo")=="SkyCamera": #Si la tabla es la de la camara del cielo no hace falta un menu de opciones
            columns=columnas.get("Columnas").keys()  #Obtenemos las columnas que se pueden descargar
            self.vars = {column: ctk.BooleanVar() for column in columns} #Creamos un diccionario con las columnas que se pueden descargar
            frame = ctk.CTkFrame(self) #Creamos un frame para poner los checkboxes
            for i, column in enumerate(columns): #Creamos un checkbox para cada columna
                #Creamos el checkbox
                checkbox=ctk.CTkCheckBox(frame, text=column,variable=self.vars[column],width=250, font=('Arial', 12)) 
                checkbox.grid(row=i, column=1, padx=10, pady=10)
            frame.place(relx=0.5, rely=0.60, anchor='center')
            #Creamos un boton para descargar los datos
            ctk.CTkButton(self, text="Descargar", font=('Arial', 18),width=200, command=self.descDat).place(relx=0.8, rely=0.46, anchor='center')
        else: #Si no es la camara del cielo se crea un menu de opciones para escoger las columnas
            columns=columnas.get("Columnas") #Obtenemos las columnas que se pueden descargar
            #Creamos un menu de opciones para escoger las columnas
            self.option_menu = ctk.CTkOptionMenu(self, values=["Irradiancia", "Iluminancia", "Par", "UV","Miscelanea"], command=self.update_checkboxes) 
            self.option_menu.pack(padx=10, pady=10)
            self.checkboxes_frame = ctk.CTkFrame(self) #Creamos un frame para poner los checkboxes
            self.checkboxes_frame.pack(fill="both", expand=True) 
            self.checkbox_vars = {} #Inicializamos las variables de los checkboxes
            self.update_checkboxes("Irradiancia") #Inicializamos los checkboxes con las columnas de la irradiancia
            #Creamos un boton para descargar los datos
            ctk.CTkButton(self, text="Descargar", font=('Arial', 18),width=200, command=self.descDat).place(relx=0.8, rely=0.46, anchor='center')
    ###########################################################################################################################################

    #Definimos una función para descargar datos
    ###########################################################################################################################################
    def descDat(self):
        self.get_dates() #Obtenemos las fechas introducidas por el usuario
        self.fechaini = self.fechain.replace('\n','') #Guardamos la fecha de inicio en un formato adecuado
        self.fechafin = self.fechafi.replace('\n','') #Guardamos la fecha de fin en un formato adecuado
        
        columnasres=[] #Inicializamos las columnas que se van a descargar
        #Si el numero de columnas es 5 significa que es la tabla de radio por lo que hay que comprobar el menu de opciones
        if len(self.columnas.get("Columnas")) ==5: 
            self.update_checkboxes(self.option_menu.get()) #Actualizamos los checkboxes para guardar los seleccionados
            for col in self.columnasres: #Guardamos las columnas seleccionadas
                index=self.columnas.get("Columnas")
                for key in index.keys():
                    if col in index.get(key).keys():
                        columnasres.append(index.get(key).get(col))
        else:# si no es la tabla de radio se comprueban los checkboxes directamente
            #Guardamos las columnas seleccionadas
            checked_columns = [column for column, var in self.vars.items() if var.get()] 
            for col in checked_columns: 
                columnasres.append(self.columnas.get("Columnas").get(col))
        #Guardamos las columnas en un formato adecuado para poderlas pasar a la base de datos
        columna=",".join(columnasres)
        try:#Intentamos descargar los datos
            self.bd2.descdat(columna,self.tabla,self.fechaini,self.fechafin)
        except ValueError as error: #Si no se escoge variable se crea un pop up expresandolo
            self.crearPopUp("""No has escogido ninguna variable\n""")
            self.log.injeErr(error) #Guardamos el error en el log
        except DataError as error: #Si las fechas no estan en el formato adecuado se crea un pop up expresandolo
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                                """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
            self.log.injeErr(error) #Guardamos el error en el log
        except Exception as error: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("""Ha ocurrido un error inesperado\n {error} \n""")
            self.log.injeErr(error) #Guardamos el error en el log
    ###########################################################################################################################################

    #Definimos una función para actualizar los checkboxes
    ###########################################################################################################################################
    def update_checkboxes(self, choice):
        #Limpiamos los checkboxes
        for widget in self.checkboxes_frame.winfo_children():
            if widget.cget("text") in self.columnasres:
                 if(not widget.get()):
                     self.columnasres.remove(widget.cget("text"))
            else:
                if(widget.get()):
                    self.columnasres.append(widget.cget("text"))
            widget.destroy()
        # Opciones para la elección de las variables
        options =self.columnas.get("Columnas")
        # Creamos las checkboxes en realcion a la elección
        self.checkbox_vars[choice] = []
        options_keys = options.get(choice, []).keys() #Obtenemos las variables que se pueden escoger
        for i, option in enumerate(options_keys): #Creamos un checkbox para cada variable
            var = ctk.BooleanVar()
            if(option in self.columnasres):
                var.set(True)
            checkbox = ctk.CTkCheckBox(self.checkboxes_frame, text=option,width=300, variable=var)
            #Establecemos la posición de los checkboxes en relación a cuantos hay
            row = i % 10
            column = i // 10
            checkbox.grid(row=row, column=column, padx=10, pady=10)
            self.checkbox_vars[choice].append((checkbox, var))

        #Centramos la posición de los checkboxes
        self.checkboxes_frame.place(relx=0.5, rely=0.65, anchor='center')
    ###########################################################################################################################################
 #########################################################################################################################

#Definimos la clase de decscarga que permite escoger variables y graficarlas
# #########################################################################################################################   
class DescVar2(DescVar1):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master,titulo,tabla,columnas):
        self.tabla=tabla
        self.bd2=BaseDatosLvl2()
        DescVar1.__init__(self, master,titulo,tabla,columnas)
        ctk.CTkButton(self, text="Graficar", font=('Arial', 18),width=200, command=self.graficar).place(relx=0.8, rely=0.5, anchor='center')
        ctk.CTkButton(self, text="Atras",font=('Arial', 18),width=150, command=lambda: master.switch_frame(DescDatos),fg_color="#1E3A8A", hover_color="#1E40AF").place(relx=0.8, rely=0.54, anchor='center')
    ###########################################################################################################################################

    #Definimos una función para graficar los datos
    ###########################################################################################################################################
    def graficar(self):
        self.get_dates() #Obtenemos las fechas introducidas por el usuario
        self.fechaini = self.fechain.replace('\n','') #Guardamos la fecha de inicio en un formato adecuado
        self.fechafin = self.fechafi.replace('\n','') #Guardamos la fecha de fin en un formato adecuado
        
        columnasres=[] #Inicializamos las columnas que se van a descargar
        #Si el numero de columnas es 5 significa que es la tabla de radio por lo que hay que comprobar el menu de opciones
        if len(self.columnas.get("Columnas")) ==5: 
            self.update_checkboxes(self.option_menu.get()) #Actualizamos los checkboxes para guardar los seleccionados
            for col in self.columnasres: #Guardamos las columnas seleccionadas
                index=self.columnas.get("Columnas") #Obtenemos las columnas que se pueden obtener
                for key in index.keys(): #Guardamos las columnas seleccionadas
                    if col in index.get(key).keys(): 
                        columnasres.append(index.get(key).get(col))
            time="TIMESTAMP" #Ponemos el tiempo que se usara en el grafico
        else: # si no es la tabla de radio se comprueban los checkboxes directamente
            checked_columns = [column for column, var in self.vars.items() if var.get()] #Guardamos las columnas seleccionadas
            for col in checked_columns:
                columnasres.append(self.columnas.get("Columnas").get(col))
            time="time" #Ponemos el tiempo que se usara en el grafico 
        try:  #Intentamos obtener los datos
            dataframe=self.bd2.obtenerdat("*",self.tabla,self.fechaini,self.fechafin) #Obtenemos los datos
        except ValueError as e: #Si no se escoge variable se crea un pop up expresandolo
            self.crearPopUp("""No has escogido ninguna tabla\n""")
            self.log.injeErr(e)  #Guardamos el error en el log
        except DataError as e: #Si las fechas no estan en el formato adecuado se crea un pop up expresandolo
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                                """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
            self.log.injeErr(e) #Guardamos el error en el log
        except Exception as e: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("""Ha ocurrido un error inesperado\n {e} \n""")
            self.log.injeErr(e) #Guardamos el error en el log
        plt.figure(figsize=(10, 6)) #Creamos la figura del grafico
        for column in columnasres: #Graficamos las columnas seleccionadas
            plt.plot(dataframe[time],dataframe[column], label=column) #Graficamos la columna con el tiempo
        plt.xlabel('Fecha') #Ponemos la etiqueta del eje x
        plt.xticks(np.arange(0, len(dataframe[time]), step=len(dataframe[time])/10)) #Ponemos las etiquetas del eje x
        plt.title('Grafica de los datos de la tabla '+self.tabla) #Ponemos el titulo del grafico
        plt.legend()
        plt.draw() #Dibujamos el grafico
        labels = [item.get_text() for item in plt.gca().get_xticklabels()] #Obtenemos las etiquetas del eje x
        labels = [label[2:10] for label in labels] #Ponemos las etiquetas del eje x en un formato adecuado
        plt.gca().set_xticklabels(labels) 
        plt.show()
    ###########################################################################################################################################
#########################################################################################################################
        
#Definimos la clase de la pagina de descarga de datos de la tabla radio
#########################################################################################################################
class DescRadio(DescVar2):

    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        #Definimos las variables que se pueden descargar de cada tipo
        varIr={"Global vertical irradiance North":"BuRaGVN_Avg","Global vertical irradiance South":"BuRaGVS_Avg","Global vertical irradiance East ":"BuRaGVE_Avg",
               "Global vertical irradiance West ":"BuRaGVW_Avg","Global horizontal irradiance":"BuRaGH_Avg","Diffuse horizontal irradiance":"BuRaDH_Avg",
               "Direct normal irradiance":"BuRaB_Avg","Diffuse vertical irradiance North":"BuRaDVN_Avg","Diffuse vertical irradiance South":"BuRaDVS_Avg",
               "Diffuse vertical irradiance East":"BuRaDVE_Avg","Diffuse vertical irradiance West":"BuRaDVW_Avg","Irradiancia del albedómetro Up":"BuRaAlUp_Avg",
               "Irradiancia del albedómetro Down":"BuRaAlDo_Avg","Alb - Albedo":"BuRaAlbe_Avg"}
        varIl={"Global vertical illuminance North":"BuLxGVN_Avg","Global vertical illuminance South":"BuLxGVS_Avg","Global vertical illuminance East":"BuLxGVE_Avg","Global vertical illuminance West":"BuLxGVW_Avg",
               "Global horizontal illuminance":"BuLxGH_Avg","Diffuse horizontal illuminance":"BuLxDH_Avg","Direct normal illuminance":"BuLxB_Avg","Illuminancia reflejada":"BuLxR_Avg"}
        varmisc={"Temperature":"BuTemp_Avg","Relative humidity":"BuRH_Avg","Pressure":"BuPres_Avg","Wind speed":"BuWS_Avg","Wind direction":"BuWD_Avg","Pluv cantidad de lluvia":"BuRain_Tot"}
        varPar={"Global vertical PAR North":"BuPaGVN_Avg","Global vertical PAR South":"BuPaGVS_Avg","Global vertical PAR East":"BuPaGVE_Avg","Global vertical PAR West":"BuPaGVW_Avg",
                "Global horizontal PAR irradiance":"BuPaGH_Avg","Diffuse horizontal PAR irradiance":"BuPaDH_Avg","Direct normal PAR irradiance":"BuPaB_Avg","PAR reflejada":"BuPaR_Avg"}
        varUv={"Global vertical UV North":"BuUvGVN_Avg","Global vertical UV South":"BuUvGVS_Avg","Global vertical UV East":"BuUvGVE_Avg","Global vertical UV West":"BuUvGVW_Avg",
               "Global horizontal UV irradiance":"BuUvGH_Avg","Diffuse horizontal UV irradiance":"BuUvDH_Avg","Direct normal UV irradiance":"BuUvB_Avg","Ultravioleta A global horizontal":"BuUvAGH_Avg",
               "Ultravioleta A difusa horizontal":"BuUvADH_Avg","Ultravioleta A global vertical sur":"BuUvAV_Avg","Ultravioleta B global horizontal":"BuUvBGH_Avg","Ultravioleta B difusa horizontal":"BuUvBDH_Avg",
               "Ultravioleta B global vertical sur":"BuUvBV_Avg","Ultravioleta E global horizontal":"BuUvEGH_Avg","Ultravioleta E difusa horizontal":"BuUvEDH_Avg","Ultravioleta E global vertical sur":"BuUvEV_Avg"}
        columnas={"Titulo":"Radio","Columnas":{"Irradiancia":varIr,"Iluminancia":varIl,"Par":varPar,"UV":varUv,"Miscelanea":varmisc}}
        DescVar2.__init__(self, master,"Tabla Radio","radio",columnas)
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla radio procesada
#########################################################################################################################
class DescRadioProc(DescVar2):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        #Definimos las variables que se pueden descargar de cada tipo
        varIr={"Global vertical irradiance North":"BuRaGVN_Avg","Global vertical irradiance South":"BuRaGVS_Avg","Global vertical irradiance East ":"BuRaGVE_Avg",
               "Global vertical irradiance West ":"BuRaGVW_Avg","Global horizontal irradiance":"BuRaGH_Avg","Diffuse horizontal irradiance":"BuRaDH_Avg",
               "Direct normal irradiance":"BuRaB_Avg","Diffuse vertical irradiance North":"BuRaDVN_Avg","Diffuse vertical irradiance South":"BuRaDVS_Avg",
               "Diffuse vertical irradiance East":"BuRaDVE_Avg","Diffuse vertical irradiance West":"BuRaDVW_Avg","Irradiancia del albedómetro Up":"BuRaAlUp_Avg",
               "Irradiancia del albedómetro Down":"BuRaAlDo_Avg","Alb - Albedo":"BuRaAlbe_Avg"}
        varIl={"Global vertical illuminance North":"BuLxGVN_Avg","Global vertical illuminance South":"BuLxGVS_Avg","Global vertical illuminance East":"BuLxGVE_Avg","Global vertical illuminance West":"BuLxGVW_Avg",
               "Global horizontal illuminance":"BuLxGH_Avg","Diffuse horizontal illuminance":"BuLxDH_Avg","Direct normal illuminance":"BuLxB_Avg","Illuminancia reflejada":"BuLxR_Avg"}
        varmisc={"Temperature":"BuTemp_Avg","Relative humidity":"BuRH_Avg","Pressure":"BuPres_Avg","Wind speed":"BuWS_Avg","Wind direction":"BuWD_Avg","Pluv cantidad de lluvia":"BuRain_Tot","Fallo":"fallo"}
        varPar={"Global vertical PAR North":"BuPaGVN_Avg","Global vertical PAR South":"BuPaGVS_Avg","Global vertical PAR East":"BuPaGVE_Avg","Global vertical PAR West":"BuPaGVW_Avg",
                "Global horizontal PAR irradiance":"BuPaGH_Avg","Diffuse horizontal PAR irradiance":"BuPaDH_Avg","Direct normal PAR irradiance":"BuPaB_Avg","PAR reflejada":"BuPaR_Avg"}
        varUv={"Global vertical UV North":"BuUvGVN_Avg","Global vertical UV South":"BuUvGVS_Avg","Global vertical UV East":"BuUvGVE_Avg","Global vertical UV West":"BuUvGVW_Avg",
               "Global horizontal UV irradiance":"BuUvGH_Avg","Diffuse horizontal UV irradiance":"BuUvDH_Avg","Direct normal UV irradiance":"BuUvB_Avg","Ultravioleta A global horizontal":"BuUvAGH_Avg",
               "Ultravioleta A difusa horizontal":"BuUvADH_Avg","Ultravioleta A global vertical sur":"BuUvAV_Avg","Ultravioleta B global horizontal":"BuUvBGH_Avg","Ultravioleta B difusa horizontal":"BuUvBDH_Avg",
               "Ultravioleta B global vertical sur":"BuUvBV_Avg","Ultravioleta E global horizontal":"BuUvEGH_Avg","Ultravioleta E difusa horizontal":"BuUvEDH_Avg","Ultravioleta E global vertical sur":"BuUvEV_Avg"}
        columnas={"Titulo":"Radio","Columnas":{"Irradiancia":varIr,"Iluminancia":varIl,"Par":varPar,"UV":varUv,"Miscelanea":varmisc}}
        DescVar2.__init__(self, master,"Tabla RadioProc","radioproc",columnas)
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skyscanner
#############################################################################################################################################
class DescSkyscanner(DescBase):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescBase.__init__(self, master,"Tabla Skyscanner","skyscanner")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18),width=200, command=self.descDat).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=150,command=lambda: master.switch_frame(DescDatos),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skyscanner procesada
###########################################################################################################################################
class DescSkyscannerProc(DescBase):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        DescBase.__init__(self, master,"Tabla SkyScannerProc","skyscannerproc")
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18),width=200, command=self.descDat).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=150,command=lambda: master.switch_frame(DescDatos),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
    ###########################################################################################################################################
#########################################################################################################################
            
#Definimos la clase de la pagina de descarga de datos de la tabla skycamera
###########################################################################################################################################
class DescSkyCammera(DescVar1):

    def __init__(self, master):
        columnas={"Titulo":"SkyCamera","Columnas":{"Azimuth":"azimuth","Bloqueado":"blocked","Covertura de nubes":"cloud_cover",
                    "Mensaje de covertura de nubes":"cloud_cover_msg","Imagen de covertura de nubes":"cloudimg","Polvo":"dust",
                    "Elevación":"elevation","Imagen":"image","Modo":"mode","Temperatura":"temperature"}}
        DescVar1.__init__(self, master,"Tabla Skycamera","skycamera",columnas)
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=150,command=lambda: master.switch_frame(DescDatos),fg_color="#1E3A8A", hover_color="#1E40AF").place(relx=0.8, rely=0.50, anchor='center')
    ###########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de descarga de datos de la tabla skycamera procesada
###########################################################################################################################################
class DescSkyCammeraProc(DescVar2):
    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        columnas={"Titulo":"SkyCamera","Columnas":{"Azimuth":"azimuth","Bloqueado":"blocked","Covertura de nubes":"cloud_cover",
                    "Mensaje de covertura de nubes":"cloud_cover_msg","Imagen de covertura de nubes":"cloudimg","Polvo":"dust",
                    "Elevación":"elevation","Imagen":"image","Modo":"mode","Temperatura":"temperature"}}
        DescVar2.__init__(self, master,"Tabla SkyCameraProc","skycameraproc",columnas)
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
        ctk.CTkButton(self, text="Atras", font=('Arial', 18), command=lambda: master.switch_frame(Descargas),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
        self.bd2=BaseDatosLvl2()
    ########################################################################################################################################
        
    #Definimos una función para deascargar las imagenes
    ########################################################################################################################################
    def descImg(self): 
        self.get_dates() #Obtenemos las fechas introducidas por el usuario
        self.fechaini = self.fechain.replace('\n','') #Guardamos la fecha de inicio en un formato adecuado
        self.fechafin = self.fechafi.replace('\n','') #Guardamos la fecha de fin en un formato adecuado
        try: #Intentamos descargar las imagenes
            self.bd2.descImg(self.fechaini,self.fechafin) #Descargamos las imagenes
        except psycopg2.errors.SyntaxError as error: #Si no se introducen fechas se crea un pop up expresandolo
            self.crearPopUp("Has introducido mal las fechas\n Recuerda introducir las fechas en formato 'YY-MM-DD-HH'")
            self.log.injeErr(error) #Guardamos el error en el log
        except psycopg2.errors.InvalidTextRepresentation as error: #Si las fechas no estan en el formato adecuado se crea un pop up expresandolo
            self.crearPopUp("No has introducido ninguna fecha")
            self.log.injeErr(error) #Guardamos el error en el log
        except Exception as error: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("Ha ocurrido un error inesperado\n {}".format(error))
            self.log.injeErr(error) #Guardamos el error en el log
    ########################################################################################################################################
#########################################################################################################################

#Definimos la clase de la pagina de actualizaciones
#########################################################################################################################
class Actualizaciones(Page):
    #Definimos el constructor de la clase
    ########################################################################################################################################
    def __init__(self, master):
        Page.__init__(self, master,"Actualizaciones") #Inicializamos la pagina con el titulo de actualizaciones
        #Creamos los botones para actualizar los datos y las imagenes
        ctk.CTkButton(self, text="Actualizar datos", font=('Arial', 18),width=200, command=self.actualizardatos).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Actualizar imáAcgenes", font=('Arial', 18),width=200, command=self.actualizarimagenes).pack(padx=10, pady=10)
        #Creamos un boton para volver a la pagina principal
        ctk.CTkButton(self, text="Atras", font=('Arial', 18),width=150,command=lambda: master.switch_frame(MainPage),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
        self.bd2=BaseDatosLvl2()
    ########################################################################################################################################

    #Definimos una función para crear un pop up
    ########################################################################################################################################
    def crearPopUpVer2(self,mensaje,titulo):
        # Crea una ventana de diálogo
        dialog = ctk.CTkToplevel(self)
        dialog.title(titulo)
        dialog.geometry("200x200")
        dialog.attributes('-topmost', True)  # Esta línea hace que la ventana emergente permanezca en primer plano
        # Bloquea la interacción con la ventana de la que proviene
        dialog.grab_set()
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
           self.crearPopUpVer2(mensaje,"Error")#Sacamops por pantalla el mensaje
        else:
            self.crearPopUpVer2("Has actualizado los datos con exito","Existo")#Sacamops por pantalla el mensaje
    ##########################################################################################################################################

    #Definimos una función para actualizar las imagenes y que devuelva por pantalla si se incluyen imagenes repetidas
    ##########################################################################################################################################
    def actualizarimagenes(self):

        cont=self.bd2.actualizarImg() #hacer la actualización de las imagenes
        
        if (cont!=0): #Si el contador no es 0 se imprimira por pantalla que ha habido almenos una entrada de imagenes repetida
            messkyscan="Has intentado introducir {} imagenes repetidas en imagenes\n".format(cont)
            self.crearPopUpVer2(messkyscan,"Error")
        else:
            #Sacamos por pantalla el mensaje de que se han actualizado las imagenes con exito
            self.crearPopUpVer2("Has actualizado todas las imagenes con exito","Existo")
    ###########################################################################################################################################
#########################################################################################################################
class Analisis(Page):
    def __init__(self, master):
        self.analisis=AnalisisIA() #Inicializamos la clase de analisis
        Page.__init__(self, master,"Análisis de los datos") # Inicializamos la pagina con el titulo de analisis de los datos
        #Creamos los botones para analizar los datos de la irradiancia
        ctk.CTkButton(self, text="Análisis de la Irradiancia", font=('Arial', 18),width=300, command=self.analisisIrra).pack(padx=10, pady=10)
        #Creamos los botones para analizar los datos de la iluminancia
        ctk.CTkButton(self, text="Análisis de la Iluminancia", font=('Arial', 18),width=300, command=self.analisisIlum).pack(padx=10, pady=10)
        #Creamos los botones para analizar los datos de la PAR
        ctk.CTkButton(self, text="Análisis de la Par", font=('Arial', 18),width=300, command=self.analsisPar).pack(padx=10, pady=10)
        #Creamos los botones para analizar los datos de la UV
        ctk.CTkButton(self, text="Análisis de la UV", font=('Arial', 18),width=300, command=self.analisiUv).pack(padx=10, pady=10)
        #Creamos un boton para volver a la pagina principal
        ctk.CTkButton(self, text="Atras",font=('Arial', 18),width=200, command=lambda: master.switch_frame(MainPage),fg_color="#1E3A8A", hover_color="#1E40AF").pack(padx=10, pady=10)
    #########################################################################################################################

    #Definimos una función para ralizar el analisis de irradiancia
    #########################################################################################################################
    def analisisIrra(self): 
        #Creamos un pop up para informar al usuario de que se esta realizando el analisis
        self.crearPopUp("Se esta realiando el analisis\n de irradiancia. Esto puede\n tardar unos minutos\n")
        try: #Intentamos realizar el analisis
            self.analisis.analisiIrra() #Realizamos el analisis
        except ValueError as e: #Si no hay suficientes datos para realizar el analisis se crea un pop up expresandolo
            self.crearPopUp("No hay suficientes datos para\nrealizar el analisis de irradiancia")
            self.log.injeErr(e) #Guardamos el error en el log
        except Exception as e: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("Ha ocurrido un error inesperado\n {} \n".format(e))
            self.log.injeErr(e) #Guardamos el error en el log
        #Creamos un pop up para informar al usuario de que se ha finalizado el analisis
        self.crearPopUp("Se ha finalizado el analisis de irradiancia\n")
    #########################################################################################################################

    #Definimos una función para ralizar el analisis de iluminancia
    #########################################################################################################################
    def analisisIlum(self):
        #Creamos un pop up para informar al usuario de que se esta realizando el analisis
        self.crearPopUp("Se esta realiando el analisis\n de iluminancia. Esto puede\n tardar unos minutos\n")
        try: #Intentamos realizar el analisis
            self.analisis.analisiIlum() #Realizamos el analisis
        except ValueError as e: #Si no hay suficientes datos para realizar el analisis se crea un pop up expresandolo
            self.crearPopUp("No hay suficientes datos para\nrealizar el analisis de iluminancia")
            self.log.injeErr(e) #Guardamos el error en el log
        except Exception as e: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("Ha ocurrido un error inesperado\n {} \n".format(e))
            self.log.injeErr(e) #Guardamos el error en el log
        self.crearPopUp("Se ha finalizado el analisis de iluminancia\n")
    #########################################################################################################################
    
    # Definimos una función para ralizar el analisis de PAR 
    #########################################################################################################################
    def analsisPar(self): 
        #Creamos un pop up para informar al usuario de que se esta realizando el analisis
        self.crearPopUp("Se esta realiando el analisis\n de la PAR. Esto puede\n tardar unos minutos\n")
        try: #Intentamos realizar el analisis
            self.analisis.analsisPar() #Realizamos el analisis
        except ValueError as e: #Si no hay suficientes datos para realizar el analisis se crea un pop up expresandolo
            self.crearPopUp("No hay suficientes datos para\nrealizar el analisis de PAR")
            self.log.injeErr(e) #Guardamos el error en el log
        except Exception as e: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("Ha ocurrido un error inesperado\n {} \n".format(e))
            self.log.injeErr(e) #Guardamos el error en el log
        #Creamos un pop up para informar al usuario de que se ha finalizado el analisis
        self.crearPopUp("Se ha finalizado el analisis de PAR\n")  
    #########################################################################################################################

    #Definimos una función para ralizar el analisis de UV
    #########################################################################################################################
    def analisiUv(self):
        #Creamos un pop up para informar al usuario de que se esta realizando el analisis
        self.crearPopUp("Se esta realiando el analisis\n de la UV. Esto puede\n tardar unos minutos\n")
        try: #Intentamos realizar el analisis
            self.analisis.analisiUv() #Realizamos el analisis
        except ValueError as e: #Si no hay suficientes datos para realizar el analisis se crea un pop up expresandolo
            self.crearPopUp("No hay suficientes datos para\nrealizar el analisis de UV")
            self.log.injeErr(e) #Guardamos el error en el log
        except Exception as e: #Si hay un error inesperado se crea un pop up expresandolo
            self.crearPopUp("Ha ocurrido un error inesperado\n {} \n".format(e))
            self.log.injeErr(e) #Guardamos el error en el log
        #Creamos un pop up para informar al usuario de que se ha finalizado el analisis
        self.crearPopUp("Se ha finalizado el analisis de UV\n")
    #########################################################################################################################
#########################################################################################################################

#Ejecutamos la interfaz de usuario
#########################################################################################################################
if __name__ == "__main__":
    app = UI()
    app.mainloop()
#########################################################################################################################