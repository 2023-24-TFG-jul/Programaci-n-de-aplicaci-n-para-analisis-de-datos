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
# db1=BaseDatosLvl1()
# db1.injectarimg("Datos\Fotos\\201D_CAM1_20231005_085100_02.jpg","Datos\Fotos\\1.jpg")
# print(db1.obtenerdat("*","images",None,None))
# db1.obtenerImg(240220)
with open("Datos\Fotos\\201D_CAM1_20231005_085100_02.jpg", 'rb') as f:
            image1_data = f.read()
with open("Datos\Fotos\\1.jpg", 'rb') as f:
            image2_data = f.read()
img1=psycopg2.Binary(image1_data)
img2=psycopg2.Binary(image2_data)
print(img1[0])
print(img2[0])
with open("Fotos resulta\\foto1.jpg", 'wb') as file:
                file.write(img1[0])
with open("Fotos resulta\\foto2.jpg", 'wb') as file:
                file.write(img2[0])
# db1.actualizardatos()
# datos1=db1.obtenerdat("*","radio","23-10-01","23-10-01")
# datos2=db1.obtenerdat("*","skyscanner","23-12-01","23-12-02")
# datos3=db1.obtenerdat("*","skycamera","23-10-01","23-10-02")
# print(datos1)
# print(datos2)
# print(datos3)
#db1.stop()

