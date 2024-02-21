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
##########################################################################################################################
#Parametros de la base de datos
db1=BaseDatosLvl1()
#db1.injectarimg("Datos\Fotos\\201D_CAM1_20231005_085100_02.jpg","Datos\Fotos\\1.jpg")
# print(db1.obtenerdat("*","images",None,None))
# db1.obtenerImg(240220)
datahost="localhost" #Host de la base de datos
dataname="postgres"  #Nombre de la base de datos
datauser="postgres"  #Nombre del usuario
datapass="1234"      #Contraseña de la base de datos
dataport=5432        #Puerto al que se conecta la base de datos
conn=psycopg2.connect(host=datahost,dbname=dataname, user=datauser, password=datapass,port=dataport)
cur=conn.cursor() 
orden="CREATE TABLE IF NOT EXISTS img_table(id SERIAL PRIMARY KEY, label TEXT, data BYTEA);"
cur.execute(orden)
conn.commit()
inp = open("Datos\Fotos\\201D_CAM1_20231005_085100_02.jpg", 'rb') 
image = inp.read() 
img1=psycopg2.Binary(image)
cur.execute("INSERT INTO img_table(label,data) VALUES (%s,%s)", ("image1", img1,)) 
conn.commit()
cur.execute("SELECT image1_data,image2_data FROM images")
conn.commit()
data = cur.fetchone()

print (data[0])
out=open("Fotos resulta\\foto1.jpg", 'wb')
out.write(data[0])
print (data[1])
out=open("Fotos resulta\\foto2.jpg", 'wb')
out.write(data[1])
# db1.actualizardatos()
# datos1=db1.obtenerdat("*","radio","23-10-01","23-10-01")
# datos2=db1.obtenerdat("*","skyscanner","23-12-01","23-12-02")
# datos3=db1.obtenerdat("*","skycamera","23-10-01","23-10-02")
# print(datos1)
# print(datos2)
# print(datos3)
db1.stop()

