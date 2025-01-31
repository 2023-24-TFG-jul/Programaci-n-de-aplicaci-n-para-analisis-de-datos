#Nombre:BasedatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:1.1.4
#Descripción: Base de datos de primer nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
import psycopg2 #Import para la conexión la base de datos
import pandas as pd #Import para gestion de datos
from sqlalchemy import create_engine #Import para pasar los datos en bulk
import sqlalchemy #import para pasar los datos en bulk
import os #import para leer los archivos en un directorio especificado
import numpy as np #Import para operar con los datos de pandas
from Log import Log
from sqlalchemy.exc import DataError
#Inicializamos la Clase de creación de base de datos
class BaseDatosLvl1:

############################################################################################################################################
#Zona de Creación de la base de datos

    #Definimos el constructor de la base de datos que hara la conexion con la base de sectos
    ####################################################################################################################
    def __init__(self):
        #Parametros de la base de datos
        self.dirradio="Datos\\datalogger" #path donde se meteran los archivos que se quieran meter en la base de datos radio
        self.dircamera="Datos\\sky-camera"#path donde se meteran los archivos que se quieran meter en la base de datos skycamera
        self.dirscanner="Datos\\Sky-scanner 2023_12"#path donde se meteran los archivos que se quieran meter en la base de datos skyscanner
        self.dirimgCam1="Datos\\Fotos\\CAM1\\imagenes"#path en el que se meteran las imagenes de la camara1 que se quiera introducir en la base de datos
        self.dirimgCam2="Datos\\Fotos\\CAM2\\imagenes"#path en el que se meteran las imagenes de la camara2 que se quieran introducir en la base de datos
        self.datahost="localhost" #Host de la base de datos
        self.dataname="postgres"  #Nombre de la base de datos
        self.datauser="postgres"  #Nombre del usuario
        self.datapass="1234"      #Contraseña de la base de datos
        self.dataport=5432        #Puerto al que se conecta la base de datos
        #Establecemos la conexion con la base de datos atraves psycog2
        self.conn=psycopg2.connect(host=self.datahost,dbname=self.dataname, user=self.datauser, password=self.datapass,port=self.dataport)
        #Inicializamos el cursor con el que operaremos en la base de datos
        self.cur=self.conn.cursor()
        #inicializamdos la conexopn que usara sqlAlchemy para operar en la base de datos
        conn_string = f'postgresql://{self.datauser}:{self.datapass}@{self.datahost}:{self.dataport}/{self.dataname}'
        self.engine = create_engine(conn_string)
        self.log=Log()
        self.log.limpiarLog()
        #llamamos a la función crear la cual creara las tablas que no esten creadas en la base de datos
        self.crear()
    ########################################################################################################################

    #Creamos las tablas de la base de datos la base de datos con los ultimos datos que hayamos obtenido
    ##########################################################################################################################
    def crear(self):
        #Creación de la tabla en caso de que no exista del skyscaner,
        #Sidedatehour tiene un formato de side,date(al estilo año-mes-día),horaini,horafin
        orden=""" CREATE TABLE IF NOT EXISTS skyscanner (side VARCHAR, hour time,date bigint,sect1 decimal,sect2 decimal,
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
        #Creación de las tabla en caso de que no exista de la Skycamera
        #La primary key de esta tabla es time que se divide en: año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS skycamera("GAIN" VARCHAR,"SHUTTER" VARCHAR(255),azimuth decimal,blocked integer,cloud_cover decimal,
        cloud_cover_msg VARCHAR(255),cloudimg VARCHAR(255),dust integer,elevation decimal,image VARCHAR,mode integer,temperature decimal,
        thumbnail VARCHAR,time VARCHAR PRIMARY KEY,date bigint); """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de las tablas en caso de que no exixta la radio
        #La primary key es timestamp la cual se divide en:año-mes-día hora
        orden=""" CREATE TABLE IF NOT EXISTS radio ("TIMESTAMP" VARCHAR PRIMARY KEY,"Year" integer,"Month" integer,"Dia" integer,"YearDay" integer,
        "Hour" integer,"Minute" integer,"BuPres_Avg" decimal,"BuRH_Avg" decimal,"BuTemp_Avg" decimal,"BuRain_Tot" decimal,"BuWS_Avg" decimal,
        "BuWD_Avg" decimal,"BuTDP_Avg" decimal,"BuTWB_Avg" decimal,"BuRaGVN_Avg" decimal,"BuRaGVE_Avg" decimal,"BuRaGVS_Avg" decimal,"BuRaGVW_Avg" decimal,
        "BuRaGH_Avg" decimal,"BuRaDH_Avg" decimal,"BuRaB_Avg" decimal,"BuLxGVN_Avg" decimal,"BuLxGVE_Avg" decimal,"BuLxGVS_Avg" decimal,"BuLxGVW_Avg" decimal,
        "BuLxGH_Avg" decimal,"BuLxDH_Avg" decimal,"BuLxB_Avg" decimal,"BuPaGVN_Avg" decimal,"BuPaGVE_Avg" decimal,"BuPaGVS_Avg" decimal,"BuPaGVW_Avg" decimal,
        "BuPaGH_Avg" decimal,"BuPaDH_Avg" decimal,"BuPaB_Avg" decimal,"BuUvGVN_Avg" decimal,"BuUvGVE_Avg" decimal, "BuUvGVS_Avg" decimal,
        "BuUvGVW_Avg" decimal,"BuUvGH_Avg" decimal,"BuUvDH_Avg" decimal,"BuUvB_Avg" decimal,"BuUvAGH_Avg" decimal,"BuUvADH_Avg" decimal,"BuUvAV_Avg" decimal,
        "BuUvBGH_Avg" decimal,"BuUvBDH_Avg" decimal,"BuUvBV_Avg" decimal,"BuUvEGH_Avg" decimal,"BuUvEDH_Avg" decimal,"BuUvEV_Avg" decimal,
        "BuRaDVN_Avg" decimal,"BuRaDVE_Avg" decimal,"BuRaDVS_Avg" decimal,"BuRaDVW_Avg" decimal,"BuRaAlUp_Avg" decimal,"BuRaAlDo_Avg" decimal,
        "BuRaAlbe_Avg" decimal,"BuPaR_Avg" decimal,"BuLxR_Avg" decimal,"BuIrGH_Avg" decimal,date bigint)"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
        #Creación de la base de datos de las imagenes
        orden=""" CREATE TABLE IF NOT EXISTS imagescam1 (name VARCHAR PRIMARY KEY,date bigint,image1_data bytea);"""
        #Enviamos la operación a la base de dactos
        self.cur.execute(orden)
        self.conn.commit()
    #################################################################################################################################################

#####################################################################################################################################################
#Zona de Obtención y descarga de datos

    #Obtenemos los datos de una tabla especifica que se pasa por base a las columna que se pase por select y entre las fechas que se pasen
    #atraves de cond1 y cond2
    #Cond1 y cond2 tienes que pasarse con el estil año(sin el 20)-mes(de dos cifras siempre)-dia(de dos cifras siempre) y en string
    ####################################################################################################################
    def obtenerdat(self,selec,base,cond1,cond2):
        # Nos aseguramos que la tabla que se pasa por base es una de las que tenemos en la base de datos
        tablas = ["radio", "radioproc", "imagescam1", "skycamera", "skycameraproc", "skyscanner", "skyscannerproc"]
        if base not in tablas:
            self.log.injeErr("Tabla no existente en la base de datos\n")
            raise ValueError("Tabla no existente en la base de datos")

        # Obtenemos los nombres de las columnas de la tabla que se pasa por base
        if selec != "*":
            #Conseguimos todos los nombres de las columnas de la tabla que se pasa por base
            colum = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
            self.cur.execute(colum, (base,))
            columnastot = [column[0] for column in self.cur.fetchall()]
            if "," in selec:
                selec = selec.split(",")
                if not set(selec).issubset(set(columnastot)):
                    self.log.injeErr("Algunas Columnas no existen en la tabla\n")
                    raise ValueError("Algunas Columnas no existen en la tabla")
                for i in range(len(selec)):
                    selec[i]=""" " """+selec[i]+""" " """
                columnas = ', '.join(selec)
            else:
                if selec not in columnastot:
                    self.log.injeErr("Algunas Columnas no existen en la tabla\n")
                    raise ValueError("Algunas Columnas no existen en la tabla")
                columnas = """ " """+selec+""" " """
        else:
            columnas = "*"

        #usamos replace para eliminar los guiones y que sea igual que la fecha tipada
        if cond1!="" and cond2!="":
            cond1=cond1.replace('-', '')
            cond2=cond2.replace('-', '')
            cond1=cond1+"0000"
            cond2=cond2+"2359"
            columnas=columnas.replace(" ", "")
            query="SELECT {} FROM {} WHERE date BETWEEN %s AND %s".format(columnas, base)
            #Recogemos los datos en un data frame
            with self.engine.connect() as db_conn:
                data = pd.read_sql(sql=query, params=(cond1, cond2), con=db_conn)
                df=pd.DataFrame(data)
        else:
            self.log.injeErr("No se ha introducido fechas correctamente")
            raise DataError("No se ha introducido fechas correctamente")
        
        #Devolvemos los datos que se encuentran en esa tabla
        return df
    ######################################################################################################################

    #Descargamos los datos de una tabla especifica que se pasa por base a las columna que se pase por select y entre las
    #fechas que se pasen atraves de cond1 y cond2
    #Cond1 y cond2 tienes que pasarse con el estil año(sin el 20)-mes(de dos cifras siempre)-dia(de dos cifras siempre) y en string
    ######################################################################################################################
    def descDat(self,selec,base,cond1,cond2):
        #Obtenemos el dataframe de los datos que queremos
        df=self.obtenerdat(selec,base,cond1,cond2)
        #Guardamos en la dirección que queramos guardar los archivos en formato tabla,fechainicio,fechafinal
        df.to_csv("DatosResulta\\{},{},{}.csv".format(base,cond1,cond2), index=False)
    #######################################################################################################################

    #Definimos un metodo para recuperar la imagen que hemos guardado en la base de datos
    #Cond1 y cond2 tienes que pasarse con el estilo:
    #Año(sin el 20)-mes(de dos cifras siempre)-dia(de dos cifras siempre)-hora(en dos cifras y en 24h) y en string
    #########################################################################################################################
    def obtenerImg(self,date1,date2):
        #usamos replace para eliminar los guiones y que sea igual que la fecha tipada
        date1=date1.replace('-', '')
        date2=date2.replace('-', '')
        date1=date1+"00"
        date2=date2+"23"
        #Hacemos la consulta para obtener las filas con la información en bits de las imagenes
        query="SELECT name,image1_data FROM imagescam1 WHERE date BETWEEN %s AND %s"
        #Ejecutamos la consulta
        self.cur.execute(query, (date1, date2))
        self.conn.commit()
        #guardamos las filas que estaban guardadas en el cursor
        record=self.cur.fetchall()
        #Creamos un contador para que cuente la cantidad de imagenes que guardamos
        for i in record:#recorremos la tupla de imagenes
            filename = i[0].replace("'", "")  # eliminamos las comillas simples del nombre del archivo
            file=open("FotosResulta\\{}".format(filename), 'wb') #Creamos un archivo para guardar la imagen
            file.write(i[1]) #guardamos los datos de la imagen
    ############################################################################################################################

#################################################################################################################################
#Zona de injección y actualización de imagenes
                    
    #Definimo la función para injectar las imagenes en la base de datos
    ##############################################################################################################################
    def injectarimg(self,nombre,fecha,route1):
        comprob=False
        #abrimos la imagen en la ruta que recibimos
        with open(route1, 'rb') as f:
            image1_data = f.read()
        #abrimos la segunda imagen de la ruta que recibimos
        #insertamos la imagen en formato binario para que se pueda guardar con el nombre que tiene originalmente y la fecha en la que estaba guardada
        orden="INSERT INTO imagescam1 (name,date,image1_data) VALUES (%s,%s,%s)"
        try:
            self.cur.execute(orden, (nombre, fecha, psycopg2.Binary(image1_data)))
        except psycopg2.errors.UniqueViolation:
            comprob= True
        self.conn.commit()
        return comprob
    #############################################################################################################################################
    
    #Definimos una función que actualice la base de datos de las imagenes
    #############################################################################################################################################
    def actuimgCam1(self):
        cont=0
        #Hacemos uso de todos estos for para ser capaces de recorrer todo el arbol de ficheros donde se guardan las imagenes
        for fold1 in os.listdir(self.dirimgCam1):#Años
            for fold2 in os.listdir(self.dirimgCam1+"\\"+fold1):#Meses
                for fold3 in os.listdir(self.dirimgCam1+"\\"+fold1+"\\"+fold2):#Días
                    for fold4 in os.listdir(self.dirimgCam1+"\\"+fold1+"\\"+fold2+"\\"+fold3):#Horas
                        for file in os.listdir(self.dirimgCam1+"\\"+fold1+"\\"+fold2+"\\"+fold3+"\\"+fold4):#Imagenes
                            #Formamos la dirección en la que estamos juntando el nombre de todas las carpetas por las que hemos pasado
                            dirección=self.dirimgCam1+"\\"+fold1+"\\"+fold2+"\\"+fold3+"\\"+fold4+"\\"+file
                            #Formamos tambien la fecha con ellas
                            date=fold1[2]+fold1[3]+fold2+fold3+fold4
                            #Injectamos la imagen en la base de datos con los datos que hemos obtenido
                            
                            comprobador=self.injectarimg(""" '{}' """.format(file),date,dirección)
                            if (comprobador):
                               cont+=1
                               self.log.injeErr("psycopg2.errors.UniqueViolation: llave duplicada viola restricción de unicidad\n")
        return cont
    ##############################################################################################################################################

##################################################################################################################################################
#Zona de injección y actualización de datos
    
    #Definimos una función que recoja los datos directamente de las carpetas en las que estan
    ##############################################################################################################################################
    def actualizardatos(self):
        #Tomamos todos los archivos en el directorio de radio y guardamos sus nombre en una lista
        radio=os.listdir(self.dirradio)
        #Tomamos todos los archivos en el directorio de camera y guardamos sus nombre en una lista
        camera=os.listdir(self.dircamera)
        #Tomamos todos los archivos en el directorio de canner y guardamos sus nombre en una lista
        scanner=os.listdir(self.dirscanner)
        radiodat=[]
        cameradat=[]
        scannerdat=[]
        contrad=0
        contcamera=0
        contScanner=0
        for datos in radio: #recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de
            
            try:#Cazamos el error en caso de que estemos introduciendo datos repetidos
                #tomamos el dataframe que hayamos introducido para pasarlo de vuelta al segundo nivel de la base de datos
                df=self.injectarCsvRadio(self.dirradio+"\\"+datos)
                
            except sqlalchemy.exc.IntegrityError: #Si hay archivos repetidos
                contrad+=1 #Añadimos 1 al contador de errores
                df=pd.DataFrame({'A' : []})#establecemos el df a uno vacio
                self.log.injeErr("sqlalchemy.exc.IntegrityError:PrimaryKeyRepetida\n")
            radiodat.append(df)#introducimos los datos a la tabla de radio
        for datos in camera:#recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de datos

            try:#Cazamos el error en caso de que estemos introduciendo datos repetidos
                #tomamos el dataframe que hayamos introducido para pasarlo de vuelta al segundo nivel de la base de datos
                df=self.injectarCsvSkycamera(self.dircamera+"\\"+datos)#introducimos los datos a la tabla de camera

            except sqlalchemy.exc.IntegrityError: #Si hay archivos repetidos
                contcamera+=1 #Añadimos 1 al contador de errores
                df=pd.DataFrame({'A' : []}) #establecemos el df a uno vacio
                self.log.injeErr("sqlalchemy.exc.IntegrityError:PrimaryKeyRepetida\n")
            cameradat.append(df) #introducimos los datos a la tabla de camera
        for datos in scanner:#recorremos la lista para ir introduciendo los datos a las distintas tablas de las bases de datos
            try:#Cazamos el error en caso de que estemos introduciendo datos repetidos
                #tomamos el dataframe que hayamos introducido para pasarlo de vuelta al segundo nivel de la base de datos
                df=self.injectarCsvSkyScanner(self.dirscanner+"\\"+datos)#introducimos los datos a la tabla de scanner

            except sqlalchemy.exc.IntegrityError: #Si hay archivos repetidos
                contScanner+=1 #Añadimos 1 al contador de errores
                df=pd.DataFrame({'A' : []})#establecemos el df a uno vacio
                self.log.injeErr("sqlalchemy.exc.IntegrityError:PrimaryKeyRepetida\n")
            scannerdat.append(df)#introducimos los datos a la tabla de scanner
        #Devolvemos los datos que hemos intoducido para que se procesen a su vez y los errores ocurridos para sacarlos por pantalla
        return radiodat,cameradat,scannerdat,contrad,contcamera,contScanner
    ################################################################################################################################

    #Definimos la función que Injectara los datos de la estación meteologica radiologica
    #################################################################################################################################
    def injectarCsvRadio(self, route):
        #lee el datalogger saltandose las filas que no nos interesan, como el titulo(0), las unidades(2), las avrg(3)
        df=pd.read_csv(route,skiprows=[0,2,3])

        #eliminamos la columna record ya que no nos interesa
        df.drop("RECORD",inplace=True,axis=1)

        #establecemos una nueva columna llamada date para tener una manera facil y estandarizada de acceso a los datos
        #Para ello tomamos la fecha de time y nos quedamos con la fecha de días y la tipamos a AñoMesDía
        df['date']=df['TIMESTAMP'].str.slice(2,10)+df['TIMESTAMP'].str.slice(11,16)
        df['date']= df['date'].str.replace('-', '')
        df['date']= df['date'].str.replace(':', '')

        self.comprNuevaCol(df,"radio")
        self.comprTodasColumnas(df,"radio")
        #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),
        #y el index a False que no recuerdo para que sirve pero ponlo
        df.to_sql('radio', con=self.engine, if_exists='append',index=False)
            
            
        return df

    ########################################################################################################################################
    
    #Definimos la función que injectara los datos del Skyscanner
    ########################################################################################################################################
    def injectarCsvSkyScanner(self, route):
        #lee el csv del skyscanner
        df=pd.read_csv(route,skiprows=8)#Leemos el csv saltandonos las 8 primeras lineas ya que no son lineas de dato si no información del csv
        fecha=pd.read_csv(route,nrows=3, names=[0,1]) #recomes las primeras filas para hallar la fecha de las mediciones
        #Hacemos el tipado de la fechas (añomesdía) y lo hacemos cogiendo solo los caracteres que nos interesan en la fecha que nos da el csv
        fechatip=fecha[1][2][2]+fecha[1][2][3]+fecha[1][2][5]+fecha[1][2][6]+fecha[1][2][8]+fecha[1][2][9]
        #tambien hay que cmabiarle los nombres a las columnas para que coincidan con los de la base de datos y sean más manejables
        names=["side","hour","date","sect1" ,"sect2" ,"sect3","sect4","sect5","sect6","sect7","sect8","sect9","sect10",
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
        #Cambiamos los nombre que hemos guardado antes en una lista
        df.columns=names
        #Cambiamos la columna sidedatehour para que sea lo que su nombre indica y no solo el lado
        df['sidedatehour']=df['side']+","+fechatip+","+df['hour']+","+df['date']
        #Modificamos la columna date para que contenga la fecha de las mediciones
        df['date']=fechatip+df['hour'].str.slice(0,5)
        df['date']= df['date'].str.replace('-', '')
        df['date']= df['date'].str.replace(':', '')
        #Como en este csv hay espacios en blancos donde debria haber nulos, sustituimos estos espacios por nulos
        df=df.replace('  ',np.nan)

        #Cazamos la excepción en caso de que se metan datos repetidos
        df.to_sql('skyscanner', con=self.engine, if_exists='append',index=False)
        return df
    ############################################################################################################################################

    #Definimos la injección de los datos de la skycamera
    ############################################################################################################################################
    def injectarCsvSkycamera(self, route):
        #lee el csv de la skycamera y no hace falta modificar nada ya que de por si ya es compatible con la base de datos
        df=pd.read_csv(route)
        #establecemos una nueva columna llamada date para tener una manera facil y estandarizada de acceso a los datos
        #Para ello tomamos la fecha de time y nos quedamos con la fecha de días y la tipamos a AñoMesDía
        df['date']=df['time'].str.slice(2,10)+df['time'].str.slice(11,16)
        df['date']= df['date'].str.replace('-', '')
        df['date']= df['date'].str.replace(':', '')
        #Metemos en to_sql: nombre de la tabla, la conexion de sqlalchemy, append (para que no elimine lo anterior),
        #y el index a False que no recuerdo para que sirve pero ponlo
        df.to_sql('skycamera', con=self.engine, if_exists='append',index=False)
        return df
    ################################################################################################################################################
   
   #Definimos una función que en caso de un csv tiene una columna nueva la añada a la base de datos
   #################################################################################################################################################
    def comprNuevaCol(self,df,base):
        #comprobamos si hay nuevas columnas en el csv que no esten en la base de datos
        #Conseguimos todos los nombres de las columnas de la tabla que se pasa por base
        colum = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
        self.cur.execute(colum, (base,))
        columnastot = [column[0] for column in self.cur.fetchall()]
        columnas = df.columns
        tables="SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        self.cur.execute(tables)
        tablas = [column[0] for column in self.cur.fetchall()]
        if base in tablas:
            for i in columnas:
                if i not in columnastot:
                    nuevCol=""" " """+i+""" " """
                    nuevCol=nuevCol.replace(" ", "")
                    orden = f"ALTER TABLE {base} ADD COLUMN {nuevCol} decimal"
                    self.cur.execute(orden)
                    self.conn.commit() 
    #################################################################################################################################################

    #Definimos una función que comparara las columnas de un csv con las de la base de datos y en caso de que falte alguna en el dataframe la añada y la rellena de 0
    #################################################################################################################################################
    def comprTodasColumnas(self,df,base):
        colum = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
        self.cur.execute(colum, (base,))
        columnastot = [column[0] for column in self.cur.fetchall()]
        columnas = df.columns
        for i in columnastot:
            if i not in columnas:
                df[i]=0
###################################################################################################################################################
#Zona de Finalizaión de la aplicación

    #Definimos el Cierre de la conexión con la base de datos
    ###############################################################################################################################################
    def stop(self):
        #Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
        self.cur.close()
        self.conn.close()

####################################################################################################################################################
