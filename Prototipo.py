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
#db1.actuimgCam1()
db1.obtenerImg(24011708,24012004)
db1.stop()

