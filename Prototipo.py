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
operacion="""DROP TABLE IF EXISTS person"""
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()
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
name=['Hugo','Martín','Lucas','Mateo','Leo' ,'Daniel','Alejandro','Pablo','Manuel','Álvaro','Adrián','David','Mario','Enzo','Diego' ]
for i in range(15):
    operacion="""INSERT INTO person (id,name,age,gender) Values (%s,%s,%s,%s) """
    gender='M'
    if ((i%2)!= 0):
        gender='F'
    value_insert=(i, name[i],i*5,gender)
    #Enviamos la operación a la base de datos
    cur.execute(operacion,value_insert)
    conn.commit()
operacion="""SELECT * FROM person """
#Enviamos la operación a la base de datos
cur.execute(operacion)
conn.commit()



#Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
cur.close()
conn.close()