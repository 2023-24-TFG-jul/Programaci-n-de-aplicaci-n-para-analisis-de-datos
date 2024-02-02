#Nombre: Prototipo
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.003
#Descripción: Por ahora nada
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd
##########################################################################################################################
#Parametros de la base de datos
datahost="localhost"
dataname="postgres"
datauser="postgres"
datapass="1234"
dataport=5432
#Establecemos la conexion con la base de datos
conn=psycopg2.connect(host=datahost,dbname=dataname, user=datauser, password=datapass,port=dataport)
#Inicializamos el cursor con el que operaremos en la base de datos
cur=conn.cursor()
#Guardamos una operación en forma de string 
operacion="""CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY,name VARCHAR (255),age INT, gender CHAR ) """
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()
operacion="""SELECT * FROM person """
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()
print(cur.fetchall())
operacion="""INSERT INTO person (id,name,age,gender) Values (72345049,'Federico',23,'M') """
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()
operacion="""SELECT * FROM person """
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()
print(cur.fetchall())



#Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
cur.close()
conn.close()