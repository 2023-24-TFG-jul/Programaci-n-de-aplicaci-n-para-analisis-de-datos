#Nombre:BaseDatosLvl1
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.1
#Descripción: Por ahora nada
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd

#Inicializamos la Clase de creación de base de datos
class BaseDatosLlv1:
    #Definimos el constructor de la base de datos que hara la conexion con la base de datos
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
