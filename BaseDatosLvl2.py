#Nombre:BasedatosLvl2
#Autor:Álvaro Villar Val
#Fecha:20/02/24
#Versión:0.6.0
#Descripción: Base de datos de segundo nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
from BaseDatosLvl1 import BaseDatosLvl1
import sqlalchemy #import para pasar los datos en bulk
from sqlalchemy import create_engine #Import para pasar los datos en bulk
import pandas as pd #Import para pasar los datos en bulk
from Calculadora import Calculadora #Importamos la calculadora para poder hacer operaciones con los datos
#Inicializamos la Clase de creación de base de datos
class BaseDatosLvl2:

    #Definimos el constructor de la base de datos que hara la conexion con la base de sectos
    ####################################################################################################################
    def __init__(self):
        #Parametros de la base de datos
        self.dirradio="Datos\\datalogger" #path donde se meteran los archivos que se quieran meter en la base de datos radio
        self.dircamera="Datos\\sky-camera"#path donde se meteran los archivos que se quieran meter en la base de datos skycamera
        self.dirscanner="Datos\\Sky-scanner 2023_12"#path donde se meteran los archivos que se quieran meter en la base de datos skyscanner
        self.dirimgCam1="Datos\\Fotos\\CAM1\\imagenes"#path en el que se meteran las imagenes de la camara1 que se quiera introducir en la base de datos
        self.dirimgCam2="Datos\\Fotos\\CAM2\\imagenes"#path en el que se meteran las imagenes de la camara2 que se quieran introducir en la base de datos
        self.db1=BaseDatosLvl1() #Inicializamos la base de primer nivel
        self.datahost="localhost" #Host de la base de datos
        self.dataname="postgres"  #Nombre de la base de datos
        self.datauser="postgres"  #Nombre del usuario
        self.datapass="1234"      #Contraseña de la base de datos
        self.dataport=5432        #Puerto al que se conecta la base de datos
        self.conn=self.db1.conn #guardamos la connexión del primer nivel de datos ya que vamos a usar la misma base de datos
        self.cur=self.db1.cur   #guardamos a su vez el cursor de la base de datos
        self.calc=Calculadora() #Inicializamos la calculadora para poder hacer operaciones con los datos
        #inicializamdos la conexopn que usara sqlAlchemy para operar en la base de datos
        conn_string = f'postgresql://{self.datauser}:{self.datapass}@{self.datahost}:{self.dataport}/{self.dataname}'
        self.engine = create_engine(conn_string)
        #llamamos a la función crear la cual creara las tablas que no esten creadas en la base de datos
        self.crear()
    #######################################################################################################################

    #Definimos la función que creara las tablas de datos procesados
    #######################################################################################################################
    def crear(self):#No hace falta crear la de scanner ya que la de base esta bien
        #Creación de la tabla en caso de que no exista del skyscaner,
        #Sidedatehour tiene un formato de side,date(al estilo año-mes-día),horaini,horafin
        orden=""" CREATE TABLE IF NOT EXISTS skyscannerproc (side VARCHAR, hour time,date integer,sect1 decimal,sect2 decimal,
        sect3 decimal,sect4 decimal,sect5 decimal,sect6 decimal,sect7 decimal,sect8 decimal,sect9 decimal,sect10 decimal,sect11 decimal,sect12 decimal,
        sect13 decimal,sect14 decimal,sect15 decimal,sect16 decimal,sect17 decimal,sect18 decimal,sect19 decimal,sect20 decimal,sect21 decimal,
        sect22 decimal,sect23 decimal,sect24 decimal,sect25 decimal,sect26 decimal,sect27 decimal,sect28 decimal,sect29 decimal,sect30 decimal,sect31 decimal,
        sect32 decimal,sect33 decimal,sect34 decimal,sect35 decimal,sect36 decimal,sect37 decimal,sect38 decimal,sect39 decimal,sect40 decimal,sect41 decimal,
        sect42 decimal,sect43 decimal,sect44 decimal,sect45 decimal,sect46 decimal,sect47 decimal,sect48 decimal,sect49 decimal,sect50 decimal,sect51 decimal,
        sect52 decimal,sect53 decimal,sect54 decimal,sect55 decimal,sect56 decimal,sect57 decimal,sect58 decimal,sect59 decimal,sect60 decimal,sect61 decimal,
        sect62 decimal,sect63 decimal,sect64 decimal,sect65 decimal,sect66 decimal,sect67 decimal,sect68 decimal,sect69 decimal,sect70 decimal,sect71 decimal,
        sect72 decimal,sect73 decimal,sect74 decimal,sect75 decimal,sect76 decimal,sect77 decimal,sect78 decimal,sect79 decimal,sect80 decimal,sect81 decimal,
        sect82 decimal,sect83 decimal,sect84 decimal,sect85 decimal,sect86 decimal,sect87 decimal,sect88 decimal,sect89 decimal,sect90 decimal,sect91 decimal,
        sect92 decimal,sect93 decimal,sect94 decimal,sect95 decimal,sect96 decimal,sect97 decimal,sect98 decimal,sect99 decimal,sect100 decimal,
        sect101 decimal,sect102 decimal,sect103 decimal,sect104 decimal,sect105 decimal,sect106 decimal,sect107 decimal,sect108 decimal,sect109 decimal,
        sect110 decimal,sect111 decimal,sect112 decimal,sect113 decimal,sect114 decimal,sect115 decimal,sect116 decimal,sect117 decimal,sect118 decimal,
        sect119 decimal,sect120 decimal,sect121 decimal,sect122 decimal,sect123 decimal,sect124 decimal,sect125 decimal,sect126 decimal,sect127 decimal,
        sect128 decimal,sect129 decimal,sect130 decimal,sect131 decimal,sect132 decimal,sect133 decimal,sect134 decimal,sect135 decimal,sect136 decimal,
        sect137 decimal,sect138 decimal,sect139 decimal,sect140 decimal,sect141 decimal,sect142 decimal,sect143 decimal,sect144 decimal,sect145 decimal, 
        azimut decimal,elevacion decimal,sidedatehour VARCHAR (255) PRIMARY KEY); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tabla en caso de que no exista de la Skycamera de datos procesados
        #La primary key de esta tabla es time que se dividi en: año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS skycameraproc("GAIN" VARCHAR,"SHUTTER" VARCHAR(255),azimuth decimal,blocked integer,cloud_cover decimal,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust integer,elevation decimal,image VARCHAR,mode integer,temperature decimal,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY,date integer); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tablas en caso de que no exixta la radio de datos procesados
        #La primary key es timestamp la cual se divide en:año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS radioproc ("TIMESTAMP" VARCHAR PRIMARY KEY,"Year" integer,"Month" integer,"Dia" integer,"YearDay" integer,
        "Hour" integer,"Minute" integer,"BuPres_Avg" decimal,"BuRH_Avg" decimal,"BuTemp_Avg" decimal,"BuRain_Tot" decimal,"BuWS_Avg" decimal,
        "BuWD_Avg" decimal,"BuTDP_Avg" decimal,"BuTWB_Avg" decimal,"BuRaGVN_Avg" decimal,"BuRaGVE_Avg" decimal,"BuRaGVS_Avg" decimal,"BuRaGVW_Avg" decimal,
        "BuRaGH_Avg" decimal,"BuRaDH_Avg" decimal,"BuRaB_Avg" decimal,"BuLxGVN_Avg" decimal,"BuLxGVE_Avg" decimal,"BuLxGVS_Avg" decimal,"BuLxGVW_Avg" decimal,
        "BuLxGH_Avg" decimal,"BuLxDH_Avg" decimal,"BuLxB_Avg" decimal,"BuPaGVN_Avg" decimal,"BuPaGVE_Avg" decimal,"BuPaGVS_Avg" decimal,"BuPaGVW_Avg" decimal,
        "BuPaGH_Avg" decimal,"BuPaDH_Avg" decimal,"BuPaB_Avg" decimal,"BuUvGVN_Avg" decimal,"BuUvGVE_Avg" decimal, "BuUvGVS_Avg" decimal,
        "BuUvGVW_Avg" decimal,"BuUvGH_Avg" decimal,"BuUvDH_Avg" decimal,"BuUvB_Avg" decimal,"BuUvAGH_Avg" decimal,"BuUvADH_Avg" decimal,"BuUvAV_Avg" decimal,
        "BuUvBGH_Avg" decimal,"BuUvBDH_Avg" decimal,"BuUvBV_Avg" decimal,"BuUvEGH_Avg" decimal,"BuUvEDH_Avg" decimal,"BuUvEV_Avg" decimal,
        "BuRaDVN_Avg" decimal,"BuRaDVE_Avg" decimal,"BuRaDVS_Avg" decimal,"BuRaDVW_Avg" decimal,"BuRaAlUp_Avg" decimal,"BuRaAlDo_Avg" decimal,
        "BuRaAlbe_Avg" decimal,"BuPaR_Avg" decimal,"BuLxR_Avg" decimal,"BuIrGH_Avg" decimal,date integer,fallo varchar(250))"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
    ##########################################################################################################################################################

    #Definimos una función que actualice las imagenes
    ##########################################################################################################################################################
    def actualizarImg(self):
        cont=self.db1.actuimgCam1()
        return cont
    ##########################################################################################################################################################

    #Definimos una función que descargue las imagenes determinadas
    ##########################################################################################################################################################
    def descImg(self,date1,date2):
        self.db1.obtenerImg(date1,date2)
    ##########################################################################################################################################################

    #Definimos una función para que descargue los datos que queramos
    ##########################################################################################################################################################
    def descdat(self,selec,base,cond1,cond2):
        self.db1.descDat(selec,base,cond1,cond2)
    ##########################################################################################################################################################

    #Definimos una función qe actualice los datos de la base de datos y los procese al mismo tiempo
    ##########################################################################################################################################################
    def actualizardatos(self):
        #Recibimos de la función de de actialización de datos los datos que se hayan introducidos en el primer nivel de la base de datos

        radio,camera,scanner,contrad,contcamera,contscanner=self.db1.actualizardatos()
        #Recorremos todos los datos introducidos,comprobamos que no estan vacios y los procesamos e introducimoes en la segunda base de datos
        for dat in radio:
            if not dat.empty:
                self.actualizarRadio(dat)
        #Recorremos todos los datos introducidos,comprobamos que no estan vacios y los procesamos e introducimoes en la segunda base de datos
        for dat in camera:
            if not dat.empty:
                self.actualizarCammera(dat)
        #Recorremos todos los datos introducidos,comprobamos que no estan vacios y los procesamos e introducimoes en la segunda base de datos
        for dat in scanner:
            if not dat.empty:
                self.actualizarScanner(dat)
        return contrad,contcamera,contscanner
    ###########################################################################################################################################
    
    #Definimos una función que procese los datos de la radio
    ##########################################################################################################################################################
    def procdatos(self,date,gHI,dHI,dNI,gHIL,dHIL,dNIL,gHP,dHP,dNP,gHUV,dHUV,dNUV):
       
        result="{}".format(self.calc.comprobarghi(gHI,dHI,dNI,date))
        result=result+"{}".format(self.calc.comprobardhi(gHI,dHI,dNI,date))
        result=result+"{}".format(self.calc.comprobardni(gHI,dHI,dNI,date))
        result=result+"{}".format(self.calc.comprobarghil(gHIL,dHIL,dNIL,date))
        result=result+"{}".format(self.calc.comprobardhil(gHIL,dHIL,dNIL,date))
        result=result+"{}".format(self.calc.comprobardnil(gHIL,dHIL,dNIL,date))
        result=result+"{}".format(self.calc.comprobarghp(gHP,dHP,dNP,date))
        result=result+"{}".format(self.calc.comprobardhp(gHP,dHP,dNP,date))
        result=result+"{}".format(self.calc.comprobardnp(gHP,dHP,dNP,date))
        result=result+"{}".format(self.calc.comprobarghuv(gHUV,dHUV,dNUV,date))
        result=result+"{}".format(self.calc.comprobardhuv(gHUV,dHUV,dNUV,date))
        result=result+"{}".format(self.calc.comprobardnuv(gHUV,dHUV,dNUV,date))
        return result
    ##########################################################################################################################################################

    #Definimos la operación que añadira los nuevos datos procesados a la base de datos
    ##########################################################################################################################################################
    def actualizarRadio(self,df):
        df['fallo']=df[['TIMESTAMP','BuRaGH_Avg', 'BuRaDH_Avg','BuRaB_Avg','BuLxGH_Avg','BuLxDH_Avg','BuLxB_Avg','BuPaGH_Avg','BuPaDH_Avg','BuPaB_Avg','BuUvGH_Avg',
                        'BuUvDH_Avg','BuUvB_Avg']].apply(lambda row: self.procdatos(row['TIMESTAMP'],row['BuRaGH_Avg'], row['BuRaDH_Avg'], row['BuRaB_Avg'], row['BuLxGH_Avg'],
                         row['BuLxDH_Avg'], row['BuLxB_Avg'], row['BuPaGH_Avg'], row['BuPaDH_Avg'], row['BuPaB_Avg'], row['BuUvGH_Avg'], row['BuUvDH_Avg'], row['BuUvB_Avg']), axis=1)
        self.db1.comprNuevaCol(df,"radioproc")
        self.db1.comprTodasColumnas(df,"radioproc")
        try:

            #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior)
            #,y el index a False que no recuerdo para que sirve pero ponlo
            df.to_sql('radioproc', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #TODO Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en radioproc")
    ##########################################################################################################################################################

    #Definimos una funcón que actualice los datos de de la skycamera que se han introducido en la base de datos
    ##########################################################################################################################################################
    def actualizarCammera(self,df):
        df.dropna(subset=['image'], inplace=True)
        try:
            #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),
            #y el index a False que no recuerdo para que sirve pero ponlo
            df.to_sql('skycameraproc', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #TODO Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en la skycameraproc")
    ##########################################################################################################################################################
    
    #Definimos una función que introduzca los datos limpiados del skyscanner
    ##########################################################################################################################################################
    def actualizarScanner(self,df):
       
        df.dropna(subset=['side'], inplace=True)
        
        try:
            #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),
            #y el index a False que no recuerdo para que sirve pero ponlo
            df.to_sql('skyscannerproc', con=self.engine, if_exists='append',index=False)
        except sqlalchemy.exc.IntegrityError:
            #TODO Hacer a futuro que se muestren atraves de la UI que son datos repetidos
            print("Esos datos ya estan introducidos en la skyscannerproc")
    ##########################################################################################################################################################

    #Definimos una función para que de momento nos devuelva datos
    #########################################################################################################################################################
    def obtenerdat(self,selec,base,cond1,cond2):
        return self.db1.obtenerdat(selec,base,cond1,cond2)
    #########################################################################################################################################################
    
    #Definimos la operación de cierre de conexiones para evitar errores en las conexiones futuras
    #SIEMPRE USAR AL FINALIZAR EL PROGRAMA
    ##########################################################################################################################################################
    def stop(self):
        #Cerramos las conexiones del primer nivel de la base de datos
        self.cur.close()
        self.conn.close()
        self.db1.stop()