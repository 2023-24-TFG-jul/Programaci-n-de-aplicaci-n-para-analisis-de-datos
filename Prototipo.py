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
db1=BaseDatosLvl1()
db1.injectarimg("Datos\Fotos\\201D_CAM1_20231005_085100_02.jpg")

db1.stop()

