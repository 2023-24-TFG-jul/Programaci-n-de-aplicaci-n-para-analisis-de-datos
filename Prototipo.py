#Nombre: Prototipo
#Autor:Álvaro Villar Val
#Fecha:25/01/24
#Versión:0.003
#Descripción: Algo habra que
#########################################################################################################################
#Definimos los imports
import psycopg2
import pandas as pd
from BaseDatosLvl1 import BaseDatosLvl1
from psycopg2 import sql
from sqlalchemy import create_engine
##########################################################################################################################
#Parametros de la base de datos
datahost="localhost"
dataname="postgres"
datauser="postgres"
datapass="1234"
dataport=5432
import psycopg2 
import pandas as pd 
from sqlalchemy import create_engine 


conn_string = 'postgresql://postgres:1234@localhost/postgres'

db = create_engine(conn_string) 
conn = db.connect() 


# our dataframe 
data = {'Name': ['Tom', 'dick', 'harry'], 
		'Age': [22, 21, 24]} 

# Create DataFrame 
df = pd.DataFrame(data) 
df.to_sql('data', con=conn, if_exists='replace', 
		index=False) 
conn = psycopg2.connect(conn_string 
						) 
conn.autocommit = True
cursor = conn.cursor() 

sql1 = '''select * from data;'''
cursor.execute(sql1) 
for i in cursor.fetchall(): 
	print(i) 

# conn.commit() 
conn.close() 

 
#Establecemos la conexion con la base de datos
# conn=psycopg2.connect(host=datahost,dbname=dataname, user=datauser, password=datapass,port=dataport)
# #Inicializamos el cursor con el que operaremos en la base de datos
# cur=conn.cursor()
# db1=BaseDatosLvl1()
# tablas=['skyscanner','skycamera','radio']
# for tab in tablas:
#     print(db1.obtenerdat(tab))
# df=pd.read_csv("Datos\datalogger\CR3000_J_OCTUBRE_2023.dat",skiprows=[0,2,3])
# df.to_sql("radio",con=conn,if_exists="append")
# df2=pd.read_sql_query("""SELECT * FROM radio;""")
# print(df2)
# db1.stop()
# operacion="""DROP TABLE IF EXISTS person"""
# #Enviamos la operación a la base de datos
# cur.execute(operacion)
# conn.commit()
# #Guardamos una operación en forma de string 
# operacion="""CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY,name VARCHAR (255),age INT, gender CHAR ) """
# #Enviamos la operación a la base de datos
# cur.execute(operacion)
# conn.commit()
# operacion="""SELECT * FROM person """
# #Enviamos la operación a la base de datos
# cur.execute(operacion)
# conn.commit()
# print(cur.fetchall())
# name=['Hugo','Martín','Lucas','Mateo','Leo' ,'Daniel','Alejandro','Pablo','Manuel','Álvaro','Adrián','David','Mario','Enzo','Diego' ]
# for i in range(15):
#     operacion="""INSERT INTO person (id,name,age,gender) Values (%s,%s,%s,%s) """
#     gender='M'
#     if ((i%2)!= 0):
#         gender='F'
#     value_insert=(i, name[i],i*5,gender)
#     #Enviamos la operación a la base de datos
#     cur.execute(operacion,value_insert)
#     conn.commit()
# operacion="""SELECT * FROM person """
# #Enviamos la operación a la base de datos
# cur.execute(operacion)
# conn.commit()
# personas=cur.fetchall()
# old=[]
# young=[]
# male=[]
# female=[]
# for pep in personas:
#     if pep[3] =='M':
#         male.append(pep)
#     else:
#         female.append(pep)
#     if(pep[2]>18):
#         old.append(pep)
#     else:
#         young.append(pep)
# print("\nLos hombre en la base de datos son:\n")
# print(male)
# print("\nLas mujeres en la base de datos son:\n")
# print(female)
# print("\nLos mayores en la base de datos son:\n")
# print(old)
# print("\nLos menores en la base de datos son:\n")
# print(young)




#Cerramos el cursor que vamos a utilizar y la conexión para que no nos de errores cuando los queramos volver a usar
#cur.close()
conn.close()
