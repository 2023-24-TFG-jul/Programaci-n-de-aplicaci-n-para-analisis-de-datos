#Nombre:BasedatosLvl2
#Autor:Álvaro Villar Val
#Fecha:20/02/24
#Versión:0.0.1
#Descripción: Base de datos de segundo nivel de una central meteorologica de la Universidad de burgos
#########################################################################################################################
#Definimos los imports
from BaseDatosLvl1 import BaseDatosLvl1
class BaseDatosLvl2:
    def __init__(self):
        #Parametros de la base de datos
        self.db1=BaseDatosLvl1() #Inicializamos la base de primer nivel
        self.datahost="localhost" #Host de la base de datos
        self.dataname="postgres"  #Nombre de la base de datos
        self.datauser="postgres"  #Nombre del usuario
        self.datapass="1234"      #Contraseña de la base de datos
        self.dataport=5432        #Puerto al que se conecta la base de datos

        self.conn=self.db1.conn #guardamos la connexión del primer nivel de datos ya que vamos a usar la misma base de datos
        self.cur=self.db1.cur   #guardamos a su vez el cursor de la base de datos

    def stop(self):
        #Cerramos las conexiones del primer nivel de la base de datos
        self.db1.stop()