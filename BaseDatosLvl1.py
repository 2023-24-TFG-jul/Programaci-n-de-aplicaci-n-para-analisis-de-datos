#Nombre:BasedatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.65
#Descripción: Base de datos de primer nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd
from psycopg2 import sql
from sqlalchemy import create_engine 
import sqlalchemy
import os
import numpy as np
from psycopg2 import Binary
from io import BytesIO
from PIL import Image

#Inicializamos la Clase de creación de base de datos
class BaseDatosLvl1:

    #Definimos el constructor de la base de datos que hara la conexion con la base de sectos
    ####################################################################################################################
    def __init__(self):
        #Parametros de la base de datos
        self.dirradio="Datos\datalogger"
        self.dircamera="Datos\sky-camera"
        self.dirscanner="Datos\Sky-scanner 2023_12"
        self.datahost="localhost"
        self.dataname="postgres"
        self.datauser="postgres"
        self.datapass="1234"
        self.dataport=5432
        #Establecemos la conexion con la base de datos
        self.conn=psycopg2.connect(host=self.datahost,dbname=self.dataname, user=self.datauser, password=self.datapass,port=self.dataport)
        #Inicializamos el cursor con el que operaremos en la base de datos
        self.cur=self.conn.cursor()

        conn_string = f'postgresql://{self.datauser}:{self.datapass}@{self.datahost}:{self.dataport}/{self.dataname}'
        self.engine = create_engine(conn_string) 
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
        orden=""" CREATE TABLE IF NOT EXISTS skyscanner (sidedatehour VARCHAR(255) PRIMARY KEY, hour time,date integer,sect1 decimal,sect2 decimal,
        sect3 decimal,sect4 decimal,sect5 decimal,sect6 decimal,sect7 decimal,sect8 decimal,sect9 decimal,sect10 decimal,sect11 decimal,sect12 decimal,
        sect13 decimal,sect14 decimal,sect15 decimal,sect16 decimal,sect17 decimal,sect18 decimal,sect19 decimal,sect20 decimal,sect21 decimal,
        sect22 decimal,sect23 decimal,sect24 decimal,sect25 decimal,sect26 decimal,sect27 decimal,sect28 decimal,sect29 decimal,sect30 decimal,sect31 decimal,
        sect32 decimal,sect33 decimal,sect34 decimal,sect35 decimal,sect36 decimal,sect37 decimal,sect38 decimal,sect39 decimal,sect40 decimal,sect41 decimal,
        sect42 decimal,sect43 decimal,sect44 decimal,sect45 decimal,sect46 decimal,sect47 decimal,sect48 decimal,sect49 decimal,sect50 decimal,sect51 decimal,
        sect52 decimal,sect53 decimal,sect54 decimal,sect55 decimal,sect56 decimal,sect57 decimal,sect58 decimal,sect59 decimal,sect60 decimal,sect61 decimal,
        sect62 decimal,sect63 decimal,sect64 decimal,sect65 decimal,sect66 decimal,sect67 decimal,sect68 decimal,sect69 decimal,sect70 decimal,sect71 decimal,
        sect72 decimal,sect73 decimal,sect74 decimal,sect75 decimal,sect76 decimal,sect77 decimal,sect78 decimal,sect79 decimal,sect80 decimal,sect81 decimal,
        sect82 decimal,sect83 decimal,sect84 decimal,sect85 decimal,sect86 decimal,sect87 decimal,sect88 decimal,sect89 decimal,sect90 decimal,sect91 decimal,
        sect92 decimal,sect93 decimal,sect94 decimal,sect95 decimal,sect96 decimal,sect97 decimal,sect98 decimal,sect99 decimal,sect100 decimal,sect101 decimal,
        sect102 decimal,sect103 decimal,sect104 decimal,sect105 decimal,sect106 decimal,sect107 decimal,sect108 decimal,sect109 decimal,sect110 decimal,sect111 decimal,
        sect112 decimal,sect113 decimal,sect114 decimal,sect115 decimal,sect116 decimal,sect117 decimal,sect118 decimal,sect119 decimal,sect120 decimal,sect121 decimal,
        sect122 decimal,sect123 decimal,sect124 decimal,sect125 decimal,sect126 decimal,sect127 decimal,sect128 decimal,sect129 decimal,sect130 decimal,sect131 decimal,
        sect132 decimal,sect133 decimal,sect134 decimal,sect135 decimal,sect136 decimal,sect137 decimal,sect138 decimal,sect139 decimal,sect140 decimal,sect141 decimal,
        sect142 decimal,sect143 decimal,sect144 decimal,sect145 decimal, azimut decimal, elevacion decimal); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tabla en caso de que no exista de la Skycamera
        orden=""" CREATE TABLE IF NOT EXISTS skycamera("GAIN" VARCHAR,"SHUTTER" VARCHAR(255),azimuth decimal,blocked integer,cloud_cover decimal,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust integer,elevation decimal,image VARCHAR,mode integer,temperature decimal,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Recordar eliminar RECORD dato ineccesario
        #Creación de las tablas en caso de que no exixta la radio
        orden=""" CREATE TABLE IF NOT EXISTS radio ("TIMESTAMP" VARCHAR PRIMARY KEY,"Year" integer,"Month" integer,"Dia" integer,"YearDay" integer,"Hour" integer,"Minute" integer,
        "BuPres_Avg" decimal,"BuRH_Avg" decimal,"BuTemp_Avg" decimal,"BuRain_Tot" decimal,"BuWS_Avg" decimal,"BuWD_Avg" decimal,"BuTDP_Avg" decimal,"BuTWB_Avg" decimal,
        "BuRaGVN_Avg" decimal,"BuRaGVE_Avg" decimal,"BuRaGVS_Avg" decimal,"BuRaGVW_Avg" decimal,"BuRaGH_Avg" decimal,"BuRaDH_Avg" decimal,"BuRaB_Avg" decimal,"BuLxGVN_Avg" decimal,
        "BuLxGVE_Avg" decimal,"BuLxGVS_Avg" decimal,"BuLxGVW_Avg" decimal,"BuLxGH_Avg" decimal,"BuLxDH_Avg" decimal,"BuLxB_Avg" decimal,"BuPaGVN_Avg" decimal,"BuPaGVE_Avg" decimal,
        "BuPaGVS_Avg" decimal,"BuPaGVW_Avg" decimal,"BuPaGH_Avg" decimal,"BuPaDH_Avg" decimal,"BuPaB_Avg" decimal,"BuUvGVN_Avg" decimal,"BuUvGVE_Avg" decimal, "BuUvGVS_Avg" decimal,
        "BuUvGVW_Avg" decimal,"BuUvGH_Avg" decimal,"BuUvDH_Avg" decimal,"BuUvB_Avg" decimal,"BuUvAGH_Avg" decimal,"BuUvADH_Avg" decimal,"BuUvAV_Avg" decimal,"BuUvBGH_Avg" decimal,
        "BuUvBDH_Avg" decimal,"BuUvBV_Avg" decimal,"BuUvEGH_Avg" decimal,"BuUvEDH_Avg" decimal,"BuUvEV_Avg" decimal,"BuRaDVN_Avg" decimal,"BuRaDVE_Avg" decimal,"BuRaDVS_Avg" decimal,
        "BuRaDVW_Avg" decimal,"BuRaAlUp_Avg" decimal,"BuRaAlDo_Avg" decimal,"BuRaAlbe_Avg" decimal,"BuPaR_Avg" decimal,"BuLxR_Avg" decimal,"BuIrGH_Avg" decimal)"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de la base de datos de las imagenes
        orden=""" CREATE TABLE IF NOT EXISTS images (id SERIAL PRIMARY KEY,image_data bytea);"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
    ########################################################################################################################################################################################

    #Definimo la función para injectar las imagenes en la base de datos
    ##############################################################################################################################################################################################
    def injectarimg(self,route):
        with open(route, 'rb') as f:
            image_data = f.read()
        self.cur.execute("INSERT INTO images (image_data) VALUES (%s)", (Binary(image_data),)) 
        self.conn.commit()   
    #Definimos la función que Injectara los datos de la estación meteologica radiologica
    ###############################################################################################################################################################################################
    def injectarCsvRadio(self, route):
        #lee el datalogger
        df=pd.read_csv(route,skiprows=[0,2,3])
        df.drop("RECORD",inplace=True,axis=1)
        try:
            df.to_sql('radio', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en radio")
    ################################################################################################################################################################################################
    
    #Definimos la función que injectara los datos del Skyscanner
    ##################################################################################################################################################################################################
    def injectarCsvSkyScanner(self, route):
        #lee el csv del skyscanner
        df=pd.read_csv(route,skiprows=8)
        fecha=pd.read_csv(route,nrows=3, names=[0,1])
        fechatip=fecha[1][2][2]+fecha[1][2][3]+fecha[1][2][5]+fecha[1][2][6]+fecha[1][2][8]+fecha[1][2][9]
        names=["sidedatehour","hour","date","sect1" ,"sect2" ,"sect3","sect4","sect5","sect6","sect7","sect8","sect9","sect10",
        "sect11","sect12","sect13","sect14","sect15","sect16","sect17","sect18","sect19","sect20" ,"sect21",
        "sect22" ,"sect23" ,"sect24" ,"sect25" ,"sect26" ,"sect27" ,"sect28" ,"sect29" ,"sect30" ,"sect31" ,
        "sect32" ,"sect33" ,"sect34" ,"sect35" ,"sect36" ,"sect37" ,"sect38" ,"sect39" ,"sect40" ,"sect41" ,
        "sect42" ,"sect43" ,"sect44" ,"sect45" ,"sect46" ,"sect47" ,"sect48" ,"sect49" ,"sect50" ,"sect51" ,
        "sect52" ,"sect53" ,"sect54" ,"sect55" ,"sect56" ,"sect57" ,"sect58" ,"sect59" ,"sect60" ,"sect61" ,
        "sect62" ,"sect63" ,"sect64" ,"sect65" ,"sect66" ,"sect67" ,"sect68" ,"sect69" ,"sect70" ,"sect71" ,
        "sect72" ,"sect73" ,"sect74" ,"sect75" ,"sect76" ,"sect77" ,"sect78" ,"sect79" ,"sect80" ,"sect81" ,
        "sect82" ,"sect83" ,"sect84" ,"sect85" ,"sect86" ,"sect87" ,"sect88" ,"sect89" ,"sect90" ,"sect91" ,
        "sect92" ,"sect93" ,"sect94" ,"sect95" ,"sect96" ,"sect97" ,"sect98" ,"sect99" ,"sect100" ,"sect101" ,
        "sect102" ,"sect103" ,"sect104" ,"sect105" ,"sect106" ,"sect107" ,"sect108" ,"sect109" ,"sect110" ,"sect111" ,
        "sect112" ,"sect113" ,"sect114" ,"sect115" ,"sect116" ,"sect117" ,"sect118" ,"sect119" ,"sect120" ,"sect121" ,
        "sect122" ,"sect123" ,"sect124" ,"sect125" ,"sect126" ,"sect127" ,"sect128" ,"sect129" ,"sect130" ,"sect131" ,
        "sect132" ,"sect133" ,"sect134" ,"sect135" ,"sect136" ,"sect137" ,"sect138" ,"sect139" ,"sect140" ,"sect141" ,
        "sect142" ,"sect143" ,"sect144" ,"sect145","azimut","elevacion"]
        df.columns=names
        df['sidedatehour']=df['sidedatehour']+","+fechatip+","+df['hour']+","+df['date']
        df['date']=fechatip
        df=df.replace('  ',np.nan)
        
        try:
            df.to_sql('skyscanner', con=self.engine, if_exists='append',index=False)
             #Hacer a futuro que se muestren atraves de la UI que son datos repetidos
        except sqlalchemy.exc.IntegrityError:
             print("Esos datos ya estan introducidos en el skyscanner")
    ####################################################################################################################################################################################################

    #Definimos la injección de los datos de la skycamera
    #####################################################################################################################################################################################################
    def injectarCsvSkycamera(self, route):
        #lee el csv de la skycamera
        df=pd.read_csv(route)
        try:
            df.to_sql('skycamera', con=self.engine, if_exists='append',index=False)
            #Hacer a futuro que se muestren atraves de la UI que son datos repetidos 
        except sqlalchemy.exc.IntegrityError:
            print("Esos datos ya estan introducidos en la Skycamera")
    #####################################################################################################################################################################################################    
    
    #Definimos una función que recoja los datos directamente de las carpetas en las que estan
    ######################################################################################################################################################################################################
    def actualizardatos(self):
        radio=os.listdir(self.dirradio)
        camera=os.listdir(self.dircamera)
        scanner=os.listdir(self.dirscanner)
        for datos in radio:
            self.injectarCsvRadio(self.dirradio+"\\"+datos)
        for datos in camera:
            self.injectarCsvSkycamera(self.dircamera+"\\"+datos)
        for datos in scanner:
            self.injectarCsvSkyScanner(self.dirscanner+"\\"+datos)
    ##################################################################################################################################################################################################### 

    #Definimos el Cierre de la conexión con la base de datos
    #####################################################################################################################################################################################################
    def stop(self):
        #Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
        self.cur.close()
        self.conn.close() 

