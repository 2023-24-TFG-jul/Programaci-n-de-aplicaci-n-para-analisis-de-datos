#Nombre: Prototipo
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.001
#Descripción: Por ahora nada
#########################################################################################################################
#Definimos los imports
import psycopg2

##########################################################################################################################
#Parametros de la base de datos
datahost="localhost"
dataname="postgres"
datauser="postgres"
datapass="1234"
dataport=5432

conn=psycopg2.connect(host=datahost,dbname=dataname, user=datauser, password=datapass,port=dataport)

cur=conn.cursor()
operacion="""CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY,name VARCHAR (255),age INT, gender CHAR ) """
cur.execute(operacion)
conn.commit()

cur.close()
conn.close()