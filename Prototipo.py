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
from BaseDatosLvl2 import BaseDatosLvl2
from psycopg2 import sql
from sqlalchemy import create_engine
##########################################################################################################################
#Parametros de la base de datos
db2=BaseDatosLvl2()
db2.actualizardatos()
data=db2.obtenerdat("*","skycameraproc","23-10-01","23-10-02")
datos=db2.obtenerdat("*","radioproc","23-10-01","23-10-01")
print(datos)
print(data)
db2.stop()

