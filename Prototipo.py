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
data=db2.obtenerdat("*","radio",None)
db2.actualizarRadio(data)
datos=db2.obtenerdat("*","radioproc",None)
print(datos)
db2.stop()

