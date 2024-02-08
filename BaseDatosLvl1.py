#Nombre:BaseDatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.37
#Descripción: Base de datos de primer nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd
from psycopg2 import sql
#Inicializamos la Clase de creación de base de datos
class BaseDatosLvl1:

    #Definimos el constructor de la base de datos que hara la conexion con la base de datos
    ####################################################################################################################
    def __init__(self):
        #Parametros de la base de datos
        self.datahost="localhost"
        self.dataname="postgres"
        self.datauser="postgres"
        self.datapass="1234"
        self.dataport=5432
        #Establecemos la conexion con la base de datos
        self.conn=psycopg2.connect(host=self.datahost,dbname=self.dataname, user=self.datauser, password=self.datapass,port=self.dataport)
        #Inicializamos el cursor con el que operaremos en la base de datos
        self.cur=self.conn.cursor()
        self.crear()
    ########################################################################################################################
        
    #Obtenemos los datos de una fecha a otra fecha
    ####################################################################################################################
    def obtenerdat(self,base):
        #Enviamos la operación a la base de datos
        query = sql.SQL("select * from {table}").format(
        table=sql.Identifier(base))
        self.cur.execute(query)
        self.conn.commit()
        return self.cur.fetchall()
    #
    # query = sql.SQL("select {field} from {table} where {pkey} = %s").format(
    # field=sql.Identifier('my_name'),
    # table=sql.Identifier('some_table'),
    # pkey=sql.Identifier('id'))
    ######################################################################################################################

    #Creamos las tablas de la base de datos la base de datos con los ultimos datos que hayamos obtenido
    ##########################################################################################################################   
    def crear(self):
        #Creación de las tablasp
        orden=""" CREATE TABLE IF NOT EXISTS skyscanner (sideDateHour VARCHAR(255) PRIMARY KEY,dat1 decimal,dat2 decimal,
        dat3 decimal,dat4 decimal,dat5 decimal,dat6 decimal,dat7 decimal,dat8 decimal,dat9 decimal,dat10 decimal,dat11 decimal,dat12 decimal,
        dat13 decimal,dat14 decimal,dat15 decimal,dat16 decimal,dat17 decimal,dat18 decimal,dat19 decimal,dat20 decimal,dat21 decimal,
        dat22 decimal,dat23 decimal,dat24 decimal,dat25 decimal,dat26 decimal,dat27 decimal,dat28 decimal,dat29 decimal,dat30 decimal,dat31 decimal,
        dat32 decimal,dat33 decimal,dat34 decimal,dat35 decimal,dat36 decimal,dat37 decimal,dat38 decimal,dat39 decimal,dat40 decimal,dat41 decimal,
        dat42 decimal,dat43 decimal,dat44 decimal,dat45 decimal,dat46 decimal,dat47 decimal,dat48 decimal,dat49 decimal,dat50 decimal,dat51 decimal,
        dat52 decimal,dat53 decimal,dat54 decimal,dat55 decimal,dat56 decimal,dat57 decimal,dat58 decimal,dat59 decimal,dat60 decimal,dat61 decimal,
        dat62 decimal,dat63 decimal,dat64 decimal,dat65 decimal,dat66 decimal,dat67 decimal,dat68 decimal,dat69 decimal,dat70 decimal,dat71 decimal,
        dat72 decimal,dat73 decimal,dat74 decimal,dat75 decimal,dat76 decimal,dat77 decimal,dat78 decimal,dat79 decimal,dat80 decimal,dat81 decimal,
        dat82 decimal,dat83 decimal,dat84 decimal,dat85 decimal,dat86 decimal,dat87 decimal,dat88 decimal,dat89 decimal,dat90 decimal,dat91 decimal,
        dat92 decimal,dat93 decimal,dat94 decimal,dat95 decimal,dat96 decimal,dat97 decimal,dat98 decimal,dat99 decimal,dat100 decimal,dat101 decimal,
        dat102 decimal,dat103 decimal,dat104 decimal,dat105 decimal,dat106 decimal,dat107 decimal,dat108 decimal,dat109 decimal,dat110 decimal,dat111 decimal,
        dat112 decimal,dat113 decimal,dat114 decimal,dat115 decimal,dat116 decimal,dat117 decimal,dat118 decimal,dat119 decimal,dat120 decimal,dat121 decimal,
        dat122 decimal,dat123 decimal,dat124 decimal,dat125 decimal,dat126 decimal,dat127 decimal,dat128 decimal,dat129 decimal,dat130 decimal,dat131 decimal,
        dat132 decimal,dat133 decimal,dat134 decimal,dat135 decimal,dat136 decimal,dat137 decimal,dat138 decimal,dat139 decimal,dat140 decimal,dat141 decimal,
        dat142 decimal,dat143 decimal,dat144 decimal,dat145 decimal); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tabla en caso de que no exista de la Skycamera
        orden=""" CREATE TABLE IF NOT EXISTS skycamera(gain decimal,shutter VARCHAR(255),azimuth decimal,blocked integer,cloud_cover decimal,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust integer,elevation decimal,image VARCHAR,mode integer,temperature decimal,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Recordar eliminar RECORD dato ineccesario
        #Creación de las tablas en caso de que no exixta la radio
        orden=""" CREATE TABLE IF NOT EXISTS radio (TIMESTAMP VARCHAR(255),Year integer,Month integer,Dia integer,YearDay integer,Hour integer,Minute integer,
        BuPres_Avg decimal,BuRH_Avg decimal,BuTemp_Avg decimal,BuRain_Tot decimal,BuWS_Avg decimal,BuWD_Avg decimal,BuTDP_Avg decimal,BuTWB_Avg decimal,
        BuRaGVN_Avg decimal,BuRaGVE_Avg decimal,BuRaGVS_Avg decimal,BuRaGVW_Avg decimal,BuRaGH_Avg decimal,BuRaDH_Avg decimal,BuRaB_Avg decimal,BuLxGVN_Avg decimal,
        BuLxGVE_Avg decimal,BuLxGVS_Avg decimal,BuLxGVW_Avg decimal,BuLxGH_Avg decimal,BuLxDH_Avg decimal,BuLxB_Avg decimal,BuPaGVN_Avg decimal,BuPaGVE_Avg decimal,
        BuPaGVS_Avg decimal,BuPaGVW_Avg decimal,BuPaGH_Avg decimal,BuPaDH_Avg decimal,BuPaB_Avg decimal,BuUvGVN_Avg decimal,BuUvGVE_Avg decimal, BuUvGVS_Avg decimal,
        BuUvGVW_Avg decimal,BuUvGH_Avg decimal,BuUvDH_Avg decimal,BuUvB_Avg decimal,BuUvAGH_Avg decimal,BuUvADH_Avg decimal,BuUvAV_Avg decimal,BuUvBGH_Avg decimal,
        BuUvBDH_Avg decimal,BuUvBV_Avg decimal,BuUvEGH_Avg decimal,BuUvEDH_Avg decimal,BuUvEV_Avg decimal,BuRaDVN_Avg decimal,BuRaDVE_Avg decimal,BuRaDVS_Avg decimal,
        BuRaDVW_Avg decimal,BuRaAlUp_Avg decimal,BuRaAlDo_Avg decimal,BuRaAlbe_Avg decimal,BuPaR_Avg decimal,BuLxR_Avg decimal,BuIrGH_Avg decimal)"""
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
    #Definimos la función que leerra el archivo csv 
    def leerCsv(self):
        #lee el csv del skyscanner
        medidas=pd.read_csv("Datos\Sky-scanner 2023_12\SS231201.csv",nrows=3, names=[0,1])
        sky=pd.read_csv("Datos\Sky-scanner 2023_12\SS231201.csv",skiprows=8)
        #lee el csv de la sky camera
        cam=pd.read_csv("Datos\sky-camera\\10-Octubre-2023.csv")
        #lee el datalogger
        dtl=pd.read_csv("Datos\datalogger\CR3000_J_OCTUBRE_2023.dat",skiprows=[0,2,3])
        return medidas,sky,cam,dtl

    #Definimos el Cierre de la conexión con la base de datos
    def stop(self):
        #Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
        self.cur.close()
        self.conn.close() 

