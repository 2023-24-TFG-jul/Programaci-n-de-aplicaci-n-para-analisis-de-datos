#Nombre: Muestra Funcionamiento.py
#Autor:Álvaro Villar Val
#Fecha:22/02/24
#Versión:0.1.3
#Descripción: Programa para enseñar como funciona la base de datos 1
#########################################################################################################################
#Definimos los imports
from BaseDatosLvl1 import BaseDatosLvl1
########################################################################################################################

db1=BaseDatosLvl1()
db1.actuimgCam1()
db1.obtenerImg(24012004,24012004)
db1.actualizardatos()
datos1=db1.obtenerdat("*","radio","23-10-01","23-10-01")
datos2=db1.obtenerdat("*","skyscanner","23-12-01","23-12-02")
datos3=db1.obtenerdat("*","skycamera","23-10-01","23-10-02")
print(datos1)
print(datos2)
print(datos3)
db1.stop()

