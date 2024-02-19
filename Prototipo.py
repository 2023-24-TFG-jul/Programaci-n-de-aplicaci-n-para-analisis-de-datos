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
db1.actualizardatos()
datos1=db1.obtenerdat("*","radio","23-10-01","23-10-01")
datos2=db1.obtenerdat("*","skyscanner","23-12-01","23-12-02")
datos3=db1.obtenerdat("*","skycamera","23-10-01","23-10-02")
print(datos1)
print(datos2)
print(datos3)
db1.stop()

