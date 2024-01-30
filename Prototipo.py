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
    

conn=psycopg2.connect(host="localhost",dbname="postgres", user="postgres", password="1234",port=5432)

cur=conn.cursor()
operacion="""CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY,name VARCHAR (255),age INT, gender CHAR ) """
cur.execute(operacion)
conn.commit()

cur.close()
conn.close()