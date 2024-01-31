#Nombre:BaseDatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.15
#Descripción: Por ahora nada
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
    def obtenerdat(self,ini,fin):
        orden=""" """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
    ######################################################################################################################

    #Actualizamos la base de datos con los ultimos datos que hayamos obtenido
    ##########################################################################################################################   
    def actualizar(self):
        orden=""" """
        #Enviamos la operación a la base de datos
        self.cur.execute(orden)
        self.conn.commit()
    #Definimos el Cierre de la conexión con la base de datos
    def stop(self):
        #Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
        self.cur.close()
        self.conn.close() 

