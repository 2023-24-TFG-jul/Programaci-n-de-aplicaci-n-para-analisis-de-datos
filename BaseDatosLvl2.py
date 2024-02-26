#Nombre:BasedatosLvl2
#Autor:Álvaro Villar Val
#Fecha:20/02/24
#Versión:0.2.3
#Descripción: Base de datos de segundo nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
from BaseDatosLvl1 import BaseDatosLvl1
import pandas as pd #Import para gestion de datos
import sqlalchemy #import para pasar los datos en bulk
from sqlalchemy import create_engine #Import para pasar los datos en bulk
import os #import para leer los archivos en un directorio especificado
#Inicializamos la Clase de creación de base de datos
class BaseDatosLvl2:

    #Definimos el constructor de la base de datos que hara la conexion con la base de sectos
    ####################################################################################################################
    def __init__(self):
        #Parametros de la base de datos
        self.dirradio="Datos\datalogger" #path donde se meteran los archivos que se quieran meter en la base de datos radio
        self.dircamera="Datos\sky-camera"#path donde se meteran los archivos que se quieran meter en la base de datos skycamera
        self.dirscanner="Datos\Sky-scanner 2023_12"#path donde se meteran los archivos que se quieran meter en la base de datos skyscanner
        self.dirimgCam1="Datos\Fotos\CAM1\imagenes"#path en el que se meteran las imagenes de la camara1 que se quiera introducir en la base de datos
        self.dirimgCam2="Datos\Fotos\CAM2\imagenes"#path en el que se meteran las imagenes de la camara2 que se quieran introducir en la base de datos
        self.db1=BaseDatosLvl1() #Inicializamos la base de primer nivel
        self.datahost="localhost" #Host de la base de datos
        self.dataname="postgres"  #Nombre de la base de datos
        self.datauser="postgres"  #Nombre del usuario
        self.datapass="1234"      #Contraseña de la base de datos
        self.dataport=5432        #Puerto al que se conecta la base de datos
        self.conn=self.db1.conn #guardamos la connexión del primer nivel de datos ya que vamos a usar la misma base de datos
        self.cur=self.db1.cur   #guardamos a su vez el cursor de la base de datos
        #inicializamdos la conexopn que usara sqlAlchemy para operar en la base de datos
        conn_string = f'postgresql://{self.datauser}:{self.datapass}@{self.datahost}:{self.dataport}/{self.dataname}'
        self.engine = create_engine(conn_string) 
        #llamamos a la función crear la cual creara las tablas que no esten creadas en la base de datos
        self.crear()
    #######################################################################################################################
    
    #Definimos la función que creara las tablas de datos procesados
    #######################################################################################################################
    def crear(self):#No hace falta crear la de scanner ya que la de base esta bien
        #Creación de las tabla en caso de que no exista de la Skycamera de datos procesados
        #La primary key de esta tabla es time que se dividi en: año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS skycameraproc("GAIN" VARCHAR,"SHUTTER" VARCHAR(255),azimuth decimal,blocked integer,cloud_cover decimal,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust integer,elevation decimal,image VARCHAR,mode integer,temperature decimal,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tablas en caso de que no exixta la radio de datos procesados
        #La primary key es timestamp la cual se divide en:año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS radioproc ("TIMESTAMP" VARCHAR PRIMARY KEY,"Year" integer,"Month" integer,"Dia" integer,"YearDay" integer,"Hour" integer,"Minute" integer,
        "BuPres_Avg" decimal,"BuRH_Avg" decimal,"BuTemp_Avg" decimal,"BuRain_Tot" decimal,"BuWS_Avg" decimal,"BuWD_Avg" decimal,"BuTDP_Avg" decimal,"BuTWB_Avg" decimal,
        "BuRaGVN_Avg" decimal,"BuRaGVE_Avg" decimal,"BuRaGVS_Avg" decimal,"BuRaGVW_Avg" decimal,"BuRaGH_Avg" decimal,"BuRaDH_Avg" decimal,"BuRaB_Avg" decimal,"BuLxGVN_Avg" decimal,
        "BuLxGVE_Avg" decimal,"BuLxGVS_Avg" decimal,"BuLxGVW_Avg" decimal,"BuLxGH_Avg" decimal,"BuLxDH_Avg" decimal,"BuLxB_Avg" decimal,"BuPaGVN_Avg" decimal,"BuPaGVE_Avg" decimal,
        "BuPaGVS_Avg" decimal,"BuPaGVW_Avg" decimal,"BuPaGH_Avg" decimal,"BuPaDH_Avg" decimal,"BuPaB_Avg" decimal,"BuUvGVN_Avg" decimal,"BuUvGVE_Avg" decimal, "BuUvGVS_Avg" decimal,
        "BuUvGVW_Avg" decimal,"BuUvGH_Avg" decimal,"BuUvDH_Avg" decimal,"BuUvB_Avg" decimal,"BuUvAGH_Avg" decimal,"BuUvADH_Avg" decimal,"BuUvAV_Avg" decimal,"BuUvBGH_Avg" decimal,
        "BuUvBDH_Avg" decimal,"BuUvBV_Avg" decimal,"BuUvEGH_Avg" decimal,"BuUvEDH_Avg" decimal,"BuUvEV_Avg" decimal,"BuRaDVN_Avg" decimal,"BuRaDVE_Avg" decimal,"BuRaDVS_Avg" decimal,
        "BuRaDVW_Avg" decimal,"BuRaAlUp_Avg" decimal,"BuRaAlDo_Avg" decimal,"BuRaAlbe_Avg" decimal,"BuPaR_Avg" decimal,"BuLxR_Avg" decimal,"BuIrGH_Avg" decimal,fallo varchar(250))"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
    ################################################################################################################################################################################################
    
    #Definimos una función que sustitye a la función de la bd1 de actualización de datos
    ################################################################################################################################################################################################
    def actualizardatos(self,):
         #Tomamos todos los archivos en el directorio de radio y guardamos sus nombre en una lista
        radio=os.listdir(self.dirradio)
        #Tomamos todos los archivos en el directorio de camera y guardamos sus nombre en una lista
        camera=os.listdir(self.dircamera)
        #Tomamos todos los archivos en el directorio de canner y guardamos sus nombre en una lista
        scanner=os.listdir(self.dirscanner)
        for datos in radio: #recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de datos
            self.db1.injectarCsvRadio(self.dirradio+"\\"+datos)#introducimos los datos a la tabla de radio
            self.actualizarRadio(self.dirradio+"\\"+datos)
        for datos in camera:#recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de datos
            self.db1.injectarCsvSkycamera(self.dircamera+"\\"+datos)#introducimos los datos a la tabla de camera
            self.actualizarCammera(self.dircamera+"\\"+datos)
        for datos in scanner:#recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de datos
            self.db1.injectarCsvSkyScanner(self.dirscanner+"\\"+datos)#introducimos los datos a la tabla de scanner
    #################################################################################################################################################################################################
    
    #Definimos la operación que añadira los nuevos datos procesados a la base de datos
    #################################################################################################################################################################################################
    def actualizarRadio(self,data):
        data['fallo']='0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'

        try:
            #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),y el index a False que no recuerdo para que sirve pero ponlo
            data.to_sql('radio', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #TODO Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en radioproc")
    #########################################################################################################################################################################################################

    #Definimos una funcón que actualice los datos de de la skycamera desde la base de datos 1
    ##########################################################################################################################################################################################################
    def actualizarCammera(self,route):
        df=pd.read_csv(route)
        #establecemos una nueva columna llamada date para tener una manera facil y estandarizada de acceso a los datos
        #Para ello tomamos la fecha de time y nos quedamos con la fecha de días y la tipamos a AñoMesDía
        df['date']=df['time'].str.slice(2,10)
        df['date']= df['date'].str.replace('-', '')
        df.dropna(subset=['image'], inplace=True)
        try:
            #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),y el index a False que no recuerdo para que sirve pero ponlo
            df.to_sql('skycameraproc', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #TODO Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en la Skycamera")
    ##########################################################################################################################################################################################################
        
    #Definimos una función para que de momento nos devuelva datos
     #########################################################################################################################################################################################################
    def obtenerdat(self,selec,base,cond):
        return self.db1.obtenerdat(selec,base,cond)
     #########################################################################################################################################################################################################
    
    #Definimos la operación de cierre de conexiones para evitar errores en las conexiones futuras
    #SIEMPRE USAR AL FINALIZAR EL PROGRAMA
    ##########################################################################################################################################################################################################
    def stop(self):
        #Cerramos las conexiones del primer nivel de la base de datos
        self.db1.stop()