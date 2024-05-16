#Nombre:UI
#Autor:Álvaro Villar Val
#Fecha:27/02/24
#Versión:0.5.7
#Descripción: Interfaz de usuario para el programa
#########################################################################################################################
#Definimos los imports
import tkinter as tk
import customtkinter as ctk
import psycopg2
import matplotlib.pyplot as plt
from sqlalchemy.exc import DataError
from BaseDatosLvl2 import BaseDatosLvl2
import numpy as np


#########################################################################################################################
class Page(ctk.CTkFrame):
    def __init__(self, master,titulo):
        ctk.CTkFrame.__init__(self, master)
        ctk.CTkLabel(self,text=titulo, font=('Helvetica', 30, "bold")).pack(side="top", fill="x", pady=5)
        if(titulo!="Login Page"):
            logout_button = ctk.CTkButton(self, text="Cerrar Sesion",command=lambda: master.switch_frame(LoginPage))
            logout_button.place(relx=1.0, rely=0.0, anchor='ne')

    def crearPopUp(self,mensaje):
        # Crea una ventana de diálogo
        dialog = ctk.CTkToplevel(self)
        dialog.title("Error")
        dialog.geometry("200x100")
        dialog.attributes('-topmost', True)  # Esta línea hace que la ventana emergente permanezca en primer plano
    
        # Bloquea la interacción con la ventana de la que proviene
        dialog.grab_set()
    
        # Mensaje de error
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
        self.switch_frame(LoginPage)
        self.overrideredirect(False)  # Esto asegura que la barra de título y los controles de la ventana sigan visibles
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()-70))

    #########################################################################################################################
    
    #Definimos una función para cambiar de frame
    #########################################################################################################################
    def switch_frame(self, frame_class):
        #Destroys current frame and replaces it with a new one.
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
        self.user=ctk.CTkEntry(self, height=1, width=200,placeholder_text="Usuario")
        self.user.pack(padx=10, pady=10)
        self.password=ctk.CTkEntry(self, height=1, width=200,placeholder_text="Contraseña",show="*")
        self.password.pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Login",command=lambda: self.login(master)).pack(padx=10, pady=10)
    
    def login(self,master):
        user=self.user.get()
        password=self.password.get()
        if user=="admin" and password=="admin":
            master.switch_frame(MainPage)
        else:
            self.crearPopUp("Usuario o contraseña incorrectos")
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
        ctk.CTkButton(self, text="Descarga de datos", font=('Arial', 18), command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Descarga de imagenes", font=('Arial', 18), command=lambda: master.switch_frame(DescImg)).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack(padx=10, pady=10)
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
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack(padx=10, pady=10)
        self.bd2=BaseDatosLvl2()
#########################################################################################################################
class Desc(Page):
    def __init__(self, master,titulo):
        self.bd2=BaseDatosLvl2()
        Page.__init__(self, master,titulo)
        ctk.CTkLabel(self, text="Introduce la fecha de inicio", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxIni = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de inicio YY-MM-DD")
        self.textboxIni.pack(padx=10, pady=10)
        ctk.CTkLabel(self, text="Introduce la fecha de fin", font=('Arial', 18)).pack(padx=10, pady=10)
        self.textboxFin = ctk.CTkEntry(self, height=1, width=200,placeholder_text="Fecha de final YY-MM-DD")
        self.textboxFin.pack(padx=10, pady=10)

    def get_dates(self):
        self.fechain = self.textboxIni.get().strip()
        self.fechafi = self.textboxFin.get().strip()
    
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
    columnas={}
    columnasres=[]
    def __init__(self, master,titulo,tabla,columnas):
        self.tabla=tabla
        self.bd2=BaseDatosLvl2()
        DescBase.__init__(self, master,titulo,tabla)
        self.columnas=columnas
        if columnas.get("Titulo")=="SkyCamera":
            columns=columnas.get("Columnas").keys()
            num_columns = 4
            self.vars = {column: ctk.BooleanVar() for column in columns}
            for i, column in enumerate(columns):
                if i % num_columns == 0:
                    frame = ctk.CTkFrame(self)
                    frame.pack(side="top")
                ctk.CTkCheckBox(frame, text=column,variable=self.vars[column], font=('Arial', 12)).pack(side="left")
            
        else:
            columns=columnas.get("Columnas")
            self.option_menu = ctk.CTkOptionMenu(self, values=["Irradiancia", "Iluminancia", "Par", "UV","Miscelanea"], command=self.update_checkboxes)
            self.option_menu.pack(padx=10, pady=10)
            self.checkboxes_frame = ctk.CTkFrame(self)
            self.checkboxes_frame.pack(fill="both", expand=True)

        # Dictionary to hold checkbox variables
            self.checkbox_vars = {}
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)       

        
    ###########################################################################################################################################

    #Definimos una función para descargar datos
    ###########################################################################################################################################
    def descDat(self):
        self.get_dates()
        self.fechaini = self.fechain.replace('\n','')
        self.fechafin = self.fechafi.replace('\n','')
        
        columnasres=[]
        if len(self.columnas.get("Columnas")) ==5:
            self.update_checkboxes(self.option_menu.get())
            for col in self.columnasres:
                index=self.columnas.get("Columnas")
                for key in index.keys():
                    if col in index.get(key).keys():
                        columnasres.append(index.get(key).get(col))
        else:
            checked_columns = [column for column, var in self.vars.items() if var.get()]
            for col in checked_columns:
                columnasres.append(self.columnas.get("Columnas").get(col))
        print(columnasres)
        columna=",".join(columnasres)
        try:
            self.bd2.descdat(columna,self.tabla,self.fechaini,self.fechafin)
        except ValueError as e:
            self.crearPopUp("""No has escogido ninguna tabla\n""")
            
        except DataError as e:
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                                """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
        except Exception as e:
            print(e)
            self.crearPopUp("""Ha ocurrido un error inesperado\n {e} \n""")
    
    def update_checkboxes(self, choice):
        # Clear current checkboxes
        for widget in self.checkboxes_frame.winfo_children():
            if widget.cget("text") in self.columnasres:
                 if(not widget.get()):
                     self.columnasres.remove(widget.cget("text"))
            else:    
                if(widget.get()):
                    self.columnasres.append(widget.cget("text"))
            widget.destroy()
        print(self.columnasres)
        # Options for checkboxes
        options =self.columnas.get("Columnas")
        print(len(options))
        # Create new checkboxes based on the choice
        self.checkbox_vars[choice] = []
        for option in options.get(choice, []).keys():
            var = ctk.BooleanVar()
            if(option in self.columnasres):
                var.set(True)
            checkbox = ctk.CTkCheckBox(self.checkboxes_frame, text=option, variable=var)
            checkbox.pack(padx=10, pady=5)
            self.checkbox_vars[choice].append((checkbox, var))
    ###########################################################################################################################################
    
class DescVar2(DescVar1):
    def __init__(self, master,titulo,tabla,columnas):
        self.tabla=tabla
        self.bd2=BaseDatosLvl2()
        DescVar1.__init__(self, master,titulo,tabla,columnas)
        ctk.CTkButton(self, text="Graficar", font=('Arial', 18), command=self.graficar).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)  
    #Definimos una función para graficar los datos
    ###########################################################################################################################################
    def graficar(self):
        self.get_dates()
        self.fechaini = self.fechain.replace('\n','')
        self.fechafin = self.fechafi.replace('\n','')
        
        columnasres=[]
        if len(self.columnas.get("Columnas")) ==5:
            self.update_checkboxes(self.option_menu.get())
            for col in self.columnasres:
                index=self.columnas.get("Columnas")
                for key in index.keys():
                    if col in index.get(key).keys():
                        columnasres.append(index.get(key).get(col))
            time="TIMESTAMP"
        else:
            checked_columns = [column for column, var in self.vars.items() if var.get()]
            for col in checked_columns:
                columnasres.append(self.columnas.get("Columnas").get(col))
            time="time"
        
        try:
            dataframe=self.bd2.obtenerdat("*",self.tabla,self.fechaini,self.fechafin)
        except ValueError as e:
            self.crearPopUp("""No has escogido ninguna tabla\n""")
            raise e
        except DataError as e:
            self.crearPopUp("""Has introducido mal las fechas\n"""+
                                """Recuerda introducir las fechas en formato 'YY-MM-DD'\n""")
            raise e
        except Exception as e:
            print(e)
            self.crearPopUp("""Ha ocurrido un error inesperado\n {e} \n""")
            raise e


        plt.figure(figsize=(10, 6))  
        for column in columnasres:
            plt.plot(dataframe[time],dataframe[column], label=column) 
        plt.xlabel('Fecha')

        plt.xticks(np.arange(0, len(dataframe[time]), step=len(dataframe[time])/10))  
        plt.title('Grafico de las columnas')

        plt.legend()  
        plt.draw()  

        
        labels = [item.get_text() for item in plt.gca().get_xticklabels()]

      
        labels = [label[2:10] for label in labels]

       
        plt.gca().set_xticklabels(labels)

        plt.show()  

#########################################################################################################################
        
#Definimos la clase de la pagina de descarga de datos de la tabla radio
#########################################################################################################################
class DescRadio(DescVar2):

    #Definimos el constructor de la clase
    ###########################################################################################################################################
    def __init__(self, master):
        varIr={"Global vertical Irradiance North":"BuRaGVN_Avg","Global Vertical irradiance South":"BuRaGVS_Avg","Global Vertical irradiance East":"BuRaGVE_Avg",
               "Global Vertical irradiance West":"BuRaGVW_Avg","global horizontal irradiance":"BuRaGH_Avg","diffuse horizontal irradiance":"BuRaDH_Avg",
               "direct normal irradiance":"BuRaB_Avg","Diffuse Vertical irradiance North":"BuRaDVN_Avg","Diffuse Vertical irradiance South":"BuRaDVS_Avg",
               "Diffuse Vertical irradiance East":"BuRaDVE_Avg","Diffuse Vertical irradiance West":"BuRaDVW_Avg","Irradiancia del albedómetro Up (mirando up)":"BuRaAlUp_Avg",
               "Irradiancia del albedómetro Down (mirando down)":"BuRaAlDo_Avg","Alb - Albedo":"BuRaAlbe_Avg"}
        varIl={"Global Vertical illuminance North":"BuLxGVN_Avg","Global Vertical illuminance South":"BuLxGVS_Avg","Global Vertical illuminance East":"BuLxGVE_Avg","Global Vertical illuminance West":"BuLxGVW_Avg",
               "global horizontal illuminance":"BuLxGH_Avg","diffuse horizontal illuminance":"BuLxDH_Avg","direct normal illuminance":"BuLxB_Avg","Illuminancia Reflejada":"BuLxR_Avg"}
        varmisc={"Temperature":"BuTemp_Avg","Relative Humidity":"BuRH_Avg","Pressure":"BuPres_Avg","Wind Speed":"BuWS_Avg","Wind Direction":"BuWD_Avg","Pluv Cantidad de lluvia":"BuRain_Tot"}
        varPar={"Global Vertical PAR North":"BuPaGVN_Avg","Global Vertical PAR South":"BuPaGVS_Avg","Global Vertical PAR East":"BuPaGVE_Avg","Global Vertical PAR West":"BuPaGVW_Avg",
                "global horizontal PAR irradiance":"BuPaGH_Avg","diffuse horizontal PAR irradiance":"BuPaDH_Avg","direct normal PAR irradiance":"BuPaB_Avg","PAR reflejada":"BuPaR_Avg"}
        varUv={"Global Vertical UV North":"BuUvGVN_Avg","Global Vertical UV South":"BuUvGVS_Avg","Global Vertical UV East":"BuUvGVE_Avg","Global Vertical UV West":"BuUvGVW_Avg",
               "global horizontal UV irradiance":"BuUvGH_Avg","diffuse horizontal UV irradiance":"BuUvDH_Avg","direct normal UV irradiance":"BuUvB_Avg","Ultravioleta A Global horizontal":"BuUvAGH_Avg",
               "Ultravioleta A Difusa horizontal":"BuUvADH_Avg","Ultravioleta A Global vertical sur":"BuUvAV_Avg","Ultravioleta B Global horizontal":"BuUvBGH_Avg","Ultravioleta B Difusa horizontal":"BuUvBDH_Avg",
               "Ultravioleta B Global vertical sur":"BuUvBV_Avg","Ultravioleta E Global horizontal":"BuUvEGH_Avg","Ultravioleta E Difusa horizontal":"BuUvEDH_Avg","Ultravioleta E Global vertical sur":"BuUvEV_Avg"}
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
        varIr={"Global vertical Irradiance North":"BuRaGVN_Avg","Global Vertical irradiance South":"BuRaGVS_Avg","Global Vertical irradiance East":"BuRaGVE_Avg",
               "Global Vertical irradiance West":"BuRaGVW_Avg","global horizontal irradiance":"BuRaGH_Avg","diffuse horizontal irradiance":"BuRaDH_Avg",
               "direct normal irradiance":"BuRaB_Avg","Diffuse Vertical irradiance North":"BuRaDVN_Avg","Diffuse Vertical irradiance South":"BuRaDVS_Avg",
               "Diffuse Vertical irradiance East":"BuRaDVEAvg","Diffuse Vertical irradiance West":"BuRaDVW_Avg","Irradiancia del albedómetro Up (mirando up)":"BuRaAlUp_Avg",
               "Irradiancia del albedómetro Down (mirando down)":"BuRaAlDo_Avg","Alb - Albedo":"BuRaAlbe_Avg"}
        varIl={"Global Vertical illuminance North":"BuLxGVN_Avg","Global Vertical illuminance South":"BuLxGVS_Avg","Global Vertical illuminance East":"BuLxGVE_Avg","Global Vertical illuminance West":"BuLxGVW_Avg",
               "global horizontal illuminance":"BuLxGH_Avg","diffuse horizontal illuminance":"BuLxDH_Avg","direct normal illuminance":"BuLxB_Avg","Illuminancia Reflejada":"BuLxR_Avg"}
        varmisc={"Temperature":"BuTemp_Avg","Relative Humidity":"BuRH_Avg","Pressure":"BuPres_Avg","Wind Speed":"BuWS_Avg","Wind Direction":"BuWD_Avg","Pluv Cantidad de lluvia":"BuRain_Tot","Fallo":"fallo"}
        varPar={"Global Vertical PAR North":"BuPaGVN_Avg","Global Vertical PAR South":"BuPaGVS_Avg","Global Vertical PAR East":"BuPaGVE_Avg","Global Vertical PAR West":"BuPaGVW_Avg",
                "global horizontal PAR irradiance":"BuPaGH_Avg","diffuse horizontal PAR irradiance":"BuPaDH_Avg","direct normal PAR irradiance":"BuPaB_Avg","PAR reflejada":"BuPaR_Avg"}
        varUv={"Global Vertical UV North":"BuUvGVN_Avg","Global Vertical UV South":"BuUvGVS_Avg","Global Vertical UV East":"BuUvGVE_Avg","Global Vertical UV West":"BuUvGVW_Avg",
               "global horizontal UV irradiance":"BuUvGH_Avg","diffuse horizontal UV irradiance":"BuUvDH_Avg","direct normal UV irradiance":"BuUvB_Avg","Ultravioleta A Global horizontal":"BuUvAGH_Avg",
               "Ultravioleta A Difusa horizontal":"BuUvADH_Avg","Ultravioleta A Global vertical sur":"BuUvAV_Avg","Ultravioleta B Global horizontal":"BuUvBGH_Avg","Ultravioleta B Difusa horizontal":"BuUvBDH_Avg",
               "Ultravioleta B Global vertical sur":"BuUvBV_Avg","Ultravioleta E Global horizontal":"BuUvEGH_Avg","Ultravioleta E Difusa horizontal":"BuUvEDH_Avg","Ultravioleta E Global vertical sur":"BuUvEV_Avg"}
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
        ctk.CTkButton(self, text="Descargar", font=('Arial', 18), command=self.descDat).pack(padx=10, pady=10)
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)
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
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)
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
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(DescDatos)).pack(padx=10, pady=10)
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
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(Descargas)).pack(padx=10, pady=10)
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
        ctk.CTkButton(self, text="Atras", command=lambda: master.switch_frame(MainPage)).pack(padx=10, pady=10)    
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