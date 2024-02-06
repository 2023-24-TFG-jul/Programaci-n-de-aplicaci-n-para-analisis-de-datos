#Nombre:BaseDatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.23
#Descripción: Base de datos de primer nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd

#Inicializamos la Clase de creación de base de datos
class BaseDatosLlv1:

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
    ########################################################################################################################
        
    #Obtenemos los datos de una fecha a otra fecha
    ####################################################################################################################
    def obtenerdat(self,ini,fin,base):
        orden="""SELECT * FROM %s"""
        #Enviamos la operación a la base de datos
        self.cur.execute(orden,base)
        self.conn.commit()
    ######################################################################################################################

    #Actualizamos la base de datos con los ultimos datos que hayamos obtenido
    ##########################################################################################################################   
    def actualizar(self):
        orden=""" CREATE TABLE IF NOT EXISTS skyscanner (sideDateHour VARCHAR(255) PRIMARY KEY,dat1 FLOAT,dat2 FLOAT,
        dat3 FLOAT,dat4 FLOAT,dat5 FLOAT,dat6 FLOAT,dat7 FLOAT,dat8 FLOAT,dat9 FLOAT,dat10 FLOAT,dat11 FLOAT,dat12 FLOAT,
        dat13 FLOAT,dat14 FLOAT,dat15 FLOAT,dat16 FLOAT,dat17 FLOAT,dat18 FLOAT,dat19 FLOAT,dat20 FLOAT,dat21 FLOAT,
        dat22 FLOAT,dat23 FLOAT,dat24 FLOAT,dat25 FLOAT,dat26 FLOAT,dat27 FLOAT,dat28 FLOAT,dat29 FLOAT,dat30 FLOAT,dat31 FLOAT,
        dat32 FLOAT,dat33 FLOAT,dat34 FLOAT,dat35 FLOAT,dat36 FLOAT,dat37 FLOAT,dat38 FLOAT,dat39 FLOAT,dat40 FLOAT,dat41 FLOAT,
        dat42 FLOAT,dat43 FLOAT,dat44 FLOAT,dat45 FLOAT,dat46 FLOAT,dat47 FLOAT,dat48 FLOAT,dat49 FLOAT,dat50 FLOAT,dat51 FLOAT,
        dat52 FLOAT,dat53 FLOAT,dat54 FLOAT,dat55 FLOAT,dat56 FLOAT,dat57 FLOAT,dat58 FLOAT,dat59 FLOAT,dat60 FLOAT,dat61 FLOAT,
        dat62 FLOAT,dat63 FLOAT,dat64 FLOAT,dat65 FLOAT,dat66 FLOAT,dat67 FLOAT,dat68 FLOAT,dat69 FLOAT,dat70 FLOAT,dat71 FLOAT,
        dat72 FLOAT,dat73 FLOAT,dat74 FLOAT,dat75 FLOAT,dat76 FLOAT,dat77 FLOAT,dat78 FLOAT,dat79 FLOAT,dat8 FLOAT,dat81 FLOAT,
        dat82 FLOAT,dat83 FLOAT,dat84 FLOAT,dat85 FLOAT,dat86 FLOAT,dat87 FLOAT,dat88 FLOAT,dat89 FLOAT,dat90 FLOAT,dat91 FLOAT,
        dat92 FLOAT,dat93 FLOAT,dat94 FLOAT,dat95 FLOAT,dat96 FLOAT,dat97 FLOAT,dat98 FLOAT,dat99 FLOAT,dat100 FLOAT,dat101 FLOAT,
        dat102 FLOAT,dat103 FLOAT,dat104 FLOAT,dat105 FLOAT,dat106 FLOAT,dat107 FLOAT,dat108 FLOAT,dat109 FLOAT,dat110 FLOAT,dat111 FLOAT,
        dat112 FLOAT,dat113 FLOAT,dat114 FLOAT,dat115 FLOAT,dat116 FLOAT,dat117 FLOAT,dat118 FLOAT,dat119 FLOAT,dat120 FLOAT,dat121 FLOAT,
        dat122 FLOAT,dat123 FLOAT,dat124 FLOAT,dat125 FLOAT,dat126 FLOAT,dat127 FLOAT,dat128 FLOAT,dat129 FLOAT,dat130 FLOAT,dat131 FLOAT,
        dat132 FLOAT,dat133 FLOAT,dat134 FLOAT,dat135 FLOAT,dat136 FLOAT,dat137 FLOAT,dat138 FLOAT,dat139 FLOAT,dat140 FLOAT,dat141 FLOAT,
        dat142 FLOAT,dat143 FLOAT,dat144 FLOAT,dat145 FLOAT); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        orden=""" CREATE TABLE IF NOT EXISTS skyscanner (gain FLOAT,shutter VARCHAR(255),azimuth FLOAT,blocked INTEGER,cloud_cover FLOAT,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust INTEGER,elevation FLOAT,image VARCHAR,mode INTEGER,temperature FLOAT,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        orden=""" CREATE TABLE IF NOT EXISTS radio ("TIMESTAMP","RECORD","Year","Month","Dia","YearDay","Hour","Minute","BuPres_Avg","BuRH_Avg","BuTemp_Avg","BuRain_Tot","BuWS_Avg","BuWD_Avg","BuTDP_Avg","BuTWB_Avg","BuRaGVN_Avg","BuRaGVE_Avg","BuRaGVS_Avg","BuRaGVW_Avg","BuRaGH_Avg","BuRaDH_Avg","BuRaB_Avg","BuLxGVN_Avg","BuLxGVE_Avg","BuLxGVS_Avg","BuLxGVW_Avg","BuLxGH_Avg","BuLxDH_Avg","BuLxB_Avg","BuPaGVN_Avg","BuPaGVE_Avg","BuPaGVS_Avg","BuPaGVW_Avg","BuPaGH_Avg","BuPaDH_Avg","BuPaB_Avg","BuUvGVN_Avg","BuUvGVE_Avg","BuUvGVS_Avg","BuUvGVW_Avg","BuUvGH_Avg","BuUvDH_Avg","BuUvB_Avg","BuUvAGH_Avg","BuUvADH_Avg","BuUvAV_Avg","BuUvBGH_Avg","BuUvBDH_Avg","BuUvBV_Avg","BuUvEGH_Avg","BuUvEDH_Avg","BuUvEV_Avg","BuRaDVN_Avg","BuRaDVE_Avg","BuRaDVS_Avg","BuRaDVW_Avg","BuRaAlUp_Avg","BuRaAlDo_Avg","BuRaAlbe_Avg","BuPaR_Avg","BuLxR_Avg","BuIrGH_Avg"
                "TS","RN","","","","","","","mbar","%","°C","mm","m/s","°","Deg C","Deg C","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","Lx","Lx","Lx","Lx","Lx","Lx","Lx","µmol/m²s","µmol/m²s","µmol/m²s","µmol/m²s","µmol/m²s","µmol/m²s","µmol/m²s","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","W/m²","[]","","","W/m²"
                    "","","Smp","Smp","Smp","Smp","Smp","Smp","Avg","Avg","Avg","Tot","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg","Avg"); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
     #Definimos el Cierre de la conexión con la base de datos
    def stop(self):
        #Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
        self.cur.close()
        self.conn.close() 

